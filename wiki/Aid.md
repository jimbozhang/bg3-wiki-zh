# 支援术

**支援术**是一个[2级防护学派法术](Spells.md "法术")。它允许施法者治疗并鼓舞其盟友和自身，增强他们的决心。受影响的生物在法术持续期间，其最大[生命值](Hit_Points.md "生命值")会得到提升。

## 描述

以坚韧和决心强化你的盟友，治疗他们并提升其[生命值](Hit_Points.md "生命值")上限。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
详情
范围：自身
范围区域：9米（30英尺）半径

## 升环施法

[升环施法](Upcasting.md "升环施法")：以更高法术位施放此法术时，目标的最大生命值会额外增加5⁠⁠[生命值](Healing.md "治疗")，每比2级法术位高一级，增加量就多5点。

## 技术细节

UID

`Shout_Aid`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：支援术

**[支援术](Aid_(Condition).md "支援术（状态）")**

持续时间：直至[长休](Long_Rest.md "长休")

- 生命值上限增加5⁠⁠[生命值](Healing.md "治疗")。
- 每使用一个高于2级的[法术位等级](Spells.md#Spell_Slot_Levels "法术")，生命值上限额外增加5⁠⁠[生命值](Healing.md "治疗")。

## 学习方式

职业：

- 职业等级3：[牧师](Cleric.md "牧师")和[生命领域](Life_Domain.md "生命领域")（领域法术）
- 职业等级5：[圣武士](Paladin.md "圣武士")

其他学习方式：

- [法师](Wizard.md "法师")_无法_将[支援术卷轴](Scroll_of_Aid.md "支援术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书中。

## 备注

- 倒地的盟友会重返战斗并额外恢复1点生命值。
- 即使施法者离开队伍，[支援术](Aid_(Condition).md "支援术（状态）")状态仍然存在。
  - 鉴于支援术状态及其赋予的生命值提升具有持久性（见下文），让伙伴[伪装术](Disguise_Self.md "伪装术")并分组，以便对所有四个预期的活跃队伍成员施放此法术的升环版本，可能很有用——尤其是在较高等级时。
- 此法术带来的最大生命值提升与[临时生命值](Temporary_Hit_Points.md "临时生命值")不同。具体来说，这些生命值可以通过正常治疗补充，而临时生命值则不能。支援术_可以_与任何单一来源的临时生命值叠加，而临时生命值来源_不能_相互叠加。
- 物品提供的替代版本：
  - [卡利德的礼物：支援术](Khalid's_Gift_colon__Aid.md "卡利德的礼物：支援术")来自[卡利德的礼物](Khalid's_Gift.md "卡利德的礼物")，等效于3级支援术（充能：[长休](Long_Rest.md "长休")）
  - [奉献之盾：支援术](Shield_of_Devotion_colon__Aid.md "奉献之盾：支援术")来自[奉献之盾](Shield_of_Devotion.md "奉献之盾")，等效于3级支援术（充能：[长休](Long_Rest.md "长休")）
  - [至上真神的护符：支援术](Absolute's_Talisman_colon__Aid.md "至上真神的护符：支援术")来自[至上真神的护符](Absolute's_Talisman.md "至上真神的护符")，等效于2级支援术（充能：[长休](Long_Rest.md "长休")）
- 当从物品获得时，它只影响佩戴者。
- 这是玩家角色可用的唯一能影响[不死生物](List_of_creature_types.md#Undead "生物类型列表")和[构装生物](List_of_creature_types.md#Construct "生物类型列表")的治疗法术。
- 如果由[圣武士](Paladin.md "圣武士")或[牧师](Cleric.md "牧师")（非生命领域）施放，此法术必须保持[预备](Spells.md#Prepared_Spells "法术")状态；从施法者的预备法术中移除支援术，会移除施法者对所有队伍成员施加的支援术增益，使其最大生命值恢复至正常值。如果通过使用[卷轴](Scroll_of_Aid.md "支援术卷轴")施放，施法者无需保持此法术预备状态来维持增益。
- 多次施放支援术不会叠加；最近施放的实例优先。
- 尽管工具提示说法术治疗施法者及其盟友，但此法术不会受益于或触发任何提升或与治疗互动的物品或职业特性，例如[生命门徒](Disciple_of_Life.md "生命门徒")或[慰藉之戒](Ring_of_Salving.md "慰藉之戒")，除非目标生命值为0。
- 支援术的咒语是 **Vita Excolatur**（“生命得以提升”）和 **Dum Vita Est Spes Est**（“有生命，就有希望”）。

## 外部链接

- ⁠[支援术](https://forgottenrealms.fandom.com/wiki/Aid) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Aid](https://bg3.wiki/wiki/Aid)*