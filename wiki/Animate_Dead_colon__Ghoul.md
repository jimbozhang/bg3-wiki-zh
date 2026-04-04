# 操纵死尸：食尸鬼

**操纵死尸：食尸鬼**是一个[5级死灵学派法术](Spells.md "Spells")。此法术允许施法者操纵一具尸体以创造一个[食尸鬼（操纵死尸）](Ghoul_(Animate_Dead).md "食尸鬼（操纵死尸）")。需要一具尸体，并持续至长休。

## 描述

创造一个擅长近战战斗的食尸鬼。

目标必须是一具中型或小型尸体。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [5级法术位](Spells.md#Spell_slots "法术")
详情
范围：3米（10英尺）

## 更高环阶

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_AnimateDead_Ghoul`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 生物：食尸鬼（操纵死尸）

| [力量](Strength.md "力量") 16 (+3) | [敏捷](Dexterity.md "敏捷") 17 (+3) | [体质](Constitution.md "体质") 10 | [智力](Intelligence.md "智力") 11 | [感知](Wisdom.md "感知") 10 | [魅力](Charisma.md "魅力") 8 (-1) |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| 持续时间 | 直至长休 |  |  |  |  |
| 生命值 | 35 |  |  |  |  |
| 护甲等级 | 17 |  |  |  |  |

[爪击](Claws_(Animate_Dead_Ghoul).md "爪击（操纵死尸食尸鬼）") ()
用致命的爪子猛击，并可能使目标[麻痹](Paralysed_(Condition).md "麻痹（状态）")。

[吞噬](Devour_(Animate_Dead_Ghoul).md "吞噬（操纵死尸食尸鬼）") ()

啃咬一个倒地、倒伏或沉睡的目标，造成3d10 + 力量调整值[挥砍](Slashing.md "挥砍")伤害。治疗等同于该伤害值的生命值。

## 如何学习

此法术是以下法术的变体：
[操纵死尸](Animate_Dead.md "操纵死尸")

## 错误

- 由于编码错误，由[死灵学派](Necromancy_School.md "死灵学派")法师使用[不死奴仆：高等召唤](Undead_Thralls_colon__Better_Summons.md "不死奴仆：高等召唤")召唤的食尸鬼，在受到[复苏瘴气](Rejuvenating_Miasma_(Condition).md "复苏瘴气（状态）")影响时，除非以尸体为目标，否则无法生成，从而浪费了用于施放操纵死尸的法术位。

---
*Source: [Animate Dead: Ghoul](https://bg3.wiki/wiki/Animate_Dead:_Ghoul)*