# 跳跃

另见：[跳跃（青蛙）](Jump_(Frog).md)

**跳跃**是一个常见的[附赠动作](Bonus_action.md "附赠动作")，允许角色垂直或水平跳跃，最远距离由其[力量](Strength.md "力量")属性决定。

## 描述

跳向一个目的地。

你的[力量](Strength.md "力量")会影响你能跳多远。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + 3米（10英尺）[移动速度](Resources.md#Movement_speed "移动速度")
详情
范围：4.5米（15英尺）

## 技术细节

UID

`Projectile_Jump`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[CannotTargetCharacter](https://bg3.wiki/w/index.php?title=CannotTargetCharacter_\(spell_flag\)&action=edit&redlink=1) "CannotTargetCharacter \(spell flag\) \(page does not exist\)")`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[Invisible](Invisible_(spell_flag).md)`, `[IsJump](https://bg3.wiki/w/index.php?title=IsJump_\(spell_flag\)&action=edit&redlink=1) "IsJump \(spell flag\) \(page does not exist\)")`, `[Stealth](Stealth_(spell_flag).md)`

## 备注

- **跳跃**的基础范围为4.5米（15英尺），每超过10点[力量](Strength.md "力量")2点，范围增加1米（3英尺）。
- 范围还可以通过各种职业特性、法术和物品增加：

| 效果 | 额外跳跃范围 |
| --- | --- |
| [强化跳跃](Enhance_Leap.md "强化跳跃") | +200%（持续时间：10驱散） |
| [运动员](Athlete_colon__Standing_Up.md "运动员：起立") | +50% |
| [增强无甲移动](Advanced_Unarmoured_Movement.md "增强无甲移动") | 范围：6米（20英尺） |
| [狂暴：猛虎之心](Rage_colon__Tiger_Heart.md "狂暴：猛虎之心") | 范围：4.5米（15英尺） |
| [运动健将：跳跃](Remarkable_Athlete_colon__Jump.md "运动健将：跳跃") | 范围：3米（10英尺） |
| [尼鲁纳](Nyrulna.md "尼鲁纳") |  |
| [骨刺靴](Bonespike_Boots.md "骨刺靴") | 范围：1.5米（5英尺） |
| [乌鸦徽记](Corvid_Token.md "乌鸦徽记") |  |
| [优雅布衣](The_Graceful_Cloth.md "优雅布衣") |  |
| [斯怀尔斯之靴](Swiresy_Shoes.md "斯怀尔斯之靴") |  |
| [怪物猎手长柄刀](Monster_Slayer_Glaive.md "怪物猎手长柄刀") |  |
| [超重](Encumbered_(Condition).md "超重（状态）") | -50% |

- 从超过4米（13英尺）的高度跳跃会导致坠落伤害。有关此伤害如何确定的详细信息，请参阅[坠落伤害](Falling_damage.md "坠落伤害")。
- 从约8米（27英尺）或更高处跳跃，落地时会使你进入[倒伏](Prone_(Condition).md "倒伏（状态）")状态。

---
*Source: [Jump](https://bg3.wiki/wiki/Jump)*