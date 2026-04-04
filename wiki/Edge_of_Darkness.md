# 黑暗之刃

**黑暗之刃** 是由 [莎尔的黄昏短矛](Shar's_Spear_of_Evening.md "莎尔的黄昏短矛") 赋予的 [武器动作](Weapon_action.md "武器动作")。

## 描述

在攻击时创造一片黑暗云。_\[[参见注释](#notes)\]_

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：

普通武器伤害

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
范围：普通武器范围
范围效果：3 米（10 英尺）半径
目标：范围效果内的每个生物和物品
创建区域：黑暗术
充能：[短休](Short_rest.md "短休")
必须 [熟练](Proficiency.md#Weapon_proficiency "熟练") 使用该武器

## 技术细节

UID

`Target_DEN_Apprentice_DaggerOfShar_Spell`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 区域：黑暗术

**[黑暗术](Darkness_(cloud).md "黑暗术 (云)")**

持续时间：3 驱散
范围效果：3 米（10 英尺）半径

一片魔法黑暗，使范围内的生物被重度遮蔽并目盲。生物无法向黑暗内或从黑暗内进行远程攻击。

类型：[云](Area.md#Cloud "云")

### 状态：目盲

**[目盲](Blinded_(Condition).md "目盲 (状态)")**

- 受影响的生物在 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。
- 受影响生物的攻击和法术范围减少至 3 米（10 英尺）。
- 对受影响生物的攻击掷骰具有 [优势](Advantage.md "优势")。

## 如何习得

由物品赋予：

- [莎尔的黄昏短矛](Shar's_Spear_of_Evening.md "莎尔的黄昏短矛")

## 注释

- 此动作实际上是一个范围效果攻击。在击中主要目标后，会向该目标周围 3 米（10 英尺）云半径内的 _每个_ 生物和物体（包括盟友）进行一次额外攻击。
- 例如 [至圣斩](Divine_Smite.md "至圣斩") 等命中反应可应用于被此动作击中的每个生物（就至圣斩而言，需消耗多个法术位）。

## 错误

- 游戏内此动作的工具提示不准确，且缺少其为范围效果攻击的关键信息。
- 工具提示声称存在关联的 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，但事实并非如此。

---
*Source: [Edge of Darkness](https://bg3.wiki/wiki/Edge_of_Darkness)*