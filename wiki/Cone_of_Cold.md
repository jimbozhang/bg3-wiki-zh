# 寒冰锥

**寒冰锥**是一个[法术](Spells.md "法术")。它允许施法者向面前区域喷射冰冷空气，对受影响生物造成伤害，并将现有的[水地表](Water_(surface).md "水地表")转化为[冰地表](Ice_(surface).md "冰地表")。

## 描述

从你的手中爆发出一阵霜冻、凛冽空气和凝结的雪晶。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [5环法术位](Spells.md#Spell_slots "法术")
伤害：8~64

8d8⁠[寒冷](Cold.md "寒冷")

详情
[体质](Constitution.md "Constitution") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：目标仍承受一半伤害。）
范围：自身
范围效果：9米（30英尺）锥形
创造区域：冰

## 升环施法效果

[升环施法](Upcasting.md "升环施法")：每比5环高一环，伤害增加1d8⁠⁠[寒冷](Cold.md "寒冷")。

## 技术细节

UID

`Zone_ConeOfCold`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：冰

**[冰](Ice_(surface).md "冰地表")**

范围效果：9米（30英尺）锥形

劣势地形 - [移动速度](Movement_speed.md "移动速度")减半，生物可能倒伏。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏状态")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "骰子检定")）

- 受影响生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作”，并在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）内对倒伏生物进行的[攻击](attack.md "攻击")具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）移动速度。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形状态")**

- [移动速度](Movement_speed.md "移动速度")减半

## 学习方式

职业：

- 职业等级9：[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[邪魔](The_Fiend.md "邪魔")、[魔契主](The_Hexblade.md "魔契主")，以及[大地结社](Circle_of_the_Land.md "大地结社")（极地）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

物品授予：

- [玛科赫什基](Markoheshkir.md "玛科赫什基")（充能：[短休](Short_rest.md "短休")）

其他学习方式：

- 拥有[5环法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[寒冰锥卷轴](Scroll_of_Cone_of_Cold.md "寒冰锥卷轴")到他们的法术书中。

## 外部链接

- ⁠[寒冰锥](https://forgottenrealms.fandom.com/wiki/Cone_of_cold) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Cone of Cold](https://bg3.wiki/wiki/Cone_of_Cold)*