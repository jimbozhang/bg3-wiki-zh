# 月光壁垒

**月光壁垒**是一个[法术](Spells.md "法术")。它由[奉献皎月长袍](Moon_Devotion_Robe.md "奉献皎月长袍")提供，允许穿着者每长休一次对自己施放相当于[魔法护甲](Mage_Armour.md "魔法护甲")效果的法术。_\[[参见：错误](#bugs)\]_

## 描述

沐浴在[塞伦涅](Sel%C3%BBne.md "塞伦涅")守护目光的护佑魔法中。

目标不能穿着[护甲](Armour.md "护甲")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
范围：自身
充能：[长休](Long_Rest.md "长休")

## 更高环阶

以此法术施放更高环阶不会获得额外收益。

## 技术细节

UID

`Shout_MAG_Selunite_MageArmor`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：魔法护甲

**[魔法护甲](Mage_Armour_(Condition).md "魔法护甲 (状态)")**

持续时间：直至[长休](Long_Rest.md "长休")

- 基础[护甲等级](Armour_Class.md "护甲等级")为13。

## 学习方式

由物品提供：

- [奉献皎月长袍](Moon_Devotion_Robe.md "奉献皎月长袍")

## 备注

- 正常的基础[护甲等级](Armour_Class.md "护甲等级")是10 + [敏捷](Dexterity.md "敏捷")，而此法术将其改为13 + 敏捷调整值。

  - 接受者仍会获得其他不改变其基础护甲等级的来源的加成，例如+1 护甲等级的[长袍](Robes.md "长袍")、[防御护腕](Bracers_of_Defence.md "防御护腕")、[虔诚护盾](Shield_of_Faith_(Condition).md "虔诚护盾 (状态)")等。

- 标记为[轻甲](Light_Armour.md "轻甲")、[中甲](Medium_Armour.md "中甲")或[重甲](Heavy_Armour.md "重甲")的[手套](Gloves.md "手套")和[头盔](Helmets.md "头盔")视为护甲，将阻止魔法护甲生效。

- 魔法护甲在佩戴[盾牌](Shields.md "盾牌")时仍有效。

- [魔法护甲](Mage_Armour_(Condition).md "魔法护甲 (状态)")、[龙族韧性](Draconic_Resilience.md "龙族韧性")、[无甲防御（野蛮人）](Unarmoured_Defence_(Barbarian).md "无甲防御（野蛮人）")、[无甲防御（武僧）](Unarmoured_Defence_(Monk).md "无甲防御（武僧）")和[树肤术](Barkskin_(Condition).md "树肤术 (状态)")都会改变一个人的基础护甲等级，因此不会叠加。

  - 如果一个人拥有多个这些效果，他们只会获得提供最高[护甲等级](Armour_Class.md "护甲等级")的那个效果。

- 魔法护甲在[荒野形态](Wild_Shape.md "荒野形态")中可以生效，只要在变形前任何槽位都没有装备护甲。

  - 此效果仅对基础[护甲等级](Armour_Class.md "护甲等级")低于13的形态有效。

- 魔法护甲不被视为穿着护甲，对于[无甲移动](Unarmoured_Movement.md "无甲移动")、[筑起壁垒](Become_the_Bulwark.md "筑起壁垒")和[防御](Defence.md "防御")等效果而言。

- 魔法护甲的咒语是 **Mactē Virtutē** ，拉丁语命令“以美德为荣！”

## 错误

- 尽管与[奉献皎月长袍](Moon_Devotion_Robe.md "奉献皎月长袍")相关的[塞伦涅的保护](Sel%C3%BBne's_Protection.md "塞伦涅的保护")应由月光壁垒激活，但它并未激活；穿着者必须让常规版本的[魔法护甲](Mage_Armour.md "魔法护甲")施放在他们身上，其光耀伤害才能生效。

---
*Source: [Lunar Bulwark](https://bg3.wiki/wiki/Lunar_Bulwark)*