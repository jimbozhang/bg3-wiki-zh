# 奥术射击：魅惑箭

**奥术射击：魅惑箭**是[奥术射手](Arcane_Archer.md "奥术射手")可用的一种特殊奥术箭攻击，可造成额外的2d6⁠⁠[心灵](Psychic.md "心灵")伤害并可能魅惑目标。

## 描述

使用惑控学派魔法造成额外的2d6⁠⁠[心灵](Psychic.md "心灵")伤害。目标必须通过[豁免检定](Saving_throw.md "豁免检定")，否则将被[魅惑](Charmed_(Condition).md "魅惑（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中消耗
[奥术箭](Arcane_Archer.md#Arcane_Archer "奥术射手")
伤害：2~12

普通武器伤害

\+ 2d6⁠[心灵](Psychic.md "心灵")

详情
远程武器[攻击掷骰](Attack_roll.md "攻击掷骰")
[感知](Wisdom.md "感知")[豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
射程：普通武器射程

## 技术细节

UID

`Projectile_ArcaneShot_BeguilingArrow`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：魅惑

**[魅惑](Charmed_(Condition).md "魅惑（状态）")**

持续时间：2驱散

[感知](Wisdom.md "感知")[豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 无法攻击施法者。施法者在对话中进行[魅力](Charisma.md "魅力")[属性检定](Ability_Check.md "属性检定")时具有[优势](Advantage.md "优势")。

## 学习方式

职业：

- 职业等级3：[奥术射手](Arcane_Archer.md "奥术射手")

## 错误

- 由于错误使用了`DamageBonus`函数，奥术射击在击中敌人时提供的额外伤害在[重击](Critical_Hit.md "重击")时不会翻倍。

---
*Source: [Arcane Shot: Beguiling Arrow](https://bg3.wiki/wiki/Arcane_Shot:_Beguiling_Arrow)*