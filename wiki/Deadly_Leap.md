# 死亡之跃

**死亡之跃**是[鲨蜥兽](Bulette.md "鲨蜥兽")使用的类动作。鲨蜥兽跃入空中并在落地时产生爆炸，同时以跳跃的力量和锋利的爪子造成伤害。

## 描述

跃向目标，将其向后推4米（13英尺），并可能使其陷入[倒伏](Prone_(Condition).md "倒伏（状态）")状态。

## 属性

消耗
6米（20英尺）[移动速度](Resources.md#Movement_speed "资源")
伤害：14~44

3d6 + 4⁠[钝击](Bludgeoning.md "钝击")

\+ 3d6 + 4⁠[挥砍](Slashing.md "挥砍")

详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 16）（豁免成功时：目标仍会被推开并承受一半伤害。）
范围：18米（60英尺）
范围效果：4米（13英尺）半径
推动：4米（13英尺）（豁免成功时减半）
充能：每回合

## 技术细节

UID

`Projectile_Jump_Bulette`

跳跃动作

`Projectile_Jump_Bulette_Spawn`

由跳跃触发的爆炸，用于施加伤害和倒伏效果

法术标志

`[CannotTargetCharacter](https://bg3.wiki/w/index.php?title=CannotTargetCharacter_\(spell_flag\)&action=edit&redlink=1) "CannotTargetCharacter \(spell flag\) \(page does not exist\)")`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[IsJump](https://bg3.wiki/w/index.php?title=IsJump_\(spell_flag\)&action=edit&redlink=1) "IsJump \(spell flag\) \(page does not exist\)")`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：2回合

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在距离倒伏生物3米（10英尺）内进行的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）移动速度。

## 如何习得

由以下生物使用：[鲨蜥兽](Bulette.md "鲨蜥兽")

## 图库

- 未使用的图像

- 工具提示图像

- 控制器图标

- 图标

---
*Source: [Deadly Leap](https://bg3.wiki/wiki/Deadly_Leap)*