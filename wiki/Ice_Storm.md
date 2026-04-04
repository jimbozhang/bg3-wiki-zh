# 冰风暴

**冰风暴**是一个[4环塑能学派法术](Spells.md "法术")。它允许施法者召唤一场冰风暴打击一个区域。

## 描述

驱使一阵冰雹和冰从天而降，覆盖地面并打击范围内所有物体和生物，造成[钝击](Bludgeoning.md "钝击")和[寒冷](Cold.md "寒冷")伤害。它还会创造一个持续2回合的[冰](Ice_(surface).md "冰（地表）")地表。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4环法术位](Spells.md#Spell_slots "法术")
伤害：6~40

2d8[钝击](Bludgeoning.md "钝击")

\+ 4d6[寒冷](Cold.md "寒冷")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（豁免成功：目标仍承受一半伤害。）
范围：18米（60英尺）
范围效果：6米（20英尺）半径
创造区域：冰

## 升环施法效果

[升环施法](Upcasting.md "升环施法")：以更高环位施放此法术时，每比4环高1环，额外造成1d8[钝击](Bludgeoning.md "钝击")伤害。

## 技术细节

UID

`Target_IceStorm`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：冰

**[冰](Ice_(surface).md "冰（地表）")**

持续时间：2回合

范围效果：6米（20英尺）半径

劣势地形 - [移动速度](Movement_speed.md "移动速度")减半，生物可能陷入[倒伏](Prone.md "倒伏")状态。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或采取[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）范围内对倒伏生物进行的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起时仅消耗1.5米（5英尺）移动速度。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半

## 学习方式

职业：

- 职业等级7：[德鲁伊](Druid.md "德鲁伊")、[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[风暴领域](Tempest_Domain.md "风暴领域")（领域法术）和[大地结社](Circle_of_the_Land.md "大地结社")（极地）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

物品授予：

- [玛科赫什基](Markoheshkir.md "玛科赫什基")（充能：[短休](Short_rest.md "短休")）

其他学习方式：

- 拥有[4环法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[冰风暴卷轴](Scroll_of_Ice_Storm.md "冰风暴卷轴")到他们的法术书中。

## 备注

- 冰风暴的咒语是 **Tremē**，拉丁语命令 _"颤抖/震动！"_

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Ice_Storm_Visuals.mp4>

## 外部链接

- [冰风暴](https://forgottenrealms.fandom.com/wiki/Ice_storm) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Ice Storm](https://bg3.wiki/wiki/Ice_Storm)*