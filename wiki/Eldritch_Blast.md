# 魔能爆

**魔能爆**是一种[法术](Spells.md "法术")。它允许施法者射出一道能量光束，造成[力场](Force.md "力场")伤害，并可通过邪术师能力进行升级。

## 描述

召唤一道噼啪作响的能量光束。对目标造成 1d10[力场](Force.md "力场")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~10

1d10[力场](Force.md "力场")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
推斥：4.5米（15英尺）（当拥有[斥力魔爆](Repelling_Blast.md "斥力魔爆")时）

## 更高等级

与其他在特定角色等级时伤害会增加的戏法不同，魔能爆在更高等级时会创建多个光束：

每道光束造成 1d10（1~10）[力场](Force.md "力场")伤害

- **2** 道光束在[角色等级](Character_level.md "角色等级") 5 时
- **3** 道光束在角色等级 10 时

你可以将光束对准单个或多个生物。每道光束进行单独的[攻击掷骰](Attack_roll.md "攻击掷骰")，并受所选[魔能祈唤](Eldritch_Invocations.md "魔能祈唤")影响（详见注释）。

## 技术细节

UID

`Projectile_EldritchBlast`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[DisplayDamageModifiers](https://bg3.wiki/w/index.php?title=DisplayDamageModifiers_\(spell_flag\)&action=edit&redlink=1) "DisplayDamageModifiers \(spell flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 学习方式

职业：

- 职业等级 1：[邪术师](Warlock.md "邪术师")
- 职业等级 6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级 10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性授予：

- [魔法学徒：邪术师](Magic_Initiate_colon__Warlock.md "魔法学徒：邪术师")
- [法术狙击](Spell_Sniper.md "法术狙击")

生物使用：[至上真神质问者](Absolute_Questioner.md "至上真神质问者")、[博尔特](Bolt.md "博尔特")、[德尔韦登](Delverdenn.md "德尔韦登")、[地精邪术师](Goblin_Warlock.md "地精邪术师")、[格里兹](Greez.md "格里兹")、[古尔克](Gurk.md "古尔克")、[赫尔希克](Helsik.md "赫尔希克")、[贾辛](Jasin.md "贾辛")、[吉维·米兹瑞姆](Jivin_Mizzrym.md "吉维·米兹瑞姆")、[契约撕裂者](Pactsplitter.md "契约撕裂者")、[苏梅拉](Sumera.md "苏梅拉")、[茨卡安](Tska'an.md "茨卡安")、[图德](Tud.md "图德")和[兹瑞尔](Z'rell.md "兹瑞尔")

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到法术书中的卷轴。

## 注释

- [威能长袍](Potent_Robe.md "威能长袍")的增益，以及各种效果如[闪电充能](Lightning_Charges_(Condition).md "闪电充能（状态）")和[魔能祈唤](Eldritch_Invocations.md "魔能祈唤")（如[苦痛魔爆](Agonising_Blast.md "苦痛魔爆")或[斥力魔爆](Repelling_Blast.md "斥力魔爆")），都会应用于每道光束。
  - 虽然[斥力魔爆](Repelling_Blast.md "斥力魔爆")适用于每道光束，但每次施法只能击退一个生物一次。
- 受[脆弱诅咒](Hex.md "脆弱诅咒")影响的目标，每道光束都会受到额外的 1d6[黯蚀](Necrotic.md "黯蚀")伤害。
- 可被[法术反制](Counterspell.md "法术反制")。
- 当与[死亡防护](Death_Ward.md "死亡防护")等效果互动并对同一生物进行多次光束攻击时，假设第一次攻击足以在死亡防护激活时[击倒](Downed_(Condition).md "倒地（状态）")该生物，第二次攻击似乎会在死亡防护激活前生效。这意味着在 2 次光束攻击后，该生物会失去死亡防护但仍保留 1 点生命值：
  - 如果初始攻击有 3 道光束，该生物会在第 2 次攻击时被击倒，并在第 3 次攻击时被实际杀死。
  - 对于拥有死亡防护的队友，他们需要承受 6 次（光束）攻击才会真正死亡：2 次打破防护，1 次被击倒，再 3 次未能通过 3 次[死亡豁免检定](Death_Saving_Throw.md "死亡豁免检定")。此效果似乎适用于所有多次应用攻击，如[魔法飞弹](Magic_Missile.md "魔法飞弹")和[灼热射线](Scorching_Ray.md "灼热射线")（截至 4.1.1.3669438）。
- 魔能爆的咒语是 **Dolor**，拉丁语意为“痛苦/苦恼”。

## 外部链接

- ⁠[魔能爆](https://forgottenrealms.fandom.com/wiki/Eldritch_blast) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Eldritch Blast](https://bg3.wiki/wiki/Eldritch_Blast)*