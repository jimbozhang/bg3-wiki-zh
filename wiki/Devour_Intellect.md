# 吞噬智力

**吞噬智力**是[噬脑怪](Intellect_Devourer.md "噬脑怪")的一项动作，允许它们吞噬敌人的思维。

## 描述

吞噬一个生物的思维。如果其[智力](Intelligence.md "智力")低于4，它将受到伤害并被[震慑](Stunned_(Condition).md "震慑（状态）")。否则，其智力将降低3点。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~20

2d10⁠[心灵](Psychic.md "心灵")（如果目标智力低于4）

详情
[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）
近战：1.5米（5英尺）

## 技术细节

UID

`Target_DevourIntellect`

噬脑怪敌人使用的版本，DC固定为12

`Target_DevourIntellect_US`

Us使用的版本，使用SourceSpellDC()

法术标志

`[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：被吞噬智力

**[被吞噬智力](Devoured_Intellect_(Condition).md "被吞噬智力（状态）")**

持续时间：3回合

[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）

- [智力](Intelligence.md "智力")每回合降低1点。

## 状态：震慑

**[震慑](Stunned_(Condition).md "震慑（状态）")**

持续时间：1回合

[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")。
- 受影响的生物自动在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")中失败。
- 可通过[行动自如](Freedom_of_Movement.md "行动自如")、[高等复原术](Greater_Restoration.md "高等复原术")、[解缚打击](Unshackling_Strike.md "解缚打击")移除。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "优势")。

## 如何习得

由以下生物使用：[噬脑怪](Intellect_Devourer.md "噬脑怪")和[Us](Us.md "Us")

## 备注

- 当普通噬脑怪使用时，DC固定为12。对于[Us](Us.md "Us")，它使用[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")，通常为11，但如果Us处于[脑叶切除](Lobotomised_(Condition).md "脑叶切除（状态）")状态，则降至9。
- [被吞噬智力](Devoured_Intellect_(Condition).md "被吞噬智力（状态）")的后续应用持续时间和效果会叠加，但智力不会低于2点。
- 此能力曾在[抢先体验](Early_Access.md "抢先体验")中可供[异化变身](Aberrant_Shape.md "异化变身")[德鲁伊](Druid.md "德鲁伊")使用。
  - 在抢先体验中，它会使高于4的智力降低11点，不造成伤害，且不会引发被吞噬智力状态。

---
*Source: [Devour Intellect](https://bg3.wiki/wiki/Devour_Intellect)*