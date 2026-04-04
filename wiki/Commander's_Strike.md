# 指挥官奇袭

**指挥官奇袭**是[战斗大师](Battle_Master.md "战斗大师")战士的职业动作。这项战斗策略允许战士消耗一个动作、附赠动作和卓越骰子，使一名盟友在其后续回合中以反应进行一次近战武器攻击。

## 描述

指挥一名盟友攻击敌人。该盟友将在其下一回合使用反应进行一次[武器攻击](Commander's_Strike_(Attack).md "指挥官奇袭（攻击）")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [附赠动作](Actions.md#Resources "动作") + [卓越骰子](Battle_Master.md#Level_3 "战斗大师")
详情
范围：9米（30英尺）

## 技术细节

UID

`Target_CommandersStrike`

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 授予

- [指挥官奇袭（攻击）](Commander's_Strike_(Attack).md "指挥官奇袭（攻击）")

## 状态：战斗职责

**[战斗职责](Onus_of_Battle_(Condition).md "战斗职责（状态）")**

持续时间：3回合

- 受影响实体可立即使用[反应](Actions.md#Reactions "动作")进行一次武器攻击。

## 学习方式

职业：

- 职业等级3：[战斗大师](Battle_Master.md "战斗大师")

由特性授予：

- [战技专家](Martial_Adept.md "战技专家")

由物品授予：

- [雷文伽德公爵的长剑](Duke_Ravengard's_Longsword.md "雷文伽德公爵的长剑")（充能：[短休](Short_rest.md "短休")）
- [雷文伽德的鞭笞](Ravengard's_Scourger.md "雷文伽德的鞭笞")（充能：[短休](Short_rest.md "短休")）

## 备注

- [战斗职责](Onus_of_Battle_(Condition).md "战斗职责（状态）")在授予的攻击完成后立即结束，即使未命中。
- 授予的攻击必须是近战武器攻击，不能是远程或徒手打击。
- 指挥官奇袭会触发使用者的[额外攻击](Extra_Attack.md "额外攻击")。
  - 给予盟友的武器攻击*不会*触发额外攻击，因为它不消耗[动作](Actions.md#Resources "动作")。
- 最佳使用对象是能进行强力武器攻击的角色，例如[圣武士](Paladin.md "圣武士")或[游荡者](Rogue.md "游荡者")。但请注意，在大多数情况下，游荡者每战斗轮只能获得一次[偷袭](Sneak_Attack_(Melee).md)（通常在他们自己的回合）。因此，在此处授予游荡者额外攻击通常无法获得期望的额外偷袭伤害。

---
*Source: [Commander's Strike](https://bg3.wiki/wiki/Commander's_Strike)*