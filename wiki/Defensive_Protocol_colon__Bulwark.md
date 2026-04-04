# 防御协议：壁垒

**防御协议：壁垒**是[钢铁卫士泰坦](Steel_Watcher_Titan.md "钢铁卫士泰坦")在受到重大伤害时使用的自由动作。泰坦进入静止的防御状态，可以发射毁灭性的[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")齐射。

## 描述

缩入[不屈](Unyielding_Construct_(Condition).md "不屈构造（状态）")状态并[修复矩阵](Repair_Matrix_(Condition).md "修复矩阵（状态）")自身。在缩入状态期间，你可以发射[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")并[推斥协议](Repelling_Protocol.md "推斥协议")战斗人员。

## 属性

详情
充能：每场战斗两次

## 技术细节

UID

`Shout_SteelWatcher_Quadruped_ActivateBulwarkMode`

首次使用在生命值低于75%时解锁

`Shout_SteelWatcher_Quadruped_ActivateBulwarkMode2`

第二次使用在生命值低于50%时解锁

法术标志

`[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`

## 赋予

- [地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")
- [推斥协议](Repelling_Protocol.md "推斥协议")

## 状态：防御协议：壁垒

**[防御协议：壁垒](Defensive_Protocol_colon__Bulwark_(Condition).md "防御协议：壁垒（状态）")**

持续时间：2回合

- 在此防御状态下，钢铁卫士变得[不屈](Unyielding_Construct_(Condition).md "不屈构造（状态）")，并可以使用其[修复矩阵](Repair_Matrix_(Condition).md "修复矩阵（状态）")、[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")和[推斥协议](Repelling_Protocol.md "推斥协议")。
- 同时赋予75点[临时生命值](Temporary_Hit_Points.md "临时生命值")。
- 如果钢铁卫士失去这些临时生命值，它会自动使用[终止壁垒协议](Terminate_Bulwark_Protocol.md "终止壁垒协议")并失去此状态。
- 如果被[闪光弹](Flashblinder.md "闪光弹")击中，钢铁卫士会失去此状态。

## 状态：不屈构造

**[不屈构造](Unyielding_Construct_(Condition).md "不屈构造（状态）")**

持续时间：2回合

- 只有造成至少15点伤害的攻击才能伤害此钢铁卫士。

## 状态：修复矩阵

**[修复矩阵](Repair_Matrix_(Condition).md "修复矩阵（状态）")**

持续时间：2回合

- 在其回合开始时，修复伺服系统会治疗此钢铁卫士3d8⁠⁠[生命值](Healing.md "治疗")。

## 学习方式

由以下生物使用：[钢铁卫士泰坦](Steel_Watcher_Titan.md "钢铁卫士泰坦")

## 备注

- 总体而言，在此状态下，钢铁卫士泰坦具有以下效果：
  - 获得75点[临时生命值](Temporary_Hit_Points.md "临时生命值")，在[荣誉](Honour.md "荣誉")模式下增加至200点[临时生命值](Temporary_Hit_Points.md "临时生命值")。
  - 每回合治疗3d8⁠⁠[生命值](Healing.md "治疗")，在荣誉模式下增加至6d8+14⁠⁠[生命值](Healing.md "治疗")。
  - 忽略任何低于15点的伤害，在荣誉模式下阈值增加至40点。请注意，这不会减少超过阈值的攻击所造成的伤害。
  - 变得无法移动。
  - 可以使用[地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹")和[推斥协议](Repelling_Protocol.md "推斥协议")。
  - 失去所有其他动作，例如[多重攻击](Multiattack_(Steel_Watcher_Titan).md "多重攻击（钢铁卫士泰坦）")、[发射协议：流星锤](Launch_Protocol_colon__Bola.md "发射协议：流星锤")和[地狱火诅咒](Hellfire_Curse.md "地狱火诅咒")。
- 此动作在技术上具有每场战斗一次的限制，但钢铁卫士泰坦被赋予了两个相同的副本。因此，它可以在每场战斗中使用此动作两次。
- 钢铁卫士泰坦在生命值降至特定阈值后解锁此动作。生命值低于75%时，可以使用该能力的第一个副本。生命值降至50%时解锁第二次使用。

---
*Source: [Defensive Protocol: Bulwark](https://bg3.wiki/wiki/Defensive_Protocol:_Bulwark)*