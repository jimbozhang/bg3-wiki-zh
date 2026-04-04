# 北风之握

**北风之握**是一项动作，允许[四象宗](Way_of_the_Four_Elements.md "四象宗")武僧通过消耗[气点](Ki_Point.md "气点")而非法术位来施放其等效的[人类定身术](Hold_Person.md "人类定身术")。

## 描述

使一个[类人生物](Humanoid.md "类人生物")敌人静止不动。他们无法移动、行动或做出反应。来自3米（10英尺）内的攻击总是[重击](Critical_Hit.md "重击")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 3 [气点](Ki_Point.md "气点")
详情
[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
[专注](Concentration.md "专注")

## 升环效果

在等级9时，可定住最多2个类人生物。

## 技术细节

UID

`Target_HoldPerson_Monk`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：人类定身术

**[人类定身术](Hold_Person_(Condition).md "人类定身术 (状态)")**

持续时间：10 驱散

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- 受影响实体无法[移动](Movement_speed.md "移动速度")或进行[动作](Action.md "动作")、[附赠动作](Bonus_action.md "附赠动作")或[反应](Reaction.md "反应")。
- 对该实体的攻击自动成功通过[攻击掷骰](Attack_roll.md "攻击掷骰")。
- 如果攻击者在范围内：3米（10英尺），则对该实体的攻击总是[重击](Critical_Hit.md "重击")。
- 受影响实体自动失败所有[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")。
- 在每个驱散结束时，受影响实体进行一次[感知](Wisdom.md "感知")[豁免检定](Saving_throw.md "豁免检定")。如果豁免成功，则移除该状态。

## 如何习得

职业：

- 职业等级6：[四象宗](Way_of_the_Four_Elements.md "四象宗")

## 备注

- 与升环的[人类定身术](Hold_Person.md "人类定身术")不同，等级9的北风之握的目标不需要是不同的。这意味着可以选择单个目标两次，迫使其进行两次初始豁免检定。然而，在后续驱散中，它只需要成功一次豁免检定即可移除[人类定身术](Hold_Person_(Condition).md "人类定身术 (状态)")效果，因为多个此效果实例不会叠加。

## 错误

- 与其他四象宗动作不同，此动作仍保留其来自父法术人类定身术的`HasVerbalComponent`法术标志，因此无法在[沉默](Silenced_(Condition).md "沉默 (状态)")状态下使用。

---
*Source: [Clench of the North Wind](https://bg3.wiki/wiki/Clench_of_the_North_Wind)*