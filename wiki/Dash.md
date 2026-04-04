# 疾走

**疾走** 是一项基本、常见的动作，几乎所有生物都可以使用。它会使生物的移动速度在一回合内翻倍。

## 描述

本回合移动更远的距离：使你的 [移动速度](Movement_speed.md "移动速度") 翻倍。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
范围：自身
持续时间：1 回合

## 技术细节

UID

`Shout_Dash`

`Shout_Dash_NPC`

`Shout_Dash_HookHorror`

法术标志

`[IgnoreSilence](IgnoreSilence_(spell_flag).md)`, `[Invisible](Invisible_(spell_flag).md)`, `[NoCameraMove](https://bg3.wiki/w/index.php?title=NoCameraMove_\(spell_flag\)&action=edit&redlink=1) "NoCameraMove \(spell flag\) \(page does not exist\)")`, `[Stealth](Stealth_(spell_flag).md)`

## 状态：疾走

**[疾走](Dash_(Condition).md "疾走（状态）")**

持续时间：1 回合

- [移动速度](Movement_speed.md "移动速度") 翻倍。

## 详情

### 疾走叠加

在一回合内多次疾走是可能的，可以通过 [动作如潮](Action_Surge.md "动作如潮") 或 [加速术](Haste.md "加速术") 等特性获得额外动作，或者通过使用附赠动作疾走，如 [灵巧动作：疾走](Cunning_Action_colon__Dash.md "灵巧动作：疾走")。当多次疾走时，来自 [疾走](Dash_(Condition).md "疾走（状态）") 的移动加成是*累加*而非相乘的。例如，一个移动速度为 9 米（30 英尺）的角色疾走两次，会获得两次 9 米（30 英尺）的额外移动速度，总计 27 米（90 英尺）（3 倍乘数），而不是将移动速度翻倍两次（那将是 4 倍乘数）。同样，疾走三次会应用 4 倍移动速度乘数，而不是 8 倍。

在一回合内疾走超过三次没有效果。后续的疾走不会增加任何额外的移动速度。<sup>[\[1\]](#cite_note-stack-1)</sup>

特殊的类疾走动作 [碰撞鞋跟](Click_Heels.md "碰撞鞋跟") *确实* 与普通疾走相乘叠加。也就是说，疾走并使用碰撞鞋跟会使移动速度翻倍，然后再次翻倍，达到 4 倍乘数。疾走三次并使用碰撞鞋跟会使移动速度提高 8 倍。疾走和碰撞鞋跟的顺序无关紧要，总的移动速度提升是相同的。

## 疾走变体

除了每个生物都可以使用的基础疾走动作外，还有一些特殊的、消耗更低的疾走动作可供特定职业或在特定条件下使用。

- [碰撞鞋跟](Click_Heels.md "碰撞鞋跟") – 由 [速度之靴](Boots_of_Speed.md "速度之靴") 提供的类疾走附赠动作。
- [灵巧动作：疾走](Cunning_Action_colon__Dash.md "灵巧动作：疾走") – [游荡者](Rogue.md "游荡者") 在 2 级时可用的附赠动作疾走。
- [疾走（附赠动作）](Dash_(bonus_action).md "疾走（附赠动作）") – 来自 [脚底抹油](Expeditious_Retreat.md "脚底抹油") 或 [狂暴：飞鹰之心](Rage_colon__Eagle_Heart.md "狂暴：飞鹰之心") 的附赠动作疾走。请注意，即使脚底抹油的初始施放会授予 [疾走](Dash_(Condition).md "疾走（状态）")，它也不计入某些交互中的疾走动作。
- [飞檐走壁：疾走](Step_of_the_Wind_colon__Dash.md "飞檐走壁：疾走") – [武僧](Monk.md "武僧") 在 2 级时可用的附赠动作疾走。此动作还需要一个 [气点](Ki_Point.md "气点")。

## 相关物品

以下物品在使用疾走时会触发效果：

- [奥术强化之靴](Boots_of_Arcane_Bolstering.md "奥术强化之靴") – 授予两回合的 [奥术充能](Arcane_Charge_(Condition).md "奥术充能（状态）")
- [跃动指套](Fleetfingers.md "跃动指套") – 授予一次免费的特殊 [跳跃](Jump_(Running).md "跳跃（奔跑）") 动作
- [破阵战靴](Linebreaker_Boots.md "破阵战靴") – 授予三层 [怒火](Wrath_(Condition).md "怒火（状态）")
- [弹力之靴](Springstep_Boots.md "弹力之靴") – 授予三层 [亢奋](Momentum_(Condition).md "亢奋（状态）")
- [闪电飞靴](The_Speedy_Lightfeet.md "闪电飞靴") – 授予三层 [闪电充能](Lightning_Charges_(Condition).md "闪电充能（状态）")

这些物品在使用任何疾走变体时也会触发。其他移动动作，如 [冲锋](Charger.md "冲锋") 或 [原始践踏](Primal_Stampede.md "原始践踏")，不计入这些物品的疾走。

## 相关特性

- [野兽之相：骏马](Aspect_of_the_Beast_colon__Stallion.md "野兽之相：骏马") – 在拥有 [疾走](Dash_(Condition).md "疾走（状态）") 状态时获得临时生命值。请注意，这不适用于碰撞鞋跟，因为碰撞鞋跟授予的是不同的状态（[碰撞鞋跟](Click_Heels_(Condition).md "碰撞鞋跟（状态）")），也不适用于叠加的疾走，因为它们是分开但名称相同的状态。<sup>[\[1\]](#cite_note-stack-1)</sup>
- [移动射击](Mobile_Shot.md "移动射击") – 需要疾走状态（或 [撤离](Disengage_(Condition).md "撤离（状态）") 状态）才能使用攻击。它也仅适用于单次疾走，不适用于叠加的疾走。

## 另请参阅

- [移动速度来源列表](List_of_sources_of_movement_speed.md "移动速度来源列表")

## 参考文献

1. ↑ [1.0](#cite_ref-stack_1-0) [1.1](#cite_ref-stack_1-1) 疾走的编码方式是，第二次疾走后，后续疾走会将普通的 `DASH` 状态替换为 `DASH_STACKED`，第三次疾走后替换为 `DASH_STACKED_2`。这不支持超过三次的疾走叠加，因此任何额外的疾走都没有效果。

---
*Source: [Dash](https://bg3.wiki/wiki/Dash)*