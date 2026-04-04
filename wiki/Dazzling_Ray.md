# 炫目射线

**炫目射线**是一种由[组装劲弩](Fabricated_Arbalest.md "组装劲弩")赋予的[武器动作](Weapon_action.md "武器动作")。

## 描述

释放一道耀眼的光束，[目盲](Blinded_(Condition).md "目盲（状态）")其路径上的所有生物。

在法术结束前，你可以重新施展该法术。每次重新施展时，可能会[燃烧](Burning_(Condition).md "燃烧（状态）")你。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~20

2d10⁠[光耀](Radiant.md "光耀")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）（豁免成功：目标仍承受一半伤害。）
范围：18米（60英尺）直线
充能：[短休](Short_rest.md "短休")
[专注](Concentration.md "专注")
必须[熟练](Proficiency.md#Weapon_proficiency "熟练项")该武器
持续时间：10回合

## 技术细节

UID

`Zone_MAG_Automaton_SunbeamShot`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 赋予

- [重新施展炫目射线](Recast_Dazzling_Ray.md "重新施展炫目射线")

## 状态：目盲

**[目盲](Blinded_(Condition).md "目盲（状态）")**

持续时间：1回合

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物在[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术范围减少至3米（10英尺）。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "优势")。

## 状态：炫目射线

**[炫目射线](Dazzling_Ray_(Condition).md "炫目射线（状态）")**

持续时间：10回合

- 受影响的生物可以发射一道[重新施展炫目射线](Recast_Dazzling_Ray.md "重新施展炫目射线")。

## 如何习得

由物品赋予：

- [组装劲弩](Fabricated_Arbalest.md "组装劲弩")

## 备注

- 炫目射线使用施法者的[法术豁免DC](Spell_save_DC.md "法术豁免DC")，而非其[武器动作DC](Weapon_action_DC.md "武器动作DC")，且不涉及攻击掷骰。因此，它不计入[额外攻击](Extra_Attack.md "额外攻击")。
- 炫目射线使用专注，类似于其他可以重新施展的法术，如[阳炎射线](Sunbeam.md "阳炎射线")。
- 专注时，施法者获得一个单独的武器动作，称为[重新施展炫目射线](Recast_Dazzling_Ray.md "重新施展炫目射线")。
  - 仅当初始施展的炫目射线击中目标时，重新施展炫目射线才可用。
  - 施展重新施展炫目射线时，施法者进行一次隐藏的[DC](Dice_rolls.md#Save_DCs "掷骰") 14 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，以避免被[燃烧](Burning_(Condition).md "燃烧（状态）")2回合。
  - 当施法者被燃烧时，他们立即承受1d4⁠⁠[火焰](Fire.md "火焰")伤害，这可能会打断他们对炫目射线的专注。

---
*Source: [Dazzling Ray](https://bg3.wiki/wiki/Dazzling_Ray)*