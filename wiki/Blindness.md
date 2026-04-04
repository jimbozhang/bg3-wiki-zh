# 失明术

**失明术**是一个[2环死灵学派法术](Spells.md "Spells")。它允许施法者对目标敌对生物施加魔法[目盲](Blindness_(Condition).md "Blindness (Condition)")效果。

## 描述

限制敌人的视线范围。使其更容易被击中，并且该生物会更频繁地失手。

对其的[攻击掷骰](Attack_roll.md "Attack Roll")具有[优势](Advantage.md "Advantage")，而该敌人的攻击则具有[劣势](Disadvantage.md "Disadvantage")。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [2环法术位](Spells.md#Spell_slots "Spells")
详情
[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")
射程：18米（60英尺）

## 升环施法

[升环施法](Upcasting.md "Upcasting")：每比2环高一环的法术位，可影响一个额外目标。

## 技术细节

UID

`Target_Blindness`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：失明术

**[失明术](Blindness_(Condition).md "Blindness (Condition)")**

持续时间：10驱散

[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）

- 受影响的生物在[攻击掷骰](Attack_roll.md "Attack Roll")上具有[劣势](Disadvantage.md "Disadvantage")。
- 受影响生物的远程攻击和法术射程为3米（10英尺）。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "Advantage")。
- 每驱散结束时，受影响的生物进行一次[体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw")。如果成功，则移除该状态。

## 学习方式

职业：

- 职业等级3：[吟游诗人](Bard.md "Bard")、[牧师](Cleric.md "Cleric")、[术士](Sorcerer.md "Sorcerer")、[法师](Wizard.md "Wizard")、[邪魔](The_Fiend.md "The Fiend")、[孢子结社](Circle_of_the_Spores.md "Circle of the Spores")（结社法术）和[死亡领域](Death_Domain.md "Death Domain")（领域法术）
- 职业等级8：[诡术师](Arcane_Trickster.md "Arcane Trickster")和[奥法骑士](Eldritch_Knight.md "Eldritch Knight")

其他学习方式：

- 拥有[2环法术位](Spells.md#Spell_slots "Spells")的[法师](Wizard.md "Wizard")可以[抄录](Transcribing_scrolls.md "Transcribing scrolls")[失明术卷轴](Scroll_of_Blindness.md "Scroll of Blindness")到他们的法术书中。

## 备注

- 另见[目盲免疫](Blind_Immunity.md "Blind Immunity")。
- 失明术是少数无需维持[专注](Concentration.md "Concentration")即可施加控制效果的法术之一。
- 失明术的咒语是 **Caeco Te**，拉丁语意为“我使你目盲”。

## 错误

- 该法术的升环版本获得了影响多个生物的能力，但由于法术缺少 `IgnorePreviouslyPickedEntities` 法术标志，同一个生物可以被多次选中，每次被选中都需要进行一次豁免检定。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Blindness_Visuals.mp4>

## 外部链接

- ⁠[失明术](https://forgottenrealms.fandom.com/wiki/Blindness) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Blindness](https://bg3.wiki/wiki/Blindness)*