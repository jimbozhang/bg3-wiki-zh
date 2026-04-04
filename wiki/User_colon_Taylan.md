你好，我是这个Wiki的创始人和系统管理员。你可以通过以下方式联系我：`bg3communitywiki (at) gmail (dot) com`，Twitter上的 [@bg3_wiki](https://twitter.com/bg3_wiki)，或者在各种平台和论坛上使用用户名 `Taylan`，例如 [bg3.wiki Discord](https://discord.gg/EYNTAQXaNs) 或 [Larian Studios Discord](https://discord.gg/ptuSAd97)、[Larian Forums](https://forums.larian.com/ubbthreads.php?ubb=showprofile&User=76178)、[Beamdog Forums](https://forums.beamdog.com/profile/Taylan) 或 [Gibberlings3 Forums](https://www.gibberlings3.net/profile/11620-taylan/)。你也可以在我的[用户讨论页](User_talk_colon_Taylan.md "User talk:Taylan")上@我。或者写信到我的个人邮箱 `taylan (dot) kammer (at) gmail (dot) com`。

## 目录

- [1 笔记、草稿、测试等如下](#notes,_drafts,_tests,_etc._follow)
  - [1.1 待办事项](#to-do)
  - [1.2 草稿空间](#draft-space)
- [2 H1](#h1)
  - [2.1 H2](#h2)
    - [2.1.1 H3](#h3)
      - [2.1.1.1 H4](#h4)
        - [2.1.1.1.1 H5](#h5)
          - [2.1.1.1.1.1 H6](#h6)

# 笔记、草稿、测试等如下

外部链接：[Example](https://example.org)

## 待办事项

- 将武器动作数据化

- 完成 [Template:SpellPage](Template_colon_SpellPage.md "Template:SpellPage")

- 对模板进行分类

- 对文件进行分类

- 对分类进行分类

- 为状态图标设计CSS技巧？

\---

一个很酷的想法：列出游戏中可以找到的普通'书籍'，并为它们创建页面，包含它们的文本。

## 草稿空间

未完成的Wiki代码，用于其他页面，放在这里。

\---

ArrayFunctions的示例用法。假设模板参数 `{{{list}}}` 包含值 `Foo, Bar`。

代码：

| {{#af_join: {{#af_map: {{#af_split: {{{list}}} }} | x | * \[[{{{x}}}]\] }} | \\n }} |

结果：

- [Foo](https://bg3.wiki/w/index.php?title=Foo&action=edit&redlink=1 "Foo (page does not exist)")
- [Bar](https://bg3.wiki/w/index.php?title=Bar&action=edit&redlink=1 "Bar (page does not exist)")

代码：

| 列表：{{#af_join: {{#af_map: {{#af_split: {{{list}}} }} | x | \[[{{{x}}}]\] }} | ,\\s }} |

结果：

列表：[Foo](https://bg3.wiki/w/index.php?title=Foo&action=edit&redlink=1 "Foo (page does not exist)"), [Bar](https://bg3.wiki/w/index.php?title=Bar&action=edit&redlink=1 "Bar (page does not exist)")

# H1

## H2

### H3

#### H4

##### H5

###### H6

---
*Source: [User:Taylan](https://bg3.wiki/wiki/User:Taylan)*