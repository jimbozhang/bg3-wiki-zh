# 纠缠

关于菘蓝树人使用的版本，请参见 [纠缠（菘蓝树人）](Entangle_(Wood_Woad).md "纠缠（菘蓝树人）")。

**纠缠**是一个[法术](Spells.md "法术")。它允许施法者召唤魔法藤蔓，并将射程内的一个区域变成劣势地形。生物在该区域内可能被[缠绕](Entangled_(Condition).md "缠绕（状态）")，并且移动速度减半。

## 描述

藤蔓从地面生长，将其变成[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")，并可能[缠绕](Entangled_(Condition).md "缠绕（状态）")其中的生物。

被缠绕的生物无法移动。盟友可以使用其协助动作尝试撕开藤蔓。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [一级法术位](Spells.md#Spell_slots "法术")
详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
射程：18 米（60 英尺）
范围：3 米（10 英尺）半径
创造区域：扭曲的藤蔓
[专注](Concentration.md "专注")

## 更高法术位

以更高法术位施放此法术不会获得额外收益。

## 区域：扭曲的藤蔓

**[扭曲的藤蔓](Twisting_Vines.md "扭曲的藤蔓")**

持续时间：10 驱散

范围：3 米（10 英尺）半径

劣势地形 - 移动速度减半，生物可能被缠绕。被缠绕的生物无法移动。

类型：[地表](Area.md#Surface "区域")

### 状态：缠绕

**[缠绕](Entangled_(Condition).md "缠绕（状态）")**

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 无法移动。
- 对该生物的[攻击掷骰](Attack_roll.md "攻击掷骰")具有[优势](Advantage.md "优势")，而该生物的攻击掷骰和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")具有[劣势](Disadvantage.md "劣势")。

### 状态：劣势地形：藤蔓

**[劣势地形：藤蔓](Difficult_Terrain_colon__Vines_(Condition).md "劣势地形：藤蔓（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半。

## 如何习得

职业：

- 职业等级 1：[德鲁伊](Druid.md "德鲁伊")
- 职业等级 6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级 10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性提供：

- [魔法学徒：德鲁伊](Magic_Initiate_colon__Druid.md "魔法学徒：德鲁伊")

生物使用：[哈弗·威洛比（自然的复仇）](Harvard_Willoughby_(Nature's_Vengeance).md)

## 备注

- 如果角色在施放此法术时被[缠绕](Entangled_(Condition).md "缠绕（状态）")，它将保持该状态直到其下一驱散结束，因为缠绕状态在*战斗*驱散结束时失去持续时间。相反，来自[油脂](Grease_(surface).md "油脂（地表）")的[倒伏](Prone_(Condition).md "倒伏（状态）")或来自[蛛网术](Web_(surface).md "蛛网术（地表）")的[网缚](Enwebbed_(Condition).md "网缚（状态）")不会阻止角色在其下一驱散期间移动（除非它们在移动时再次获得此状态）。
- 一个等效法术，[信仰守望者的藤蔓](Faithwarden's_Vines.md "信仰守望者的藤蔓")，由[苍白橡树](Pale_Oak.md "苍白橡树")提供。

## 错误

- 纠缠具有 `TargetConditions` 为 `not Grounded()`，这意味着它无法以具有 `Grounded` 属性的生物为目标（例如具有[收割者的刚体](Reaper's_Rigidity.md "收割者的刚体")的[凯瑟里克·索姆](Ketheric_Thorm.md "凯瑟里克·索姆")）。尽管有此限制，纠缠*确实*影响具有 `Grounded` 属性的生物（功能上没有任何变化），并且可以通过在范围圆内间接以它们为目标来施放。

## 外部链接

- ⁠[纠缠](https://forgottenrealms.fandom.com/wiki/Entangle) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Entangle](https://bg3.wiki/wiki/Entangle)*