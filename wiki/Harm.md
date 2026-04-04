# 重伤术

**重伤术**是一个[法术](Spells.md "法术")。它允许施法者使敌人变得极为虚弱。

## 描述

降低目标的最大[生命值](Hit_Points.md "Hit Points")，但永远不会低于1。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [6级法术位](Spells.md#Spell_slots "Spells")
伤害：14~84

14d6⁠[黯蚀](Necrotic.md "Necrotic")

详情
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "Saving throws")（豁免成功时：目标仍承受一半伤害，但其最大生命值不会降低。）
射程：18米（60英尺）

## 升环施法效应

以此法术升环施法不会获得额外收益。

## 技术细节

UID

`Target_Harm`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：重伤术

**[重伤术](Harm_(Condition).md "Harm (Condition)")**

持续时间：直至[长休](Long_Rest.md "Long rest")

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）

- 受影响实体的最大[生命值](Hit_Points.md "Hit Points")已被重伤术造成的伤害降低
- 此状态是一种**疾病**

## 学习方式

职业：

- 职业等级11：[牧师](Cleric.md "Cleric")

## 错误

- 豁免失败时，重伤术会将目标的最大生命值降低14d6，但不会实际造成任何⁠[黯蚀](Necrotic.md "Necrotic")伤害。这意味着它不会触发需要伤害来源的伤害附加效果或其他效果。此外，有效伤害（通过降低最大生命值计算）会因目标已损失的生命值而减少，可能降至_零_。
  - 豁免成功时，重伤术会按预期造成14d6 / 2⁠⁠[黯蚀](Necrotic.md "Necrotic")伤害。

## 外部链接

- ⁠[重伤术](https://forgottenrealms.fandom.com/wiki/Harm) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Harm](https://bg3.wiki/wiki/Harm)*