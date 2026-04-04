# 粉碎跃击（枭熊荒野形态）

本文介绍的是在**荒野形态：枭熊**形态下可用的该能力版本。关于枭熊NPC使用的版本，请参见[粉碎跃击](Crushing_Flight.md "粉碎跃击")。

**粉碎跃击**是[荒野形态：枭熊](Wild_Shape_colon__Owlbear.md "荒野形态：枭熊")形态下可用的**职业动作**。枭熊使用此能力在攻击对手的同时覆盖大片区域。

## 描述

跃向目标进行啃咬并将其击至[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + 6米（20英尺）[移动速度](Resources.md#Movement_speed "资源")
伤害：2~16

2d8[钝击](Bludgeoning.md "钝击")

详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）（豁免成功：目标承受减少的伤害 _\[[参见：错误](#bugs)\]_。）
范围：21米（70英尺）
范围效果：3米（10英尺）半径

## 更高等级

- 在4级时，此攻击额外造成1d4[钝击](Bludgeoning.md "钝击")伤害。
- 在8级时，此额外伤害变为1d6[钝击](Bludgeoning.md "钝击")。
- 在12级时，此额外伤害变为1d8[钝击](Bludgeoning.md "钝击")。

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：1回合

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在距离倒伏生物3米（10英尺）内进行的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）的移动速度。

## 如何习得

由以下生物使用：[披甲枭熊](Armoured_Owlbear.md "披甲枭熊")和[荒野形态：枭熊](Wild_Shape_colon__Owlbear.md "荒野形态：枭熊")

## 备注

- 此动作有两个独立且重叠的组件，可造成[倒伏](Prone_(Condition).md "倒伏（状态）")。每个组件都有独立的[法术豁免DC](Dice_rolls.md#Save_DCs "掷骰")[力量](Strength.md "力量")[豁免检定](Saving_throw.md "豁免检定")，因此敌人必须两次豁免成功，否则将被击至倒伏。
  - 首先是动作固有的倒伏效果，仅造成一回合倒伏。它将在战斗日志中显示为“对抗粉碎跃击的豁免检定”。
  - 落地时会产生二次爆炸（`Projectile_Jump_Knockdown_AOE`）。它将造成两回合倒伏，并在战斗日志中显示为“对抗...爆炸的豁免检定”。
- 跳跃的基础范围为16米（53英尺）。它随[力量](Strength.md "力量")缩放，并受益于与普通[跳跃](Jump.md "跳跃")相同的调整值。在枭熊拥有20力量且无其他调整值的情况下，范围为21米（70英尺）。
- 枭熊落地时不会承受[坠落伤害](Fall_damage.md "坠落伤害")。
- 额外伤害将根据枭熊的重量和垂直移动距离添加到攻击中。这使用与[投掷](Throw.md "投掷")类似的伤害计算。增加重量的效果（如[巨化](Enlarge.md "巨化")）会增加伤害，从更高处坠落也会增加伤害。

## 错误

- 豁免成功时，目标并非承受半伤（即(2d8 + 额外伤害)/2[钝击](Bludgeoning.md "钝击")），而是承受(1d8 + 额外伤害)/2[钝击](Bludgeoning.md "钝击")，这更接近四分之一伤害。
  - 无论攻击者是否拥有[原初打击](Primal_Strike.md "原初打击")，此伤害始终以魔法形式造成。

---
*Source: [Crushing Flight (Owlbear Wild Shape)](https://bg3.wiki/wiki/Crushing_Flight_(Owlbear_Wild_Shape)*