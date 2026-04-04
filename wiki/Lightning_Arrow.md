# 闪电箭

**闪电箭** 是一个 [法术](Spells.md "法术")。它允许施法者射出一支电箭，在撞击时爆裂，对附近的生物造成额外的闪电伤害。

## 描述

箭矢命中后，较小的闪电会从目标身上蜿蜒射出，击中附近的生物。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [等级 3 法术位](Spells.md#Spell_slots "法术位")
伤害：6~48

4d8⁠[闪电](Lightning.md "闪电")（仅主要目标）

\+ 2d8⁠[闪电](Lightning.md "闪电")（通过 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 可减半）

详情
远程法术 [攻击掷骰](Attack_roll.md "攻击掷骰")（未命中时：范围伤害仍然生效）
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免 DC](Dice_rolls.md#Spell_save_DC "掷骰")）（豁免成功时：目标仍会受到范围伤害的一半。）
范围：18 米（60 英尺）
范围效果：3 米（10 英尺）半径

## 更高施法等级

当法术以 4 级或更高法术位施放时，主要箭矢伤害和爆裂伤害都会比 3 级法术位高 1d8⁠⁠[闪电](Lightning.md "闪电")。

## 技术细节

UID

`Projectile_LightningArrow`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 学习方式

职业：

- 职业等级 9：[游侠](Ranger.md "游侠")

由物品提供：

- [地狱火引擎弩](Hellfire_Engine_Crossbow.md "地狱火引擎弩")（充能：[长休](Long_Rest.md "长休")）

## 备注

- 此法术涉及两次掷骰：一次法术 [攻击掷骰](Attack_roll.md "攻击掷骰") 决定 4d8⁠⁠[闪电](Lightning.md "闪电") 伤害是否作用于主要目标，以及一次 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 决定 2d8⁠⁠[闪电](Lightning.md "闪电") 爆裂伤害是否减半。

## 错误

- 当瞄准法术时，预览中显示的命中率是针对豁免检定的，而非攻击掷骰。
- 如果目标初始豁免检定失败，攻击掷骰总是成功。
- 攻击掷骰未在战斗日志中显示。如果攻击者未命中，则没有迹象表明为何主要 4d8⁠⁠[闪电](Lightning.md "闪电") 伤害未生效。

## 外部链接

- ⁠[闪电箭](https://forgottenrealms.fandom.com/wiki/Lightning_arrow) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Lightning Arrow](https://bg3.wiki/wiki/Lightning_Arrow)*