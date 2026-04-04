# 多重攻击（暗影德鲁伊）

本文介绍的是某些NPC使用的额外攻击动作。其他用法，请参见[多重攻击（消歧义）](Multiattack_(disambiguation)..md)

**多重攻击（远程）**是一种[武器动作](Weapon_action.md "武器动作")，由数名[暗影德鲁伊](Shadow_Druids.md "暗影德鲁伊")使用。这是一种自由攻击，可以在进行另一次攻击后执行，类似于[额外攻击](Extra_Attack.md "额外攻击")。

## 描述

使用装备的武器进行一次额外的远程攻击。

## 属性

伤害：

普通武器伤害

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
充能：每回合

## 技术细节

UID

`Projectile_ExtraAttack`

法术标志

`[CanDualWield](https://bg3.wiki/w/index.php?title=CanDualWield_\(spell_flag\)&action=edit&redlink=1) "CanDualWield \(spell_flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell_flag\) \(page does not exist\)")`

## 如何习得

由以下生物使用：[平塔](Pinta.md "平塔")和[欧罗丹](Olodan.md "欧罗丹")

## 备注

- 这似乎是[额外攻击](Extra_Attack.md "额外攻击")的早期实现，因为名称是`Projectile_ExtraAttack`，且该动作是一种自由攻击，只能在执行另一次攻击后使用。
- 该动作除AI外不可用。如果一名拥有此动作的德鲁伊被[活化孢子](Animating_Spores.md "活化孢子")复活，它将由队伍直接控制。在这种情况下，该攻击将不可用，因为它无法以任何目标为目标。

---
*Source: [Multiattack (Shadow Druid)](https://bg3.wiki/wiki/Multiattack_(Shadow_Druid)*