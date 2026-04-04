# 偷袭（远程）

本文介绍的是攻击的远程版本。对于近战版本，请参见 [偷袭（近战）](Sneak_Attack_(Melee).md)>。对于其他用途，请参见 [偷袭（消歧义）](Sneak_Attack_(disambiguation).md)>。

**偷袭（远程）** 是 [游荡者](Rogue.md "游荡者") 的武器动作和反应。此能力允许游荡者利用敌人的分心，使用远程武器对其弱点造成额外伤害。

## 描述

对一名你拥有 [优势](Advantage.md "优势") 的敌人造成额外 1d6 伤害。

如果你在目标 1.5 米（5 英尺）范围内有一名盟友，且你没有 [劣势](Disadvantage.md "劣势")，你也可以使用偷袭。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~6

正常武器伤害

\+ 1d6⁠[武器](Weapon.md "武器")

详情
射程：正常武器射程
充能：每回合

## 更高等级

每超过 1 级 [游荡者](Rogue.md "游荡者") 2 级，偷袭额外造成 1d6⁠⁠[物理](Physical.md "物理") 伤害，最高在 11 级时达到 6d6：

- 3 级时：2d6⁠⁠[武器](Weapon.md "武器")
- 5 级时：3d6⁠⁠[武器](Weapon.md "武器")
- 7 级时：4d6⁠⁠[武器](Weapon.md "武器")
- 9 级时：5d6⁠⁠[武器](Weapon.md "武器")
- 11 级时：6d6⁠⁠[武器](Weapon.md "武器")

## 技术细节

UID

`Projectile_SneakAttack`

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell_flag\) \(page does not exist\)")`, `[CannotTargetTerrain](https://bg3.wiki/w/index.php?title=CannotTargetTerrain_\(spell_flag\)&action=edit&redlink=1) "CannotTargetTerrain \(spell_flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell_flag\) \(page does not exist\)")`

## 如何习得

职业：

- 职业等级 1：[游荡者](Rogue.md "游荡者")

## 备注

- 偷袭可以直接通过此动作使用，也可以在任何其他远程武器攻击命中后作为攻击后反应触发。此反应通过 [反应选项卡](Actions.md#Reactions "动作") 配置，但不消耗 [反应](Actions.md#Reactions "动作") 资源。
- 如果偷袭通过反应系统应用于触发攻击，则视为 [伤害附加源](Damage_rider_source.md "伤害附加源")（仅限硬核及以下难度）。
- 由副手攻击触发的偷袭使用主手远程武器的伤害类型。例如，在主手装备 [从未射失](Ne'er_Misser.md "从未射失") 会导致副手偷袭造成 ⁠[力场](Force.md "力场") 伤害。
- 此动作在双持 [手弩](Hand_Crossbows.md "手弩") 时不会自动触发副手攻击。

---
*Source: [Sneak Attack (Ranged)](https://bg3.wiki/wiki/Sneak_Attack_(Ranged)*