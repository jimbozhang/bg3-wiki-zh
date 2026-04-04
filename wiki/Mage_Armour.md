# 魔法护甲

**魔法护甲**是一个[法术](Spells.md "法术")。它允许施法者用魔法保护包围一个未着甲的生物（包括自己，如果未着甲）。

## 描述

用保护性的魔法力场包围一个未着甲的生物。其[护甲等级](Armour_Class.md "护甲等级")提升至 13 + 其[敏捷调整值](Dexterity.md#Dexterity_modifier_chart "敏捷")。

此效果不与无甲防御叠加。

目标不能穿着[护甲](Armour.md "护甲")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
详情
近战：1.5 米（5 英尺）

## 更高环阶

以此法术的更高环阶施放不会获得额外收益。

## 技术细节

UID

`Target_MageArmor`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：魔法护甲

**[魔法护甲](Mage_Armour_(Condition).md "魔法护甲 (状态)")**

持续时间：直至[长休](Long_Rest.md "长休")

- 基础[护甲等级](Armour_Class.md "护甲等级")为 13。

## 如何习得

职业：

- 职业等级 1：[术士](Sorcerer.md "术士")和[法师](Wizard.md "法师")
- 职业等级 3：[诡术师](Arcane_Trickster.md "诡术师")和[奥法骑士](Eldritch_Knight.md "奥法骑士")

由特性授予：

- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "魔法学徒：术士")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

由物品授予：

- [奉献皎月长袍](Moon_Devotion_Robe.md "奉献皎月长袍")

其他习得方式：

- [法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[魔法护甲卷轴](Scroll_of_Mage_Armour.md "魔法护甲卷轴")到他们的法术书中。

## 备注

- 选择[邪术师](Warlock.md "邪术师")在 2 级以上选择[异界恩赐](Eldritch_Invocation.md "异界恩赐")[暗影护甲](Armour_of_Shadows.md "暗影护甲")也会获得此法术。此版本的法术只以施法者自身为目标，且不消耗[法术位](Spells.md#Spell_Slots "法术位")。
- 如果施法者从当前队伍中移除，此增益仍然存在，即使稍后重新加入。
  - 如果由[法师](Wizard.md "法师")施放，此法术必须由施放它的队伍成员[预备](Prepared_spells.md "预备法术")；从施法者的预备法术列表中移除魔法护甲会立即移除施法者施加给所有队伍成员的增益。如果直接使用[魔法护甲卷轴](Scroll_of_Mage_Armour.md "魔法护甲卷轴")施放，而不是[抄录](Transcribing_scrolls.md "抄录卷轴")到法师的法术书中，则施法者无需保持该法术预备来维持增益。
- 如果拥有魔法护甲的队伍成员装备了一件护甲，增益会被移除。脱下该护甲后，魔法护甲不会重新施加；必须再次对他们施放。
- 正常的基础[护甲等级](Armour_Class.md "护甲等级")是 10 + [敏捷](Dexterity.md "敏捷")；此法术将其更改为 13 + 敏捷调整值。
  - 接受者仍然可以从其他不改变其基础护甲等级的来源获得奖励，例如 +1 护甲等级的[长袍](Robes.md "长袍")、[防御护腕](Bracers_of_Defence.md "防御护腕")、[虔诚护盾](Shield_of_Faith_(Condition).md "虔诚护盾 (状态)")等。
- 标记为[轻甲](Light_Armour.md "轻甲")、[中甲](Medium_Armour.md "中甲")或[重甲](Heavy_Armour.md "重甲")的[手套](Gloves.md "手套")和[头盔](Helmets.md "头盔")被视为护甲，并阻止魔法护甲生效。
- 装备[盾牌](Shields.md "盾牌")时魔法护甲仍然有效。
- [魔法护甲](Mage_Armour_(Condition).md "魔法护甲 (状态)")、[龙族韧性](Draconic_Resilience.md "龙族韧性")、[无甲防御（野蛮人）](Unarmoured_Defence_(Barbarian).md "无甲防御（野蛮人）")、[无甲防御（武僧）](Unarmoured_Defence_(Monk).md "无甲防御（武僧）")和[树肤术](Barkskin_(Condition).md "树肤术 (状态)")都会改变基础护甲等级，因此不叠加。
  - 如果接受者拥有多个此类效果，他们只获得提供最佳[护甲等级](Armour_Class.md "护甲等级")的那个。
- 魔法护甲在[荒野形态](Wild_Shape.md "荒野形态")中有效，只要使用者在变形前没有装备护甲。
  - 此效果仅对基础[护甲等级](Armour_Class.md "护甲等级")低于 13 的形态有效。
- 魔法护甲不被视为穿着护甲，因此不影响[无甲移动](Unarmoured_Movement.md "无甲移动")、[筑起壁垒](Become_the_Bulwark.md "筑起壁垒")和[防御](Defence.md "防御")。
- 魔法护甲的咒语是 **Mactē Virtutē**，拉丁语意为“以伟大的美德”。

## 外部链接

- ⁠[魔法护甲](https://forgottenrealms.fandom.com/wiki/Mage_armor) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Mage Armour](https://bg3.wiki/wiki/Mage_Armour)*