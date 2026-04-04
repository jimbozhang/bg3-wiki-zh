# 给予飞行

另请参阅：[飞行（消歧义）](Fly_(disambiguation).md)

**给予飞行**是一个[3级变化学派法术](Spells.md "法术")。它允许施法者为他们触碰的生物赋予飞行能力。

## 描述

将[飞行](Flight_(Condition).md "飞行（状态）")能力赋予自己或一名盟友。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
近战：1.5米（5英尺）
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：每比3环高一环的法术位，可影响一个额外目标。

## 技术细节

UID

`Target_Fly`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：飞行

**[飞行](Flight_(Condition).md "飞行（状态）")**

持续时间：10回合

- 每回合使用你的[移动速度](Movement_speed.md "移动速度")，飞至目标位置，最多18米（60英尺）。

## 如何习得

职业：

- 职业等级5：[术士](Sorcerer.md "术士")、[邪术师](Warlock.md "邪术师")、[法师](Wizard.md "法师")和[大地结社](Circle_of_the_Land.md "大地结社")（山岳）
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

其他习得方式：

- 拥有[3级法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以将[飞行术卷轴](Scroll_of_Fly.md "飞行术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 此法术已从桌面版的名称**飞行**更名，以区别于自然飞行生物拥有的[飞行](Fly.md "飞行")动作。
- 受影响的生物没有真正的飞行能力，而是在每次移动结束时必须落地。
- 给予飞行的咒语是**Tibi Do Penna**，拉丁语意为“我给你（一根）羽毛”。

## 错误

- 此法术的升环版本获得了以多个生物为目标的能力，但由于该法术缺少`IgnorePreviouslyPickedEntities`法术标志，同一个生物可以被多次选择，但不会产生额外效果。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Grant_Flight_Visuals.mp4>

---
*Source: [Grant Flight](https://bg3.wiki/wiki/Grant_Flight)*