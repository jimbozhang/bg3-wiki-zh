# 卡哈的信

本文介绍的内容在**[正常游戏过程中无法获取](Category_colon_Inaccessible.md "Category:Inaccessible")**。但仍可通过第三方工具访问。

**卡哈的信**是玩家角色在[终章](Epilogue.md "Epilogue")中可以收到的信件之一。

一张朴素无华的便条。

## 属性

- [笔记](Notes.md "Notes")

- 作者：[卡哈](Kagha.md "Kagha")

- 稀有度：普通

- 重量：0.05 千克 (0.1 磅)

- 价格：14 金币

- UID `S_EPI_Letter_Kagha` UUID `c0de891b-f804-4d89-953d-97c5dcd54946` ## 获取地点

- 在[感恩之箱](Chest_of_Grateful_Words.md "Chest_of_Grateful Words")中

## 文本

我的朋友，

在我漫长的一生中，我走过许多道路，有些被阴影纠缠，有些布满荆棘。但没有哪条路比宽恕之路更难行走。[席尔瓦努斯](Silvanus.md "Silvanus")的宽恕，我德鲁伊同袍的宽恕——以及，我希望，还有你的宽恕。

当我曾是翻腾的风暴时，[高林大德鲁伊弗朗西斯卡](Francesca.md "Francesca")是温暖的午后阳光。她再次任命我为见习德鲁伊，我欣然接受了这个头衔。我曾自诩为母亲，但她教导我，我仍是那最青嫩的嫩芽。仍在成长，仍在追寻光明。

[翠绿林地](Emerald_Grove.md "Emerald Grove")回荡着新的和谐。我多么希望你能听到它。

致以永恒的感激，

卡哈

## 注释

- 取决于卡哈在[第一幕](Act_One.md "Act One")中存活并忏悔。
- 此信目前（补丁 #8，热修复 #34）无法获得，因为要发送此信，需要检查默认状态下是否设置了标志 `DEN_GroveHostileState_04a03da4-b046-4332-9e1e-d6719626c210`，但该标志从未以这种方式设置。它会检查林地状态是否变为默认状态列表之外的任何状态。当提夫林离开林地时，状态会变为 `DEN_State_Final`，而该状态不在默认状态列表中。因此，该标志无法在默认状态下设置，信件也无法发送。

---
*Source: [Letter from Kagha](https://bg3.wiki/wiki/Letter_from_Kagha)*