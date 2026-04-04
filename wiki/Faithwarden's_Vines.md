# 信仰守望者的藤蔓

**信仰守望者的藤蔓** 是一个 [法术](Spells.md "法术")。此法术允许施法者召唤魔法藤蔓，并将射程内的一个区域转变为劣势地形。生物在该区域内站立时可能被 [缠绕](Entangled_(Condition).md "缠绕 (状态)")，且移动速度减半。其效果等同于德鲁伊的等级 1 法术 [纠缠](Entangle.md "纠缠")。

## 描述

藤蔓从地面生长出来，将地面转变为 [劣势地形](Difficult_Terrain_(Condition).md "劣势地形 (状态)")，并可能 [缠绕](Entangled_(Condition).md "缠绕 (状态)") 区域内的生物。

被缠绕的生物无法移动。盟友可以使用其协助动作尝试撕开藤蔓。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
射程：18 米（60 英尺）
范围：3 米（10 英尺）半径
创造区域：扭曲的藤蔓
充能：[长休](Long_Rest.md "长休")
[专注](Concentration.md "专注")

## 更高环阶施法

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_DEN_Entangle_Staff`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：扭曲的藤蔓

**[扭曲的藤蔓](Twisting_Vines.md "扭曲的藤蔓")**

持续时间：10 驱散
范围：3 米（10 英尺）半径
劣势地形 - 移动速度减半，生物可能被缠绕。被缠绕的生物无法移动。
类型：[地表](Area.md#Surface "区域")

### 状态：缠绕

**[缠绕](Entangled_(Condition).md "缠绕 (状态)")**

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免 DC](Dice_rolls.md#Spell_save_DC "骰子掷骰"))

- 无法移动。
- 对该生物的 [攻击掷骰](Attack_roll.md "攻击掷骰") 具有 [优势](Advantage.md "优势")，而该生物的攻击掷骰和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 具有 [劣势](Disadvantage.md "劣势")。

### 状态：劣势地形：藤蔓

**[劣势地形：藤蔓](Difficult_Terrain_colon__Vines_(Condition).md "劣势地形：藤蔓 (状态)")**

- [移动速度](Movement_speed.md "移动速度") 减半。

## 如何习得

由物品授予：

- [苍白橡树](Pale_Oak.md "苍白橡树") (充能：[长休](Long_Rest.md "长休"))

---
*Source: [Faithwarden's Vines](https://bg3.wiki/wiki/Faithwarden's_Vines)*