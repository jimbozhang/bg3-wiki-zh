# 恐惧射线

本文介绍的是观察者眼魔NPC使用的技能。关于由观察者之眼授予的版本，请参见[恐惧射线](Ray_of_Fear.md "恐惧射线")。

**恐惧射线**是[观察者眼魔](Spectator.md "观察者眼魔")可用的类动作，允许它们恐吓一个目标。

## 描述

发射一道眼射线，使目标[恐慌](Frightened_(Condition).md "恐慌（状态）")。

## 属性

消耗
[眼柄动作](Spectator.md#Combat "观察者眼魔")
详情
[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
射程：18米（60英尺）
充能：每回合

## 技术细节

UID

`Target_FearRay_Spectator`

`Target_UND_Spectator_Ray_Fear`

法术标志

`[CannotRotate](https://bg3.wiki/w/index.php?title=CannotRotate_\(spell_flag\)&action=edit&redlink=1) "CannotRotate \(spell flag\) \(页面不存在\)")`, `[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(页面不存在\)")`

## 状态：恐慌

**[恐慌](Frightened_(Condition).md "恐慌（状态）")**

持续时间：2回合

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动。恐慌的生物在[属性检定](Ability_Check.md "属性检定")和[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")。

## 如何习得

由生物使用：[观察者眼魔](Spectator.md "观察者眼魔")

## 备注

- 观察者眼魔每回合有两个[眼柄动作](Spectator.md#Combat "观察者眼魔")来使用其射线攻击，但每个单独的射线每回合只能使用一次。
- 处于[减速](Slowed_(Condition).md "减速（状态）")状态时无法使用此动作。减速时，观察者眼魔唯一能使用的射线攻击是[致伤射线](Wounding_Ray.md "致伤射线")。

## 错误

- 此技能的工具提示说明其会施加持续3回合的[恐慌](Frightened_(Condition).md "恐慌（状态）")。

---
*Source: [Fear Ray](https://bg3.wiki/wiki/Fear_Ray)*