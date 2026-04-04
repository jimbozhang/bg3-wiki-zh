# 狂暴

本文介绍的是基础野蛮人动作。关于同名的驯兽师野猪版本，请参见[狂暴（野猪）](Rage_(Boar).md)。关于其他用途，请参见[狂暴（消歧义）](Rage_(disambiguation).md)。

**狂暴**是[野蛮人](Barbarian.md "野蛮人")的[附赠动作](Actions.md#Resources "动作")和职业特性。进入狂暴状态可获得对[物理伤害](Physical.md "物理")的[抗性](Resistance.md "抗性")，造成额外的近战和投掷伤害，并在力量[检定](Checks.md "检定")和[豁免检定](Saving_throw.md "豁免检定")上获得[优势](Advantage.md "优势")。穿着[重甲](Heavy_Armour.md "重甲")会施加[狂暴受阻](Rage_Impeded_(Condition).md "狂暴受阻（状态）")状态，移除狂暴的大部分增益效果。

## 描述

使用近战和即兴武器，以及投掷时，造成**2**点额外伤害。

获得对[物理伤害](Physical.md "物理")的[抗性](Resistance.md "抗性")，并在力量[检定](Checks.md "检定")和[豁免检定](Saving_throws.md "豁免检定")上获得[优势](Advantage.md "优势")。

仅在战斗中可用。
如果每回合未攻击敌人或未受到伤害，狂暴会提前结束。_\[[参见：错误](#bugs)\]_
在狂暴状态下，无法施放或专注[法术](Spells.md "法术")。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + [狂暴次数](Rage_Charge.md "狂暴次数")
详情
范围：自身
持续时间：10 回合

## 更高等级

在 9 级时，狂暴提供的攻击额外伤害增加至 **+3**。

## 技术细节

UID

`Shout_Rage`

## 赋予

- [结束狂暴](End_Rage.md "结束狂暴")

## 状态：狂暴

**[狂暴](Rage_(Condition).md "狂暴（状态）")**

持续时间：10 回合

- 使用近战和即兴武器、徒手打击以及投掷物体时，额外造成 2 点伤害（在 9 级时增加至 3 点）。
- 拥有对[物理](Physical.md "物理")伤害的[抗性](Resistance.md "抗性")，并在力量[属性检定](Ability_Check.md "属性检定")和[豁免检定](Saving_throw.md "豁免检定")上获得[优势](Advantage.md "优势")。
- 无法施放或专注[法术](Spells.md "法术")。

## 状态：狂暴受阻

**[狂暴受阻](Rage_Impeded_(Condition).md "狂暴受阻（状态）")**

持续时间：永久

- 被[重甲](Heavy_Armour.md "重甲")所累。在卸下护甲前，狂暴不会提供额外伤害、对物理伤害的[抗性](Damage_types.md#Damage_Vulnerability,_Resistance_and_Immunity "伤害类型")，或在力量[属性检定](Ability_Check.md "属性检定")和[豁免检定](Saving_throw.md "豁免检定")上获得[优势](Advantage.md "优势")。

## 学习方式

职业：

- 职业等级 1：[野蛮人](Barbarian.md "野蛮人")

## 注释

- 维持狂暴的“攻击”可以是任何以非盟友生物为目标的能力，不仅限于标准武器攻击。像[推击](Shove.md "推击")或[灵吸怪威能](Illithid_powers.md "灵吸怪威能")如[黑洞](Black_Hole.md "黑洞")等能力也计入维持狂暴。
- 在被[镇定](Calmed_(Condition).md "镇定（状态）")时无法使用狂暴。
- 与 D&D 5e 规则不同，狂暴的额外伤害可应用于不使用[力量](Strength.md "力量")的近战武器（例如使用[敏捷](Dexterity.md "敏捷")的[灵巧](Finesse.md "灵巧")武器）。
- 尽管游戏内提示未说明，狂暴的额外伤害也适用于[徒手打击](Unarmed_Strike.md "徒手打击")。
- 进入狂暴状态会自动结束所有来源的[专注](Concentration.md "专注")，但非施法来源的专注可以在狂暴期间开始，例如[诡术祝福](Blessing_of_the_Trickster.md "诡术祝福")和[威严斗篷：命令术](Mantle_of_Majesty_colon__Command.md "威严斗篷：命令术")。

## 错误

- 如果野蛮人拥有另一个在受到伤害时触发的被动特性（更准确地说，任何带有 `OnDamaged` `StatsFunctorContext` 的被动），则受到伤害不会维持狂暴。示例包括：
  - [直觉闪避](Uncanny_Dodge.md "直觉闪避")
  - 来自[吸血服](Bloodguzzler_Garb.md "吸血服")和[布衣](Cloth_Armour.md "布衣")的[以牙还牙](Grievous_Retribution.md "以牙还牙")
  - 来自[血肉消熔披风](Fleshmelter_Cloak.md "血肉消熔披风")的[腐蚀性掠夺](Caustic_Reprisal.md "腐蚀性掠夺")
  - 来自[带电马甲](The_Jolty_Vest.md "带电马甲")的[电流反击](Countershock.md "电流反击")
- [导力](Force_Conduit_(Condition).md "导力（状态）")（即使冲锋次数不足以触发爆炸）
- 如果在回合制模式下玩家失去控制时播放狂暴动画（例如，通过结束回合且没有其他角色处于[主动回合顺序](Turn-based_mode.md#Turn_order "回合制模式")中），则不会消耗狂暴次数。这适用于所有其他狂暴变体。
- 狂暴包含一个隐藏功能，可将坠落伤害减半。虽然这导致[跳跃](Jump.md "跳跃")提示正确显示坠落伤害减半，但它与狂暴提供的固有钝击抗性叠加，实际上将坠落伤害降至四分之一。
- 当野蛮人达到 9 级时，此版本的狂暴在已受狂暴影响时仍可使用。

---
*Source: [Rage](https://bg3.wiki/wiki/Rage)*