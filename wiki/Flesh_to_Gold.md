# 血肉成金

另请参阅：[石化术](Flesh_to_Stone.md "Flesh to Stone")

**血肉成金**是一个[6级法术](Spells.md "Spells")。它束缚目标并在3回合后将其转化为黄金。

## 描述

[束缚](Restrained_(Condition).md "Restrained (Condition)")一个目标，并在3轮后，目标变为静止的实心黄金，直到法术结束。

如果目标在3回合内未能通过其[豁免检定](Saving_throw.md "Saving Throw")，则目标将[石化](Petrified_(Condition).md "Petrified (Condition)")。_\[[参见注释](#notes)\]_

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [6级法术位](Spells.md#Spell_slots "Spells")
详情
[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws")
射程：18米（60英尺）
[专注](Concentration.md "Concentration")

## 更高环阶施法

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_TWN_Tollhouse_FleshToGold`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：化为黄金

**[化为黄金](Turned_to_Gold_(Condition).md "Turned to Gold (Condition)")**

持续时间：永久

[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "Saving throws") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "Dice rolls"))

- 受影响的生物化为黄金。它无法移动或执行动作、附赠动作或反应。

## 如何习得

由物品提供：

- [已署名的贸易签证](Signed_Trade_Visa.md "Signed Trade Visa")

## 注释

- 此法术只能通过消耗[已署名的贸易签证](Signed_Trade_Visa.md "Signed Trade Visa")施放一次。如果某些角色无法死亡，使用它可能会带来意外（导致游戏结束）的后果。此法术无法复制到[法师](Wizard.md "Wizard")的法术书中。然而，功能相同的[石化术](Flesh_to_Stone.md "Flesh to Stone")可以被11级[法师](Wizard.md "Wizard")和[邪术师](Warlock.md "Warlock")习得。
- 与所有卷轴一样，施放此法术时不会消耗法术位，只会消耗卷轴本身和一个[动作](Actions.md#Resources "Actions")。
- 目标必须总共失败四次[豁免检定](Saving_throw.md "Saving Throw")才能化为黄金。目标每回合失败一次豁免检定，就会进入**血肉成金**减益的新阶段，所有阶段的效果均与[束缚](Restrained_(Condition).md "Restrained (Condition)")相同：
  - **血肉成金：阶段1：** 受影响实体无法移动，因为其身体开始在3回合内转变为黄金。
  - **血肉成金：阶段2：** 受影响实体无法移动，因为其身体正在转变为黄金。
  - **血肉成金：阶段3：** 受影响实体无法移动，因为其身体进入黄金化的最后阶段。

## 错误

- 尽管描述中说明效果持续“直到法术结束”，但此法术导致的石化效果确实是永久的，直到目标被[石化蜥蜴油](Basilisk_Oil.md "Basilisk Oil")或[高等复原术](Greater_Restoration.md "Greater Restoration")等法术治愈。
- 血肉成金错误地使用了石化术的图标，因为石化术是其父法术。
- 尽管施放需要专注，但一旦目标进入血肉成金：阶段2，血肉成金的专注立即结束，之后不再需要。
- 通过使用名为 `HasFleshToSToneCheck()` 的 `khn` 函数，石化术和血肉成金应无法施放在已受这两种法术影响的目标上。然而，此函数仅包含对石化术状态的检查，因此石化术可以施放在已受血肉成金影响的生物上。

---
*Source: [Flesh to Gold](https://bg3.wiki/wiki/Flesh_to_Gold)*