# 艾嘉西斯之铠

**艾嘉西斯之铠**是一个[法术](Spells.md "法术")。它允许施法者创造一个覆盖施法者及其装备的冰霜灵体护甲。该护甲为施法者提供额外的[生命值](Hit_Points.md "生命值")，并在附加生命值存在时对敌对目标造成伤害。

## 描述

获得5点[临时生命值](Temporary_Hit_Points.md "临时生命值")，并对任何以近战攻击命中你的生物造成5点[寒冷](Cold.md "寒冷")伤害。

只能拥有来自一个来源的[临时生命值](Hit_Points.md#Temporary_Hit_Points "生命值")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：5

5点[寒冷](Cold.md "寒冷")（当被近战攻击命中时）

详情
范围：自身

## 升环施法

[升环施法](Upcasting.md "升环施法")：每提升一个环级，额外获得5点[临时生命值](Temporary_Hit_Points.md "临时生命值")，并额外造成5点[寒冷](Cold.md "寒冷")伤害。

## 技术细节

UID

`Shout_ArmorOfAgathys`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：艾嘉西斯之铠

**[艾嘉西斯之铠](Armour_of_Agathys_(Condition).md "艾嘉西斯之铠（状态）")**

持续时间：直至[长休](Long_Rest.md "长休")

获得5 × 法术等级的[临时生命值](Temporary_Hit_Points.md "临时生命值")。如果被近战攻击命中，攻击者将受到5 × 法术等级的[寒冷](Cold.md "寒冷")伤害。当临时生命值耗尽时，此效果结束。

## 如何习得

职业：

- 职业等级1：[邪术师](Warlock.md "邪术师")和[龙族血脉](Draconic_Bloodline.md "龙族血脉")（白色/寒冷血脉）
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性提供：

- [魔法学徒：邪术师](Magic_Initiate_colon__Warlock.md "魔法学徒：邪术师")

由物品提供：

- [冰噬长袍](Icebite_Robe.md "冰噬长袍")（充能：[长休](Long_Rest.md "长休")）

其他习得方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到法术书中的卷轴。

## 备注

  - [共生实体](Symbiotic_Entity.md "共生实体")提供的[临时生命值](Temporary_Hit_Points.md "临时生命值")，如果高于艾嘉西斯之铠的临时生命值，可以用来增加艾嘉西斯之铠的临时生命值。否则，大多数临时生命值来源会将此法术视为任何其他临时生命值来源：
  - 如果它们低于艾嘉西斯之铠提供的*最大*生命值，则无效。
  - 如果它们高于艾嘉西斯之铠提供的*最大*生命值，它们将替换临时生命值并结束艾嘉西斯之铠。
- 艾嘉西斯之铠的咒语是 **Mactē Virtutē**，拉丁语命令“以美德为荣！”
- 如果通过[冰噬长袍](Icebite_Robe.md "冰噬长袍")施放，当卸下冰噬长袍时，法术会结束。

## 错误

- 当升环至3级或4级法术位时，工具提示描述错误地引用了通过1级法术位版本施加的状态。

## 外部链接

- ⁠[Armor of Agathys](https://forgottenrealms.fandom.com/wiki/Armor_of_Agathys) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Armour of Agathys](https://bg3.wiki/wiki/Armour_of_Agathys)*