# 帮助:使用模板

本文是关于使用模板的介绍。如需更技术性的指南，请参阅 [帮助:模板](Help_colon_Templates.md "帮助:模板")。如需所有常用模板的列表，请参阅 [帮助:模板列表](Help_colon_List_of_templates.md "帮助:模板列表")。

[索引](Help_colon_Index.md "帮助:索引") • [指南](Help_colon_Guide_namespace.md "帮助:指南命名空间") • [模组](Modding_colon_Modding_resources.md "模组:模组资源") • [Discord](https://discord.gg/EYNTAQXaNs)

## bg3.wiki 侧边栏

- [项目](bg3wiki_colon_Project.md "bg3wiki:项目")
- [模组](Modding_colon_Modding_resources.md "模组:模组资源")
- [指南](Guide_colon_Guides.md "指南:指南")

维护

- [维护](Help_colon_Maintenance.md "帮助:维护")
- [模板](Help_colon_Templates.md "帮助:模板")

[帮助](Help_colon_Index.md "帮助:索引")

- [常见问题](Help_colon_FAQ.md "帮助:常见问题")
- [搜索](Help_colon_Searching_bg3.wiki.md "帮助:搜索 bg3.wiki")
- [模板列表](Help_colon_List_of_templates.md "帮助:模板列表")
- [术语表](Help_colon_Glossary.md "帮助:术语表")
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
[编辑手册](Help_colon_Editing_manual.md "帮助:编辑手册")

- [编辑基础](Help_colon_Editing_basics.md "帮助:编辑基础")
- 使用模板
- [上传文件](Help_colon_Uploading_files.md "帮助:上传文件")

[样式手册](Help_colon_Style_manual.md "帮助:样式手册")

- [样式手册](Help_colon_Style_manual.md "帮助:样式手册")

- [内容警告](Help_colon_Content_warnings.md "帮助:内容警告")

- [分类](Help_colon_Categories.md "帮助:分类")

[常见问题](Help_colon_FAQ.md "帮助:常见问题") • [搜索](Help_colon_Searching_bg3.wiki.md "帮助:搜索 bg3.wiki") • [模板](Help_colon_Templates.md "帮助:模板") ([文档](Help_colon_Template_documentation.md "帮助:模板文档")) • [社区](bg3wiki_colon_Community.md "bg3wiki:社区") ([维护](Help_colon_Maintenance.md "帮助:维护") • [梗](bg3wiki_colon_Community_gags.md "bg3wiki:社区梗"))

[编辑政策](bg3wiki_colon_Editing_policy.md "bg3wiki:编辑政策") • [验证](bg3wiki_colon_Verification.md "bg3wiki:验证") • [内容规则](bg3wiki_colon_Content_rules.md "bg3wiki:内容规则") ([版权](bg3wiki_colon_Copyrights.md "bg3wiki:版权") • [许可](bg3wiki_colon_Licensing.md "bg3wiki:许可"))

[编辑手册](Help_colon_Editing_manual.md "帮助:编辑手册") • [样式手册](Help_colon_Style_manual.md "帮助:样式手册") • [模板列表](Help_colon_List_of_templates.md "帮助:模板列表") • [术语表](Help_colon_Glossary.md "帮助:术语表")

**模板**是一种特殊类型的页面，设计用于嵌入到其他页面中，为编辑者提供一致的设计和格式。

## 目录

- [1 将模板添加到页面](#adding-templates-to-pages)
  - [1.1 通过可视化编辑器](#via-the-visual-editor)
  - [1.2 通过源代码编辑器](#via-the-source-editor)
- [2 模板的具体用途](#specific-uses-of-templates)
  - [2.1 添加页面导航](#adding-navigation-to-pages)
    - [2.1.1 页首注释](#hatnotes)
    - [2.1.2 歧义页](#disambiguation-pages)
    - [2.1.3 导航框](#navboxes)
  - [2.2 页面创建](#page-creation)
- [3 另请参阅](#see-also)

## 将模板添加到页面

### 通过可视化编辑器

使用可视化编辑器插入模板

可以通过点击可视化编辑器上方的工具栏中的 _插入_ ，然后在下拉框中选择 _模板_ 来搜索和添加模板。大多数模板都可以通过这种方式轻松插入到页面中。要稍后编辑其内容，只需在可视化编辑器中单击插入的模板即可获取选项。

### 通过源代码编辑器

模板通过使用双括号 `{{ ... }}` 添加。例如，模板 `foo` 通过键入 `{{foo}}` 添加。

| 模板的参数通过使用管道符 ` | ` 指定。 |

- 带有一个参数的模板：
| - 代码：`{{enchantment | +1}}` |
  - 结果：惑控学派：**+ 1**
- 带有多个参数的模板：
| - 代码：`{{AttributeBlock | 8 | 15 | 7 | 6 | 10 | 8 | dex save = yes | race=Bird | hp=10}}` |
- 结果：

| [力量](Strength.md "力量") 8 (-1) | [敏捷](Dexterity.md "敏捷") 15 (+2) | [体质](Constitution.md "体质") 7 (-2) | [智力](Intelligence.md "智力") 6 (-2) | [感知](Wisdom.md "感知") 10 | [魅力](Charisma.md "魅力") 8 (-1) |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| 种族 | 鸟 |  |  |  |  |
| 生命值 | 10 |  |  |  |  |

## 模板的具体用途

### 添加页面导航

#### 页首注释

当一篇文章的主题与另一篇相似但不同时，可以使用 [页首注释](Template_colon_Hatnote.md "模板:页首注释") 模板在文章顶部添加一个注释，并附上指向另一篇文章的链接。

#### 歧义页

当存在多个同名文章时，可以使用 [歧义](Template_colon_Disambig.md "模板:歧义") 模板创建歧义页。

#### 导航框

BG3Wiki 上的许多页面都使用“导航框”来创建相关主题页面之间的导航。导航框的完整列表可在此处找到：[导航框](Help_colon_List_of_templates.md#Navboxes "帮助:模板列表")。

### 页面创建

模板可以接受标准参数形式的输入，并使用它来生成预格式化的页面。

## 另请参阅

- [MediaWiki 帮助:模板](https://www.mediawiki.org/wiki/Help:Templates)
- [模板快速参考](Help_colon_Template_Quick_Reference.md "帮助:模板快速参考")

---
*Source: [Help:Using templates](https://bg3.wiki/wiki/Help:Using_templates)*