#!/usr/bin/env python3
"""
Aligned mistranslation check - check file alignment first, then check translations.
Uses greedy (longest match) strategy and worker-level initialization for performance.
"""
import os
import re
from multiprocessing import Pool, cpu_count

# Worker-level shared state (initialized once per worker process)
_glossary_list = []
_glossary_patterns = []
_en_wiki_path = ''
_zh_wiki_path = ''

def _init_worker(glossary_list, en_wiki_path, zh_wiki_path):
    """Initialize worker process with shared data (called once per worker)."""
    global _glossary_list, _glossary_patterns, _en_wiki_path, _zh_wiki_path
    _glossary_list = glossary_list
    _en_wiki_path = en_wiki_path
    _zh_wiki_path = zh_wiki_path
    # Pre-compile regex patterns for all terms
    # Use case-sensitive matching for mixed-case terms (e.g., "Conditions")
    # Use case-insensitive matching for lowercase terms (e.g., "attack")
    _glossary_patterns = []
    for en, chs in glossary_list:
        if en.islower():
            pattern = re.compile(r'\b' + re.escape(en) + r'\b', re.IGNORECASE)
        else:
            pattern = re.compile(r'\b' + re.escape(en) + r'\b')
        _glossary_patterns.append((pattern, en, chs))

def load_glossary(path):
    """Load glossary."""
    pairs = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('| ') and '|' in line[2:]:
                parts = line.split('|')
                if len(parts) >= 4:
                    en = parts[1].strip()
                    chs = parts[2].strip()
                    if en and chs and en != 'English' and chs != '中文' and len(en) > 2:
                        pairs[en] = chs
    return pairs

def get_visible_text(line):
    """Extract visible text from a markdown line, removing link URLs and markup.

    Converts:
    - [text](url "title") -> text
    - [text](url) -> text
    - *Source: [text](url)* -> (removed)
    - ### heading -> heading

    Returns the visible text portion of the line.
    """
    # Remove source lines entirely
    if '*Source:' in line:
        return ''

    # Strip markdown links character by character to handle nested parens in URLs
    result = []
    i = 0
    while i < len(line):
        # Check for markdown link: [text](...)
        if line[i] == '[' and (i == 0 or line[i-1] != '!'):
            # Find matching ]
            bracket_end = line.find(']', i + 1)
            if bracket_end != -1 and bracket_end + 1 < len(line) and line[bracket_end + 1] == '(':
                # Extract display text
                display_text = line[i + 1:bracket_end]
                # Find matching ) - handle nested parens
                paren_depth = 1
                j = bracket_end + 2
                while j < len(line) and paren_depth > 0:
                    if line[j] == '(':
                        paren_depth += 1
                    elif line[j] == ')':
                        paren_depth -= 1
                    j += 1
                # Add only the display text
                result.append(display_text)
                i = j
                continue
        result.append(line[i])
        i += 1

    text = ''.join(result)

    # Remove heading markers
    text = re.sub(r'^#+\s*', '', text)

    # Remove bold/italic markers
    text = text.replace('**', '').replace('*', '').replace('__', '').replace('_', '')

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    return text

def check_file(fname):
    """Check a single file for alignment and mistranslations."""
    en_file = os.path.join(_en_wiki_path, fname)
    zh_file = os.path.join(_zh_wiki_path, fname)

    if not os.path.exists(zh_file):
        return {'type': 'missing', 'file': fname}

    with open(en_file, 'r', encoding='utf-8', errors='ignore') as f:
        en_lines = f.readlines()
    with open(zh_file, 'r', encoding='utf-8', errors='ignore') as f:
        zh_lines = f.readlines()

    en_count = len(en_lines)
    zh_count = len(zh_lines)

    # Check alignment: allow 10% difference
    max_diff = max(en_count, zh_count) * 0.1
    if abs(en_count - zh_count) > max_diff:
        return {
            'type': 'misaligned',
            'file': fname,
            'en_lines': en_count,
            'zh_lines': zh_count,
            'diff': abs(en_count - zh_count)
        }

    # File has similar line count, but lines might not be aligned
    line_misalign_count = 0
    for line_num in range(min(en_count, zh_count)):
        en_line = en_lines[line_num].strip()
        zh_line = zh_lines[line_num].strip()

        if not en_line and not zh_line:
            continue
        if not en_line or not zh_line:
            continue

        if not _lines_are_aligned(en_line, zh_line):
            line_misalign_count += 1

    # If more than 20% of non-empty lines don't align, report as misaligned
    non_empty_lines = sum(1 for i in range(min(en_count, zh_count))
                          if en_lines[i].strip() and zh_lines[i].strip())
    if non_empty_lines > 0 and line_misalign_count / non_empty_lines > 0.2:
        return {
            'type': 'misaligned',
            'file': fname,
            'en_lines': en_count,
            'zh_lines': zh_count,
            'diff': abs(en_count - zh_count)
        }

    # File is aligned, check translations with greedy (longest match) strategy
    issues = []
    for line_num, en_line in enumerate(en_lines, 1):
        # Get visible text (strip link URLs and markup)
        visible_text = get_visible_text(en_line)

        if not visible_text.strip():
            continue

        # Find all matching terms in visible text (greedy order from pre-sorted list)
        matched_terms = []
        for pattern, en_term, chs_term in _glossary_patterns:
            if pattern.search(visible_text):
                matched_terms.append((en_term, chs_term))

        if not matched_terms:
            continue

        # Track which positions in visible text are already covered
        reported_positions = set()

        for en_term, chs_term in matched_terms:
            # Use case-appropriate pattern
            if en_term.islower():
                term_pattern = re.compile(r'\b' + re.escape(en_term) + r'\b', re.IGNORECASE)
            else:
                term_pattern = re.compile(r'\b' + re.escape(en_term) + r'\b')

            for match in term_pattern.finditer(visible_text):
                # Check if this position is already covered by a longer term
                covered = False
                for pos in range(match.start(), match.end()):
                    if pos in reported_positions:
                        covered = True
                        break

                if covered:
                    continue

                # Mark positions as covered
                for pos in range(match.start(), match.end()):
                    reported_positions.add(pos)

                # Check corresponding Chinese line (with 3-line tolerance)
                found_correct = False
                zh_context = ""

                for offset in [-3, -2, -1, 0, 1, 2, 3]:
                    zh_line_idx = line_num - 1 + offset
                    if 0 <= zh_line_idx < len(zh_lines):
                        zh_line = zh_lines[zh_line_idx]
                        if chs_term in zh_line:
                            found_correct = True
                            break
                        if offset == 0:
                            zh_context = zh_line.strip()

                if not found_correct:
                    issues.append({
                        'file': fname,
                        'en_line': line_num,
                        'en_term': en_term,
                        'expected_chs': chs_term,
                        'en_content': en_line.strip()[:200],
                        'zh_content': zh_context[:200]
                    })

    return {'type': 'checked', 'file': fname, 'issues': issues}


def _lines_are_aligned(en_line, zh_line):
    """Check if two lines are structurally aligned."""
    # Check 1: Both are headings
    if en_line.startswith('#') and zh_line.startswith('#'):
        return True

    # Check 2: Both are table rows
    if en_line.startswith('|') and zh_line.startswith('|'):
        return True

    # Check 3: Both are list items
    if (en_line.startswith('- ') or en_line.startswith('* ')) and \
       (zh_line.startswith('- ') or zh_line.startswith('* ')):
        return True

    # Check 4: Both contain the same link target (e.g., [text](url))
    en_links = set(re.findall(r'\[.*?\]\((.*?)\)', en_line))
    zh_links = set(re.findall(r'\[.*?\]\((.*?)\)', zh_line))
    if en_links and zh_links and en_links & zh_links:
        return True

    # Check 5: Both contain the same numbers
    en_nums = set(re.findall(r'\d+', en_line))
    zh_nums = set(re.findall(r'\d+', zh_line))
    if en_nums and zh_nums and en_nums & zh_nums:
        return True

    # Check 6: Both contain the same HTML tags
    en_tags = set(re.findall(r'</?[a-zA-Z][^>]*>', en_line))
    zh_tags = set(re.findall(r'</?[a-zA-Z][^>]*>', zh_line))
    if en_tags and zh_tags and en_tags & zh_tags:
        return True

    # Check 7: Both are empty or whitespace-only
    if not en_line.strip() and not zh_line.strip():
        return True

    # Default: not aligned
    return False

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    glossary_path = os.path.join(base_dir, 'GLOSSARY.md')
    en_wiki_path = os.path.join(parent_dir, 'bg3-wiki', 'markdown', 'wiki')
    zh_wiki_path = os.path.join(base_dir, 'wiki')
    output_path = os.path.join(base_dir, 'potential_mistranslations.md')

    print('Loading glossary...')
    glossary_pairs = load_glossary(glossary_path)
    glossary_list = list(glossary_pairs.items())
    glossary_list.sort(key=lambda x: len(x[0]), reverse=True)  # Greedy: longest first
    print(f'Loaded {len(glossary_list)} glossary pairs')

    # Get common files
    en_files = set(f for f in os.listdir(en_wiki_path) if f.endswith('.md'))
    zh_files = set(f for f in os.listdir(zh_wiki_path) if f.endswith('.md'))
    common_files = sorted(en_files.intersection(zh_files))
    print(f'Found {len(common_files)} common files')

    # Process in parallel
    num_workers = cpu_count()
    print(f'Using {num_workers} workers...')

    results = []
    with Pool(
        num_workers,
        initializer=_init_worker,
        initargs=(glossary_list, en_wiki_path, zh_wiki_path)
    ) as pool:
        for i, result in enumerate(pool.imap_unordered(check_file, common_files, chunksize=50)):
            results.append(result)
            if (i + 1) % 500 == 0:
                print(f'  Processed {i + 1}/{len(common_files)} files...')

    # Categorize results
    missing_files = []
    misaligned_files = []
    mistranslations = []

    for result in results:
        if result['type'] == 'missing':
            missing_files.append(result['file'])
        elif result['type'] == 'misaligned':
            misaligned_files.append(result)
        elif result['type'] == 'checked':
            if result['issues']:
                mistranslations.extend(result['issues'])

    # Save results as markdown
    print(f'\nSaving results to {output_path}...')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# 潜在误译报告\n\n')

        # Summary
        f.write('## 统计摘要\n\n')
        f.write(f'- 总文件数：{len(common_files)}\n')
        f.write(f'- 缺失文件：{len(missing_files)}\n')
        f.write(f'- 不对齐文件：{len(misaligned_files)}\n')
        f.write(f'- 潜在误译：{len(mistranslations)}\n\n')

        # Misaligned files
        if misaligned_files:
            f.write('## 不对齐文件\n\n')
            f.write('| 文件名 | 英文行数 | 中文行数 | 差异 |\n')
            f.write('|--------|----------|----------|------|\n')
            for item in sorted(misaligned_files, key=lambda x: x['diff'], reverse=True):
                f.write(f"| {item['file']} | {item['en_lines']} | {item['zh_lines']} | {item['diff']} |\n")
            f.write('\n')

        # Mistranslations
        if mistranslations:
            f.write('## 潜在误译\n\n')
            f.write('| 文件 | 行号 | 英文术语 | 期望翻译 | 英文内容 | 中文内容 |\n')
            f.write('|------|------|----------|----------|----------|----------|\n')
            for item in sorted(mistranslations, key=lambda x: (x['file'], x['en_line'])):
                en_content = item['en_content'].replace('|', '\\|').replace('\n', ' ')
                zh_content = item['zh_content'].replace('|', '\\|').replace('\n', ' ')
                f.write(f"| {item['file']} | {item['en_line']} | {item['en_term']} | {item['expected_chs']} | {en_content} | {zh_content} |\n")

    print(f'\n=== Summary ===')
    print(f'Missing files: {len(missing_files)}')
    print(f'Misaligned files: {len(misaligned_files)}')
    print(f'Potential mistranslations: {len(mistranslations)}')
    print(f'Saved to: {output_path}')

if __name__ == '__main__':
    main()
