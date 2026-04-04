# 暗影宗法术：沉默术

本文介绍的是暗影宗武僧的动作。关于幻术学派法术，请参见 [沉默术](Silence.md "沉默术")。

**暗影宗法术：沉默术** 是 [暗影宗](Way_of_Shadow.md "暗影宗") 武僧的职业动作。它允许武僧在射程内的区域召唤一个绝对寂静的球体。处于该球体内的生物免疫 [雷鸣](Thunder.md "雷鸣") 伤害，并且无法施放言语类法术。

## 描述

创造一个隔音球体。所有在其中的生物都会 [沉默](Silenced_(Condition).md "沉默（状态）") 并 [免疫](Damage_types.md#Immunity "伤害类型") [雷鸣](Thunder.md "雷鸣") 伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 2 [气点](Ki_Point.md "气点")
详情
射程：18 米（60 英尺）
范围效果：6 米（20 英尺）半径
创造区域：沉默
[专注](Concentration.md "专注")
持续时间：100 驱散

使用此法术可能会使目标变为敌对。

## 技术细节

UID

`Target_Silence_Monk`

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell_flag\) \(页面不存在\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`

## 区域：沉默

**[沉默](Silence_(area).md "沉默（区域）")**

持续时间：100 驱散

范围效果：6 米（20 英尺）半径

停留在光环内的生物会 [沉默](Silenced_(Condition).md "沉默（状态）")。

类型：[召唤](Area.md#Summoned "区域")

### 状态：沉默

**[沉默](Silenced_(Condition).md "沉默（状态）")**

- 生物无法说话或施放带有言语成分的法术，并且免疫 [雷鸣](Thunder.md "雷鸣") 伤害。

## 如何习得

职业：

- 职业等级 3：[暗影宗](Way_of_Shadow.md "暗影宗")

---
*Source: [Shadow Arts: Silence](https://bg3.wiki/wiki/Shadow_Arts:_Silence)*