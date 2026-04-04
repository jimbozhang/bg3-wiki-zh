# 神圣打击：雷鸣（近战）

本文介绍近战版本。远程版本请参见 [神圣打击：雷鸣（远程）](Divine_Strike_colon__Thunder_(Ranged).md)。关于此特性的通用信息，请参见 [神圣打击](Divine_Strike.md "神圣打击")。

**神圣打击：雷鸣（近战）** 是 [风暴领域](Tempest_Domain.md "风暴领域") 牧师的武器动作和反应，可在近战武器攻击时造成额外的雷鸣伤害。

## 描述

每回合一次，在进行近战攻击时，除武器伤害外额外造成 1d8⁠⁠[雷鸣](Thunder.md "雷鸣") 伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~8

正常武器伤害

\+ 1d8⁠[雷鸣](Thunder.md "雷鸣")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
近战：1.5 米（5 英尺）
充能：每回合

## 技术细节

UID

`Target_DivineStrike_Melee_Tempest`

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 如何习得

此法术是以下法术的变体：
[神圣打击：雷鸣](Divine_Strike_colon__Thunder.md "神圣打击：雷鸣")

## 备注

- 此动作可作为攻击后反应触发（无需消耗 [反应](Actions.md#Reactions "动作")），类似于 [至圣斩](Divine_Smite.md "至圣斩")。
- 有关此系列武器动作的详细信息，请参阅 [神圣打击](Divine_Strike.md "神圣打击")。

## 错误

- 此攻击未正确标记雷鸣 `DamageType` 标志，这意味着它不会触发某些检查雷鸣伤害的效果，最显著的是 [毁灭狂怒](Destructive_Wrath.md "毁灭狂怒")。

---
*Source: [Divine Strike: Thunder (Melee)](https://bg3.wiki/wiki/Divine_Strike:_Thunder_(Melee)*