# 繁彩球：毒素

武僧版本请参见 [元素平衡球：毒素](Sphere_of_Elemental_Balance_colon__Poison.md "元素平衡球：毒素")

**繁彩球：毒素** 是一个 [法术](Spells.md "法术")。此法术是 [繁彩球](Chromatic_Orb.md "繁彩球") 的变体。它允许施法者投掷一个毒素球体，造成毒素伤害并创建一个中毒地表。

## 描述

投掷有毒能量，对目标造成伤害，并创建一个冒泡的地表以[中毒](Poisoned_(Condition).md "中毒（状态）")生物。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：2~16

2d8⁠[中毒](Poison.md "中毒")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
创建区域：简易毒素

## 升环施法

- [升环施法](Upcasting.md "升环施法")：以更高法术位施放此法术时，每比1环高1环，额外造成1d8⁠⁠[中毒](Poison.md "中毒")伤害。

## 技术细节

UID

`Projectile_ChromaticOrb_Poison`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：简易毒素

**[简易毒素](Simple_Toxin_(surface).md "简易毒素（地表）")**

持续时间：2回合

范围：2米（7英尺）半径

施加中毒。

类型：[地表](Area.md#Surface "区域")

### 状态：简易毒素

**[简易毒素](Simple_Toxin_(Condition).md "简易毒素（状态）")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响实体在其下一回合结束时受到1d4⁠⁠[中毒](Poison.md "中毒")伤害。

## 如何习得

此法术是以下法术的变体：
[繁彩球](Chromatic_Orb.md "繁彩球")

---
*Source: [Chromatic Orb: Poison](https://bg3.wiki/wiki/Chromatic_Orb:_Poison)*