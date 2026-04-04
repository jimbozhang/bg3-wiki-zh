# 震荡猛击 (灵体武器)

本文介绍的是灵体武器使用的攻击版本。关于普通武器动作，请参见 [震荡猛击](Concussive_Smash.md "震荡猛击")。

**震荡猛击**是 [灵体武器](Spiritual_Weapon.md "灵体武器") 召唤的 [巨锤](Spiritual_Weapon_(maul).md) 所使用的武器动作。

## 描述

可能使目标[眩晕](Dazed_(Condition).md "眩晕 (状态)")。目标无法采取[反应](Reaction.md "反应")，并失去其[护甲等级](Armour_Class.md "护甲等级")的[敏捷](Dexterity.md "敏捷")加值。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作")
伤害：2~9 + 调整值

1d8 + 1 + [施法调整值](Spells.md#Spellcasting_ability "法术")⁠[力场](Force.md "力场")

详情
近战法术 [攻击掷骰](Attack_roll.md "攻击掷骰")
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([混合难度等级](Dice_rolls.md#Hybrid_DC "掷骰"))
近战：1.5 米 (5 英尺)
充能：[短休](Short_rest.md "短休")

## 升环效果

[升环施法](Upcasting.md "升环施法")：此攻击的伤害增加 1d8⁠⁠[力场](Force.md "力场") 伤害，每比 2 环高 2 个法术位等级（用于施放 [灵体武器](Spiritual_Weapon.md "灵体武器")）。

## 技术细节

UID

`Target_ConcussiveSmash_SpiritualWeapon_Maul`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：眩晕

**[眩晕](Dazed_(Condition).md "眩晕 (状态)")**

持续时间：2 驱散

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([混合难度等级](Dice_rolls.md#Hybrid_DC "掷骰"))

- 在[感知](Wisdom.md "感知") [豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")，无法采取[反应](Reaction.md "反应")，并失去其[护甲等级](Armour_Class.md "护甲等级")的[敏捷](Dexterity.md "敏捷")加值。
- 如果盟友[协助](Help.md "协助")此生物，则移除此状态。

## 如何习得

由生物使用：[灵体武器 (巨锤)](Spiritual_Weapon_(maul).md)

## 备注

- 此攻击的攻击掷骰和伤害使用召唤者的施法调整值，但施加状态的难度等级基于*召唤武器*的[武器动作难度等级](Dice_rolls.md#Save_DCs "掷骰")（具有固有 +2 加值）。由于武器的属性值为 10，这导致难度等级仅为 12（熟练项加值为 2）至 14（熟练项加值为 4）。
- 此攻击的短休充能冷却在重新召唤灵体武器时重置，因此实际上是每次召唤使用一次。

## 错误

- 游戏内工具提示不正确 - 所有造成的伤害都是⁠[力场](Force.md "力场") 伤害。
  - 与其他灵体武器攻击不同，造成的伤害是非魔法的。

---
*Source: [Concussive Smash (Spiritual Weapon)](https://bg3.wiki/wiki/Concussive_Smash_(Spiritual_Weapon)*