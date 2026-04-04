# 超重 (状态)

**超重**

- 携带过多重量。
- [移动速度](Resources.md#Movement_speed "资源")降低，且[跳跃](Jump.md "跳跃")距离减半。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID")：`ENCUMBERED` [堆叠优先级](Stack_priority.md "堆叠优先级")：0

[更多属性](Status_properties.md "状态属性")：

- [忽略休息](Status_properties/IgnoreResting.md "状态属性/忽略休息")

## 说明

- 当队伍成员超过其[负重](Carrying_capacity.md "负重")的80%时，会获得此状态。
- 从技术上讲，此状态并不会实际降低移动速度；而是将移动消耗乘以1.5（相当于[移动速度](Resources.md#Movement_speed "资源")为9米（30英尺）的角色损失3米（10英尺）的移动距离）。
- 除了列出的效果外，此状态还会减慢角色的行走动画。

## 具有相同堆叠ID的状态

- 携带过多重量。
- [移动速度](Resources.md#Movement_speed "资源")降低，且[跳跃](Jump.md "跳跃")距离减半。

| 状态 | 效果 |
| --- | --- |
| 超重 | 携带过多重量。[移动速度](Resources#Movement_speed.md#Movement_speed "资源")降低，且[跳跃](Jump.md "跳跃")距离减半。 |
| [严重超重](Heavily_Encumbered_(Condition).md "严重超重 (状态)") | 携带远超负荷的重量。[移动速度](Resources#Movement_speed.md#Movement_speed "资源")大幅降低，且无法再攀爬或[跳跃](Jump.md "跳跃")。同时，你在[属性检定](Ability_Check.md "属性检定")和[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")，并且力量、敏捷和体质的[豁免检定](Saving_throw.md "豁免检定")也具有劣势。 |

- 携带远超负荷的重量。
- [移动速度](Resources.md#Movement_speed "资源")大幅降低，且无法再攀爬或[跳跃](Jump.md "跳跃")。同时，你在[属性检定](Ability_Check.md "属性检定")和[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")，并且力量、敏捷和体质的[豁免检定](Saving_throw.md "豁免检定")也具有劣势。

---
*Source: [Encumbered (Condition)](https://bg3.wiki/wiki/Encumbered_(Condition)*