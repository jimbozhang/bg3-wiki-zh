# 帮助：编辑基础

Wiki 上使用的标记语言称为 _wikitext_。BG3Wiki 上的大多数文章都可以通过直接操作 wikitext（通过 _源代码编辑器_）或使用 _可视化编辑器_（其功能类似于文字处理器）进行编辑。

本手册中的大部分信息将使用 wikitext 进行解释，但它同时适用于源代码编辑器和可视化编辑器。

## 目录

- [1 页面标签](#页面标签)
  - [1.1 编辑](#编辑)
  - [1.2 讨论](#讨论)
  - [1.3 查看历史](#查看历史)
- [2 链接](#链接)
  - [2.1 内部链接](#内部链接)
  - [2.2 外部链接](#外部链接)
- [3 模板](#模板)
  - [3.1 使用可视化编辑器添加模板](#使用可视化编辑器添加模板)
  - [3.2 使用源代码编辑器添加模板](#使用源代码编辑器添加模板)
- [4 分类](#分类)
- [5 创建新页面](#创建新页面)
  - [5.1 创建重定向](#创建重定向)
- [6 附加资源](#附加资源)

## 页面标签

### 编辑

- 可视化编辑器和源代码编辑器。
- 在编辑器类型之间切换。

要编辑现有页面，请单击页面上方的 _编辑_（打开可视化编辑器）或 _编辑源代码_（打开源代码编辑器）。在任一编辑器中，您都可以随时通过右上角的菜单按钮在可视化编辑器和源代码编辑器之间切换。

编辑完成后，可以添加更改的简要摘要。您还可以在保存之前预览所做的任何更改。

### 讨论

文章的 _讨论_ 页面——或 _谈话页面_——用于解决有关文章的分歧。使用文章的讨论页面讨论文章的内容和编辑。使用 `~~~~` 签署您的评论。

### 查看历史

单击 **查看历史** 标签可查看对该页面执行的编辑历史。每行描述页面的一个修订版，包括日期/时间、进行该编辑的贡献者，以及可能的编辑摘要。

## 链接

### 内部链接

| 内部链接（指向其他 BG3Wiki 文章的链接）使用双括号 `[[...]]` 添加。管道符 ` | ` 可以放在目标文章名称之后，并跟上要显示的文本。例如，`[[Help: Style Guide | Style Guide]]` 显示为 [样式指南](Help_colon_Style_Guide.md "Help:Style Guide")。 |

要链接到 [分类](Help_colon_Categories.md "Help:Categories")，请在开头添加冒号 `:`，例如 `[[:Category:Areas]]`。否则，页面将被标记为属于该分类。

链接也可用于显示图像。有关更多说明，请参阅 [MediaWiki 上的图像帮助](https://www.mediawiki.org/wiki/Help:Images)。

### 外部链接

外部链接（指向其他网站）通过将 URL 后跟一个空格，然后将链接文本括在单括号中 `[URL LinkText]` 来添加。例如，`[https://www.mediawiki.org/wiki/Help:Links MediaWiki Help - Links]` 显示为 [MediaWiki Help - Links](https://www.mediawiki.org/wiki/Help:Links)。

对于常用引用的网站，如被遗忘的国度 wiki、Wikipedia 或 IMDB，请使用预设的 [外部链接模板](Category_colon_External_link_templates.md "Category:External link templates")。

## 模板

有关所有常用模板的列表，请参阅 [帮助：模板列表](Help_colon_List_of_templates.md "Help:List of templates")。

_模板_ 是一种特殊类型的页面，设计用于包含在其他页面中。模板在 BG3Wiki 上被广泛使用。

本手册的 [下一步](Help_colon_Using_templates.md "Help:Using templates") 将介绍模板的具体用法。

### 使用可视化编辑器添加模板

使用可视化编辑器插入模板

可以通过单击可视化编辑器上方的工具栏中的 _插入_，然后在下拉框中选择 _模板_ 来搜索和添加模板。大多数模板都可以通过这种方式轻松插入到页面上。要稍后编辑其内容，只需在可视化编辑器中单击插入的模板即可获取选项。

### 使用源代码编辑器添加模板

模板通过使用双括号 `{{ ... }}` 添加。例如，模板 `foo` 通过键入 `{{foo}}` 添加。

| 模板的参数通过管道符 ` | ` 指定。 |

- 带有一个参数的模板：
| - 代码：`{{enchantment | +1}}` |
- 结果：附魔：**+ 1**
  - 带有多个参数的模板：
| - 代码：`{{AttributeBlock | 8 | 15 | 7 | 6 | 10 | 8 | dex save = yes | race=Bird | hp=10}}` |
- 结果：

| [力量](Strength.md "Strength") 8 (-1) | [敏捷](Dexterity.md "Dexterity") 15 (+2) | [体质](Constitution.md "Constitution") 7 (-2) | [智力](Intelligence.md "Intelligence") 6 (-2) | [感知](Wisdom.md "Wisdom") 10 | [魅力](Charisma.md "Charisma") 8 (-1) |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| 种族 | 鸟 |  |  |  |  |
| 生命值 | 10 |  |  |  |  |

## 分类

[分类](Special_colon_Categories.md "Special:Categories") 页面列出了该分类中的所有页面。

_所有内容_ 搜索选项在搜索结果中包含分类。您也可以在 [特殊：分类](Special_colon_Categories.md "Special:Categories") 页面上找到它们。分类在查找特定图像或页面时非常有用，尤其是在您不知道要查找内容的确切名称时。

- 在可视化编辑器中添加分类。
- 分类页面示例。

某些模板会自动将正确的分类添加到使用它的页面。但是，在某些情况下，您需要手动将页面添加到其他分类。

要将页面添加到分类：

- 使用可视化编辑器时，可以通过单击右上角菜单并选择 **分类** 来将页面添加到分类。在提供的框中键入分类名称，编辑器将建议分类的自动完成选项（如果存在）。
- 使用源代码编辑器时，在页面底部使用标记 `[[Category:_分类名称_]]`。您可以根据需要重复此操作以添加更多分类。

## 创建新页面

只需打开指向尚未创建的页面的链接（例如单击红色链接），或在 Wiki 上搜索该页面，即可创建新页面。如果尚不存在，则可以创建它。BG3Wiki 上的大多数页面都是在模板的帮助下创建的，这起初可能看起来令人生畏，但实际上它们非常易于使用。

### 创建重定向

如果页面存在，但用户可能使用多个术语搜索它，则可以使用 `#REDIRECT [[文章链接]]` 创建重定向页面。

## 附加资源

- [MediaWiki 帮助页面](https://www.mediawiki.org/wiki/Help:Contents)
- [MediaWiki 格式](https://www.mediawiki.org/wiki/Help:Formatting)

---
*Source: [Help:Editing basics](https://bg3.wiki/wiki/Help:Editing_basics)*