# 石化术

另请参阅：[血肉成金](Flesh_to_Gold.md "血肉成金")

**石化术**是一个[6级变化学派法术](Spells.md "Spells")。它允许施法者使敌人[衰弱](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)")，将其[束缚](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)")，直到其暂时变为石头。

## 描述

使敌人[衰弱](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)")，将其[束缚](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)")，直到其暂时变为石头。

如果目标在3回合内未能通过其[豁免检定](Saving_throw.md "Saving Throw")，它将[石化](Petrified_(Condition).md "Petrified (Condition)")。_\[[参见注释](#notes)\]_

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [6级法术位](Spells.md#Spell_slots "Spells")
详情
[体](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）
射程：18米（60英尺）
[专注](Concentration.md "Concentration")

## 更高法术位施法

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_FleshToStone`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：石化术：束缚阶段 1

**[石化术：束缚阶段 1](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)")**

持续时间：3回合

- 受影响实体无法移动，因为其身体在3回合的过程中开始石化。
- 对其进行的[攻击掷骰](Attack_roll.md "Attack Roll")具有[优势](Advantage.md "Advantage")，而该实体的攻击掷骰和敏捷[豁免检定](Saving_throw.md "Saving Throw")具有[劣势](Disadvantage.md "Disadvantage")。

## 状态：石化

**[石化](Petrified_(Condition).md "Petrified (Condition)")**

持续时间：永久

[体](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）

- 变为石头。无法移动或执行[动作](Actions.md#Resources "Actions")、[附赠动作](Actions.md#Resources "Actions")或[反应](Actions.md#Reactions "Actions")。

## 学习方式

职业：

- 职业等级 11：[法师](Wizard.md "Wizard")和[邪术师](Warlock.md "Warlock")

其他学习方式：

- 拥有[6级法术位](Spells.md#Spell_slots "Spells")的[法师](Wizard.md "Wizard")可以将[石化术卷轴](Scroll_of_Flesh_to_Stone.md "Scroll of Flesh to Stone")[抄录](Transcribing_scrolls.md "Transcribing scrolls")到其法术书中。

## 注释

- 目标必须总共失败_四_次[豁免检定](Saving_throw.md "Saving Throw")才能变为石头。目标每次豁免检定失败，都会进入**石化术**减益的新阶段，所有阶段的效果均与[束缚](Restrained_(Condition).md "Restrained (Condition)")相同：
- **[石化术：束缚阶段 1](Flesh_to_Stone_colon__Restrained_Stage_1_(Condition).md "Flesh to Stone: Restrained Stage 1 (Condition)"):** 受影响实体无法移动，因为其身体在3回合的过程中开始石化。
- **[石化术：束缚阶段 2](Flesh_to_Stone_colon__Restrained_Stage_2_(Condition).md "Flesh to Stone: Restrained Stage 2 (Condition)"):** 受影响实体无法移动，因为其身体正朝着石化进展。
- **[石化术：束缚阶段 3](Flesh_to_Stone_colon__Restrained_Stage_3_(Condition).md "Flesh to Stone: Restrained Stage 3 (Condition)"):** 受影响实体无法移动，因为其身体进入了石化的最后骨僵阶段。
  - 在第四回合，目标变为[石化](Petrified_(Condition).md "Petrified (Condition)")。
- 在四次石化豁免检定期间，对此生物施放此法术不会引发敌意。然而，一旦生物变为石头或通过豁免检定，其附近的盟友将变得敌对和/或引发守卫反应。

## 错误

- 尽管描述说明效果是“暂时的”，但此法术导致的石化确实是永久的，直到目标被[石化蜥蜴油](Basilisk_Oil.md "Basilisk Oil")或[高等复原术](Greater_Restoration.md "Greater Restoration")等法术治愈。
- 通过使用名为 `HasFleshToSToneCheck()` 的 `khn` 函数，**石化术**和[血肉成金](Flesh_to_Gold.md "Flesh to Gold")不应施放在已受这两种法术之一影响的目标上。然而，此函数仅包含对石化术状态的检查，因此石化术可以施放在已受血肉成金影响的生物上。

## 外部链接

- ⁠[石化术](https://forgottenrealms.fandom.com/wiki/Flesh_to_stone) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Flesh to Stone](https://bg3.wiki/wiki/Flesh_to_Stone)*