# 繁彩球：火焰

武僧版本请参见 [元素平衡球：火焰](Sphere_of_Elemental_Balance_colon__Fire.md "元素平衡球：火焰")

**繁彩球：火焰** 是一个 [等级1 塑能学派法术](Spells.md "法术")。此法术是 [繁彩球](Chromatic_Orb.md "繁彩球") 的一个变体。它允许施法者投掷一个火球术，造成火焰伤害并创建火焰地表。

## 描述

投掷一个能量球，造成 2d8⁠⁠[火焰](Fire.md "火焰") 伤害并创建一个 [火焰](Fire_(surface).md "火焰（地表）") 地表。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [一级法术位](Spells.md#Spell_slots "法术")
伤害：2~16

2d8⁠[火焰](Fire.md "火焰")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18 米（60 英尺）
创建区域：火焰

## 升环效果

- [升环施法](Upcasting.md "升环施法")：以更高的法术位等级施放此法术时，每比1环高1环，额外造成 1d8⁠⁠[火焰](Fire.md "火焰") 伤害。

## 技术细节

UID

`Projectile_ChromaticOrb_Fire`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：火焰

**[火焰](Fire_(surface).md "火焰（地表）")**

持续时间：2 回合

范围：2 米（7 英尺）半径

每回合造成 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。

类型：[地表](Area.md#Surface "区域")

### 状态：燃烧

**[燃烧](Burning_(Condition).md "燃烧（状态）")**

- 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- 可通过 [协助](Help.md "协助") 动作、使用 [治疗药水](Potion_of_Healing.md "治疗药水") 或获得 [濡湿](Wet_(Condition).md "濡湿（状态）") 状态来移除。
- 如果处于 [濡湿](Wet_(Condition).md "濡湿（状态）") 状态则免疫。
- [蘸取](Dip.md "蘸取") 动作可用于燃烧的角色或物体。

## 如何习得

此法术是以下法术的变体：
[繁彩球](Chromatic_Orb.md "繁彩球")

---
*Source: [Chromatic Orb: Fire](https://bg3.wiki/wiki/Chromatic_Orb:_Fire)*