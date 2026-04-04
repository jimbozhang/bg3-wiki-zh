# 火墙术

**火墙术**是一个[法术](Spells.md "法术")。它允许施法者创造一道长长的火焰屏障，对区域内的任何事物造成伤害。

## 描述

创造一道炽热的火墙，对任何胆敢站得太近的单位施加[燃烧](Burning_(Condition).md "燃烧（状态）")状态。对任何进入该区域或在该区域内结束其回合的单位造成[火焰](Fire.md "火焰")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4环法术位](Spells.md#Spell_slots "法术")
伤害：5~40

5d8[火焰](Fire.md "火焰")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：目标仍承受一半伤害。）
范围：18米（60英尺）
创造区域：火墙术
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：以更高环位施放此法术时，每比4环高1环，额外造成1d8[火焰](Fire.md "火焰")伤害。

## 技术细节

UID

`Wall_WallOfFire`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：火墙术

**[火墙术](Wall_of_Fire_(area).md "火墙术（区域）")**

持续时间：10回合

范围效果：36米（120英尺）线型

类型：[召唤](Area.md#Summoned "区域")

### 状态：火墙术

**[火墙术](Wall_of_Fire_(Condition).md "火墙术（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 一道炽热的火墙，对3米（10英尺）内的任何单位造成5d8[火焰](Fire.md "火焰")伤害。

### 状态：燃烧

**[燃烧](Burning_(Condition).md "燃烧（状态）")**

- 每回合承受1d4[火焰](Fire.md "火焰")伤害。
- 可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿（状态）")状态来移除。
- 如果处于[濡湿](Wet_(Condition).md "濡湿（状态）")状态则免疫。
- [蘸取](Dip.md "蘸取")动作可用于燃烧中的角色或物体。

## 如何习得

职业：

- 职业等级7：[德鲁伊](Druid.md "德鲁伊")、[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[光明领域](Light_Domain.md "光明领域")（领域法术）、[邪魔](The_Fiend.md "邪魔")、以及[大地结社](Circle_of_the_Land.md "大地结社")（沙漠）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由物品提供：

- [玛科赫什基](Markoheshkir.md "玛科赫什基")（充能：[短休](Short_rest.md "短休")）

其他习得方式：

- 拥有[4环法术位](Spells.md#Spell_slots "法术")的[法师](Wizard.md "法师")可以将[火墙术卷轴](Scroll_of_Wall_of_Fire.md "火墙术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 此法术从第一个目标点到第二个目标点创造一道墙，距离最远36米（120英尺）。墙宽3米（10英尺）。
- 不会打破隐匿。
- 火墙术的咒语是 **Ira Et Dolor**，拉丁语意为“愤怒与痛苦”。

## 错误

- 在墙内结束回合时受到伤害的法术豁免DC固定为10。
- 升环描述未提及火焰伤害，仅说明法术“每环额外造成1d8伤害”。
- 火墙持续10回合结束后专注不会中断，为[奇异通道之戒](Strange_Conduit_Ring.md "奇异通道之戒")创造了永久的专注来源。
- 火墙术实际上会对2米（7英尺）内的生物造成伤害。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Wall_of_Fire_Visuals.mp4>

## 外部链接

[遗忘国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)上的[火墙术](https://forgottenrealms.fandom.com/wiki/Wall_of_fire)

---
*Source: [Wall of Fire](https://bg3.wiki/wiki/Wall_of_Fire)*