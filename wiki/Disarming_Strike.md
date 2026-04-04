# 缴械打击

请勿与[缴械攻击](Disarming_Attack.md "缴械攻击")混淆

**缴械打击**是一种[武器动作](Weapon_action.md "武器动作")，可供[重甲的](Proficient.md "重甲的")使用[三叉戟](Tridents.md "三叉戟")并将其握在主手的角色使用。

## 描述

集中攻击敌人的手部，有可能迫使他们丢弃所持武器。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~4 + 调整值

1d4 + [灵巧](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺")

详情
近战武器[攻击掷骰](Attack_roll.md "攻击掷骰")
[力量](Strength.md "力量")[豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰")）
射程：正常武器射程
目标：装备武器的生物
充能：[短休](Short_rest.md "短休")
必须[熟练](Proficiency.md#Weapon_proficiency "熟练项")该武器

## 技术细节

UID

`Target_DisarmingStrike`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：武器掉落

**[武器掉落！](Weapon_Dropped!_(Condition).md "武器掉落！（状态）")**

[力量](Strength.md "力量")[豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- 敌人使你将武器掉落在地，类似于[缴械](Disarmed_(Condition).md "缴械（状态）")。

## 学习方式

通过[熟练项](Proficiency.md "熟练项")装备以下武器类型获得：

- [三叉戟](Tridents.md "三叉戟")

## 备注

- 目标必须装备实际武器；爪击等不计入且无法被掉落。
- 成功的[力量](Strength.md "力量")[豁免检定](Saving_throw.md "豁免检定")可防止武器掉落，但伤害仍然生效。
- 此动作本质上是[战斗大师](Battle_Master.md "战斗大师")战士可用的[缴械攻击（近战）](Disarming_Attack_(Melee).md "缴械攻击（近战）")动作的较弱变体。

## 错误

- 此动作的提示文本显示“未命中时：不消耗卓越骰”。这是一个简单的显示错误；该动作不需要[卓越骰](Battle_Master.md#Level_3 "战斗大师")，命中成功时也不会消耗任何骰子。

---
*Source: [Disarming Strike](https://bg3.wiki/wiki/Disarming_Strike)*