# 放逐术

**放逐术** 是一个 [4级防护学派法术](Spells.md "法术")。它允许施法者暂时将目标发送到另一个位面。

## 描述

暂时将你的目标[放逐](Banished_(Condition).md "流放（状态）")到另一个位面。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")
详情
[魅力](Charisma.md "魅力") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：每升一环，可影响一个额外目标。

## 技术细节

UID

`Target_Banishment`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：流放

**[流放](Banished_(Condition).md "流放（状态）")**

持续时间：2回合

[魅力](Charisma.md "魅力") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- 从此位面被放逐。
- 无法被选为目标。
- 无法移动或进行[动作](Action.md "动作")、[附赠动作](Bonus_action.md "附赠动作")或[反应](Reaction.md "反应")

## 学习方式

职业：

- 职业等级7：[牧师](Cleric.md "牧师")、[术士](Sorcerer.md "术士")、[邪术师](Warlock.md "邪术师")和[法师](Wizard.md "法师")
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

其他学习方式：

- 拥有[4级法术位](Spells.md#Spell_slots "法术")的[法师](Wizard.md "法师")可以将[放逐术卷轴](Scroll_of_Banishment.md "放逐术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 注释

- 放逐术的咒语是 **Expellum Te**，拉丁语意为“我将驱逐你”或 **Iacto Te**，拉丁语意为“我投掷/抛出你”。

## 错误

- 该法术的升环版本获得了以多个生物为目标的能力，但由于该法术缺少 `IgnorePreviouslyPickedEntities` 法术标志，同一生物可以被多次选中，每次被选中都需要进行一次豁免检定。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Banish_Visuals.mp4>

## 外部链接

- ⁠[放逐术](https://forgottenrealms.fandom.com/wiki/Banishment) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Banishment](https://bg3.wiki/wiki/Banishment)*