# 啄咬眼珠 (恐鸦)

本文介绍的是恐鸦使用的攻击。其他版本请参见 [啄咬眼珠 (消歧义)](Rend_Vision_(disambiguation)..md)

**啄咬眼珠**是恐鸦可用的攻击，包括[驯兽师](Beast_Master.md "驯兽师")的[恐鸦伙伴](Dire_Raven_Companion.md "恐鸦伙伴")或处于[荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven.md "荒野形态：恐鸦")形态的[德鲁伊](Druid.md "德鲁伊")。这是一种近战攻击，造成⁠[穿刺](Piercing.md "穿刺")伤害，伤害随乌鸦等级提升，并会使目标[目盲](Blinded_(Condition).md "目盲 (状态)")。

## 描述

攻击生物的眼睛并使其[目盲](Blinded_(Condition).md "目盲 (状态)")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~6 + 调整值

1d6 + [敏捷调整值](Dexterity.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺")

详情
近战 非武装 [攻击掷骰](Attack_roll.md "攻击掷骰")
近战：1.5 米 (5 英尺)

## 更高等级

此攻击在更高等级时造成额外伤害：

- 德鲁伊等级 4 或驯兽师伙伴等级 5 时，额外 +1d4⁠[穿刺](Piercing.md "穿刺")（[乌鸦座](Corvus_Major.md "乌鸦座")）
- 德鲁伊等级 8 或驯兽师伙伴等级 11 时，额外 +1d6⁠[穿刺](Piercing.md "穿刺")（[神速鸦](Corvus_Celer.md "神速鸦")）
- 德鲁伊等级 12 时，额外 +1d8⁠[穿刺](Piercing.md "穿刺")

## 技术细节

UID

`Target_RendVision_Raven_Summon`

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：目盲

**[目盲](Blinded_(Condition).md "目盲 (状态)")**

持续时间：2 回合

- 受影响的生物在[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术范围减少至 3 米 (10 英尺)。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "优势")。

## 如何习得

由以下生物使用：[乌鸦座](Corvus.md "乌鸦座")、[神速鸦](Corvus_Celer.md "神速鸦")、[乌鸦座](Corvus_Major.md "乌鸦座")、[变形术：恐鸦](Polymorph_colon__Dire_Raven.md "变形术：恐鸦")、[渡鸦 (白色)](Raven_(white).md)、以及[荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven.md "荒野形态：恐鸦")

## 备注

- 没有[豁免检定](Saving_throw.md "豁免检定")来避免[目盲](Blinded_(Condition).md "目盲 (状态)")效果。攻击只需命中即可应用效果。
- 在[荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven.md "荒野形态：恐鸦")形态下，此攻击会从[酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")专长获得额外的攻击加值（来自力量调整值），即使正常攻击加值由敏捷调整值决定。
- 驯兽师伙伴的等级在 5、7 和 11 级时离散提升，因此它在 5 级前不会获得 4 级额外伤害（[乌鸦座](Corvus_Major.md "乌鸦座")），在 11 级前不会获得 8 级额外伤害（[神速鸦](Corvus_Celer.md "神速鸦")）。它永远不会获得 12 级伤害升级。

---
*Source: [Rend Vision (Dire Raven)](https://bg3.wiki/wiki/Rend_Vision_(Dire_Raven)*