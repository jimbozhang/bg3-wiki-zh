# 跳跃（奔跑）

本文介绍由跃动指套授予的特殊跳跃动作。关于普通跳跃动作，请参阅 [跳跃](Jump.md "跳跃")。

**跳跃** 是 [跳跃](Jump.md "跳跃") 的一种独特变体，由 [跃动指套](Fleetfingers.md "跃动指套") 在 [疾走](Dash.md "疾走") 后授予，允许穿戴者免费跳跃，无需消耗 [移动速度](Resources.md#Movement_speed "资源") 或 [附赠动作](Actions.md#Resources "动作")。

## 描述

向上、向下或横向跳跃。你的 [力量](Strength.md "力量") 影响你能跳跃的距离。

## 属性

详情
范围：[跳跃](Jump.md "跳跃") 范围
充能：每回合

## 技术细节

UID

`Projectile_MAG_Mobility_JumpOnDash_Action`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[CannotTargetCharacter](https://bg3.wiki/w/index.php?title=CannotTargetCharacter_\(spell_flag\)&action=edit&redlink=1) "CannotTargetCharacter \(spell flag\) \(page does not exist\)")`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[Invisible](Invisible_(spell_flag).md)`, `[IsJump](https://bg3.wiki/w/index.php?title=IsJump_\(spell_flag\)&action=edit&redlink=1) "IsJump \(spell flag\) \(page does not exist\)")`, `[Stealth](Stealth_(spell_flag).md)`

## 学习方式

由物品授予：

- [跃动指套](Fleetfingers.md "跃动指套")

## 错误

- 由于条件要求检查错误，跳跃（奔跑）可能在角色使用后的下一回合出现在角色的快捷栏上（甚至可被选择/瞄准），但在角色再次使用疾走动作之前无法使用。

---
*Source: [Jump (Running)](https://bg3.wiki/wiki/Jump_(Running)*