# 华舞

**华舞**是一种[武器动作](Weapon_action.md "Weapon action")，可供主手装备[刺剑](Rapiers.md "Rapiers")、[弯刀](Scimitars.md "Scimitars")或[短剑](Shortswords.md "Shortswords")且[重甲的](Proficient.md "Proficient")使用该武器类型的角色使用。

## 描述

佯攻以可能使对手陷入[失衡](Off_Balance_(Condition).md "Off Balance (Condition)")状态。

## 属性

消耗
[附赠动作](Actions.md#Resources "Actions")
伤害：1~4

1d4⁠[钝击](Bludgeoning.md "Bludgeoning")（非致命）

详情
近战武器[攻击掷骰](Attack_roll.md "Attack Roll")
[敏捷](Dexterity.md "Dexterity")[豁免检定](Saving_throws.md "Saving throws")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "Dice rolls")）
射程：正常武器射程
充能：[短休](Short_rest.md "Short rest")
必须[熟练](Proficiency.md#Weapon_proficiency "Proficiency")使用该武器

## 技术细节

UID

`Target_OpeningAttack`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：失衡

**[失衡](Off_Balance_(Condition).md "Off Balance (Condition)")**

持续时间：2回合

[敏捷](Dexterity.md "Dexterity")[豁免检定](Saving_throws.md "Saving throws")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "Dice rolls") + 2）

- 受影响实体在[力量](Strength.md "Strength")和[敏捷](Dexterity.md "Dexterity")[属性检定](Ability_Check.md "Ability Check")上具有[劣势](Disadvantage.md "Disadvantage")，且针对该实体的[攻击掷骰](Attack_roll.md "Attack Roll")具有[优势](Advantage.md "Advantage")。
- 受到伤害或被[协助](Help.md "Help")时移除。

## 如何习得

通过熟练使用以下武器类型获得：

- [刺剑](Rapiers.md "Rapiers")
- [弯刀](Scimitars.md "Scimitars")
- [短剑](Shortswords.md "Shortswords")

## 备注

- 造成的伤害为[非致命](Toggle_Non-Lethal_Attacks.md "Toggle Non-Lethal Attacks")，当目标生命值降至0时会使其昏迷而非死亡。

---
*Source: [Flourish](https://bg3.wiki/wiki/Flourish)*