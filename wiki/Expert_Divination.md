# 预言专家

**预言专家**是[预言学派](Divination_School.md "预言学派")法师的被动特性，它会额外提供一个预兆骰子，并允许使用者在短休时通过完成预言来恢复所有已消耗的预兆骰子。这些预言通常需要施放特定学派的法术或造成特定类型的伤害。

## 描述

你获得一个额外的[预兆](Portent.md "预兆")。进行[短休](Short_rest.md "短休")时，你会收到一组[预言](Prophecy.md "预言")。完成它们以恢复缺失的预兆骰子。

## 如何习得

职业：

- 职业等级 6：[预言学派](Divination_School.md "预言学派")

## 备注

- 此特性将使用者的预兆骰子最大数量增加至 3。
- 短休后，使用者会为每个已消耗的预兆骰子随机获得一个预言。完成该预言会恢复一个具有新随机值的骰子。
- 这意味着**预言专家**将预兆骰子的使用上限从每次长休最多 2 个扩展到每次短休最多 3 个。
- 可能的不同预言有：
  - 造成特定伤害类型：
- [预言：阅后即焚](Prophecy_colon__Burn_After_Reading_(Condition).md "预言：阅后即焚（状态）")
- [预言：冰冷接待](Prophecy_colon__Frosty_Reception_(Condition).md "预言：冰冷接待（状态）")
- [预言：惊人启示](Prophecy_colon__Shocking_Revelation_(Condition).md "预言：惊人启示（状态）")
- [预言：雷鸣掌声](Prophecy_colon__Thunderous_Applause_(Condition).md "预言：雷鸣掌声（状态）")
- [预言：强力坚持](Prophecy_colon__Forceful_Insistence_(Condition).md "预言：强力坚持（状态）")
- [预言：沉重命运](Prophecy_colon__Grave_Fate_(Condition).md "预言：沉重命运（状态）")
- [预言：恶毒言语](Prophecy_colon__Venomous_Words_(Condition).md "预言：恶毒言语（状态）")
- [预言：头痛](Prophecy_colon__Headache_(Condition).md "预言：头痛（状态）")
- [预言：神圣顿悟](Prophecy_colon__Holy_Epiphany_(Condition).md "预言：神圣顿悟（状态）")
- [预言：大熔炉](Prophecy_colon__Melting_Pot_(Condition).md "预言：大熔炉（状态）")
- [预言：钝器](Prophecy_colon__A_Blunt_Tool_(Condition).md "预言：钝器（状态）")
- [预言：小刺](Prophecy_colon__A_Little_Prick_(Condition).md "预言：小刺（状态）")
- [预言：锋芒毕露](Prophecy_colon__Cutting_Edge_(Condition).md "预言：锋芒毕露（状态）")
  - 施放特定学派的法术：
- [预言：戒备](Prophecy_colon__Guarded_(Condition).md "预言：戒备（状态）")
- [预言：小帮助](Prophecy_colon__A_Little_Help_(Condition).md "预言：小帮助（状态）")
- [预言：可预测](Prophecy_colon__Predictable_(Condition).md "预言：可预测（状态）")
- [预言：迷人法术](Prophecy_colon__Spellbinding_(Condition).md "预言：迷人法术（状态）")
- [预言：唤起](Prophecy_colon__Evocative_(Condition).md "预言：唤起（状态）")
- [预言：佯装惊讶](Prophecy_colon__Feign_Surprise_(Condition).md "预言：佯装惊讶（状态）")
- [预言：死得其所](Prophecy_colon__Dead_Right_(Condition).md "预言：死得其所（状态）")
- [预言：变化](Prophecy_colon__Changes_(Condition).md "预言：变化（状态）")
- [预言：博学](Prophecy_colon__Well-Read_(Condition).md "预言：博学（状态）")：使用[卷轴](Scroll.md "卷轴")学习或施放法术。
- [预言：施舍](Prophecy_colon__Delivering_Alms_(Condition).md "预言：施舍（状态）")：[协助](Help.md "协助")一名盟友。_\[[参见：错误](#bugs)\]_
- [预言：收获回报](Prophecy_colon__Reap_Rewards_(Condition).md "预言：收获回报（状态）")：击杀一名敌人。

## 错误

- [预言：施舍](Prophecy_colon__Delivering_Alms_(Condition).md "预言：施舍（状态）")永远无法完成，因为它引用了一个游戏中不存在的被动特性。
- 预言法师每个数值只能拥有一个骰子，但游戏仅确保长休后获得的预兆骰子具有唯一值。这意味着完成一个**预言**（在休息之外达成）可能不会产生额外的骰子，如果法师已经拥有相同数值的骰子。例如，拥有 2 个预兆骰子的法师有 10% 的几率不会获得新骰子，而拥有单个骰子的法师有 5% 的几率。
- 在非回合制模式下施放区域法术，可能导致由造成某些类型伤害触发的预言多次激活，从而产生多个新的预兆骰子，通常会超过 3 个的限制。示例：在加入战斗前，使用[闪电充能](Lightning_Charges_(Condition).md "闪电充能")施放[火球术](Fireball.md "火球术")攻击 5 个敌人，同时满足[预言：阅后即焚](Prophecy_colon__Burn_After_Reading_(Condition).md "预言：阅后即焚（状态）")和[预言：惊人启示](Prophecy_colon__Shocking_Revelation_(Condition).md "预言：惊人启示（状态）")，将导致预言法师最多获得 10 个新的预兆骰子，因为两个预言都会对每个敌人触发一次。

---
*Source: [Expert Divination](https://bg3.wiki/wiki/Expert_Divination)*