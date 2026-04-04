# 挑衅攻击（远程）

本文介绍的是该攻击的远程版本。关于近战版本，请参见[挑衅攻击（近战）](Goading_Attack_(Melee)..md)

**挑衅攻击（远程）**是[战斗大师](Battle_Master.md "战斗大师")的武器动作。这项战斗策略允许战斗大师嘲讽另一个生物攻击自己，同时造成额外伤害。

## 描述

嘲讽一个敌人只攻击你。它在攻击除你以外的目标时获得[劣势](Disadvantage.md "劣势")。_\[[参见：漏洞](#bugs)\]_

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中时消耗
[卓越骰子](Battle_Master.md#Level_3 "战斗大师")
伤害：

普通武器伤害

\+ [卓越骰子](Battlemaster.md#Superiority_dice "战斗大师")

详情
远程武器[攻击掷骰](Attack_roll.md "攻击掷骰")
[感知](Wisdom.md "Wisdom") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰")）
射程：普通武器射程

## 高等级时

在10级时，拥有[精通卓越战技](Improved_Combat_Superiority.md "精通卓越战技")，伤害加成从1d8提升至1d10。

## 技术细节

UID

`Projectile_GoadingAttack`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：被挑衅

**[被挑衅](Goaded_(Condition).md "被挑衅（状态）")**

持续时间：1回合

[感知](Wisdom.md "Wisdom") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰")）

- 如果可能，必须攻击挑衅的生物。
- 在攻击施法者以外的目标时获得[劣势](Disadvantage.md "劣势")。

## 如何习得

职业：

- 职业等级3：[战斗大师](Battle_Master.md "战斗大师")

由特性授予：

- [战技专家](Martial_Adept.md "战技专家")

## 漏洞

- 目标在所有攻击上都有[劣势](Disadvantage.md "劣势")，即使是对挑衅攻击者也是如此。

---
*Source: [Goading Attack (Ranged)](https://bg3.wiki/wiki/Goading_Attack_(Ranged)*