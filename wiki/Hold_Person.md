# 人类定身术

关于四象宗武僧的等效法术，请参见[北风之握](Clench_of_the_North_Wind.md "北风之握")。

**人类定身术**是一个[2环惑控学派法术](Spells.md "法术")。它允许施法者将一个[类人生物](Humanoid.md "类人生物")目标定在原地。受影响的生物无法移动或行动，并且更容易受到攻击。

## 描述

定住一个类人生物敌人。他们无法[移动](Movement_speed.md "移动速度")、[行动](Action.md "动作")或[反应](Reaction_(Resource)..md) 在3米（10英尺）范围内的攻击总是[重击](Critical_Hit.md "重击")。

在每个回合结束时，受影响的生物可以进行一次[感知](Wisdom.md "感知")[豁免检定](Saving_throw.md "豁免检定")以结束此状态。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [2环法术位](Spells.md#Spell_slots "法术")
详情
[WIS](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")
射程：18米（60英尺）
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：每比2环高一环的法术位，可影响一个额外目标。

## 技术细节

UID

`Target_HoldPerson`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：人类定身术

**[人类定身术](Hold_Person_(Condition).md "人类定身术 (状态)")**

持续时间：10回合

[WIS](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- 受影响实体无法[移动](Movement_speed.md "移动速度")或进行[动作](Action.md "动作")、[附赠动作](Bonus_action.md "附赠动作")或[反应](Reaction.md "反应")。
- 对该实体的攻击自动成功其[攻击掷骰](Attack_roll.md "攻击掷骰")。
- 如果攻击者在射程内（3米/10英尺），对该实体的攻击总是[重击](Critical_Hit.md "重击")。
- 受影响实体自动失败所有[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")。
- 在每个回合结束时，受影响实体进行一次[感知](Wisdom.md "感知")[豁免检定](Saving_throw.md "豁免检定")。豁免成功时，状态被移除。

## 学习方式

职业：

- 职业等级3：[吟游诗人](Bard.md "吟游诗人")、[牧师](Cleric.md "牧师")、[德鲁伊](Druid.md "德鲁伊")、[术士](Sorcerer.md "术士")、[邪术师](Warlock.md "邪术师")、[法师](Wizard.md "法师")，以及[大地结社](Circle_of_the_Land.md "大地结社")（极地和森林）
- 职业等级5：[复仇之誓](Oath_of_Vengeance.md "复仇之誓")
- 职业等级7：[诡术师](Arcane_Trickster.md "诡术师")
- 职业等级8：[奥法骑士](Eldritch_Knight.md "奥法骑士")

物品授予：

- [静止者](Stillmaker.md "静止者")（充能：[长休](Long_Rest.md "长休")）

其他学习方式：

- 拥有[2环法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[人类定身术卷轴](Scroll_of_Hold_Person.md "人类定身术卷轴")到他们的法术书中。

## 注释

- 人类定身术有两个咒语：**Ad Lapidē**（拉丁语，意为“化为石头”）和**Non Moverē**（拉丁语命令“别动！”）。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Hold_Person_Visuals.mp4>

## 外部链接

- ⁠[Hold person](https://forgottenrealms.fandom.com/wiki/Hold_person) 在 [遗忘国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Hold Person](https://bg3.wiki/wiki/Hold_Person)*