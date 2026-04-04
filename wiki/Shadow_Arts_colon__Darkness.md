# 暗影宗艺：黑暗术

本文介绍的是暗影宗武僧的动作。关于等效的塑能学派法术，请参见 [黑暗术](Darkness.md "黑暗术")。

**暗影宗艺：黑暗术** 是 [暗影宗](Way_of_Shadow.md "暗影宗") 武僧的职业动作。此能力允许这些武僧在射程内的区域召唤一团黑暗云，遮蔽并目盲其中的生物。

## 描述

创造一团魔法黑暗云，使范围内的生物 [重度遮蔽](Heavily_Obscured_(Condition).md "重度遮蔽 (状态)") 并 [目盲](Blinded_(Condition).md "目盲 (状态)")。生物无法向内或向外进行远程攻击。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 2 [气点](Ki_Point.md "气点")
详情
射程：18 米（60 英尺）
创造区域：黑暗术
[专注](Concentration.md "专注")

## 技术细节

UID

`Target_Darkness_Monk`

法术标志

`[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[Invisible](Invisible_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[Stealth](Stealth_(spell_flag).md)`

## 区域：黑暗术

**[黑暗术](Darkness_(cloud).md "黑暗术 (云)")**

持续时间：10 驱散

范围效果：5 米（17 英尺）半径

一团魔法黑暗帷幕，使范围内的生物重度遮蔽并目盲。生物无法向内或向外进行远程攻击。

类型：[云](Area.md#Cloud "区域")

### 状态：目盲

**[目盲](Blinded_(Condition).md "目盲 (状态)")**

- 受影响的生物在 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术射程减少至 3 米（10 英尺）。
- 对受影响的生物进行的攻击掷骰具有 [优势](Advantage.md "优势")。

## 如何习得

职业：

- 职业等级 3：[暗影宗](Way_of_Shadow.md "暗影宗")

---
*Source: [Shadow Arts: Darkness](https://bg3.wiki/wiki/Shadow_Arts:_Darkness)*