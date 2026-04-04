# 死亡爆裂（火焰）

本文介绍岩浆魔蝠的死亡爆裂动作爆炸组件。对应的被动特性，请参见 [死亡爆裂：火焰](Death_Burst_colon__Fire.md "死亡爆裂：火焰")。其他死亡爆裂变体，请参见 [死亡爆裂](Death_Burst.md "死亡爆裂")。

**死亡爆裂**是 [岩浆魔蝠](Magma_Mephit.md "岩浆魔蝠") 在死亡时使用的动作。岩浆魔蝠爆炸，对附近生物造成 2d6⁠⁠[火焰](Fire.md "火焰") 伤害并点燃地面。

## 描述

在火焰爆发中爆炸。

## 属性

伤害：2~12

2d6⁠[火焰](Fire.md "火焰")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 11）（豁免成功：目标仍承受一半伤害。）
范围：自身
区域效果：2 米（7 英尺）半径
创建区域：火焰

## 技术细节

UID

`Projectile_DeathBurst_MagmaMephit`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[IsTrap](IsTrap_(spell_flag).md)`

## 区域：火焰

**[火焰](Fire_(surface).md "火焰（地表）")**

区域效果：3 米（10 英尺）半径

每回合造成 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。

类型：[地表](Area.md#Surface "区域")

### 状态：燃烧

**[燃烧](Burning_(Condition).md "燃烧（状态）")**

- 每回合承受 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- 可通过 [协助](Help.md "协助") 动作、使用 [治疗药水](Potion_of_Healing.md "治疗药水") 或获得 [濡湿](Wet_(Condition).md "濡湿（状态）") 来移除。
- 如果处于 [濡湿](Wet_(Condition).md "濡湿（状态）") 状态则免疫。
- [蘸取](Dip.md "蘸取") 动作可用于燃烧的角色或物体。

## 如何习得

由以下生物使用：[岩浆魔蝠](Magma_Mephit.md "岩浆魔蝠")

## 备注

- 与对应的 [死亡爆裂（寒冷）](Death_Burst_(Cold).md "死亡爆裂（寒冷）") 和 [死亡爆裂（泥巴）](Death_Burst_(Mud).md "死亡爆裂（泥巴）") 不同，此版本的死亡爆裂无法手动触发以造成双倍伤害。

---
*Source: [Death Burst (Fire)](https://bg3.wiki/wiki/Death_Burst_(Fire)*