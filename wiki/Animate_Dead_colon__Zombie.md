# 操纵死尸：僵尸

**操纵死尸：僵尸** 是一个 [3级死灵学派法术](Spells.md "法术")。此法术允许施法者操纵一具尸体，创造一个擅长近战的 [僵尸](Zombie_(Animate_Dead).md "僵尸（操纵死尸）")。他们必须以一具尸体为目标，该僵尸会持续存在直到被杀死或下一次长休。

## 描述

创造一个擅长近战的僵尸。

目标必须是一具中型或小型尸体。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
射程：3米（10英尺）
目标：中型或小型尸体

## 更高环位施法

以更高环位施法此法术不会获得额外收益。

## 技术细节

UID

`Target_AnimateDead_Zombie`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 生物：僵尸（操纵死尸）

| [力](Strength.md "力量") 16 (+3) | [敏](Dexterity.md "敏捷") 6 (-2) | [体](Constitution.md "体质") 16 (+3) | [智](Intelligence.md "智力") 3 (-4) | [感](Wisdom.md "感知") 6 (-2) | [魅](Charisma.md "魅力") 5 (-3) |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| 持续时间 | 直至长休 |  |  |  |  |
| 生命值 | 22 |  |  |  |  |
| 护甲等级 | 8 |  |  |  |  |

用你的赤手空拳击中目标，并用 [蠕行啃咬](Crawling_Gnaw_(Condition).md "蠕行啃咬（状态）") 感染它。

## 如何习得

此法术是以下法术的变体：
[操纵死尸](Animate_Dead.md "操纵死尸")

## 备注

- 此僵尸会施加一个名为 [蠕行啃咬](Crawling_Gnaw_(Condition).md "蠕行啃咬（状态）") 的状态。如果一个敌人在拥有此状态时被杀死，会从其尸体中自动生成一个 [新生僵尸](Newborn_Zombie.md "新生僵尸")。

---
*Source: [Animate Dead: Zombie](https://bg3.wiki/wiki/Animate_Dead:_Zombie)*