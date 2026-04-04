# 盾牌大师：格挡

**盾牌大师：格挡** 是通过 [盾牌大师](Shield_Master.md "盾牌大师") [专长](Feat.md "Feat") 获得的反应/被动特性。它能在成功的 [豁免检定](Saving_throw.md "豁免检定") 上抵消许多区域效果攻击的伤害。

## 描述

如果一个 [法术](Spells.md "法术") 强制你进行一次 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") _\[[参见注释](#notes)\]_，你可以使用你的 [反应](Reaction.md "反应") 来保护自己并减弱效果的伤害。

豁免失败时，你只承受一半伤害 _\[[参见：错误](#bugs)\]_。豁免成功时，你不会承受任何伤害，即使你通常会承受。

## 属性

消耗
[反应](Actions.md#Reactions "动作")
详情
范围：自身

## 技术细节

UID

`Interrupt_ShieldBlow`

反应

`ShieldMaster_Block`

授予该反应的被动特性

## 学习方式

由以下特性授予：

- [盾牌大师（专长）](Shield_Master_(Feat).md)

## 注释

- 尽管该特性的描述如此，但动作是否具有敏捷豁免检定或是否是法术并不严格重要。根据经验，涉及敏捷豁免检定的爆炸可以被格挡（例如 [火球术](Fireball.md "火球术")，但不包括 [圣火术](Sacred_Flame.md "圣火术")，后者使用敏捷豁免检定但是单目标）。然而，并非所有此类爆炸都如此，并且有些没有敏捷豁免检定的动作也可以被格挡（例如 [霜冻吐息](Frost_Breath.md "霜冻吐息")，它使用体质豁免检定）。请参考 [此表格](CanAreaDamageEvade_(spell_flag).md#List_of_actions_with_CanAreaDamageEvade).md#List_of_actions_with_CanAreaDamageEvade> "CanAreaDamageEvade (spell flag)") 以获取可被此特性格挡的动作的完整列表。

## 错误

- 此被动目前在豁免失败时不会产生任何效果。

---
*Source: [Shield Master: Block](https://bg3.wiki/wiki/Shield_Master:_Block)*