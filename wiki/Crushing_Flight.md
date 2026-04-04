# 粉碎跃击

本文介绍的是NPC枭熊使用的版本。关于荒野形态：枭熊形态下的版本，请参见[粉碎跃击（枭熊荒野形态）](Crushing_Flight_(Owlbear_Wild_Shape)..md)

**粉碎跃击**是[枭熊](Owlbear.md "枭熊")生物使用的类动作，允许它们跃向目标并可能将其击倒。

## 描述

跃向目标进行啃咬，并将其击至[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + 6米（20英尺）[移动速度](Resources.md#Movement_speed "资源")
详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "骰子检定")）
范围：21米（70英尺）
充能：每回合

## 技术细节

UID

`Projectile_Jump_Owlbear`

法术标志

`[CannotTargetCharacter](https://bg3.wiki/w/index.php?title=CannotTargetCharacter_\(spell_flag\)&action=edit&redlink=1) "CannotTargetCharacter \(spell_flag\) \(页面不存在\)")`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell_flag\) \(页面不存在\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[IsJump](https://bg3.wiki/w/index.php?title=IsJump_\(spell_flag\)&action=edit&redlink=1) "IsJump \(spell_flag\) \(页面不存在\)")`, `[NoAOEDamageOnLand](https://bg3.wiki/w/index.php?title=NoAOEDamageOnLand_\(spell_flag\)&action=edit&redlink=1) "NoAOEDamageOnLand \(spell_flag\) \(页面不存在\)")`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell_flag\) \(页面不存在\)")`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：2回合

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在距离该生物3米（10英尺）内进行的攻击对倒伏生物具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）的移动速度。

## 学习方式

生物使用：[枭熊](Owlbear.md "枭熊")和[幽影毛绒玩具](Shadow_Plush.md "幽影毛绒玩具")

## 备注

- 用于此能力DC的施法关键属性是[智力](Intelligence.md "智力")。枭熊的智力为3，这为DC提供了-4的调整值。
- 枭熊在落地时不会受到[坠落伤害](Fall_damage.md "坠落伤害")。

---
*Source: [Crushing Flight](https://bg3.wiki/wiki/Crushing_Flight)*