# 黑洞

本文讨论的是普通灵吸怪威能。关于强化的完整灵吸怪版本，请参见[星云黑洞](Nebulous_Black_Hole.md "星云黑洞")。

**黑洞**是一个动作和[灵吸怪威能](Illithid_power.md "灵吸怪威能")。此能力会创造一个黑洞，将附近的敌人拉入其中，并可能使其[减速](Slow.md "减速")。

## 描述

创造一个强引力点，将所有附近的敌人拉入其中，并可能使其[减速](Slowed_(Condition).md "减速（状态）")。

在此法术初始施放后，可再召唤五个黑洞_\[[参见注释](#notes)\]_。之后，你必须[短休](Short_rest.md "短休")才能再次施放。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
射程：18米（60英尺）
范围效果：9米（30英尺）半径
牵引：6米（20英尺）（朝向范围效果中心，无豁免检定）
目标：范围效果内的所有敌人
充能：[短休](Short_rest.md "短休")
持续时间：5回合

## 技术细节

UID

`Target_TAD_BlackHole`

法术标志

`[DisableBlood](https://bg3.wiki/w/index.php?title=DisableBlood_\(spell_flag\)&action=edit&redlink=1) "DisableBlood \(spell_flag\) \(页面不存在\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：减速

**[减速](Slowed_(Condition).md "减速（状态）")**

持续时间：1回合

[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- [移动速度](Movement_speed.md "移动速度")减半
- [护甲等级](Armour_Class.md "护甲等级")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")降低2点
- 只能执行一个[动作](Action.md "动作")或一个[附赠动作](Bonus_action.md "附赠动作")，不能同时执行两者
- 无法执行[反应](Reaction.md "反应")
- 无法进行[额外攻击](Extra_Attack.md "额外攻击")或[精通额外攻击](Improved_Extra_Attack.md "精通额外攻击")_\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速（状态）")\]_
- 施放的法术可能会延迟一回合_\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速（状态）")\]_

## 学习方式

被以下生物使用：[门徒泽'瑞尔](Disciple_Z'rell.md "门徒泽'瑞尔")和[超魔虐待者](Metamage_Persecutor.md "超魔虐待者")

其他学习方式：

- 在获得以下[灵吸怪威能](Illithid_powers.md "灵吸怪威能")之一后，使用[夺心魔寄生虫标本](Mind_Flayer_Parasite_Specimen.md "夺心魔寄生虫标本")解锁：
- [移位](Displace.md "移位")
  - [灵能统御](Psionic_Dominance.md "灵能统御")

## 注释

- 描述中“在此法术初始施放后，可再召唤五个黑洞”具有误导性。实际上，施法者被授予在5回合内重新施放黑洞的能力。无论黑洞是否被使用了五次，此能力都将在5回合后消失。相反，借助额外动作来源，黑洞在此期间可以被重新施放超过五次。

---
*Source: [Black Hole](https://bg3.wiki/wiki/Black_Hole)*