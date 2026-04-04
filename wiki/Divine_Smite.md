# 至圣斩

本文介绍执行至圣斩的动作。关于在攻击后应用至圣斩的反应，请参见[至圣斩（反应）](Divine_Smite_(reaction).md)>。关于至圣斩的一般信息，请参见[至圣斩](Smite.md "至圣斩")。

至圣斩是一种类法术能力，允许[圣武士](Paladin.md "圣武士")消耗一个[法术位](Spells.md#Spell_slots "法术位")，使近战武器攻击造成额外的[光耀](Radiant.md "光耀")伤害。

## 描述

你的武器造成额外 2d8[光耀](Radiant.md "光耀")[伤害来源附加](Damage_rider_as_source.md "伤害来源附加")伤害，当攻击[邪魔](Fiends.md "邪魔")或[不死生物](Undead.md "不死生物")时，伤害增加 1d8[光耀](Radiant.md "光耀")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中后消耗
[1级法术位](Spells.md#Spell_slots "法术位")
伤害：3~24

普通武器伤害

\+ 2d8[光耀](Radiant.md "光耀")

\+ 1d8[光耀](Radiant.md "光耀")（如果目标是不死生物或邪魔）

详情
近战武器[攻击掷骰](Attack_roll.md "攻击掷骰")
范围：普通武器范围

## 升环施法

- 当至圣斩以 2 级或更高法术位施法时，伤害每比 1 级法术位高一级，增加 1d8[光耀](Radiant.md "光耀")伤害。此伤害上限为 5d8，因此使用 4 级以上法术位不会增加额外伤害。

## 技术细节

UID

`Target_Smite_Divine`

基础法术

`Target_Smite_Divine_2`

升环至 2 级，造成 3d8 伤害

`Target_Smite_Divine_3`

升环至 3 级，造成 4d8 伤害

`Target_Smite_Divine_4`

升环至 4 级，造成 5d8 伤害

`Target_Smite_Divine_5`

升环至 5 级，仍造成 5d8 伤害

`Target_Smite_Divine_6`

升环至 6 级，仍造成 5d8 伤害

法术标志

`[IsHarmful](IsHarmful_(spell_flag\>).md)`, `[IsMelee](IsMelee_(spell_flag\>).md)`

## 学习方式

职业：

- 职业等级 2：[圣武士](Paladin.md "圣武士")

## 备注

- 有关适用于所有至圣斩变体的其他详情，请参见[至圣斩](Smite.md "至圣斩")。

## 错误

- [1级法术位](Spells.md#Spell_slots "法术位")版本的此动作在荣誉模式下会因代码覆盖而改变攻击动画。
- [4级法术位](Spells.md#Spell_slots "法术位")、[5级法术位](Spells.md#Spell_slots "法术位")和[6级法术位](Spells.md#Spell_slots "法术位")版本的此动作在荣誉模式下用作攻击时不会失去伤害来源附加，而等效的[反应](Divine_Smite_(reaction).md)>版本会失去。

---
*Source: [Divine Smite](https://bg3.wiki/wiki/Divine_Smite)*