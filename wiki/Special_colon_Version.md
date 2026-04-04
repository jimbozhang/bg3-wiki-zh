# 版本

[跳转到导航](#mw-head) [跳转到搜索](#searchInput)

## MediaWiki 许可证

本维基由 **[MediaWiki](https://www.mediawiki.org/)** 提供支持，版权 © 2001-2026 Magnus Manske, Brooke Vibber, Lee Daniel Crocker, Tim Starling, Erik Möller, Gabriel Wicke, Ævar Arnfjörð Bjarmason, Niklas Laxström, Domas Mituzas, Rob Church, Yuri Astrakhan, Aryeh Gregor, Aaron Schulz, Andrew Garrett, Raimond Spekking, Alexandre Emsenhuber, Siebrand Mazeland, Chad Horohoe, Roan Kattouw, Trevor Parscal, Bryan Tong Minh, Sam Reed, Victor Vasiliev, Rotem Liss, Platonides, Antoine Musso, Timo Tijhof, Daniel Kinzler, Jeroen De Dauw, Brad Jorsch, Bartosz Dziewoński, Ed Sanders, Moriel Schottlender, Kunal Mehta, James D. Forrester, Brian Wolff, Adam Shorland, DannyS712, Ori Livneh, Max Semenik, Amir Sarabadani, Derk-Jan Hartman, Petr Pchelko, [其他人](Special_colon_Version/Credits.md "Special:Version/Credits") 以及 [translatewiki.net 翻译者](https://translatewiki.net/wiki/Translating:MediaWiki/Credits)。

MediaWiki 是自由软件；您可以根据自由软件基金会发布的 GNU 通用公共许可证条款重新分发和/或修改它；可以选择许可证的第 2 版，或（根据您的选择）任何更高版本。

MediaWiki 分发的目的是希望它有用，但 _不提供任何保证_；不提供任何**适销性**或**特定用途适用性**的默示保证。有关更多详细信息，请参阅 GNU 通用公共许可证。

您应该随本程序一起收到[一份 GNU 通用公共许可证副本](https://bg3.wiki/w/COPYING)；如果没有，请[在线阅读](//www.gnu.org/licenses/old-licenses/gpl-2.0.md)。

## 目录

- [1 已安装软件](#已安装软件)
- [2 入口点 URL](#入口点-URL)
- [3 已安装皮肤](#已安装皮肤)
- [4 已安装扩展](#已安装扩展)
  - [4.1 特殊页面](#sv-credits-specialpage)
  - [4.2 编辑器](#sv-credits-editor)
  - [4.3 解析器钩子](#sv-credits-parserhook)
  - [4.4 媒体处理器](#sv-credits-media)
  - [4.5 垃圾邮件防护](#sv-credits-antispam)
  - [4.6 API](#sv-credits-api)
  - [4.7 其他](#sv-credits-other)
- [5 已安装库](#已安装库)
  - [5.1 已安装服务器端库](#已安装服务器端库)
  - [5.2 已安装客户端库](#已安装客户端库)
- [6 解析器扩展标签](#mw-version-parser-extensiontags)
- [7 解析器函数钩子](#mw-version-parser-function-hooks)

## 已安装软件

2026年1月11日 04:07
| [PHP](https://php.net/) | 8.4.16 (fpm-fcgi) [ICU](https://icu.unicode.org/) | 76.1 [MariaDB](https://mariadb.org/) | 11.8.6-MariaDB-0+deb13u1 from Debian [Elasticsearch](https://www.elastic.co/elasticsearch) | 7.10.2 [LuaSandbox](https://www.mediawiki.org/wiki/LuaSandbox) | 4.1.2 [Lua](http://www.lua.org/) | 5.1.5 [Pygments](https://pygments.org/) | 2.19.2 [libvips](https://www.libvips.org) | 8.16.1 |

## 入口点 URL

## 已安装皮肤

| 产品 | 版本 |
| --- | --- |
| [MediaWiki](https://www.mediawiki.org/ "MediaWiki") | [1.43.6](https://www.mediawiki.org/wiki/MediaWiki_1.43 "1.43.6") [(81f6d5f)](https://gerrit.wikimedia.org/g/mediawiki/core.git/+/81f6d5f6cb2aeac0ada7510db97b01592b3c20d7 "(81f6d5f)") / 2026年1月11日 04:07 |
| [PHP](https://php.net/ "PHP") | 8.4.16 (fpm-fcgi) |
| [ICU](https://icu.unicode.org/ "ICU") | 76.1 |
| [MariaDB](https://mariadb.org/ "MariaDB") | 11.8.6-MariaDB-0+deb13u1 from Debian |
| [Elasticsearch](https://www.elastic.co/elasticsearch "Elasticsearch") | 7.10.2 |
| [LuaSandbox](https://www.mediawiki.org/wiki/LuaSandbox "LuaSandbox") | 4.1.2 |
| [Lua](http://www.lua.org/ "Lua") | 5.1.5 |
| [Pygments](https://pygments.org/ "Pygments") | 2.19.2 |
| [libvips](https://www.libvips.org "libvips") | 8.16.1 |

- 2011 - MonoBook 的现代版本，具有全新的外观和许多可用性改进。
- 2022 - Vector 作为 WMF [桌面改进](https://www.mediawiki.org/wiki/Desktop_Improvements) 项目的一部分构建。

| [读者网络团队](https://www.mediawiki.org/wiki/Readers/Web/Team), Trevor Parscal, Roan Kattouw, Alex Hollender, Bernard Wang, Clare Ming, Jan Drewniak, Jon Robson, Nick Ray, Sam Smith, Stephen Niedzielski 和 Volker E.|

## 已安装扩展

| 入口点 | URL |
| --- | --- |
| [文章路径](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:$wgArticlePath "Article path") | [/wiki/$1](https://bg3.wiki/wiki/$1 "/wiki/$1") |
| [脚本路径](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:$wgScriptPath "Script path") | [/w](https://bg3.wiki/w "/w") |
| [index.php](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:index.php "index.php") | [/w/index.php](https://bg3.wiki/w/index.php "/w/index.php") |
| [api.php](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:api.php "api.php") | [/w/api.php](https://bg3.wiki/w/api.php "/w/api.php") |
| [rest.php](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:rest.php "rest.php") | [/w/rest.php](https://bg3.wiki/w/rest.php "/w/rest.php") |

## 已安装库

### 已安装服务器端库

| 皮肤 | 版本 | 许可证 | 描述 | 作者 |
| --- | --- | --- | --- | --- |
| [Citizen](https://www.mediawiki.org/wiki/Skin:Citizen "Citizen") | 3.12.0 (262790e) 2025年12月25日 00:32 | [GPL-3.0-or-later](Special_colon_Version/License/Citizen.md "Special:Version/License/Citizen") | 一款美观、可用、响应式的 MediaWiki 皮肤，使扩展成为连贯体验的一部分。最初为 [Star Citizen Wiki](https://starcitizen.tools/ "Star Citizen Wiki") 创建。 | [Alistair3149](https://www.mediawiki.org/wiki/User:Alistair3149 "Alistair3149"), [Octfx](https://www.mediawiki.org/wiki/User:Octfx "Octfx") 和其他人 |
| [Vector](https://www.mediawiki.org/wiki/Skin:Vector "Vector") | 1.0.0 [(227b9dd)](https://gerrit.wikimedia.org/g/mediawiki/skins/Vector/+/227b9dd87e17c2bc21214a5e69514a442cb20100 "(227b9dd)") 2026年1月6日 08:09 | [GPL-2.0-or-later](Special_colon_Version/License/Vector.md "Special:Version/License/Vector") | 提供 2 种 Vector 皮肤：2011 - MonoBook 的现代版本，具有全新的外观和许多可用性改进。2022 - Vector 作为 WMF [桌面改进](https://www.mediawiki.org/wiki/Desktop_Improvements "Desktop Improvements") 项目的一部分构建。 | [读者网络团队](https://www.mediawiki.org/wiki/Readers/Web/Team "Readers Web Team"), Trevor Parscal, Roan Kattouw, Alex Hollender, Bernard Wang, Clare Ming, Jan Drewniak, Jon Robson, Nick Ray, Sam Smith, Stephen Niedzielski 和 Volker E. |

### 已安装客户端库

| 扩展 | 版本 | 许可证 | 描述 | 作者 |
| --- | --- | --- | --- | --- |
| [CheckUser](https://www.mediawiki.org/wiki/Extension:CheckUser "CheckUser") | 2.5 [(6b4befc)](https://gerrit.wikimedia.org/g/mediawiki/extensions/CheckUser/+/6b4befcad776d710e357b9ec88d6488f96b32664 "(6b4befc)") 2026年1月8日 23:50 | [GPL-2.0-or-later](Special_colon_Version/License/CheckUser.md "Special:Version/License/CheckUser") | 授予具有适当权限的用户检查用户 IP 地址和其他信息的能力 | Tim Starling, Aaron Schulz 和 Dreamy Jazz |
| [ContributionScores](https://www.mediawiki.org/wiki/Extension:Contribution_Scores "ContributionScores") | 1.26.1 (a00a217) 2024年11月23日 07:17 |  | 轮询维基数据库以获取最高的[用户贡献量](Special_colon_ContributionScores.md "Special:ContributionScores") | Tim Laqua |
| [Delete Batch](https://www.mediawiki.org/wiki/Extension:DeleteBatch "Delete Batch") | 1.8.1 (34e639a) 2025年12月30日 08:18 | [GPL-2.0-or-later](Special_colon_Version/License/DeleteBatch.md "Special:Version/License/DeleteBatch") | [批量删除页面](Special_colon_DeleteBatch.md "Special:DeleteBatch") | Bartek Łapiński 和其他人 |
| [Echo](https://www.mediawiki.org/wiki/Extension:Echo "Echo") | – [(d9efc54)](https://gerrit.wikimedia.org/g/mediawiki/extensions/Echo/+/d9efc54c7a8ec00d7ad59ca9359cc1f9cc241d84 "(d9efc54)") 2026年1月6日 07:37 | [MIT](Special_colon_Version/License/Echo.md "Special:Version/License/Echo") | 用于通知用户事件和消息的系统 | Andrew Garrett, Ryan Kaldari, Benny Situ, Luke Welling, Kunal Mehta, Moriel Schottlender, Jon Robson 和 Roan Kattouw |
| [Linter](https://www.mediawiki.org/wiki/Extension:Linter "Linter") | – [(2f4ced0)](https://gerrit.wikimedia.org/g/mediawiki/extensions/Linter/+/2f4ced0accd45c81169ca41af099164d78596866 "(2f4ced0)") 2026年1月6日 07:43 | [GPL-2.0-or-later](Special_colon_Version/License/Linter.md "Special:Version/License/Linter") | 跟踪来自外部服务的 lint 错误并向用户显示 | Kunal Mehta, Arlo Breault 和 Subramanya Sastry |
| [Mass Edit via Regular Expressions](https://www.mediawiki.org/wiki/Extension:MassEditRegex "Mass Edit via Regular Expressions") | 8.4.1 (a3649a5) 2026年1月6日 07:43 | [GPL-2.0-or-later](Special_colon_Version/License/MassEditRegex.md "Special:Version/License/MassEditRegex") | 允许使用正则表达式[一次操作编辑多个页面](Special_colon_MassEditRegex.md "Special:MassEditRegex") | Adam Nielsen 和其他人 |
| [SimpleBatchUpload](https://professional.wiki/en/extension/simplebatchupload "SimpleBatchUpload") | 3.0.0 (f73bfb4) 2025年11月24日 14:12 | [GPL-2.0-or-later](Special_colon_Version/License/SimpleBatchUpload.md "Special:Version/License/SimpleBatchUpload") | 允许简单地批量上传文件 | [Stephan Gambke](https://www.mediawiki.org/wiki/User:F.trott "Stephan Gambke"), [Professional Wiki](https://professional.wiki/ "Professional Wiki") 和其他人 |
| [UserMerge](https://www.mediawiki.org/wiki/Extension:UserMerge "UserMerge") | 1.10.2 [(fcfcb5d)](https://gerrit.wikimedia.org/g/mediawiki/extensions/UserMerge/+/fcfcb5dde85c0b9b6c322675b61a7bd4c8a266b0 "(fcfcb5d)") 2025年12月2日 08:23 | [GPL-2.0-or-later](Special_colon_Version/License/UserMerge.md "Special:Version/License/UserMerge") | [将一个用户的引用合并到另一个用户](Special_colon_UserMerge.md "Special:UserMerge")到维基数据库中 - 合并后也将删除旧用户。需要 usermerge 权限 | Tim Laqua, Thomas Gries 和 Matthew April |

## [解析器扩展标签](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Tag_extensions)

`<ab>`, `<archiveorg>`, `<bandcamp>`, `<bilibili>`, `<categorytree>`, `<ccc>`, `<ce>`, `<chem>`, `<dailymotion>`, `<deezeralbum>`, `<deezerartist>`, `<deezerepisode>`, `<deezerplaylist>`, `<deezershow>`, `<deezertrack>`, `<details>`, `<embedvideo>`, `<evlplayer>`, `<externalvideo>`, `<gallery>`, `<htmltag>`, `<imagemap>`, `<indicator>`, `<infobox>`, `<kakaotv>`, `<langconvert>`, `<loom>`, `<math>`, `<mobileonly>`, `<navertv>`, `<niconico>`, `<nomobile>`, `<nowiki>`, `<poem>`, `<pre>`, `<ref>`, `<references>`, `<section>`, `<seo>`, `<sharepoint>`, `<soundcloud>`, `<source>`, `<spotifyalbum>`, `<spotifyartist>`, `<spotifyepisode>`, `<spotifyshow>`, `<spotifytrack>`, `<substack>`, `<summary>`, `<syntaxhighlight>`, `<tabber>`, `<tabbertransclude>`, `<templatedata>`, `<templatestyles>`, `<twitch>`, `<twitchclip>`, `<twitchvod>`, `<videolink>`, `<vimeo>`, `<vk>`, `<vplayer>`, `<wistia>`, `<youku>`, `<youtube>`, `<youtubeoembed>`, `<youtubeplaylist>` 和 `<youtubevideolist>`

## [解析器函数钩子](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Parser_functions)

`{{#af_bool}}`, `{{#af_count}}`, `{{#af_difference}}`, `{{#af_exists}}`, `{{#af_float}}`, `{{#af_foreach}}`, `{{#af_get}}`, `{{#af_if}}`, `{{#af_int}}`, `{{#af_intersect}}`, `{{#af_isarray}}`, `{{#af_join}}`, `{{#af_keysort}}`, `{{#af_ksort}}`, `{{#af_list}}`, `{{#af_map}}`, `{{#af_merge}}`, `{{#af_object}}`, `{{#af_print}}`, `{{#af_push}}`, `{{#af_reduce}}`, `{{#af_search}}`, `{{#af_set}}`, `{{#af_show}}`, `{{#af_slice}}`, `{{#af_sort}}`, `{{#af_split}}`, `{{#af_stringmap}}`, `{{#af_template}}`, `{{#af_trim}}`, `{{#af_unique}}`, `{{#af_unset}}`, `{{anchorencode}}`, `{{#arraydefine}}`, `{{#arraydiff}}`, `{{#arrayindex}}`, `{{#arrayintersect}}`, `{{#arraymerge}}`, `{{#arrayprint}}`, `{{#arrayreset}}`, `{{#arraysearch}}`, `{{#arraysearcharray}}`, `{{#arraysize}}`, `{{#arrayslice}}`, `{{#arraysort}}`, `{{#arrayunion}}`, `{{#arrayunique}}`, `{{BASEPAGENAME}}`, `{{BASEPAGENAMEE}}`, `{{#batchupload}}`, `{{#bcp47}}`, `{{bidi}}`, `{{canonicalurl}}`, `{{canonicalurle}}`, `{{#cargo_attach}}`, `{{#cargo_compound_query}}`, `{{#cargo_declare}}`, `{{#cargo_display_map}}`, `{{#cargo_query}}`, `{{#cargo_store}}`, `{{CASCADINGSOURCES}}`, `{{#categorytree}}`, `{{#count}}`, `{{#cscore}}`, `{{#css}}`, `{{DEFAULTSORT}}`, `{{#dir}}`, `{{DISPLAYTITLE}}`, `{{#dowhile}}`, `{{#ev}}`, `{{#evl}}`, `{{#evt}}`, `{{#evu}}`, `{{#explode}}`, `{{#expr}}`, `{{filepath}}`, `{{#forargs}}`, `{{#FORMAL}}`, `{{#formatdate}}`, `{{formatnum}}`, `{{#fornumargs}}`, `{{FULLPAGENAME}}`, `{{FULLPAGENAMEE}}`, `{{fullurl}}`, `{{fullurle}}`, `{{gender}}`, `{{grammar}}`, `{{#if}}`, `{{#ifeq}}`, `{{#iferror}}`, `{{#ifexist}}`, `{{#ifexpr}}`, `{{int}}`, `{{#invoke}}`, `{{#language}}`, `{{lc}}`, `{{lcfirst}}`, `{{#len}}`, `{{localurl}}`, `{{localurle}}`, `{{#loop}}`, `{{#lst}}`, `{{#lsth}}`, `{{#lstx}}`, `{{#lvar}}`, `{{#lvardef}}`, `{{#mobileonly}}`, `{{NAMESPACE}}`, `{{NAMESPACEE}}`, `{{NAMESPACENUMBER}}`, `{{#nomobile}}`, `{{ns}}`, `{{nse}}`, `{{NUMBERINGROUP}}`, `{{NUMBEROFACTIVEUSERS}}`, `{{NUMBEROFADMINS}}`, `{{NUMBEROFARTICLES}}`, `{{NUMBEROFEDITS}}`, `{{NUMBEROFFILES}}`, `{{NUMBEROFPAGES}}`, `{{NUMBEROFUSERS}}`, `{{padleft}}`, `{{padright}}`, `{{pageid}}`, `{{PAGENAME}}`, `{{PAGENAMEE}}`, `{{PAGESINCATEGORY}}`, `{{PAGESIZE}}`, `{{plural}}`, `{{#pos}}`, `{{PROTECTIONEXPIRY}}`, `{{PROTECTIONLEVEL}}`, `{{#recurring_event}}`, `{{#rel2abs}}`, `{{#replace}}`, `{{REVISIONDAY}}`, `{{REVISIONDAY2}}`, `{{REVISIONID}}`, `{{REVISIONMONTH}}`, `{{REVISIONMONTH1}}`, `{{REVISIONTIMESTAMP}}`, `{{REVISIONUSER}}`, `{{REVISIONYEAR}}`, `{{#rmatch}}`, `{{ROOTPAGENAME}}`, `{{ROOTPAGENAMEE}}`, `{{#rpos}}`, `{{#rreplace}}`, `{{#rsplit}}`, `{{#seo}}`, `{{#special}}`, `{{#speciale}}`, `{{#sub}}`, `{{SUBJECTPAGENAME}}`, `{{SUBJECTPAGENAMEE}}`, `{{SUBJECTSPACE}}`, `{{SUBJECTSPACEE}}`, `{{SUBPAGENAME}}`, `{{SUBPAGENAMEE}}`, `{{#switch}}`, `{{#tag}}`, `{{TALKPAGENAME}}`, `{{TALKPAGENAMEE}}`, `{{TALKSPACE}}`, `{{TALKSPACEE}}`, `{{#time}}`, `{{#timef}}`, `{{#timefl}}`, `{{#timel}}`, `{{#titleparts}}`, `{{uc}}`, `{{ucfirst}}`, `{{#urldecode}}`, `{{urlencode}}`, `{{#var}}`, `{{#vardefine}}`, `{{#vardefineecho}}`, `{{#varexists}}`, `{{#vlink}}`, `{{#while}}` 和 `{{#widget}}` 由 111.201.29.46 访问

从 "<https://bg3.wiki/wiki/Special:Version>" 检索

## 导航菜单

### 个人工具

- 未登录
- [讨论](Special_colon_MyTalk.md "讨论此 IP 地址的编辑 [n]")
- [贡献](Special_colon_MyContributions.md "从此 IP 地址进行的编辑列表 [y]")
- [创建账户](https://bg3.wiki/w/index.php?title=Special:CreateAccount&returnto=Special%3AVersion "鼓励您创建账户并登录；但这不是强制性的")
- [登录](https://bg3.wiki/w/index.php?title=Special:UserLogin&returnto=Special%3AVersion "鼓励您登录；但这不是强制性的 [o]")

### 命名空间

- [特殊页面](Special_colon_Version.md "这是一个特殊页面，无法编辑")

English

### 视图

更多

### 搜索

### 导航

- [主页](/ "访问主页 [z]")
- [帮助索引](Help_colon_Index.md)
- [学习编辑](Help_colon_Editing_manual.md)
- [指南](Help_colon_Guide_namespace.md)
- [模组](Modding_colon_Modding_resources.md)
- [上传文件](Special_colon_Upload.md)
- [Discord](https://discord.gg/EYNTAQXaNs)
- [备份](bg3wiki_colon_Backups.md)
- [支付](bg3wiki_colon_Payment.md)

### 特殊

- [近期更改](Special_colon_RecentChanges.md "维基中近期更改的列表 [r]")
- [新添加的文件](Special_colon_NewFiles.md)
- [特殊页面](Special_colon_SpecialPages.md)
- [随机页面](Special_colon_Random.md "加载随机页面 [x]")
- [维护](Category_colon_Wiki_maintenance.md)
- [版本](Special_colon_Version.md)

### 工具

- [特殊页面](Special_colon_SpecialPages.md "所有特殊页面的列表 [q]")
- \[可打印版本\](\<javascript:print();> "此页面的可打印版本 [p]")

### 广告

- [关于 bg3.wiki 上的广告](bg3wiki_colon_Ads.md)
- [请报告不良广告](bg3wiki_colon_Report_ads.md)

广告占位符

- [隐私政策](bg3wiki_colon_Privacy_policy.md)

- [关于 bg3.wiki](bg3wiki_colon_About.md)

- [版权](bg3wiki_colon_Copyrights.md)

- [移动视图](https://bg3.wiki/w/index.php?title=Special:Version&mobileaction=toggle_view_mobile)

- \*\[v\]: 查看此模板

---
*来源: [Special:Version](https://bg3.wiki/wiki/Special:Version)*

---
*Source: [Special:Version](https://bg3.wiki/wiki/Special:Version)*
