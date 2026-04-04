# 元素平衡球：毒素

**元素平衡球：毒素** 是一个动作，允许四象宗武僧发射一个[毒素](Poison.md "毒素")元素能量球，对目标造成伤害并在身后留下一个持续的毒性区域。这个动作是武僧版本的[繁彩球：毒素](Chromatic_Orb_colon__Poison.md "繁彩球：毒素")。

## 描述

猛投有毒能量，对目标造成伤害并创建一个冒泡的地表，对生物施加[中毒](Simple_Toxin_(Condition).md "简易毒素（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 2 [气点](Ki_Point.md "气点")
伤害：2~16

2d8⁠[毒素](Poison.md "毒素")

详情
远程法术 [攻击掷骰](Attack_roll.md "攻击掷骰")
范围：18 米（60 英尺）
创建区域：简易毒素

## 技术细节

UID

`Projectile_ChromaticOrb_Poison_Monk`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 授予

- [武艺：附赠徒手打击](Martial_Arts_colon__Bonus_Unarmed_Strike.md "武艺：附赠徒手打击")

## 区域：简易毒素

**[简易毒素](Simple_Toxin_(surface).md "简易毒素（地表）")**

持续时间：2 回合
范围：2 米（7 英尺）半径
施加中毒。
类型：[地表](Area.md#Surface "区域")

### 状态：简易毒素

**[简易毒素](Simple_Toxin_(Condition).md "简易毒素（状态）")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响实体在其下一回合结束时受到 1d4⁠⁠[毒素](Poison.md "毒素") 伤害。

## 如何习得

此法术是以下法术的变体：
[元素平衡球](Sphere_of_Elemental_Balance.md "元素平衡球")

## 备注

- 尽管工具提示描述说它使生物中毒，但它实际上施加的是[简易毒素](Simple_Toxin_(Condition).md "简易毒素（状态）")状态，而不是普通的[中毒](Poisoned_(Condition).md "中毒（状态）")状态。

---
*Source: [Sphere of Elemental Balance: Poison](https://bg3.wiki/wiki/Sphere_of_Elemental_Balance:_Poison)*