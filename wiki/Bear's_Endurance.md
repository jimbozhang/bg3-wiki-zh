# 熊之坚韧

**熊之坚韧**是一个[法术](Spells.md "法术")。此法术允许施法者赋予生物熊的坚韧。受影响的生物获得[临时生命值](Hit_Points.md#Temporary_Hit_Points "Hit Points")和在[体质](Constitution.md "Constitution")[属性检定](Ability_Check.md "属性检定")上的[优势](Advantage.md "Advantage")。

## 描述

生物获得在[体质](Constitution.md "Constitution")[属性检定](Ability_Check.md "属性检定")上的[优势](Advantage.md "Advantage")，并获得 7 点[临时生命值](Hit_Points.md#Temporary_Hit_Points "Hit Points")。

只能拥有来自一个来源的临时生命值。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [2 级法术位](Spells.md#Spell_slots "Spells")
细节
近战：1.5 米（5 英尺）
[专注](Concentration.md "Concentration")

## 升环施法

[升环施法](Upcasting.md "Upcasting")：当此法术以 3 级或更高法术位施放时，你可以为每个高于 2 级的法术位等级额外指定一个目标。

## 技术细节

UID

`Target_EnhanceAbility_BearsEndurance`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：熊之坚韧

**[熊之坚韧](Bear's_Endurance_(Condition).md "Bear's Endurance (Condition)")**

持续时间：直到[长休](Long_Rest.md "Long rest")

- 拥有在[体质](Constitution.md "Constitution")[属性检定](Ability_Check.md "属性检定")上的[优势](Advantage.md "Advantage")。
- 获得 7 点[临时生命值](Hit_Points.md#Temporary_Hit_Points "Hit Points")。

## 如何学习

此法术是以下法术的变体：
[强化属性](Enhance_Ability.md "Enhance Ability")

## 错误

- 临时生命值缺少 `StackPriority`，因此会被任何其他来源的临时生命值覆盖，即使新来源的值更小。

## 外部链接

- ⁠[熊之坚韧](https://forgottenrealms.fandom.com/wiki/Bear%27s_endurance) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Bear's Endurance](https://bg3.wiki/wiki/Bear's_Endurance)*