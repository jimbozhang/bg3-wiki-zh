# 灼热血液

**灼热血液**是一种由[断裂之刃](Rupturing_Blade.md "断裂之刃")赋予的[武器动作](Weapon_action.md "武器动作")。

## 描述

切入敌人，对其造成额外的[熟练项加值](Proficiency_Bonus.md "熟练项加值")⁠[火焰](Fire.md "火焰")伤害和1d6⁠[火焰](Fire.md "火焰")伤害，同时自身承受1d6⁠[挥砍](Slashing.md "挥砍")伤害。此外，该攻击可能使目标[流血](Bleeding_(Condition).md "流血（状态）")和[燃烧](Burning_(Condition).md "燃烧（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~12 + 调整值

普通武器伤害

\+ [熟练项加值](Proficiency_Bonus.md "熟练项加值")⁠[火焰](Fire.md "火焰")

\+ 1d6⁠[火焰](Fire.md "火焰")

\+ 1d6⁠[穿刺](Piercing.md "穿刺")（对自身）

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）
近战：1.5米（5英尺）
充能：[短休](Short_rest.md "短休")
必须[熟练项](Proficiency.md#Weapon_proficiency "熟练项")该武器

## 技术细节

UID

`Target_MAG_WeaponAction_SearingBlood`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell_flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：流血

**[流血](Bleeding_(Condition).md "流血（状态）")**

持续时间：2回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- 生物每回合开始时承受2⁠[挥砍](Slashing.md "挥砍")[DRS](Damage_rider_as_source.md "伤害驱动源")伤害，并在[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 通过治疗移除。

## 状态：燃烧

**[燃烧](Burning_(Condition).md "燃烧（状态）")**

持续时间：2回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰") + 2）

- 每回合承受1d4⁠[火焰](Fire.md "火焰")伤害。
- 可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿（状态）")来移除。
- 如果处于[濡湿](Wet_(Condition).md "濡湿（状态）")状态则免疫。
- [蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。

## 如何习得

由物品赋予：

- [断裂之刃](Rupturing_Blade.md "断裂之刃")

## 注释

- 目标会分别进行豁免检定以避免[流血](Bleeding_(Condition).md "流血（状态）")和[燃烧](Burning_(Condition).md "燃烧（状态）")。
- 该攻击的伤害调整值作为[伤害驱动源](Damage_rider_source.md "伤害驱动源")起作用，即使在[荣誉模式](Honour_Mode.md "荣誉模式")中也是如此。因此，诸如[生离死别：尖啸](Phalar_Aluve_colon__Shriek.md "生离死别：尖啸")和[脆弱诅咒](Hex.md "脆弱诅咒")等驱动效果会分别对武器基础伤害、1d6火焰伤害和熟练项加值火焰伤害触发。值得注意的是，这些加成也适用于反射回攻击者的1d6挥砍伤害。

## 错误

- 工具提示未提及施加流血和燃烧。

## 视觉效果

加载视频

本地文件

本地文件可能收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Searing_Blood_Action.mp4>

---
*Source: [Searing Blood](https://bg3.wiki/wiki/Searing_Blood)*