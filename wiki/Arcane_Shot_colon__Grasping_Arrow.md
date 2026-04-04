# 奥术射击：缠绕箭

**奥术射击：缠绕箭**是[奥术射手](Arcane_Archer.md "奥术射手")可用的一种特殊奥术箭攻击，可造成额外的2d6⁠⁠[中毒](Poison.md "中毒")伤害并阻碍目标的移动。

## 描述

造成额外的2d6⁠⁠[中毒](Poison.md "中毒")伤害。受影响实体的移动速度降低3米（10英尺），并且当其移动时将受到2d6⁠⁠[挥砍](Slashing.md "挥砍")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中消耗
[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")
伤害：4~24

普通武器伤害

\+ 2d6⁠[中毒](Poison.md "中毒")

\+ 2d6⁠[挥砍](Slashing.md "挥砍")（每回合移动时）

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
射程：普通武器射程

## 技术细节

UID

`Projectile_ArcaneShot_GraspingArrow`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：缠绕箭：缠绕

**[缠绕箭：缠绕](Grasping_Arrow_colon__Entangled_(Condition).md "缠绕箭：缠绕 (状态)")**

持续时间：10回合

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响实体移动时将受到2d6⁠⁠[挥砍](Slashing.md "挥砍")伤害，并且其[移动速度](Movement_speed.md "移动速度")降低3米（10英尺）。

## 如何习得

职业：

- 职业等级3：[奥术射手](Arcane_Archer.md "奥术射手")

## 错误

- 由于错误使用了`DamageBonus`函数，奥术射击在击中敌人时提供的额外伤害在[重击](Critical_Hit.md "重击")时不会翻倍。

---
*Source: [Arcane Shot: Grasping Arrow](https://bg3.wiki/wiki/Arcane_Shot:_Grasping_Arrow)*