# 协助:模板

本文是关于在BG3Wiki上创建模板的技术指南。关于如何使用模板的指南，请参见[协助:使用模板](Help_colon_Using_templates.md "协助:使用模板")。有关模板列表，请参见[协助:模板列表](Help_colon_List_of_templates.md "协助:模板列表")。

[索引](Help_colon_Index.md "协助:索引") • [指南](Help_colon_Guide_namespace.md "协助:指南命名空间") • [模组](Modding_colon_Modding_resources.md "模组:模组资源") • [Discord](https://discord.gg/EYNTAQXaNs)

## bg3.wiki 侧边栏

- [项目](bg3wiki_colon_Project.md "bg3wiki:项目")
- [模组](Modding_colon_Modding_resources.md "模组:模组资源")
- [指南](Guide_colon_Guides.md "指南:指南")

维护

- [维护](Help_colon_Maintenance.md "协助:维护")
- 模板

[协助](Help_colon_Index.md "协助:索引")

- [常见问题](Help_colon_FAQ.md "协助:常见问题")
- [搜索](Help_colon_Searching_bg3.wiki.md "协助:搜索 bg3.wiki")
- [模板列表](Help_colon_List_of_templates.md "协助:模板列表")
- [术语表](Help_colon_Glossary.md "协助:术语表")
- [许可](bg3wiki_colon_Licensing.md "bg3wiki:许可")
- [贡献者支付](bg3wiki_colon_Payment.md "bg3wiki:支付")

政策

- [内容规则](bg3wiki_colon_Content_rules.md "bg3wiki:内容规则")
- [编辑政策](bg3wiki_colon_Editing_policy.md "bg3wiki:编辑政策")
- [图片政策](bg3wiki_colon_Image_policy.md "bg3wiki:图片政策")
- [版权](bg3wiki_colon_Copyrights.md "bg3wiki:版权")
- [验证](bg3wiki_colon_Verification.md "bg3wiki:验证")
- [广告](bg3wiki_colon_Ads.md "bg3wiki:广告")

手册
[编辑手册](Help_colon_Editing_manual.md "协助:编辑手册")

- [编辑基础](Help_colon_Editing_basics.md "协助:编辑基础")
- [使用模板](Help_colon_Using_templates.md "协助:使用模板")
- [上传文件](Help_colon_Uploading_files.md "协助:上传文件")

[样式手册](Help_colon_Style_manual.md "协助:样式手册")

- [样式手册](Help_colon_Style_manual.md "协助:样式手册")

- [内容警告](Help_colon_Content_warnings.md "协助:内容警告")

- [分类](Help_colon_Categories.md "协助:分类")

[常见问题](Help_colon_FAQ.md "协助:常见问题") • [搜索](Help_colon_Searching_bg3.wiki.md "协助:搜索 bg3.wiki") • 模板 ([文档](Help_colon_Template_documentation.md "协助:模板文档")) • [社区](bg3wiki_colon_Community.md "bg3wiki:社区") ([维护](Help_colon_Maintenance.md "协助:维护") • [梗](bg3wiki_colon_Community_gags.md "bg3wiki:社区梗"))

[编辑政策](bg3wiki_colon_Editing_policy.md "bg3wiki:编辑政策") • [验证](bg3wiki_colon_Verification.md "bg3wiki:验证") • [内容规则](bg3wiki_colon_Content_rules.md "bg3wiki:内容规则") ([版权](bg3wiki_colon_Copyrights.md "bg3wiki:版权") • [许可](bg3wiki_colon_Licensing.md "bg3wiki:许可"))

[编辑手册](Help_colon_Editing_manual.md "协助:编辑手册") • [样式手册](Help_colon_Style_manual.md "协助:样式手册") • [模板列表](Help_colon_List_of_templates.md "协助:模板列表") • [术语表](Help_colon_Glossary.md "协助:术语表")

**模板**是一种特殊类型的页面，设计用于在其他页面中被包含。模板允许编辑者自动在页面上插入常用的图像、代码和格式。

为确保维基上的标准化实践，本文提供了**模板创建**过程的指南。

**模板文档**是模板创建的重要组成部分，确保模板在整个维基上被正确理解和使用。

要创建或编辑模板，您需要访问权限。这可以通过 Discord 请求，或访问管理员的讨论页。

## 目录

- [1 模板名称](#template-names)
  - [1.1 模板页面名称](#template-page-names)
    - [1.1.1 例外](#exceptions)
  - [1.2 快捷方式](#shortcuts)
- [2 模板创建指南](#template-creation-guidelines)
  - [2.1 需要注意的事项](#what-to-keep-in-mind)
  - [2.2 重要考虑因素](#important-considerations)
  - [2.3 格式](#formatting)
- [3 模板文档](#template-documentation)
  - [3.1 如何包含文档](#how-to-include-documentation)
  - [3.2 编写模板数据](#writing-template-data)
- [4 Cargo 数据库](#cargo-database)
- [5 附加资源](#additional-resources)

## 模板名称

为确保模板命名约定在整个维基上标准化，所有模板都遵循相同的命名约定。

### 模板页面名称

模板页面名称应使用小写字母，单词之间用单个空格分隔。

请注意，模板页面名称的首字母始终被视为大写，包括在链接或包含模板时。

良好模板页面名称的示例

- {{[引用文本](Template_colon_Cite_text.md "模板:引用文本")}}
- {{[相对位置](Template_colon_Relative_location.md "模板:相对位置")}}
- {{[法术页面](Template_colon_Spell_page.md "模板:法术页面")}}

#### 例外

有时模板名称可能由缩写或单个单词组成。

例如，{{[参考列表](Template_colon_Reflist.md "模板:参考列表")}} 被如此命名是因为它添加了 <reference> 标签来列出参考。如果它被命名为 {{参考列表}}，名称将暗示它是用于 _参考_ 标签的列表或列表。

类似地，某些模板的缩写名称，如 {{[sai](Template_colon_Sai.md "模板:Sai")}}、{{[ref](Template_colon_Ref.md "模板:Ref")}} 和 {{[em](Template_colon_Em.md "模板:Em")}}，由于其简单性，也被认为是可接受的。

### 快捷方式

为使模板更易于使用，每个模板应有 1-5 个_快捷方式_，使用 {{[快捷方式](Template_colon_Shortcut.md "模板:快捷方式")}} 添加。这些是重定向，具有更短的名称以便于访问。这些不需要遵循模板页面命名约定。

应尽可能少地创建快捷方式，以防止歧义。如果单个快捷方式就足够，则_不应_创建额外的快捷方式。

命名快捷方式没有精确的标准，但它们应直观且无歧义。

通常，如果快捷方式满足以下条件，则被认为是合理的：

- 它是目标模板名称的明确缩写。
- 比完整模板名称更易于输入。
- 与模板功能密切相关。

快捷方式示例

- {{[t 链接](Template_colon_T_link.md "模板:t 链接")}}, 重定向到 {{[模板链接](Template_colon_Template_link.md "模板:模板链接")}}
- {{[cw](Template_colon_Cw.md "模板:cw")}}, 重定向到 {{[内容警告](Template_colon_Content_warning.md "模板:内容警告")}}

## 模板创建指南

模板创建是BG3Wiki技术工作流程的重要组成部分。然而，在创建或改进模板时，需要注意。

### 需要注意的事项

理想情况下，新模板应：

1. 易于使用，参数尽可能少。
2. 具有清晰易懂的[模板文档](Help_colon_Template_documentation.md "协助:模板文档")，并附有示例。
3. 始终包含模板所有快捷方式的列表。
4. 具有易于使用的 TemplateData。

### 重要考虑因素

创建模板时的一些重要考虑因素：

- 换行与表格解析器交互异常，这可能会破坏某些模板。
| - 向模板参数 {{{parameter}}} 添加管道 > {{{parameter | }}} 将为其提供默认值（在本例中为空字符串）。 - 在使用 {{#if:}} 解析器函数时，记住这一点很重要，因为在参数未定义的情况下，{{{parameter}}} 将返回值 "true"，而 {{{parameter | }}} 将返回值 "false"。 - 当参数用作值时，记住这一点也很重要，因为在参数未定义的情况下，{{{parameter}}} 将返回值 "{{{parameter}}}"，而 {{{parameter | }}} 将返回其默认值（在本例中为空字符串）。 |
- Expr 和 ifeq 在计算数字时会产生不同的结果。这是因为 expr 将数字视为浮点数，而 ifeq 将其视为整数。

### 格式

- 模板_必须_具有“模板数据”，通过单击页面顶部的“管理模板数据”实现。这使模板可以被可视化编辑器使用。
- 如果模板没有文档子页面，模板数据_必须_位于模板的主页面上。如果模板有文档子页面，则_必须_位于模板的文档子页面上。
- 模板_应_包含至少一个使用示例的文档。
| - 模板_应_使用 `{{documentation | content=}}` 作为其所有文档。 |
- 长文档_可以_移动到 `/doc` 子页面。在这种情况下，在主页面上使用 `{{documentation}}` 代替。
- 模板_必须_有分类。至少，它应被分类为 [分类:模板](Category_colon_Templates.md "分类:模板") 或其子分类之一。
- 分类_应_位于文档子页面（如果存在）。文档子页面_必须_在分类周围使用 `<noinclude>` 标签，否则子页面将在分类索引中被计为模板。
- Cargo 声明_必须_在模板主页面的 noinclude 中，即使存在文档子页面。

## 模板文档

模板文档理想情况下应包括以下内容：

- 模板功能的描述。
- 模板使用示例，可以使用 {{[模板演示](Template_colon_Template_demo.md "模板:模板演示")}}、{{[c](Template_colon_C.md "模板:c")}} 和/或 <pre></pre> 标签。
- 模板参数的清晰描述。
- 链接到类似或相关的模板。

### 如何包含文档

模板本身应放置在标签 `<includeonly></includeonly>` 内。模板文档应紧随其后，并放置在标签 `<noinclude></noinclude>` 内，并使用 [模板:文档](Template_colon_Documentation.md "模板:文档")。注意不要留下任何不必要的空格或换行！示例：

| `<includeonly>模板在此。</includeonly><noinclude>{{documentation | content=模板文档在此。}}</noinclude>` |

示例可以使用 {{code}} 模板和 <nowiki></nowiki> 标签编写：

| `{{code | <nowiki>{{示例模板 | 示例参数}}</nowiki>}}` |

或者使用 <pre>...</pre> 标签。

代码示例之后应是实际使用的模板。

具有很长文档的模板可以将文档（包括模板数据）移动到 `/doc` 子页面。主页面可以简单地包含 `<noinclude>{{documentation}}</noinclude>`。然后 `/doc` 子页面的内容将自动包含在模板页面上。请注意，分类应保留在主模板页面上，仍在 `noinclude` 标签内。

### 编写模板数据

有关 TemplateData 的详细指南，请参见 [关于 TemplateData 的信息](https://m.mediawiki.org/wiki/Special:MyLanguage/Help:TemplateData)

TemplateData 可以通过模板文档菜单管理，该菜单可以通过源代码编辑器上方的“管理 TemplateData”按钮打开：

TemplateData 允许使用可视化编辑器的编辑者轻松地将模板添加到文章中，但也可以作为使用源代码编辑器的编辑者的有效速记文档。

## Cargo 数据库

模板还允许维基使用 [Cargo 查询](https://m.mediawiki.org/wiki/Extension:Cargo) 用存储的值填充数据库表。这使维基可以创建自动生成的物品或法术列表。

## 附加资源

- [MediaWiki 协助:模板](https://www.mediawiki.org/wiki/Help:Templates)

---
*Source: [Help:Templates](https://bg3.wiki/wiki/Help:Templates)*