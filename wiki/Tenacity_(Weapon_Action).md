# 韧性

关于被动特性，请参见 [韧性（被动特性）](Tenacity_(passive_feature).md)>。

**韧性**是角色在主手装备并熟练使用[链枷](Flails.md "链枷")、[钉头锤](Morningstars.md "钉头锤")、[巨棒](Greatclubs.md "巨棒")或[巨锤](Mauls.md "巨锤")时可用的[武器动作](Weapon_action.md "武器动作")。

## 描述

当你攻击未命中时，依然造成等于你[力量](Strength.md "力量")[调整值](Ability_Scores.md#Ability_score_modifiers "属性值")的[钝击](Bludgeoning.md "钝击")伤害（最低为1）。

## 属性

消耗
[反应](Actions.md#Reactions "反应")
伤害：

[力量调整值](Strength.md#Strength_modifier_chart "力量")[钝击](Bludgeoning.md "钝击")

## 技术细节

UID

`Interrupt_Overwhelm`

## 学习方式

通过熟练装备以下武器类型获得：

- [链枷](Flails.md "链枷")
- [钉头锤](Morningstars.md "钉头锤")
- [巨棒](Greatclubs.md "巨棒")
- [巨锤](Mauls.md "巨锤")

## 备注

- 如果[武器动作](Weapon_action.md "武器动作")未命中，使用韧性不会触发其效果。
- 尽管是巨棒，[卑劣短棒](Rat_Bat.md "卑劣短棒")和[东倒西歪](Punch-Drunk_Bastard.md "东倒西歪")都不提供韧性。[风元素执政官](Air_Myrmidon.md "风元素执政官")的[旋涡链枷](Flail_of_the_Vortex.md "旋涡链枷")也缺乏韧性。
- 由于韧性造成武器伤害，即使攻击未命中，也能触发装备的许多命中效果。
  - 例如武器涂层、[威能手套](Gloves_of_Power.md "威能手套")、[无情光芒之戒](Callous_Glow_Ring.md "无情光芒之戒")，以及[元素注能戒指](Ring_of_Elemental_Infusion.md "元素注能戒指")的任何注能效果。
  - [厄运之锤](Doom_Hammer.md "厄运之锤")和[圣星](The_Sacred_Star.md "圣星")的命中效果将被触发。这在你需要持续施加状态时尤为重要，例如对强大的不死生物或快速治疗的敌人施加[冻僵](Bone_Chilled_(Condition).md "冻僵（状态）")。
  - 当被[强酸注能](Acid_Infusion_(Condition).md "强酸注能（状态）")、[寒冷注能](Cold_Infusion_(Condition).md "寒冷注能（状态）")或[火焰注能](Fire_Infusion_(Condition).md "火焰注能（状态）")强化时，[传古链枷](Flail_of_Ages.md "传古链枷")可以通过韧性触发其效果。

## 错误

- 当使用[双持客](Dual_Wielder.md "双持客")专长双持链枷或钉头锤与非韧性武器时，使用非韧性武器攻击未命中可触发韧性。无论使用何种武器，伤害始终为[钝击](Bludgeoning.md "钝击")。
  - 一些非韧性武器也可以通过韧性触发其命中效果，例如[仪式匕首](Ritual_Dagger.md "仪式匕首")和[劳薇塔的灾祸](Loviatar's_Scourge.md "劳薇塔的灾祸")。
- 由于[灭族者（近战）](Horde_Breaker_(Melee).md "灭族者（近战）")会对灭族者作用区域内的所有敌人进行隐形、零伤害的武器攻击，即使第一次攻击命中，也可能提示对它们触发韧性。因此，一次攻击可能造成2次命中：对原始灭族者目标的完整攻击，以及对另一个目标的韧性命中。

---
*Source: [Tenacity](https://bg3.wiki/wiki/Tenacity)*