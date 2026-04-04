# 巴尔的恩赐 (状态)

**巴尔的恩赐**

- 巴尔陶醉于受影响实体的谋杀天赋，每标记一次击杀，便为其提供+1的[护甲等级](Armour_Class.md "护甲等级")加值。
- 每当杀戮者躲避一次攻击时，此护甲等级加值会失去1点。_\[[参见：漏洞](#bugs)\]_

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `BHAALS_BOON_SLAYER` [持续时间损失](Conditions.md#Duration "状态"): [否](Status_properties/FreezeDuration.md "状态属性/FreezeDuration")

[若已应用](Conditions.md#Stack_type "状态"): 增加持续时间

[更多属性](Status_properties.md "状态属性"):

- [按持续时间倍增效果](Status_properties/MultiplyEffectsByDuration.md "状态属性/MultiplyEffectsByDuration")
- [冻结持续时间](Status_properties/FreezeDuration.md "状态属性/FreezeDuration")

## 漏洞

- 此状态的堆叠在远超预期的情况下被移除，这使得几乎不可能积累堆叠。
  - 每当从杀戮者身上移除任何类型的状态时，堆叠数都会减少。许多特性涉及频繁应用和移除隐藏的技术状态。特别是，每次使用[额外攻击](Extra_Attack.md "额外攻击")进行的攻击都涉及应用和移除跟踪额外攻击的隐藏技术状态。因此，仅仅进行攻击就会导致堆叠减少，通常在获得第一个堆叠后立即发生。

## 巴尔的恩赐来源

- [让屠杀开始](Let_the_Slaughter_Begin.md "让屠杀开始")

## 拥有巴尔的恩赐的生物

_维基数据库中未定义_

## 具有相同堆叠ID的状态

- 巴尔陶醉于受影响实体的谋杀天赋，每标记一次击杀，便为其提供+1的[护甲等级](Armour_Class.md "护甲等级")加值。
- 每当杀戮者躲避一次攻击时，此护甲等级加值会失去1点。_\[[参见：漏洞](#bugs)\]_

---
*Source: [Bhaal's Boon (Condition)](https://bg3.wiki/wiki/Bhaal's_Boon_(Condition)*