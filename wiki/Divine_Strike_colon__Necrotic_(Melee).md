# 至圣斩：黯蚀（近战）

本文介绍近战版本。关于远程版本，请参见[至圣斩：黯蚀（远程）](Divine_Strike_colon__Necrotic_(Ranged).md)>。关于此特性的通用信息，请参见[至圣斩](Divine_Strike.md "至圣斩")。

**至圣斩：黯蚀（近战）** 是[死亡领域](Death_Domain.md "死亡领域")牧师的武器动作和反应，可在近战武器攻击时造成额外的黯蚀伤害。

## 描述

造成额外 1d8⁠⁠[黯蚀](Necrotic.md "黯蚀")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~8

普通武器伤害

\+ 1d8⁠[黯蚀](Necrotic.md "黯蚀")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
近战：1.5 米（5 英尺）
充能：每回合

## 技术细节

UID

`Target_DivineStrike_Melee_Death`

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 学习方式

此法术是以下法术的变体：
[至圣斩：黯蚀](Divine_Strike_colon__Necrotic.md "至圣斩：黯蚀")

## 备注

- 此动作可作为攻击后反应触发（不消耗[反应](Actions.md#Reactions "动作")），类似于[至圣斩](Divine_Smite.md "至圣斩")。
- 有关此系列武器动作的详细信息，请参阅[至圣斩](Divine_Strike.md "至圣斩")。

## 错误

- 此攻击错误地标记了穿刺 `DamageType` 标志，而非黯蚀，这意味着它不会触发某些检查黯蚀伤害的效果，例如[邪恶真菌](Malefic_Funghi.md "邪恶真菌")。
- 一个隐藏的技术条件（负责对击中目标施加视觉效果）会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。

---
*Source: [Divine Strike: Necrotic (Melee)](https://bg3.wiki/wiki/Divine_Strike:_Necrotic_(Melee)*