# 反击

**反击**是[战斗大师](Battle_Master.md "战斗大师")触发为[反应](Actions.md#Reactions "动作")的战斗策略。此能力允许战斗大师对在近战攻击中未击中的敌人进行近战武器反击。

## 描述

当生物对你进行的近战攻击未命中时，以强力打击进行反击。

这是一个[反应](Actions.md#Reactions "动作")。在你的回合中切换反应。它将在需要时自动执行。

## 属性

消耗
[反应](Actions.md#Reactions "动作") + [卓越骰子](Battle_Master.md#Level_3 "战斗大师")
伤害：

正常武器伤害

\+ [卓越骰子](Battlemaster.md#Superiority_dice "战斗大师")

详情
近战武器[攻击掷骰](Attack_roll.md "攻击掷骰")
范围：2 米（7 英尺）

## 更高等级

在等级 10 时，拥有[精通卓越战技](Improved_Combat_Superiority.md "精通卓越战技")，伤害加成从 1d8 增加到 1d10。

## 技术细节

UID

`Target_Riposte`

由反应触发的攻击

`Interrupt_Riposte`

触发攻击的反应

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 如何学习

职业：

- 职业等级 3：[战斗大师](Battle_Master.md "战斗大师")

由特性授予：

- [战技专家](Martial_Adept.md "战技专家")

## 备注

- 反击仅触发于 2 米（7 英尺）范围内进行的近战攻击（包括近战法术攻击）。这略长于正常武器范围 1.5 米（5 英尺），但小于[额外范围](Extra_Reach.md "额外范围")的 2.5 米（8 英尺）。这意味着反击无法反击由[长矛](Pikes.md "长矛")等武器在最大范围进行的攻击。
- 与正常的[借机攻击](Opportunity_Attack.md "借机攻击")不同，反击不需要角色主动装备近战武器即可使用。如果在装备远程武器时触发，角色会在执行反击前自动切换到近战武器。
  - 如果未装备近战武器，则反击将以[徒手打击](Unarmed_Strike.md "徒手打击")进行。

---
*Source: [Riposte](https://bg3.wiki/wiki/Riposte)*