# 云雾术

**云雾术**是一个[法术](Spells.md "法术")。它允许施法者在射程内的区域召唤一个[雾](Fog.md "雾")球体，并使该区域变为重度遮蔽。区域内的生物将陷入目盲状态。

## 描述

制造一团浓雾，以[重度遮蔽](Heavily_Obscured_(Condition).md "重度遮蔽 (状态)")并[目盲](Blinded_(Condition).md "目盲 (状态)")区域内的生物。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
详情
射程：18米（60英尺）
范围：4.5米（15英尺）半径
创造区域：雾
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：当此法术以2级或更高法术位施放时，其作用区域每比1级法术位高一级，增加2米（7英尺）。

## 技术细节

UID

`Target_FogCloud`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：雾

**[雾](Fog.md "雾")**

持续时间：10回合

范围：4.5米（15英尺）半径

使区域内的生物陷入重度遮蔽和目盲。

类型：[云](Area.md#Cloud "区域")

### 状态：目盲

**[目盲](Blinded_(Condition).md "目盲 (状态)")**

- 受影响的生物在[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术射程减少至3米（10英尺）。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "优势")。

## 学习方式

职业：

- 职业等级1：[德鲁伊](Druid.md "德鲁伊")、[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[风暴领域](Tempest_Domain.md "风暴领域")（领域法术）和[龙族血脉](Draconic_Bloodline.md "龙族血脉")（青铜/闪电血脉）
- 职业等级2：[游侠](Ranger.md "游侠")
- 职业等级3：[诡术师](Arcane_Trickster.md "诡术师")和[奥法骑士](Eldritch_Knight.md "奥法骑士")

由特性授予：

- [魔法学徒：德鲁伊](Magic_Initiate_colon__Druid.md "魔法学徒：德鲁伊")
- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "魔法学徒：术士")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

由物品授予：

- [严厉之锤的薄雾护符](Hammergrim_Mist_Amulet.md "严厉之锤的薄雾护符")

其他学习方式：

- [法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[云雾术卷轴](Scroll_of_Fog_Cloud.md "云雾术卷轴")到他们的法术书中。

## 备注

- 云雾术的咒语是 **Voco Nubes** ，拉丁语意为“我呼唤/召唤烟雾”。

## 错误

- 云雾术的半径不会因施放高于1级的法术位而始终增加2米（7英尺）。相反，会发生以下情况：
  - 法术位1到法术位2，半径增加1.5米（5英尺）。
  - 法术位2到法术位3，半径增加2米（7英尺）。
  - 法术位3到法术位4，半径增加2米（7英尺）。
  - 法术位4到法术位5，半径增加0.5米（2英尺）。
  - 法术位5到法术位6，半径增加1.5米（5英尺）。
- 在1级法术位时，云雾术的显示施放半径为4米（13英尺），但它实际创造的云半径为4.5米（15英尺）。
- 在5级法术位时，云雾术的显示施放半径为12米（40英尺），但它实际创造的云半径为10.5米（35英尺）。
- 在6级法术位时，云雾术的显示施放半径为14米（47英尺），但它实际创造的云半径为12米（40英尺）。

## 视觉效果

<https://bg3.wiki/wiki/File:Fog_Cloud_Visuals.mp4>

## 外部链接

- ⁠[Fog cloud](https://forgottenrealms.fandom.com/wiki/Fog_cloud) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Fog Cloud](https://bg3.wiki/wiki/Fog_Cloud)*