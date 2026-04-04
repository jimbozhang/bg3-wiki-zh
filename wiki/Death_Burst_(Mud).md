# 死亡爆裂 (泥巴)

本文介绍的是手动触发泥魔蝠死亡爆裂的动作。关于对应的被动特性，请参见 [死亡爆裂：力场](Death_Burst_colon__Force.md "死亡爆裂：力场")。关于其他变体的死亡爆裂，请参见 [死亡爆裂](Death_Burst.md "死亡爆裂")。

**死亡爆裂**是[泥魔蝠](Mud_Mephit.md "泥魔蝠")的一个动作。泥魔蝠爆炸，对附近的生物造成 4d6⁠⁠[力场](Force.md "力场") _\[[参见注释](#notes)\]_ 伤害，并用泥巴覆盖周围区域。如果魔蝠以其他方式死亡，也会触发此爆炸，但伤害减半。

## 描述

在一团粘稠的泥巴中爆炸。泥巴会瞬间干燥在任何附近非泥巴构成的生物上，[束缚](Muddy_(Condition).md "泥泞 (状态)")并伤害它们。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：6~36

4d6⁠[力场](Force.md "力场")（如果手动触发）

\+ 2d6⁠[力场](Force.md "力场")（如果在死亡时触发）

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 13）
范围：自身
区域效果：3 米（10 英尺）半径
创建区域：泥巴

## 技术细节

UID

`Shout_DeathBurst_Chosen_MudMephit`

触发爆炸的动作

`Projectile_DeathBurst_Died_MudMephit`

由动作触发的爆炸

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[IsTrap](IsTrap_(spell_flag).md)`

## 状态：泥泞

**[泥泞](Muddy_(Condition).md "泥泞 (状态)")**

持续时间：2 驱散

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 13）

- 受影响实体被硬化的泥巴覆盖，其[移动速度](Movement_speed.md "移动速度")减半。
- 对其进行的[攻击掷骰](Attack_rolls.md "攻击掷骰")具有[优势](Advantage.md "优势")，而该实体的攻击掷骰和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")具有[劣势](Disadvantage.md "劣势")。
- [免疫](Immune.md "免疫")于[燃烧](Burning_(Condition).md "燃烧 (状态)")和[狂野魔法：燃烧](Wild_Magic_colon__Burning_(Condition).md "狂野魔法：燃烧 (状态)")。
- [抗性](Resistant.md "抗性")于⁠[火焰](Fire.md "火焰")伤害。

## 区域：泥巴

**[泥巴](Mud.md "泥巴")**

持续时间：3 驱散

区域效果：3 米（10 英尺）半径

劣势地形 - [移动速度](Movement_speed.md "移动速度")减半。

类型：[地表](Area.md#Surface "区域")

### 状态：劣势地形：泥巴

**[劣势地形：泥巴](Difficult_Terrain_colon__Mud_(Condition).md "劣势地形：泥巴 (状态)")**

- [移动速度](Movement_speed.md "移动速度")减半。

## 如何习得

由以下生物使用：[泥魔蝠](Mud_Mephit.md "泥魔蝠")

## 注释

- 使用此动作手动触发死亡爆裂造成的伤害，是在死亡时由[死亡爆裂：力场](Death_Burst_colon__Force.md "死亡爆裂：力场")触发的伤害的两倍。

---
*Source: [Death Burst (Mud)](https://bg3.wiki/wiki/Death_Burst_(Mud)*