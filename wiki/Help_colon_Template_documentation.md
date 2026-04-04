# 帮助:模板

本文是关于在BG3Wiki上创建模板的技术指南。有关如何使用模板的指南，请参阅[帮助:使用模板](Help_colon_Using_templates.md "Help:Using templates")。有关模板列表，请参阅[帮助:模板列表](Help_colon_List_of_templates.md "Help:List of templates")。

**模板**是一种特殊类型的页面，设计用于在其他页面中被包含。模板允许编辑者自动在页面上插入常用的图像、代码和格式。

为确保维基上的标准化实践，本页面提供了**模板创建**过程的指南。

**模板文档**是模板创建的重要组成部分，确保模板在整个维基中得到正确理解和使用。

要创建或编辑模板，您需要访问权限。这可以通过 Discord 请求或访问管理员的讨论页面来实现。

## 目录

- [1 模板名称](#模板名称)
  - [1.1 模板页面名称](#模板页面名称)
    - [1.1.1 例外](#例外)
  - [1.2 快捷方式](#快捷方式)
- [2 模板创建指南](#模板创建指南)
  - [2.1 需要考虑的事项](#需要考虑的事项)
  - [2.2 重要注意事项](#重要注意事项)
  - [2.3 格式](#格式)
- [3 模板文档](#模板文档)
  - [3.1 如何包含文档](#如何包含文档)
  - [3.2 编写模板数据](#编写模板数据)
- [4 Cargo 数据库](#Cargo-数据库)
- [5 附加资源](#附加资源)

## 模板名称

为确保模板命名约定在整个维基上标准化，所有模板都遵循相同的命名约定。

### 模板页面名称

模板页面名称应使用小写字母，单词之间用单个空格分隔。

请注意，模板页面名称的首字母始终被视为大写，包括在链接或包含模板时。

良好模板页面名称的示例

- {{[引用文本](Template_colon_Cite_text.md "Template:Cite text")}}
- {{[相对位置](Template_colon_Relative_location.md "Template:Relative location")}}
- {{[法术页面](Template_colon_Spell_page.md "Template:Spell page")}}

#### 例外

有时模板名称可能由缩写或单个单词组成。

例如，{{[参考列表](Template_colon_Reflist.md "Template:Reflist")}} 被如此命名是因为它添加了 <reference> 标签来列出参考。如果它被命名为 {{参考列表}}，则名称会暗示它是用于或关于 _参考_ 标签的列表。

同样，某些模板的缩写名称，如 {{[sai](Template_colon_Sai.md "Template:Sai")}}、{{[ref](Template_colon_Ref.md "Template:Ref")}} 和 {{[em](Template_colon_Em.md "Template:Em")}}，由于其简单性，也被认为是可接受的。

### 快捷方式

为使模板更易于使用，每个模板应有 1-5 个_快捷方式_，使用 {{[快捷方式](Template_colon_Shortcut.md "Template:Shortcut")}} 添加。这些是重定向，具有更短的名称以便于访问。这些不需要遵循模板页面命名约定。

应尽可能少地创建快捷方式以防止歧义。如果单个快捷方式就足够了，则_不应_创建额外的快捷方式。

快捷方式的命名没有精确的标准，但理想情况下应直观且无歧义。

通常，如果快捷方式满足以下条件，则被认为是合理的：

- 它是目标模板名称的明确缩写。
- 比完整模板名称更易于输入。
- 与模板功能密切相关。

快捷方式示例

- {{[t 链接](Template_colon_T_link.md "Template:T link")}}，重定向到 {{[模板链接](Template_colon_Template_link.md "Template:Template link")}}
- {{[cw](Template_colon_Cw.md "Template:Cw")}}，重定向到 {{[内容警告](Template_colon_Content_warning.md "Template:Content warning")}}

## 模板创建指南

模板创建是 BG3Wiki 技术工作流程的重要组成部分。然而，在创建或改进模板时需要小心。

### 需要考虑的事项

理想情况下，新模板应：

1. 易于使用，参数尽可能少。
2. 具有清晰易懂的[模板文档](Help_colon_Template_documentation.md "Help:Template documentation")和示例。
3. 始终包含模板所有快捷方式的列表。
4. 具有易于使用的模板数据。

### 重要注意事项

创建模板时的一些重要注意事项：

- 换行与表格解析器交互异常，这可能会破坏某些模板。
| - 向模板参数 {{{parameter}}} 添加管道符 > {{{parameter | }}} 将为其提供默认值（在本例中为空字符串）。 - 这在使用 {{#if:}} 解析器函数时很重要，因为在参数未定义的情况下，{{{parameter}}} 将返回值 "true"，而 {{{parameter | }}} 将返回值 "false"。 - 当参数用作值时，记住这一点也很重要，因为在参数未定义的情况下，{{{parameter}}} 将返回值 "{{{parameter}}}"，而 {{{parameter | }}} 将返回其默认值（在本例中为空字符串）。 |
- Expr 和 ifeq 在计算数字时会产生不同的结果。这是因为 expr 将数字视为浮点数，而 ifeq 将其视为整数。

### 格式

- 模板_必须_有“模板数据”，通过单击页面顶部的“管理模板数据”实现。这使得模板可以被可视化编辑器使用。
- 模板数据_必须_位于模板的主页面上（如果没有文档子页面）。如果存在文档子页面，则_必须_位于模板的文档子页面上。
- 模板_应_包含至少一个使用示例的文档。
| - 模板_应_使用 `{{documentation | content=}}` 作为其所有文档。 |
- 长文档_可以_移动到 `/doc` 子页面。在这种情况下，在主页面上使用 `{{documentation}}` 代替。
- 模板_必须_有分类。至少，它应被分类为 [分类:模板](Category_colon_Templates.md "Category:Templates") 或其子分类之一。
- 分类_应_位于文档子页面（如果存在）。文档子页面_必须_在分类周围使用 `<noinclude>` 标签，否则子页面将在分类索引中被计为模板。
- Cargo 声明_必须_在模板主页面的 noinclude 中，即使存在文档子页面。

## 模板文档

模板文档理想情况下应包括以下内容：

- 模板功能的描述。
- 模板使用示例，使用 {{[模板演示](Template_colon_Template_demo.md "Template:Template demo")}}、{{[c](Template_colon_C.md "Template:C")}} 和/或 <pre></pre> 标签。
- 模板参数的清晰描述。
- 链接到类似或相关的模板。

### 如何包含文档

模板本身应放在 `<includeonly></includeonly>` 标签内。模板文档应紧随其后，并放在 `<noinclude></noinclude>` 标签内，并使用 [模板:文档](Template_colon_Documentation.md "Template:Documentation")。注意不要留下任何不必要的空格或换行！示例：

| `<includeonly>模板在此。</includeonly><noinclude>{{documentation | content=模板文档在此。}}</noinclude>` |

示例可以使用 {{code}} 模板和 <nowiki></nowiki> 标签编写：

| `{{code | <nowiki>{{示例模板 | 示例参数}}</nowiki>}}` |

或者使用 <pre>...</pre> 标签。

代码示例之后应是实际使用的模板。

具有非常长文档的模板可以将文档（包括模板数据）移动到 `/doc` 子页面。主页面可以简单地包含 `<noinclude>{{documentation}}</noinclude>`。然后 `/doc` 子页面的内容将自动包含在模板页面上。请注意，分类应保留在主模板页面上，仍在 `noinclude` 标签内。

### 编写模板数据

有关 TemplateData 的详细指南，请参阅 [关于 TemplateData 的信息](https://m.mediawiki.org/wiki/Special:MyLanguage/Help:TemplateData)

TemplateData 可以通过模板文档菜单管理，该菜单可以通过源代码编辑器上方的“管理 TemplateData”按钮打开：

TemplateData 允许使用可视化编辑器的编辑者轻松地将模板添加到文章中，但也可以作为使用源代码编辑器的编辑者的有效速记文档。

## Cargo 数据库

模板还允许维基使用 [Cargo 查询](https://m.mediawiki.org/wiki/Extension:Cargo) 用存储的值填充数据库表。这使得维基可以创建自动化的物品或法术列表。

## 附加资源

- [MediaWiki 帮助:模板](https://www.mediawiki.org/wiki/Help:Templates)

---
*Source: [Help:Templates](https://bg3.wiki/wiki/Help:Templates)*