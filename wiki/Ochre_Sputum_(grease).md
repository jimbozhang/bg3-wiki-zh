# 赭色唾液（油脂）

本文介绍的是油脂球（Greaseball）使用的版本。关于赭色史莱姆（Ochre Jelly）使用的版本，请参见[赭色唾液（强酸）](Ochre_Sputum_(acid).md)>。

**赭色唾液**是[油脂球](Greaseball.md "油脂球")可用的类动作，允许它们向目标喷吐强酸，并留下油脂地表。

## 描述

喷吐一种酸性物质，并在命中时创造一个[油脂](Grease_(surface).md "油脂（地表）")地表。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~12

2d6⁠[强酸](Acid.md "强酸")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
创造区域：油脂

## 技术细节

UID

`Projectile_LOW_GreaseWizard_Ooze_Spit`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`

## 区域：油脂

**[油脂](Grease_(surface).md "油脂（地表）")**

持续时间：3驱散

范围效果：1米（3英尺）半径

劣势地形 - [移动速度](Movement_speed.md "移动速度")减半，且生物可能倒伏。易燃。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或采取[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在距离生物3米（10英尺）内进行的攻击对倒伏生物具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）移动速度。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半

## 如何习得

由以下生物使用：[油脂球](Greaseball.md "油脂球")

## 错误

- 游戏内描述提到它会创造一个[强酸](Acid_(surface).md "强酸（地表）")地表，但实际上它创造的是[油脂](Grease_(surface).md "油脂（地表）")地表。它还说会施加[中毒](Poisoned_(Condition).md "中毒（状态）")并涉及[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，但这也不正确。

---
*Source: [Ochre Sputum (grease)](https://bg3.wiki/wiki/Ochre_Sputum_(grease)*