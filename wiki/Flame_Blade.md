# 火焰刀

本文介绍的是法术。关于召唤武器，请参见 [火焰刀（武器）](Flame_Blade_(weapon).md "火焰刀（武器）")。

**火焰刀**是一个[法术](Spells.md "法术")。它允许施法者在空闲的手中召唤一把散发明亮光芒的火焰弯刀。施法者可以用刀进行近战武器攻击，对敌人造成火焰伤害。

## 描述

在手中召唤一把燃烧的[弯刀](Flame_Blade_(weapon).md "火焰刀（武器）")，持续10回合，造成3d6⁠⁠[火焰](Fire.md "火焰")伤害。它在3米（10英尺）半径内散发明亮光线，在6米（20英尺）半径内散发微光。

刀可以卸下并重新装备，但必须留在施法者身上。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
详情
范围：自身

## 升环施法

[升环施法](Upcasting.md "升环施法")：当此法术以4环或更高环级施放时，每比2环高两个法术位等级，伤害增加1d6⁠⁠[火焰](Fire.md "火焰")。

## 技术细节

UID

`Shout_FlameBlade`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 物品：火焰刀（武器）

[火焰刀](Flame_Blade_(weapon).md "火焰刀（武器）") – 持续时间：10回合

伤害：3~18

3d6⁠[火焰](Fire.md "火焰")

**属性**

- [弯刀](Scimitars.md "弯刀")

- [近战](List_of_melee_weapons.md "近战武器列表")

- [军用](Martial_weapons.md "军用武器")

- [单手](Weapons.md#Weapon_slots "武器")

- 价格：30 gp

- 重量：0.5 千克（1 磅）

## 如何习得

职业：

- 职业等级3：[德鲁伊](Druid.md "德鲁伊")

种族：

- 角色等级5：[梅菲斯特提夫林](Mephistopheles_Tiefling.md "梅菲斯特提夫林")

（_角色等级_ 是多职业角色所有职业等级的总和。）

由物品授予：

- [提夫林罪恶灵药](Elixir_of_Tiefling_Vice.md "提夫林罪恶灵药")（充能：单次使用）

其他学习方式：

- [法师](Wizard.md "法师") _无法_ 将[火焰刀卷轴](Scroll_of_Flame_Blade.md "火焰刀卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 刀可以装备在主手或副手，也可以卸下，但必须留在施法者身上。刀没有与之关联的[武器动作](Weapon_actions.md "武器动作")，只有基础攻击。
- 刀使用施法者的[施法关键属性](Spells.md#Spellcasting_Ability_and_Proficiency "法术")（[德鲁伊](Druid.md "德鲁伊")为[感知](Wisdom.md "感知")，提夫林为魅力）进行[攻击掷骰](Attack_roll.md "攻击掷骰")，而非[力量](Strength.md "力量")或[敏捷](Dexterity.md "敏捷")，但与大多数法术攻击一样，[伤害掷骰](Damage_Roll.md "伤害掷骰")不添加调整值。
  - 当作为德鲁伊习得时，施法者当前的施法关键属性是施法者最近首次就职的职业的属性，因此不一定是感知。
  - 对于提夫林习得的版本，施法关键属性始终是魅力。
- 法术结束时，施法者会自动重新装备施法前装备的武器，且不消耗动作点。
- 如果施法者主手持有轻型武器（或拥有[双持客](Dual_Wielder.md "双持客")专长且主手持有_非_双手武器），火焰刀将与该武器以[双武器战斗](Two-Weapon_Fighting.md "双武器战斗")风格一同持握。这些武器的位置如下：

1. 如果施法者在施放法术时_已经_在副手持有武器，火焰刀将_替换_副手武器。当法术以这种方式结束时（火焰刀在副手），先前在副手的武器将_不会_重新装备，副手将保持空置。
2. 如果施放法术时副手_为空_，刀将被召唤在_主手_，先前装备在主手的武器将被移动到_副手_。当法术以这种方式结束时，原始武器将移回_主手_，副手现在为空。

- 火焰刀与[橡棍术](Shillelagh.md "橡棍术")有相同的两个咒语：**Canto Te**（拉丁语，意为“我为你施法”）和 **Para Bellum**（拉丁语，意为“备战”）。

## 错误

- 由梅菲斯特提夫林召唤的火焰刀进行的攻击，在检查被动/状态时被视为武器/近战武器攻击，而通过德鲁伊职业法术召唤的火焰刀进行的攻击被视为近战法术攻击，类似于[电爪](Shocking_Grasp.md "电爪")和[吸血鬼之触](Vampiric_Touch.md "吸血鬼之触")等法术。
- 让雇佣兵[丹顿](Danton.md "丹顿")施放此法术，立即召回他的灵魂，然后再次雇佣他，会创建一个永久的[火焰刀](Flame_Blade_(weapon).md)（武器）），可由任何其他队友持握。此版本的刀造成最多（5d6 + 力量调整值）[火焰](Fire.md "火焰")伤害，并且是唯一没有[灵巧](Finesse.md "灵巧")属性的[弯刀](Scimitars.md "弯刀")。

## 外部链接

- ⁠[火焰刀](https://forgottenrealms.fandom.com/wiki/Flame_blade) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Flame Blade](https://bg3.wiki/wiki/Flame_Blade)*