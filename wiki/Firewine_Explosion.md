# 火酒爆炸

**火酒爆炸**是当火焰点燃受[火酒腹](Firewine_Belly_(Condition).md "火酒腹 (状态)")影响的[狗头人](Kobold.md "狗头人")尸体时触发的爆炸。

## 描述

火焰点燃尸体中残留的酒精，引发爆炸。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~12

2d6⁠[火焰](Fire.md "火焰")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）（豁免成功时：目标仍承受全额伤害。_\[[参见：错误](#bugs)\]_）
范围效果：4米（13英尺）半径
创造区域：火焰

## 技术细节

UID

`Projectile_CRE_BreweryKobolds_FirewineBelly_Explosion`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[ImmediateCast](https://bg3.wiki/w/index.php?title=ImmediateCast_\(spell_flag\)&action=edit&redlink=1) "ImmediateCast \(spell flag\) \(page does not exist\)")`, `[IsTrap](IsTrap_(spell_flag).md)`

## 区域：火焰

**[火焰](Fire_(surface).md "火焰 (地表)")**

持续时间：3回合

范围效果：2米（7英尺）半径

每回合造成1d4⁠⁠[火焰](Fire.md "火焰")伤害。

类型：[地表](Area.md#Surface "区域")

### 状态：燃烧

**[燃烧](Burning_(Condition).md "燃烧 (状态)")**

- 每回合承受1d4⁠⁠[火焰](Fire.md "火焰")伤害。
- 可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。
- 若处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态则免疫。
- [蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。

## 学习方式

其他学习途径：

- 当拥有[火酒腹](Firewine_Belly_(Condition).md "火酒腹 (状态)")状态的[狗头人](Kobold.md "狗头人")被[火焰](Fire.md "火焰")伤害击杀时触发。

## 错误

- 豁免成功时，目标承受(4d6)/2⁠⁠[火焰](Fire.md "火焰")伤害，而非(2d6)/2⁠⁠[火焰](Fire.md "火焰")伤害，这实际上相当于全额伤害。

---
*Source: [Firewine Explosion](https://bg3.wiki/wiki/Firewine_Explosion)*