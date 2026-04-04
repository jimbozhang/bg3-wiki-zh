# 黎明爆裂打击

**黎明爆裂打击** 是由 [圣星](The_Sacred_Star.md "圣星") 赋予的 [武器动作](Weapon_action.md "武器动作")。

## 描述

造成额外的 [光耀](Radiant.md "光耀") 伤害，伤害值等于你的 [熟练项加值](Proficiency_Bonus.md "熟练项加值")。命中时，光芒在你周围 3 米（10 英尺）的区域内爆发。光芒中的敌人必须通过 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，否则将被 [目盲](Blinded_(Condition).md "目盲（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")

伤害：

普通武器伤害

\+ [熟练项加值](Proficiency_Bonus.md "熟练项加值")⁠[光耀](Radiant.md "光耀")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
[体质](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定")（[武器动作 DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）
范围：普通武器范围
区域效果：3 米（10 英尺）半径
充能：[短休](Short_rest.md "短休")
必须 [熟练](Proficiency.md#Weapon_proficiency "熟练项") 使用该武器

## 技术细节

UID

`Target_MAG_WeaponAction_FlashingDawn`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell_flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：目盲

**[目盲](Blinded_(Condition).md "目盲（状态）")**

持续时间：3 驱散

[体质](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定")（[武器动作 DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- 受影响的生物在 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术范围缩小至 3 米（10 英尺）。
- 对受影响生物的攻击掷骰具有 [优势](Advantage.md "优势")。

## 如何习得

由物品赋予：

- [圣星](The_Sacred_Star.md "圣星")

## 错误

- 游戏内描述注明了错误的 [DC](Dice_rolls.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")。它需要一个武器动作豁免检定，并带有 +2 DC 加值。
  - 尽管游戏内描述说明只有光芒中的敌人必须通过豁免检定以避免目盲，但目盲会影响区域内的所有生物，包括盟友。
- 由于编码错误，目盲不会影响攻击的原始目标。

---
*Source: [Dawnburst Strike](https://bg3.wiki/wiki/Dawnburst_Strike)*