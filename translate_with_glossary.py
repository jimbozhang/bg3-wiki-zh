#!/usr/bin/env python3
"""
Translate wiki files using three-step process:
1. Copy English version to Chinese location
2. Apply glossary replacements (greedy/longest match first)
   - Only replace visible text and link titles
   - NEVER replace link filenames/URLs
3. LLM polish for natural Chinese
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def load_glossary(glossary_path):
    """Load glossary into dict and sorted list for greedy matching."""
    glossary_dict = {}
    with open(glossary_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('| ') and '|' in line[2:]:
                parts = line.split('|')
                if len(parts) >= 4:
                    en = parts[1].strip()
                    chs = parts[2].strip()
                    if en and chs and en != 'English' and chs != '中文' and len(en) > 2:
                        glossary_dict[en] = chs

    # Sort by length (longest first) for greedy matching
    sorted_terms = sorted(glossary_dict.keys(), key=len, reverse=True)

    return glossary_dict, sorted_terms

def apply_glossary_to_text(text, glossary_dict, sorted_terms):
    """Apply glossary replacements using greedy (longest match) strategy.

    Uses regex with word boundaries for accurate matching.
    """
    if not text:
        return text

    result = text

    # Build a single combined pattern for efficiency
    # Group terms by case sensitivity
    case_sensitive = [t for t in sorted_terms if not t.islower()]
    case_insensitive = [t for t in sorted_terms if t.islower()]

    # Build lowercase lookup dict for case-insensitive terms
    lower_dict = {t.lower(): t for t in case_insensitive}

    # Process case-sensitive terms first (longer terms)
    if case_sensitive:
        pattern_str = '|'.join(re.escape(t) for t in case_sensitive)
        pattern = re.compile(r'\b(?:' + pattern_str + r')\b')
        result = pattern.sub(lambda m: glossary_dict[m.group(0)], result)

    # Process case-insensitive terms
    if case_insensitive:
        pattern_str = '|'.join(re.escape(t) for t in case_insensitive)
        pattern = re.compile(r'\b(?:' + pattern_str + r')\b', re.IGNORECASE)
        def replace_ci(m):
            matched = m.group(0)
            # Look up using lowercase version
            key = lower_dict.get(matched.lower())
            if key:
                return glossary_dict[key]
            return matched
        result = pattern.sub(replace_ci, result)

    return result

def process_url_part(url_part, glossary_dict, sorted_terms):
    """Process URL part: translate title but keep filename unchanged."""
    title_match = re.search(r'''(['"])(.+?)\1$''', url_part)
    if title_match:
        quote_char = title_match.group(1)
        title = title_match.group(2)
        filename = url_part[:title_match.start()].strip()
        processed_title = apply_glossary_to_text(title, glossary_dict, sorted_terms)
        return f'{filename} {quote_char}{processed_title}{quote_char}'
    else:
        return url_part

def process_markdown_links(text, glossary_dict, sorted_terms):
    """Process markdown links, translating display text and titles but NOT filenames."""
    result = []
    i = 0

    while i < len(text):
        # Check if we're at a markdown link
        if text[i] == '[' and (i == 0 or text[i-1] != '!'):
            # Find matching ]
            bracket_end = text.find(']', i + 1)
            if bracket_end != -1 and bracket_end + 1 < len(text) and text[bracket_end + 1] == '(':
                # This is a link: [display](url "title")

                # Extract and process display text (inside [])
                display_text = text[i+1:bracket_end]
                processed_display = apply_glossary_to_text(display_text, glossary_dict, sorted_terms)
                result.append('[')
                result.append(processed_display)
                result.append(']')

                # Find matching ) for the URL part
                paren_start = bracket_end + 2
                paren_depth = 1
                j = paren_start
                while j < len(text) and paren_depth > 0:
                    if text[j] == '(':
                        paren_depth += 1
                    elif text[j] == ')':
                        paren_depth -= 1
                    j += 1

                # Extract URL part - process title but NOT filename
                url_part = text[paren_start:j-1]
                processed_url = process_url_part(url_part, glossary_dict, sorted_terms)
                result.append('(')
                result.append(processed_url)
                result.append(')')

                i = j
                continue

        # Not a link, add character as-is
        result.append(text[i])
        i += 1

    return ''.join(result)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    glossary_path = os.path.join(base_dir, 'GLOSSARY.md')
    en_wiki_path = os.path.join(os.path.dirname(base_dir), 'bg3-wiki', 'markdown', 'wiki')
    zh_wiki_path = os.path.join(base_dir, 'wiki')

    print('Loading glossary...')
    glossary_dict, sorted_terms = load_glossary(glossary_path)
    print(f'Loaded {len(glossary_dict)} glossary terms')

    # Test with samples
    print('\n--- Sample Translations ---')
    samples = [
        '- [Performance](Performance.md "Performance") +1',
        '| Given to the party by [Hope](Hope.md "Hope")|',
        '- In various containers in the [House of Hope](House_of_Hope.md "House of Hope")',
        '[Shield Blow](Shield_Blow.md "Shield Blow")',
        'When a foe hits you with a melee attack, you can use your reaction to knock it Prone.',
        'The Flaming Fist guards are stationed at Baldur\'s Gate.',
    ]

    for sample in samples:
        result = process_markdown_links(sample, glossary_dict, sorted_terms)
        print(f'Original: {sample}')
        print(f'Result:   {result}')
        print()

    # Process first file
    print('--- Processing first file ---')
    en_path = os.path.join(en_wiki_path, 'Guide_colon_Where_To_Find_Equipment.md')
    zh_path = os.path.join(zh_wiki_path, 'Guide_colon_Where_To_Find_Equipment.md')

    print(f'Reading {en_path}...')
    with open(en_path, 'r', encoding='utf-8') as f:
        en_content = f.read()

    print('Applying glossary replacements...')
    replaced_content = process_markdown_links(en_content, glossary_dict, sorted_terms)

    print(f'Writing to {zh_path}...')
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(replaced_content)

    print(f'Done! Lines: {en_content.count(chr(10)) + 1}')

if __name__ == '__main__':
    main()
