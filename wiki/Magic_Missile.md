# 魔法飞弹

**魔法飞弹**是一个[1级塑能学派法术](Spells.md "法术")。它允许施法者用多个投射物击中敌人，造成[力场](Force.md "力场")伤害。

## 描述

创造**三**枚魔法力场飞镖，每枚对目标造成1d4 + 1[力场](Force.md "力场")伤害。

飞镖总是命中目标，并且可以单独瞄准。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：6~15

1d4 + 1[力场](Force.md "力场")

\+ 1d4 + 1[力场](Force.md "力场")

\+ 1d4 + 1[力场](Force.md "力场")

详情
射程：18米（60英尺）

## 升环施法

[升环施法](Upcasting.md "升环施法")：每升一环额外创造一枚飞镖，同样造成1d4 + 1[力场](Force.md "力场")伤害。

## 技术细节

UID

`Projectile_MagicMissile`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 学习方式

职业：

- 职业等级1：[术士](Sorcerer.md "术士")和[法师](Wizard.md "法师")
- 职业等级3：[诡术师](Arcane_Trickster.md "诡术师")和[奥法骑士](Eldritch_Knight.md "奥法骑士")
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性提供：

- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "魔法学徒：术士")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

由物品提供：

- [心灵火花](Psychic_Spark.md "心灵火花")（充能：[长休](Long_Rest.md "长休")）
- [从未射失](Ne'er_Misser.md "从未射失")（充能：[短休](Short_rest.md "短休")")

其他学习方式：

- [法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[魔法飞弹卷轴](Scroll_of_Magic_Missile.md "魔法飞弹卷轴")到他们的法术书中。

## 注释

- [护盾术](Shield_(spell).md "护盾术（法术）")使其受术者免疫魔法飞弹。
- 10级[塑能学派](Evocation_School.md "塑能学派")[法师](Wizard.md "法师")特性[强效塑能](Empowered_Evocation.md "强效塑能")将法师的[智力](Intelligence.md "智力")调整值加到每枚飞弹上。
- [心灵火花](Psychic_Spark.md "心灵火花")为每次施放魔法飞弹增加一枚额外飞镖（例如，法术等级1时总共四枚）。
- 当与[死亡防护](Death_Ward.md "死亡防护")等效果互动并对同一生物造成多次飞弹攻击时，假设第一次攻击足以在死亡防护激活时[击倒](Downed_(Condition).md "倒地（状态）")该生物，第二次攻击似乎在死亡防护激活前生效。这意味着在2次飞弹攻击后，生物失去死亡防护但仍保留1点生命值：
  - 如果初始攻击有3枚飞弹，生物在第2次攻击时被击倒，并在第3次攻击时实际被杀死。
  - 对于施加了死亡防护的队友，他们需要承受6次飞弹攻击才会真正死亡：2次打破防护，1次被击倒，再3次以在3次[死亡豁免检定](Death_Saving_Throw.md "死亡豁免检定")中失败。此效果似乎适用于所有多次应用的攻击，如[灼热射线](Scorching_Ray.md "灼热射线")和[魔能爆](Eldritch_Blast.md "魔能爆")（截至4.1.1.3669438版本）。
- 魔法飞弹的咒语是**Tormentum**，拉丁语意为“投石机”、“飞弹”和“折磨”。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Magic_Missile_Visuals.mp4>

## 外部链接

- [魔法飞弹](https://forgottenrealms.fandom.com/wiki/Magic_missile)在[被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)上

---
*Source: [Magic Missile](https://bg3.wiki/wiki/Magic_Missile)*