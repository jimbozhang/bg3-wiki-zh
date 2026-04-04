# 激励斩

**激励斩** 是一项被动特性，当穿戴者通过至圣斩施加状态时，会获得临时生命值。

## 描述

当你通过至圣斩法术施加状态时，你获得等于你的 [魅力调整值](Charisma.md "魅力") 的 [临时生命值](Temporary_Hit_Points.md "临时生命值")。

只能拥有来自一个来源的临时生命值。

## 状态：临时生命值（激励斩）

**\_(状态)[临时生命值](Temporary_Hit_Points_(Bolstering_Smite)_(Condition).md "临时生命值（激励斩）（状态）")**

- 从激励斩获得魅力调整值 [临时生命值](Temporary_Hit_Points.md "临时生命值")。

## 如何习得

由以下装备提供：

- [斩击头盔](Helmet_of_Smiting.md "斩击头盔")

## 备注

- 目前与 **激励斩** 配合使用的法术有：[炽焰斩](Searing_Smite.md "炽焰斩")、[雷鸣打击](Thunderous_Smite.md "雷鸣打击")、[激愤斩](Wrathful_Smite.md "激愤斩") 和 [印记斩](Branding_Smite.md "印记斩")。

## 错误

- **激励斩** 无法与 [雷鸣打击](Thunderous_Smite.md "雷鸣打击") 或 [惊惧斩](Staggering_Smite.md "惊惧斩") 配合使用。
- 穿戴者施加的任何 [恐慌](Frightened_(Condition).md "恐慌（状态）") 都会触发激励斩。
- 尽管描述中未说明，但临时生命值仅持续两轮。
  - 临时生命值的 `StackPriority` 仅为 1，因此会被任何其他 `StackPriority` 为 1 或更高的临时生命值来源覆盖，即使新来源的数值更低。

---
*Source: [Bolstering Smite](https://bg3.wiki/wiki/Bolstering_Smite)*