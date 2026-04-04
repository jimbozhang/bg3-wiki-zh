# 钩子 (职业动作)

本文介绍的是恐爪怪使用的攻击。关于炼金材料，请参见 [钩子](Hook.md "钩子")。

**钩子**是 [恐爪怪](Hook_Horror.md "恐爪怪") 使用的基本攻击，可以将目标推回并可能造成 [流血](Bleeding_(Condition).md "流血 (状态)")。

## 描述

猛击目标，将其推回 2 米（7 英尺），并可能使其 [流血](Bleeding_(Condition).md "流血 (状态)")。

如果目标体型为大型或巨型，则无法被推动。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~12 + 调整值

2d6 + [灵巧](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺")

详情
近战 非武装 [攻击掷骰](Attack_roll.md "攻击掷骰")
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免 DC](Dice_rolls.md#Spell_save_DC "掷骰")）
近战：1.5 米（5 英尺）
推动：2 米（7 英尺）

## 技术细节

UID

`Target_Hook`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：流血

**[流血](Bleeding_(Condition).md "流血 (状态)")**

持续时间：2 驱散

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免 DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 生物在每回合开始时受到 2⁠⁠[挥砍](Slashing.md "挥砍")[DRS](Damage_rider_as_source.md "伤害来源")伤害，并在 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")上具有 [劣势](Disadvantage.md "劣势")。
- 通过治疗移除。

## 如何习得

由生物使用：[恐爪怪](Hook_Horror.md "恐爪怪")

---
*Source: [Hook (class action)](https://bg3.wiki/wiki/Hook_(class_action)*