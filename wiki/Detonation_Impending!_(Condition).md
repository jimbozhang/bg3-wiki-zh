# 即将爆炸！（状态）

**即将爆炸！**

- 这台钢铁卫士正在准备[爆炸](Self-Detonate.md "爆炸")。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `BULWARK_MODE` [持续时间消失](Conditions.md#Duration "状态"): 回合开始时

[堆叠优先级](Stack_priority.md "堆叠优先级"): 0

[更多属性](Status_properties.md "状态属性"):

- [UnavailableInActiveRoll](Status_properties/UnavailableInActiveRoll.md "状态属性/UnavailableInActiveRoll")

## 说明

| 状态 | 效果 |
| --- | --- |
| [防御协议：壁垒](Defensive_Protocol_colon__Bulwark_(Condition).md "防御协议：壁垒（状态）") | 在此防御状态下，钢铁卫士变得[不屈](Unyielding_Construct_(Condition).md "不屈构造（状态）")，并可以使用其[修复矩阵](Repair_Matrix_(Condition).md "修复矩阵（状态）")、[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")和[推斥协议](Repelling_Protocol.md "推斥协议")。同时获得75点[临时生命值](Temporary_Hit_Points.md "临时生命值")。如果钢铁卫士失去这些临时生命值，它会自动使用[终止壁垒协议](Terminate_Bulwark_Protocol.md "终止壁垒协议")并失去此状态。如果被[闪光弹](Flashblinder.md "闪光弹")击中，钢铁卫士会失去此状态。 |
| 即将爆炸！ | 这台钢铁卫士正在准备[爆炸](Self-Detonate.md "爆炸")。 |

- 对于[钢铁卫士泰坦](Steel_Watcher_Titan.md "钢铁卫士泰坦")，[自爆（钢铁卫士泰坦）](Self-Detonate_(Steel_Watcher_Titan).md "自爆（钢铁卫士泰坦）")类似于[钢铁卫士](Steel_Watcher.md "钢铁卫士")的自由动作[爆炸](Self-Detonate.md "爆炸")。
- 在某些情况下，可能有多层“即将爆炸！”状态，特别是：
  - 当钢铁卫士处于[故障](Malfunctioning_(Condition).md "故障（状态）")或[震慑](Stunned_(Condition).md "震慑（状态）")状态且生命值降至0时（如果它没有“即将爆炸！”状态）——之后它会恢复1点生命值并立即获得两层“即将爆炸！”状态。
- 对至少有一层“即将爆炸！”状态的钢铁卫士施放[怪物定身术](Hold_Monster.md "怪物定身术")——每次成功施法都会额外增加一层状态。
  - 第二种方法似乎允许无限堆叠此状态。
    - 如果拥有多层“即将爆炸！”状态的钢铁卫士在其回合被允许[爆炸](Self-Detonate.md "爆炸")，它只会爆炸一次。
  - 如果在其回合前被杀死，它会爆炸的次数等于其拥有的“即将爆炸！”层数。（仅对普通钢铁卫士验证）

## 即将爆炸的来源

- [自爆程序](Self-Detonation_Protocol.md "自爆程序")

## 拥有即将爆炸的生物

*维基数据库中未定义*

## 具有相同堆叠ID的状态

| 状态 | 效果 |
| --- | --- |
| [防御协议：壁垒](Defensive_Protocol_colon__Bulwark_(Condition).md "防御协议：壁垒（状态）") | 在此防御状态下，钢铁卫士变得[不屈](Unyielding_Construct_(Condition).md "不屈构造（状态）")，并可以使用其[修复矩阵](Repair_Matrix_(Condition).md "修复矩阵（状态）")、[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")和[推斥协议](Repelling_Protocol.md "推斥协议")。同时获得75点[临时生命值](Temporary_Hit_Points.md "临时生命值")。如果钢铁卫士失去这些临时生命值，它会自动使用[终止壁垒协议](Terminate_Bulwark_Protocol.md "终止壁垒协议")并失去此状态。如果被[闪光弹](Flashblinder.md "闪光弹")击中，钢铁卫士会失去此状态。 |
| 即将爆炸！ | 这台钢铁卫士正在准备[爆炸](Self-Detonate.md "爆炸")。 |

- 这台钢铁卫士正在准备[爆炸](Self-Detonate.md "爆炸")。

---
*Source: [Detonation Impending! (Condition)](https://bg3.wiki/wiki/Detonation_Impending!_(Condition)*