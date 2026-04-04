# 魔法护甲

**魔法护甲**是一个[法术](Spells.md "法术")。它允许施法者用魔法保护包围一个未穿护甲的生物（包括自己，如果未穿护甲）。

## 描述

用保护性的魔法力场包围一个未穿护甲的生物。其[护甲等级](Armour_Class.md "Armour Class")提升至 13 + 其[敏捷调整值](Dexterity.md#Dexterity_modifier_chart "Dexterity")。

此效果不与无甲防御叠加。

目标不能穿着[护甲](Armour.md "Armour")。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [1级法术位](Spells.md#Spell_slots "Spells")
细节
近战：1.5 米（5 英尺）

## 更高环阶

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_MageArmor`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：魔法护甲

**[魔法护甲](Mage_Armour_(Condition).md "Mage Armour (Condition)")**

持续时间：直至[长休](Long_Rest.md "Long rest")

- 基础[护甲等级](Armour_Class.md "Armour Class")为 13。

## 如何学习

职业：

- 职业等级 1：[术士](Sorcerer.md "Sorcerer")和[法师](Wizard.md "Wizard")
- 职业等级 3：[诡术师](Arcane_Trickster.md "Arcane Trickster")和[奥法骑士](Eldritch_Knight.md "Eldritch Knight")

由特性授予：

- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "Magic Initiate: Sorcerer")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "Magic Initiate: Wizard")

由物品授予：

- [奉献皎月长袍](Moon_Devotion_Robe.md "Moon Devotion Robe")

其他学习方式：

- [法师](Wizard.md "Wizard")可以[抄录](Transcribing_scrolls.md "Transcribing scrolls")[魔法护甲卷轴](Scroll_of_Mage_Armour.md "Scroll of Mage Armour")到他们的法术书中。

## 备注

- 选择[邪术师](Warlock.md "Warlock")在 2 级以上选择[异界恩赐](Eldritch_Invocation.md "Eldritch Invocation")[暗影护甲](Armour_of_Shadows.md "Armour_of_Shadows")也会获得此法术。此版本的法术只以施法者自身为目标，并且不消耗[法术位](Spells.md#Spell_Slots "Spells")。
- 如果施法者被移出当前队伍，此增益仍然存在，即使之后重新加入。
  - 如果由[法师](Wizard.md "Wizard")施放，此法术必须由施放它的队伍成员[预备](Prepared_spells.md "Prepared spells")；从施法者的预备法术列表中移除魔法护甲会立即移除施法者施加给所有队伍成员的增益。如果直接使用[魔法护甲卷轴](Scroll_of_Mage_Armour.md "魔法护甲卷轴")施放，而不是[抄录](Transcribing_scrolls.md "Transcribing scrolls")到法师的法术书中，则施法者无需保持该法术预备来维持增益。
- 如果拥有魔法护甲的队伍成员装备了一件护甲，增益会被移除。脱下该护甲后，魔法护甲不会重新施加；必须再次对他们施放。
- 正常的[护甲等级](Armour_Class.md "Armour Class")基础值为 10 + [敏捷](Dexterity.md "敏捷")；此法术将其改为 13 + 敏捷调整值。
  - 接受者仍然可以获得其他不改变其基础护甲等级的来源的加成，例如 +1 护甲等级的[长袍](Robes.md "Robes")、[防御护腕](Bracers_of_Defence.md "Bracers_of_Defence")、[虔诚护盾](Shield_of_Faith_(Condition).md "Shield of Faith (Condition)")等。
- 标记为[轻甲](Light_Armour.md "轻甲")、[中甲](Medium_Armour.md "中甲")或[重甲](Heavy_Armour.md "重甲")的[手套](Gloves.md "Gloves")和[头盔](Helmets.md "Helmets")被视为护甲，并阻止魔法护甲生效。
- 装备[盾牌](Shields.md "Shields")时魔法护甲仍然有效。
- [魔法护甲](Mage_Armour_(Condition).md "Mage Armour (Condition)")、[龙族韧性](Draconic_Resilience.md "Draconic Resilience")、[无甲防御（野蛮人）](Unarmoured_Defence_(Barbarian).md "Unarmoured Defence (Barbarian)")、[无甲防御（武僧）](Unarmoured_Defence_(Monk).md "Unarmoured Defence (Monk)")和[树肤术](Barkskin_(Condition).md "Barkskin (Condition)")都会改变基础护甲等级，因此不叠加。
  - 如果接受者拥有多个此类效果，他们只获得提供最佳[护甲等级](Armour_Class.md "Armour Class")的那个效果。
- 只要使用者在变形前没有装备护甲，魔法护甲在[荒野形态](Wild_Shape.md "Wild_Shape")中仍然有效。
  - 此效果仅对基础[护甲等级](Armour_Class.md "Armour Class")低于 13 的形态有效。
- 魔法护甲不被视为穿着护甲，因此不影响[无甲移动](Unarmoured_Movement.md "Unarmoured_Movement")、[筑起壁垒](Become_the_Bulwark.md "Become_the_Bulwark")和[防御](Defence.md "Defence")等效果。
- 魔法护甲的咒语是 **Mactē Virtutē**，拉丁语意为“以伟大的美德”。

## 外部链接

- ⁠[魔法护甲](https://forgottenrealms.fandom.com/wiki/Mage_armor) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Mage Armour](https://bg3.wiki/wiki/Mage_Armour)*