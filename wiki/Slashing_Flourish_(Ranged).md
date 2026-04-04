# 挥砍华舞（远程）

本文介绍该动作的远程版本。关于近战版本，请参见 [挥砍华舞（近战）](Slashing_Flourish_(Melee)..md)

**挥砍华舞（远程）** 是 [剑舞学院](College_of_Swords.md "剑舞学院") 吟游诗人的武器动作。此华舞策略允许诗人使用 [诗人激励](Bardic_Inspiration_(resource).md) 发动一次远程武器攻击，发射两个独立的投射物并造成额外伤害。这两个投射物可以指向两个不同的目标，也可以同时指向一个目标。

## 描述

同时攻击最多 2 个敌人。

你必须装备远程武器。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中时消耗
[诗人激励](Bardic_Inspiration_(resource).md)
伤害：2~12

正常武器伤害

\+ 1d6⁠[武器](Weapon.md "武器")

\+ 正常武器伤害

\+ 1d6⁠[武器](Weapon.md "武器")

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程：正常武器射程
目标：2 个目标或 1 个目标两次

## 等级提升效果

- 等级 5 时，拥有 [精通诗人激励](Improved_Bardic_Inspiration_(passive_feature).md "精通诗人激励（被动特性）")，伤害加成提升至 1d8。
- 等级 10 时，拥有 [精通诗人激励](Improved_Bardic_Inspiration_(passive_feature).md "精通诗人激励（被动特性）")，伤害加成提升至 1d10。

## 技术细节

UID

`Projectile_BladeFlourish_Slashing`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 学习方式

职业：

- 职业等级 3：[剑舞学院](College_of_Swords.md "剑舞学院")

## 错误

- 尽管描述如此，此动作缺少法术标志 `IgnorePreviouslyPickedEntities`，并允许对同一敌人攻击两次。

---
*Source: [Slashing Flourish (Ranged)](https://bg3.wiki/wiki/Slashing_Flourish_(Ranged)*