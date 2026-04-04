# 灼热金属：重新施加伤害

**重新施加灼热金属**是一个[法术](Spells.md "法术")。此法术允许施法者重新加热目标生物身上的金属武器或护甲，迫使他们松手或承受伤害或遭受各种惩罚。

## 描述

使金属[武器](Weapons.md "Weapons")或[护甲](Armour.md "Armour")炽热发红，并迫使接触它的生物松手或在[攻击掷骰](Attack_roll.md "Attack Roll")和[属性检定](Ability_Check.md "Ability Check")上获得[劣势](Disadvantage.md "Disadvantage")。如果该生物只穿着金属护甲，它总是获得劣势。

如果该生物仍然接触金属，你可以在后续回合使用[附赠动作](Bonus_action.md "Bonus Action")来[重新施加灼热金属](Reapply_Heat_Metal.md "Reapply Heat Metal")，造成额外的2d8⁠⁠[火焰](Fire.md "Fire")伤害，并迫使该生物松手或获得劣势。

## 属性

消耗
[附赠动作](Actions.md#Resources "Actions")
伤害：2~16

2d8⁠[火焰](Fire.md "Fire")

详情
[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）（豁免成功：目标承受完整伤害，但攻击掷骰获得[劣势](Disadvantage.md "Disadvantage")，而非被缴械）
范围：18米（60英尺）
[专注](Concentration.md "Concentration")

## 更高等级

[升环施法](Upcasting.md "Upcasting")：以更高环级施放[灼热金属](Heat_Metal.md "Heat Metal")时，重新施加该法术会为每个高于2环的法术位等级额外造成1d8⁠⁠[火焰](Fire.md "Fire")伤害。

## 技术细节

UID

`Target_HeatMetal_Reapply`

法术标志

`[IsSpell](IsSpell_(spell_flag).md)`, `[Temporary](Temporary_(spell_flag).md)`

## 状态：武器掉落

**[武器掉落！](Weapon_Dropped!_(Condition).md "Weapon Dropped! (Condition)")**

[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）

- 敌人使你将武器掉落在地，类似于[缴械](Disarmed_(Condition).md "Disarmed (Condition)")。

## 状态：灼热金属：劣势

**[灼热金属：劣势](Heat_Metal_colon__Disadvantage_(Condition).md "Heat Metal: Disadvantage (Condition)")**

持续时间：1回合

- 在施法者下一回合开始前，[攻击掷骰](Attack_roll.md "Attack Roll")和[属性检定](Ability_Check.md "Ability Check")获得[劣势](Disadvantage.md "Disadvantage")。

## 学习方式

其他学习方式：

- 在对目标施放[灼热金属](Heat_Metal.md "Heat Metal")后，只要专注维持，下一回合即可获得此法术。

## 错误

- 由于khn脚本错误，灼热金属：重新施加*永远*不会导致敌人掉落武器，并且总是施加劣势。

## 外部链接

- ⁠[灼热金属](https://forgottenrealms.fandom.com/wiki/Heat_metal) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Heat Metal: Reapply Damage](https://bg3.wiki/wiki/Heat_Metal:_Reapply_Damage)*