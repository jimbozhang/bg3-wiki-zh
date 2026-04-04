# 繁彩球：寒冷

武僧版本，请参见 [元素平衡球：寒冷](Sphere_of_Elemental_Balance_colon__Cold.md "元素平衡球：寒冷")

**繁彩球：寒冷** 是一个 [法术](Spells.md "法术")。此法术是 [繁彩球](Chromatic_Orb.md "繁彩球") 的一个变体。它允许施法者投掷一个寒冷能量球体，造成寒冷伤害并创造一个冰面。

## 描述

投掷一个能量球体，造成 2d8⁠⁠[寒冷](Cold.md "寒冷") 伤害并创造一个 [冰](Ice_(surface).md "冰（地表）") 地表。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：2~16

2d8⁠[寒冷](Cold.md "寒冷")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
创造区域：冰

## 升环施法

- [升环施法](Upcasting.md "升环施法")：以更高的法术位施放此法术时，每比1环高1环，额外造成 1d8⁠⁠[寒冷](Cold.md "寒冷") 伤害。

## 技术细节

UID

`Projectile_ChromaticOrb_Cold`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：冰

**[冰](Ice_(surface).md "冰（地表）")**

持续时间：2回合

范围：2米（7英尺）半径

劣势地形 - [移动速度](Movement_speed.md "移动速度") 减半，生物可能 [倒伏](Prone.md "倒伏")。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或进行 [动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作") 或 [反应](Actions.md#Reactions "动作")，并且在 [力量](Strength.md "力量") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 上具有 [劣势](Disadvantage.md "劣势")。
- 在距离生物 3米（10英尺）范围内进行的攻击对倒伏生物具有 [优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的 [移动速度](Movement_speed.md "移动速度") 才能站起。
  - 拥有 [运动员](Athlete.md "运动员") 专长的角色仅需花费 1.5米（5英尺）的移动速度即可站起。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")**

- [移动速度](Movement_speed.md "移动速度") 减半

## 如何习得

此法术是以下法术的变体：
[繁彩球](Chromatic_Orb.md "繁彩球")

---
*Source: [Chromatic Orb: Cold](https://bg3.wiki/wiki/Chromatic_Orb:_Cold)*