# 断筋

**断筋**是一种由[骨锯 (+1)](Bonesaw_(+1).md "骨锯 (+1)")赋予的[武器动作](Weapon_action.md "武器动作")，它会造成额外的[黯蚀](Necrotic.md "黯蚀")伤害，并可能使目标[减速](Slowed_(Condition).md)。玩家角色无法使用此动作，即使装备了该武器。

## 描述

将锯子最黑的锯齿磨入敌人的小腿，并可能使其[减速](Slowed_(Condition).md "减速 (状态)")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~6 + 调整值

普通武器伤害

\+ [熟练项加值](Proficiency_Bonus.md "熟练项加值")⁠[挥砍](Slashing.md "挥砍")

\+ 1d6⁠[黯蚀](Necrotic.md "黯蚀")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
[敏](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）
射程：普通武器射程
充能：[短休](Short_rest.md "短休")
必须[熟练](Proficiency.md#Weapon_proficiency "熟练项")该武器

## 技术细节

UID

`Target_MAG_WeaponAction_Bonesaw`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell_flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：减速

**[减速](Slowed_(Condition).md "减速 (状态)")**

持续时间：2 回合

[敏](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- [移动速度](Movement_speed.md "移动速度") 减半
- [护甲等级](Armour_Class.md "护甲等级") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 降低 2
- 只能执行一个[动作](Action.md "动作")或一个[附赠动作](Bonus_action.md "附赠动作")，不能同时执行两者
- 无法执行[反应](Reaction.md "反应")
- 无法进行[额外攻击](Extra_Attack.md "额外攻击")或[精通额外攻击](Improved_Extra_Attack.md "精通额外攻击") _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_
- 施放的法术可能会延迟一回合 _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_

## 学习方式

由物品赋予：

- [骨锯 (+1)](Bonesaw_(+1).md "骨锯 (+1)")

---
*Source: [Incise Ligaments](https://bg3.wiki/wiki/Incise_Ligaments)*