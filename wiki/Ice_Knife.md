# 冰刃术

关于四象宗武僧的等价法术，请参见[白霜之刃](Blade_of_Rime.md "白霜之刃")。

**冰刃术**是一个[法术](Spells.md "法术")。它允许施法者投掷一片冰刃，冰刃爆炸后会留下一片冰面。

## 描述

投掷一片冰刃，造成1d10⁠⁠[穿刺](Piercing.md "Piercing")伤害。它会爆炸并对附近的任何人造成2d6⁠⁠[寒冷](Cold.md "Cold")伤害。它会留下一片[冰](Ice_(surface).md "冰（地表）")地表。即使未命中，冰刃仍会爆炸。

此法术可在你[沉默](Silenced_(Condition).md "沉默（状态）")时施放。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [一级法术位](Spells.md#Spell_slots "法术")
伤害：3~22

1d10⁠[穿刺](Piercing.md "穿刺")

\+ 2d6⁠[寒冷](Cold.md "寒冷")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")（未命中时：冰刃仍会爆炸。）
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：爆炸造成的伤害被抵消）
射程：18米（60英尺）
范围：2米（7英尺）半径
创建区域：冰

## 升环效果

[升环施法](Spells.md#Upcasting "法术")：以更高环位施放此法术时，每比1环高1环，额外造成1d6⁠⁠[寒冷](Cold.md "Cold")伤害。

## 技术细节

UID

`Projectile_IceKnife`

普通一级变体

`Projectile_IceKnife_2`

升环二级变体

`Projectile_IceKnife_3`

升环三级变体

`Projectile_IceKnife_4`

升环四级变体

`Projectile_IceKnife_5`

升环五级变体

`Projectile_IceKnife_6`

升环六级变体

`Projectile_MAG_IceKnife`

通过冰霜王子获得的每长休一次变体

`Projectile_MAG_IceKnife_MonkGloves`

通过雪尘修道院手套获得的每长休一次变体

`Projectile_WYR_SmugglersCave_IceKnife_3`

NPC专用变体，由迷人的莱瑟姆使用

`Projectile_LOW_BhaalCultist_IceKnife`

NPC专用变体，由巴尔唤魔师使用

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：冰

**[冰](Ice_(surface).md "冰（地表）")**

持续时间：2回合

范围：2米（7英尺）半径

劣势地形 - [移动速度](Movement_speed.md "移动速度")减半，生物可能[倒伏](Prone.md "倒伏")。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或采取[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）范围内对倒伏生物进行的[攻击](attack.md "攻击")具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）的移动速度即可站起。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半

## 学习方式

职业：

- 职业等级1：[德鲁伊](Druid.md "德鲁伊")、[术士](Sorcerer.md "术士")和[法师](Wizard.md "法师")
- 职业等级3：[诡术师](Arcane_Trickster.md "诡术师")和[奥法骑士](Eldritch_Knight.md "奥法骑士")
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性提供：

- [魔法学徒：德鲁伊](Magic_Initiate_colon__Druid.md "魔法学徒：德鲁伊")
- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "魔法学徒：术士")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

由物品提供：

- [冰霜王子](Frost_Prince.md "冰霜王子")（充能：[长休](Long_Rest.md "长休")）
- [雪尘修道院手套](Snow-Dusted_Monastery_Gloves.md "雪尘修道院手套")（充能：[长休](Long_Rest.md "长休")）

其他学习方式：

- [法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[冰刃术卷轴](Scroll_of_Ice_Knife.md "冰刃术卷轴")到他们的法术书中。

## 备注

- 位于[冰](Ice_(surface).md "冰（地表）")上的生物若[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")失败，会[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Ice_Knife_Visuals.mp4>

## 外部链接

- ⁠[冰刃术](https://forgottenrealms.fandom.com/wiki/Ice_knife) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Ice Knife](https://bg3.wiki/wiki/Ice_Knife)*