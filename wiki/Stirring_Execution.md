# 激励击杀

**激励击杀**是一项被动特性，当[雷文伽德公爵的长剑](Duke_Ravengard's_Longsword.md "雷文伽德公爵的长剑")的持有者击杀敌人时，会基于盟友各自的[魅力](Charisma.md "魅力")调整值为其提供临时生命值。

## 描述

当你击杀敌人时，9米（30英尺）范围内的盟友将获得等于你的魅力[属性调整值](Ability_Modifier.md "属性调整值")（最低为1）的[临时生命值](Temporary_Hit_Points.md "临时生命值") _\[[参见：错误](#bugs)\]_。

## 状态：临时生命值（激励击杀）

**\_(状态)[临时生命值](Temporary_Hit_Points_(Stirring_Execution)_(Condition).md "临时生命值（激励击杀）（状态）")**

- 受影响实体已获得魅力调整值的[临时生命值](Temporary_Hit_Points.md "临时生命值")。

## 如何习得

由武器授予：

- [雷文伽德公爵的长剑](Duke_Ravengard's_Longsword.md "雷文伽德公爵的长剑")

由生物使用：

- [乌尔德·雷文伽德](Ulder_Ravengard.md "乌尔德·雷文伽德")

## 错误

- 临时生命值实际上基于*接收*该效果的角色的魅力调整值，而非使用此剑造成致命一击的角色。最低值1仍然适用。
  - 临时生命值的`StackPriority`仅为1，因此会被任何其他`StackPriority`为1或更高的临时生命值来源覆盖，即使新来源的数值较低。

## 简要预览

击杀敌人后，9米（30英尺）范围内的盟友将获得基于[魅力](CHA.md "魅力")的[临时生命值](Temporary_Hit_Points.md "临时生命值")。

---
*Source: [Stirring Execution](https://bg3.wiki/wiki/Stirring_Execution)*