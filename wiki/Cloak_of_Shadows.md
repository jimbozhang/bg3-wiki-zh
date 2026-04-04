# 幽影斗篷

对于类似的牧师动作，请参见[引导神力：幽影斗篷](Channel_Divinity_colon__Cloak_of_Shadows.md "引导神力：幽影斗篷")。

**幽影斗篷**是[暗影宗](Way_of_Shadow.md "暗影宗")武僧的类动作。它允许武僧进入阴影并从视野中消失。

## 描述

将自己包裹在阴影中，如果你处于[遮蔽](Obscured.md "遮蔽")状态，则变为[隐形](Cloak_of_Shadow_(Condition).md "幽影斗篷（状态）")。

区域必须是轻度遮蔽或重度遮蔽。
如果你攻击、施放另一个法术、执行动作或受到伤害，隐形效果会提前结束。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
范围：自身

## 状态：幽影斗篷

**[幽影斗篷](Cloak_of_Shadow_(Condition).md "幽影斗篷（状态）")**

持续时间：10 驱散

- 对[攻击掷骰](Attack_roll.md "攻击掷骰")拥有[优势](Advantage.md "优势")，并对敌人的攻击掷骰施加[劣势](Disadvantage.md "劣势")。
- 攻击、施放法术或进入明亮光照区域会结束此状态。

## 如何习得

职业：

- 职业等级 5：[暗影宗](Way_of_Shadow.md "暗影宗")

## 备注

- 进入[清晰区域](Clear_Area_(Condition).md "清晰区域（状态）")时效果消失。

## 错误

- 由于 `RemoveConditions` 字段编码不当，当从[轻度遮蔽](Lightly_Obscured_(Condition).md "轻度遮蔽（状态）")区域过渡到[重度遮蔽](Heavily_Obscured_(Condition).md "重度遮蔽（状态）")区域，或反之亦然时，**幽影斗篷**效果会丢失。

---
*Source: [Cloak of Shadows](https://bg3.wiki/wiki/Cloak_of_Shadows)*