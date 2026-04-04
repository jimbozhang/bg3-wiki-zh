# 疫病术

**疫病术**是一个[法术](Spells.md "法术")。它允许施法者用他们选择的疾病感染目标，可能导致目标患上疾病。

## 描述

毒害一个目标，并可能使其患上你选择的疾病。

一旦感染，目标每回合将进行一次[体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw")。如果累计3次成功，它将恢复。如果累计3次失败，它将患上施法者选择的疾病。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [5级法术位](Spells.md#Spell_slots "Spells")
详情
近战法术 [攻击掷骰](Attack_roll.md "Attack Roll")
近战：1.5米（5英尺）

## 升环施法效应

以此法术升环施法不会获得额外效果。

## 技术细节

UID

`Target_Contagion`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 变体

- [疫病术：污秽热](Contagion_colon__Filth_Fever.md "Contagion: Filth Fever")
- [疫病术：血肉腐烂](Contagion_colon__Flesh_Rot.md "Contagion: Flesh Rot")
- [疫病术：黏滑末日](Contagion_colon__Slimy_Doom.md "Contagion: Slimy Doom")
- [疫病术：癫痫](Contagion_colon__Seizure.md "Contagion: Seizure")
- [疫病术：脑火](Contagion_colon__Mindfire.md "Contagion: Mindfire")
- [疫病术：失明症](Contagion_colon__Blinding_Sickness.md "Contagion: Blinding Sickness")

## 状态：疫病中毒

**[疫病中毒](Contagion_Poisoned_(Condition).md "Contagion Poisoned (Condition)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）

- 在[攻击掷骰](Attack_roll.md "Attack Roll")和[属性检定](Ability_Check.md "属性检定")上具有[劣势](Disadvantage.md "Disadvantage")。
- 每回合，它必须成功通过一次[豁免检定](Saving_throw.md "Saving Throw")，否则毒素将进入下一阶段。累计3次成功，它将恢复。累计3次失败，它将患上与所施放的疫病术变体相对应的疾病。

## 如何习得

职业：

- 职业等级9：[牧师](Cleric.md "Cleric")、[德鲁伊](Druid.md "Druid")、[孢子结社](Circle_of_the_Spores.md "Circle of the Spores")（结社法术）、[大地结社](Circle_of_the_Land.md "Circle of the Land")（极地/森林/幽暗地域），以及[死亡领域](Death_Domain.md "Death Domain")（领域法术）
- 职业等级10：[吟游诗人](Bard.md "Bard")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）

## 备注

- 此法术命中后，目标仅受较弱的疫病中毒状态影响，直到它失败3次豁免检定。然后所选疾病变体生效，并在长休后持续存在，本质上是永久性的。要移除此效果，需用[恢复](Lesser_Restoration.md "Lesser Restoration")或[类似效果](Diseased_(status_group).md#Removal).md#Removal> "Diseased (status group)")治疗目标。
- 在战斗外对任何NPC施放疫病术不被视为攻击性动作。
  - 然而，施放法术时攻击掷骰失败*是*被视为攻击性的，并可能导致NPC敌对。
  - 感染[疫病术：脑火](Contagion_colon__Mindfire.md "Contagion: Mindfire")后，NPC将永久对所有人[敌对](Hostile.md "Hostile")，这对于关键任务NPC可能是不希望的。
- 不同法术变体施加的状态不共享[堆叠ID](Stack_ID.md "Stack ID")。这意味着一个目标可以同时受到多个不同的疫病感染。

## 外部链接

- ⁠[疫病术](https://forgottenrealms.fandom.com/wiki/Contagion) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Contagion](https://bg3.wiki/wiki/Contagion)*