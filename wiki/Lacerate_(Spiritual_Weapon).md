# 割裂（灵体武器）

本文介绍的是灵体武器使用的攻击版本。关于普通武器动作，请参见[割裂](Lacerate.md "割裂")。

**割裂**是[灵体武器](Spiritual_Weapon.md "灵体武器")召唤的[长戟](Spiritual_Weapon_(halberd).md)、[巨剑](Spiritual_Weapon_(greatsword).md)和[巨斧](Spiritual_Weapon_(greataxe)可用的武器动作.md)。

## 描述

斩击目标的要害部位，使其[流血](Bleeding_(Condition).md "流血（状态）")。

[不死生物](Undead.md "不死生物")和[构装生物](Constructs.md "构装生物")不会流血。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作")
伤害：2~9 + 调整值

1d8 + 1 + [施法调整值](Spells.md#Spellcasting_ability "法术")⁠[力场](Force.md "力场")

详情
近战法术 [攻击掷骰](Attack_roll.md "攻击掷骰")
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰")）
近战：1.5米（5尺）
充能：[短休](Short_rest.md "短休")

## 升环效果

[升环施法](Upcasting.md "升环施法")：此攻击的伤害增加1d8⁠⁠[力场](Force.md "力场")伤害，每比2环高2环使用法术位施放[灵体武器](Spiritual_Weapon.md "灵体武器")时。

## 技术细节

UID

`Target_Slash_SpiritualWeapon_Greataxe`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell_flag\) \(页面不存在\)")`、`[IsHarmful](IsHarmful_(spell_flag).md)`、`[IsMelee](IsMelee_(spell_flag).md)`

## 状态：流血

**[流血](Bleeding_(Condition).md "流血（状态）")**

持续时间：2回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- 生物在每回合开始时受到2⁠⁠[挥砍](Slashing.md "挥砍")[DRS](Damage_rider_as_source.md "伤害驱动源")伤害，并在[体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 通过治疗移除。

## 如何习得

由以下生物使用：[灵体武器（长戟）](Spiritual_Weapon_(halberd).md)、[灵体武器（巨斧）](Spiritual_Weapon_(greataxe).md)和[灵体武器（巨剑）](Spiritual_Weapon_(greatsword).md)

## 备注

- 此攻击的攻击掷骰和伤害使用召唤者的施法调整值，但施加状态的DC基于*召唤武器*的[武器动作DC](Dice_rolls.md#Save_DCs "掷骰")（带有固有+2加值）。由于武器的属性值为10，这导致DC仅为12（熟练项加值为2时）至14（熟练项加值为4时）。
- 此攻击的短休充能重置在重新召唤灵体武器时生效，因此实际上是每次召唤可使用一次。

## 错误

- 游戏内工具提示不正确 - 所有伤害均为⁠[力场](Force.md "力场")伤害。
  - 与其他灵体武器攻击不同，此攻击造成的伤害是非魔法的。

---
*Source: [Lacerate (Spiritual Weapon)](https://bg3.wiki/wiki/Lacerate_(Spiritual_Weapon)*