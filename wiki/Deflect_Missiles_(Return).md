# 拨挡飞弹：反弹

本文介绍的是用于反弹飞弹的后续反应。关于初始的接住飞弹反应，请参见 [拨挡飞弹](Deflect_Missiles.md "拨挡飞弹")。

**拨挡飞弹**是 [武僧](Monk.md "武僧") 的一种 [反应](Reaction.md "反应")，允许在首先使用 [拨挡飞弹](Deflect_Missiles.md "拨挡飞弹") 接住飞弹后，将远程武器投射物扔回攻击者。

## 描述

利用你的反射神经接住远程武器攻击的投射物，并将其射回攻击者。

## 属性

消耗
[气点](Ki_Point.md "气点")
伤害：

徒手[钝击](Bludgeoning.md "钝击")

详情
近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18 米（60 英尺）

## 技术细节

UID

`Projectile_Deflect_Missiles`

实际攻击动作

`Interrupt_DeflectMissiles_Return`

触发攻击的反应

法术标志

`[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 如何习得

职业：

- 职业等级 3：[武僧](Monk.md "武僧")

## 备注

- 此攻击视为近战徒手攻击，并受益于所有通常影响 [徒手打击](Unarmed_Strike.md "徒手打击") 的效果，例如 [酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")。
- 如果两名武僧被同一 [游侠](Ranger.md "游侠") 的一次 [疾速齐射](Volley.md "疾速齐射") 击中，他们可以同时将伤害反弹回发送者。

---
*Source: [Deflect Missiles: Redirect](https://bg3.wiki/wiki/Deflect_Missiles:_Redirect)*