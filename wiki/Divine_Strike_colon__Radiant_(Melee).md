# 神圣打击：光耀（近战）

本文介绍近战版本。远程版本请参见 [神圣打击：光耀（远程）](Divine_Strike_colon__Radiant_(Ranged).md)>。关于此特性的通用信息，请参见 [神圣打击](Divine_Strike.md "神圣打击")。

**神圣打击：光耀（近战）** 是 [生命领域](Life_Domain.md "生命领域") 牧师的武器动作和反应，可在近战武器攻击时造成额外光耀伤害。

## 描述

挥动武器劈砍敌人，武器上燃烧着精妙的光耀。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~8

普通武器伤害

\+ 1d8⁠[光耀](Radiant.md "光耀")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
近战：1.5 米（5 英尺）
充能：每回合

## 技术细节

UID

`Target_DivineStrike_Melee_Life`

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsHarmful_(spell_flag).md)`

## 学习方式

此法术是以下法术的变体：
[神圣打击：光耀](Divine_Strike_colon__Radiant.md "神圣打击：光耀")

## 备注

- 此动作可作为攻击后反应触发（无需消耗 [反应](Actions.md#Reactions "动作")），类似于 [至圣斩](Divine_Smite.md "至圣斩")。
- 有关此系列武器动作的详细信息，请参阅 [神圣打击](Divine_Strike.md "神圣打击")。

## 错误

- 此攻击未正确标记光耀 `DamageType` 标志，这意味着它不会触发某些检查光耀伤害的效果。

---
*Source: [Divine Strike: Radiant (Melee)](https://bg3.wiki/wiki/Divine_Strike:_Radiant_(Melee)*