# 纠缠（菘蓝树人）

关于普通等级法术，请参阅 [纠缠](Entangle.md "纠缠")。

**纠缠**是[法术](Spells.md "法术")的[法术](Spells.md "法术")。它是[菘蓝树人](Wood_Woad.md "菘蓝树人")可用的[纠缠](Entangle.md "纠缠")变体。与标准法术相比，它的射程显著缩短，但影响范围更大。

## 描述

创造一个藤蔓地表，减缓生物速度，并可能使它们[缠绕](Entangled_(Condition).md "缠绕（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）
射程：6米（20英尺）
范围：6米（20英尺）半径
创造区域：扭曲的藤蔓
[专注](Concentration.md "专注")

## 高等级施法

以更高等级施放此法术不会获得额外收益。

## 技术细节

UID

`Target_Entangle_WoodWoad`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：扭曲的藤蔓

**[扭曲的藤蔓](Twisting_Vines.md "扭曲的藤蔓")**

持续时间：10驱散
范围：6米（20英尺）半径

劣势地形 - 移动速度减半，生物可能被缠绕。被缠绕的生物无法移动。

类型：[地表](Area.md#Surface "区域")

### 状态：缠绕

**[缠绕](Entangled_(Condition).md "缠绕（状态）")**

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 无法移动。
- 对该生物的[攻击掷骰](Attack_roll.md "攻击掷骰")具有[优势](Advantage.md "优势")，而该生物的攻击掷骰和[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")具有[劣势](Disadvantage.md "劣势")。

### 状态：劣势地形：藤蔓

**[劣势地形：藤蔓](Difficult_Terrain_colon__Vines_(Condition).md "劣势地形：藤蔓（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半。

## 如何习得

生物使用：[菘蓝树人](Wood_Woad.md "菘蓝树人")

## 备注

- 菘蓝树人有两个几乎相同的能力版本（`Target_Entangle_WoodWoad` 和 `Target_Entangle_WoodWoad_Hardcore`），仅影响范围半径不同。当您通过[坠落连理](Fallen_Lover.md "坠落连理")召唤菘蓝树人时，您将在快捷栏上看到这两个版本。

---
*Source: [Entangle (Wood Woad)](https://bg3.wiki/wiki/Entangle_(Wood_Woad)*