# 隶属之盾

本文介绍基础灵吸怪威能。关于升级版的完整灵吸怪威能，请参见[强化隶属之盾](Augmented_Shield_of_Thralls.md "强化隶属之盾")。

**隶属之盾**是一项[动作](Actions.md#Resources "动作")和[灵吸怪威能](Illithid_power.md "灵吸怪威能")。使用时，此能力为角色提供10点[临时生命值](Temporary_Hit_Points.md "临时生命值")。如果临时生命值丧失，所有附近的敌人可能被[震慑](Stunned_(Condition).md "震慑（状态）")1回合。

## 描述

在自身或盟友周围召唤一个易爆护盾，为目标提供10点[临时生命值](Temporary_Hit_Points.md "临时生命值")。

如果这些临时生命值因受到伤害而丧失，护盾会爆裂，可能[震慑](Stunned_(Condition).md "震慑（状态）")附近的敌人。

只能拥有来自一个来源的[临时生命值](Hit_Points.md#Temporary_Hit_Points "生命值")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
范围：9米（30英尺）
充能：[短休](Short_rest.md "短休")
持续时间：直至[长休](Long_Rest.md "长休")

范围效果：3米（10英尺）（爆炸半径）

## 技术细节

UID

`Target_TAD_ShieldOfThralls`

护盾动作

`Projectile_TAD_ShieldOfThralls_Explosion`

护盾破裂时触发的爆炸

法术标志

`[DisableBlood](https://bg3.wiki/w/index.php?title=DisableBlood_\(spell_flag\)&action=edit&redlink=1) "DisableBlood \(spell_flag\) \(page does not exist\)")`

## 状态：易爆护盾

**[易爆护盾](Volatile_Shield_(Condition).md "易爆护盾（状态）")**

持续时间：直至[长休](Long_Rest.md "长休")

- 受影响实体已被灵吸怪授予临时生命值。如果这些生命值因受到伤害而丧失，护盾会爆裂，可能[震慑](Stunned_(Condition).md "震慑（状态）")附近的敌人。
- 护盾仅在所有临时生命值丧失后才会爆裂。这也会移除该状态。
- 当护盾爆裂时，9米（30英尺）内的敌人会被[震慑](Stunned_(Condition).md "震慑（状态）")1回合，除非他们成功通过[DC](Dice_rolls.md#Save_DCs "掷骰")15的[智力](Intelligence.md "智力")[豁免检定](Saving_throw.md "豁免检定")。

## 状态：震慑

**[震慑](Stunned_(Condition).md "震慑（状态）")**

持续时间：1回合

[智力](Intelligence.md "智力")[豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 15）

- 受影响生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")。
- 受影响生物自动在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")中失败。
- 可通过[行动自如](Freedom_of_Movement.md "行动自如")、[高等复原术](Greater_Restoration.md "高等复原术")、[解缚打击](Unshackling_Strike.md "解缚打击")移除。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "优势")。

## 如何习得

其他习得方式：

- 在获得以下能力后，使用[夺心魔寄生虫标本](Mind_Flayer_Parasite_Specimen.md "夺心魔寄生虫标本")从灵吸怪威能技能树中解锁：
  - [灌注生命](Transfuse_Health.md "灌注生命")

## 错误

- 施放隶属之盾所需的短休可以通过在[第一幕](Act_One.md "第一幕")和[第二幕](Act_Two.md "第二幕")之间旅行来规避。这可以让多个队伍成员在一天开始时拥有激活的隶属之盾，即使只有一名队伍成员拥有此能力。
  - 这也可以在[第三幕](Act_Three.md "第三幕")中完成，通过在有加载区域的地点之间旅行。例如，从[利文顿](Rivington.md "利文顿")旅行到[下城区](Lower_City.md "下城区")的一个地点，反之亦然。

---
*Source: [Shield of Thralls](https://bg3.wiki/wiki/Shield_of_Thralls)*