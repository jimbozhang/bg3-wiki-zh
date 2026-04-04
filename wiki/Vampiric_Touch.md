# 吸血鬼之触

**吸血鬼之触**是一个[法术](Spells.md "法术")。它允许施法者在近战范围内吸取目标的生命力。

## 描述

触摸一个敌人以吸取其生命力，并恢复一半的[生命值](Hit_Points.md "Hit_Points")。

在10回合内，你可以再次使用**吸血鬼之触**，而无需消耗额外的[法术位](Spells.md#Spell_Slots "Spells")。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [3环法术位](Spells.md#Spell_slots "Spells")
伤害：3~18

3d6⁠[黯蚀](Necrotic.md "Necrotic")

详情
近战法术 [攻击掷骰](Attack_roll.md "Attack Roll")
近战：1.5米（5英尺）
[专注](Concentration.md "Concentration")

## 升环施法

[升环施法](Upcasting.md "Upcasting")：以更高环位施放此法术时，每比3环高一环，额外造成1d6⁠⁠[黯蚀](Necrotic.md "Necrotic")伤害。

## 技术细节

UID

`Target_VampiricTouch`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：吸血鬼之触

**[吸血鬼之触](Vampiric_Touch_(Condition).md "吸血鬼之触 (状态)")**

持续时间：10回合

- 每回合，使用一个[动作](Action.md "Action")，可以重新施展吸血鬼之触，而无需消耗[法术位](Spells.md#Spell_Slots "Spells")。

## 如何习得

职业：

- 职业等级5：[邪术师](Warlock.md "Warlock")、[法师](Wizard.md "Wizard")、[大地结社](Circle_of_the_Land.md "Circle_of_the_Land")（沼泽），以及[死亡领域](Death_Domain.md "Death Domain")（领域法术）
- 职业等级6：[逸闻学院](College_of_Lore.md "College_of_Lore")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）
- 职业等级10：[吟游诗人](Bard.md "Bard")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）

其他习得方式：

- 拥有[3环法术位](Spells.md#Spell_slots "Spells")的[法师](Wizard.md "Wizard")可以[抄录](Transcribing_scrolls.md "Transcribing scrolls")[吸血鬼之触卷轴](Scroll_of_Vampiric_Touch.md "吸血鬼之触卷轴")到他们的法术书中。

## 备注

- 在激活期间，[吸血鬼之触](Vampiric_Touch_(Condition).md "吸血鬼之触 (状态)")为施法者提供一个相同环位的_授予_吸血鬼之触法术。_授予法术_在使用原始法术后发放给施法者，并且只要[专注](Concentration.md "Concentration")未被打破，就可以[重新施展](Category_colon_Recastable_spells.md "Category:Recastable spells")而无需花费另一个法术位。授予法术不直接与施法者已知法术的列表（即游戏中的法术书图标）相关联。因此，如果在身兼多职时使用授予法术，后续的重新使用将使用最近获得的施法职业的施法调整值，而不是初始施放吸血鬼之触时使用的施法调整值。在这种情况下，可能会导致法术豁免DC意外偏低。

## 错误

- 可重新施展法术的[4环法术位](Spells.md#Spell_slots "Spells")、[5环法术位](Spells.md#Spell_slots "Spells")和[6环法术位](Spells.md#Spell_slots "Spells")版本缺少`PowerLevel`条目，这导致这些法术版本在UI上显示为[3环法术位](Spells.md#Spell_slots "Spells")版本，尤其是在使用控制器时。但是，这些法术版本_确实_以正确的环位施放。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Vampiric_Touch_Visuals.mp4>

## 外部链接

- ⁠[吸血鬼之触](https://forgottenrealms.fandom.com/wiki/Vampiric_touch) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Vampiric Touch](https://bg3.wiki/wiki/Vampiric_Touch)*