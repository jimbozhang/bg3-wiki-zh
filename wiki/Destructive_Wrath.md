# 毁灭狂怒

**毁灭狂怒**是[风暴领域](Tempest_Domain.md "风暴领域")牧师可用的[反应](Reaction.md "反应")。此能力允许这些牧师通过消耗一个[引导神力](Channel_Divinity_Charge.md "引导神力")来最大化[雷鸣](Thunder.md "雷鸣")和[闪电](Lightning.md "闪电")伤害的掷骰。

## 描述

当你掷出[雷鸣](Thunder.md "雷鸣")或[闪电](Lightning.md "闪电")伤害时，你可以使用你的[引导神力](Cleric.md#Level_2 "牧师")来造成最大伤害。

## 属性

消耗
[引导神力](Channel_Divinity_Charge.md "引导神力")

## 技术细节

UID

`Interrupt_DestructiveWrath`

反应

`DestructiveWrath`

授予该反应的被动特性

## 如何习得

职业：

- 职业等级 2：[风暴领域](Tempest_Domain.md "风暴领域")

## 备注

- 反应提示将在触发动作的[攻击掷骰](Attack_Roll.md "攻击掷骰")之前显示。这意味着它可能会浪费在最终未命中的攻击上。
- 并非所有造成闪电或雷鸣伤害的法术或动作都能触发此反应。以下是玩家可使用的、与毁灭狂怒配合的动作列表。<sup>[\[1\]](#cite_note-DamageType-1)</sup>
  - [闪电箭](Arrow_of_Lightning.md "闪电箭")
  - [召雷术](Call_Lightning.md "召雷术") / [激活召雷术](Activate_Call_Lightning.md "激活召雷术")
  - [链状闪电](Chain_Lightning.md "链状闪电")
  - [繁彩球](Chromatic_Orb.md "繁彩球") / [元素平衡球](Sphere_of_Elemental_Balance.md "元素平衡球")（仅限雷鸣或闪电变体）
- [神圣打击：雷鸣（远程）](Divine_Strike_colon__Thunder_(Ranged).md "神圣打击：雷鸣（远程）")，但不包括[神圣打击：雷鸣（近战）](Divine_Strike_colon__Thunder_(Melee).md "神圣打击：雷鸣（近战）")
  - [风暴之心](Heart_of_the_Storm.md "风暴之心")
  - [闪电箭](Lightning_Arrow.md "闪电箭")
  - [闪电束](Lightning_Bolt.md "闪电束")
  - [闪电吐息](Lightning_Breath.md "闪电吐息")
  - [粉碎音波](Shatter.md "粉碎音波") / [震峰拳](Gong_of_the_Summit.md "震峰拳")
  - [电爪](Shocking_Grasp.md "电爪") / [风暴之触](Touch_of_the_Storm.md "风暴之触")
  - [雷鸣打击](Thunderous_Smite.md "雷鸣打击")
  - [雷鸣波](Thunderwave.md "雷鸣波") / [四雷拳](Fist_of_Four_Thunders.md "四雷拳")
  - [巫术箭](Witch_Bolt.md "巫术箭") / [激活巫术箭](Activate_Witch_Bolt.md "激活巫术箭")
  - [风暴狂怒](Wrath_of_the_Storm.md "风暴狂怒")
  - [西风闪](Zephyr_Flash.md "西风闪")，但不包括[西风破裂](Zephyr_Break.md "西风破裂")
- 其他动作，即使造成闪电或雷鸣伤害，_无法_触发毁灭狂怒。显著例子包括：
  - [湮灭波](Destructive_Wave.md "湮灭波")
  - [轰鸣剑](Booming_Blade.md "轰鸣剑")
  - 使用带有闪电或雷鸣伤害附加的普通武器攻击

## 错误

- 当施放[守卫刻文](Glyph_of_Warding.md "守卫刻文")的闪电或雷鸣变体时，毁灭狂怒会触发，但守卫爆炸的伤害不受影响。
- 当施放一些不造成伤害的法术时，该反应也会触发。<sup>[\[1\]](#cite_note-DamageType-1)</sup> 如果用于这些法术，毁灭狂怒将被浪费：
  - [毁灭飞矢](Bolts_of_Doom.md "毁灭飞矢")
  - [震骨雷鸣](Bone-shaking_Thunder.md "震骨雷鸣")
  - [召唤元素生物：风元素](Conjure_Elemental_colon__Air_Elemental.md "召唤元素生物：风元素")
  - [召唤元素生物：风元素执政官](Conjure_Elemental_colon__Air_Myrmidon.md "召唤元素生物：风元素执政官")
  - [召唤元素生物：土元素](Conjure_Elemental_colon__Earth_Elemental.md "召唤元素生物：土元素")
  - [召唤元素生物：土元素执政官](Conjure_Elemental_colon__Earth_Myrmidon.md "召唤元素生物：土元素执政官")
  - [召唤初级元素生物：泥魔蝠](Conjure_Minor_Elemental_colon__Mud_Mephits.md "召唤初级元素生物：泥魔蝠")
  - [异界誓盟：气巨灵](Planar_Ally_colon__Djinni.md "异界誓盟：气巨灵")

## 外部链接

- ⁠[毁灭狂怒](https://forgottenrealms.fandom.com/wiki/Destructive_wrath) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

## 脚注

1. ↑ [1.0](#cite_ref-DamageType_1-0) [1.1](#cite_ref-DamageType_1-1) 这些是 `DamageType` 字段设置为 `Lightning` 或 `Thunder` 的动作。此字段并非对所有实际造成这些伤害类型的动作都一致设置，并且设置在一些根本不造成伤害的动作上。

---
*Source: [Destructive Wrath](https://bg3.wiki/wiki/Destructive_Wrath)*