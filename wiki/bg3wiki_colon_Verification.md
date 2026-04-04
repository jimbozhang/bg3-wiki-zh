# bg3wiki:验证

我们希望维基上的信息是可信的，并且在某些情况下，可以通过外部来源进行验证。

我们使用_参考文献_来告知读者维基上的信息来源。有关注释、脚注和参考文献的详细信息，请参见[帮助:样式手册](Help_colon_Style_manual.md "Help:Style manual")。

或者，信息可能来自受信任的编辑者，他们保证通过游戏内测试或数据挖掘来验证关于游戏行为或内容的声明，在这种情况下，不需要引用外部来源，尽管仍然可以使用解释性_注释_或_脚注_来澄清某些声明或解释如何确定其为真。

何时需要参考文献？

并非维基上的所有信息都需要参考文献。但是，信息在游戏中的查找难度越大，添加适当参考文献就越重要。

请求验证

如果您在维基上遇到没有参考文献的信息，或者您认为参考文献不充分，可以通过在可能不正确的信息句子或段落后添加 {{[验证](Template_colon_Verify.md "Template:Verify")}} 模板来请求验证。这会让其他编辑者知道某些内容缺少验证。

除非您知道信息不正确，否则不要删除信息——请将其提交到讨论页。

## 添加参考文献

使用模板 {{[引用](Template_colon_Ref.md "Template:Ref")}} 向文章添加引用标签。此模板通常应添加在相关句子或段落的末尾，紧接在标点符号之后（无空格）。

只有在文章中包含 {{[引用列表](Template_colon_Reflist.md "Template:Reflist")}} 模板时，引用才会正确显示。为此，只需添加一个_参考文献_部分，并将该模板作为该部分的唯一内容。有关详细信息，请参见[帮助:样式手册](Help_colon_Style_manual.md "Help:Style manual")。

参考文献
| {{引用列表}} | 莱埃泽尔擅长冷笑。<sup>[\[1\]](#cite_note-1)</sup> |

参考文献

1. [↑](#cite_ref-1) 莱埃泽尔的介绍场景。

### 分组参考文献

可以向文章添加_分组参考文献_。这些参考文献被分配了一个组，并将与其他参考文献分开列出。

要向引用添加组，只需在引用模板的第二个参数中输入组的名称。

参考文献

1. [↑](#cite_ref-2) 莱埃泽尔的介绍场景。

要列出这些参考文献，还必须将组添加到 t:引用列表 模板中，作为其第一个参数。

### 引用标签

也可以使用类似 HTML 的标签添加简单引用，用 <ref> </ref> 替换 t:引用，用 <references/> 替换 t:引用列表。

## 分节参考文献

可以通过显式命名要包含在参考文献列表中的引用，添加仅限于文章特定部分的参考文献：

| 示例 | 结果 |
| --- | --- |
| 莱埃泽尔擅长冷笑。{{引用|莱埃泽尔的介绍场景。}} 参考文献 {{引用列表}} | 莱埃泽尔擅长冷笑。[[](#cite_note-1 "[")1] 参考文献 .mw-parser-output .reflist .references{list-style-type:inherit}.mw-parser-output .refs-act1::before{content:"Act 1";text-decoration:none;background:none;font-size:100%;font-weight:bold;direction:ltr}.mw-parser-output .refs-act2::before{content:"Act 2";text-decoration:none;background:none;font-size:100%;font-weight:bold;direction:ltr}.mw-parser-output .refs-act3::before{content:"Act 3";text-decoration:none;background:none;font-style:italic;font-size:100%;font-weight:bold;direction:ltr}.mw-parser-output .refs-url::before{content:"External links";text-decoration:none;background:none;font-size:100%;font-weight:bold;direction:ltr}.mw-parser-output .refs-text::before{content:"Literature";text-decoration:none;background:none;font-size:100%;font-weight:bold;direction:ltr}.mw-parser-output .refs-note::before{content:"Notes";text-decoration:none;background:none;font-size:100%;font-weight:bold;direction:ltr} [↑](#cite_ref-1 "↑") 莱埃泽尔的介绍场景。
这是一个示例文本。<ref name="Example 1"/> 这也是一个示例。<ref name="Example 2"/>

参考文献
| <references> <ref name="Example 1">示例引用 1</ref> <ref name="Example 2">示例引用 2</ref> </references> | 这是一个示例文本。<sup>[\[1\]](#cite_note-Example_1-3)</sup> 这也是一个示例。<sup>[\[2\]](#cite_note-Example_2-4)</sup> |

参考文献

1. [↑](#cite_ref-Example_1_3-0) 示例引用 1
1. [↑](#cite_ref-Example_2_4-0) 示例引用 2

## 引用模板列表

通用参考文献
使用 {{[引用](Template_colon_Ref.md "Template:Ref")}} 添加引用。通过在文章的参考文献部分添加 {{[引用列表](Template_colon_Reflist.md "Template:Reflist")}} 模板来列出这些引用。这些引用可以使用任何组。
链接
| 使用 {{[引用网页](Template_colon_Cite_web.md "Template:Cite web")}} 添加 URL 作为引用。这些引用始终具有 _url_ 组，并通过在文章的参考文献部分添加 {{[引用列表](Template_colon_Reflist.md "Template:Reflist") | url}} 来列出。 |
文本
| 使用 {{[引用文本](Template_colon_Cite_text.md "Template:Cite text")}} 添加游戏内书籍或作为引用。这些引用始终具有 _text_ 组，并通过在文章的参考文献部分添加 {{[引用列表](Template_colon_Reflist.md "Template:Reflist") | text}} 来列出。 |
验证
使用 {{[验证](Template_colon_Verify.md "Template:Verify")}} 请求验证。

## 另请参阅

- [带有验证模板的页面](Special_colon_WhatLinksHere/Template_colon_Verify.md "Special:WhatLinksHere/Template:Verify")，列出了需要验证的页面。
- [分类:引用模板](Category_colon_Citation_templates.md "Category:Citation templates")，引用模板列表。

---
*Source: [bg3wiki:Verification](https://bg3.wiki/wiki/bg3wiki:Verification)*