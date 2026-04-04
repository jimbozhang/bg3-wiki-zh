# 轰鸣剑

**轰鸣剑** 是一个 [戏法（塑能学派）](Spells.md "法术")。它允许施法者用近战武器攻击，如果目标之后移动，会造成额外伤害。

## 描述

用你的武器攻击，使你的敌人受到共振影响，当他们移动时，会受到 1d8⁠⁠[雷鸣](Thunder.md "雷鸣") 伤害。

此法术可以在你处于 [沉默](Silenced_(Condition).md "沉默（状态）") 状态时施放。

需要对装备的武器具有 [熟练项](Proficiency.md "熟练项")

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~8

正常武器伤害

\+ 1d8⁠[雷鸣](Thunder.md "雷鸣")（当目标移动时）

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
范围：正常武器范围
充能：每次动作

## 更高等级

在 [角色等级](Character_level.md "角色等级") 5 时，伤害增加至

伤害：3~24

正常武器伤害

\+ 1d8⁠[雷鸣](Thunder.md "雷鸣")

\+ 2d8⁠[雷鸣](Thunder.md "雷鸣")（当目标移动时）

在角色等级 11 时，伤害增加至

伤害：5~40

正常武器伤害

\+ 2d8⁠[雷鸣](Thunder.md "雷鸣")

\+ 3d8⁠[雷鸣](Thunder.md "雷鸣")（当目标移动时）

## 技术细节

UID

`Target_BoomingBlade_ClassSpell`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：轰鸣剑

**[轰鸣剑](Booming_Blade_(Condition).md "轰鸣剑（状态）")**

持续时间：1 驱散

- 受影响实体移动时将受到 1d8⁠⁠[雷鸣](Thunder.md "雷鸣") 伤害。

## 如何学习

职业：

- 职业等级 1：[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师") 和 [邪术师](Warlock.md "邪术师")
- 职业等级 3：[诡术师](Arcane_Trickster.md "诡术师") 和 [奥法骑士](Eldritch_Knight.md "奥法骑士")

种族：

- 角色等级 1：[高精灵](High_Elf.md "高精灵") 和 [半高精灵](High_Half-Elf.md "半高精灵")

（_角色等级_ 是多职业角色所有职业等级的总和。）

由特性授予：

- [魔法学徒：术士](Magic_Initiate_colon__Sorcerer.md "魔法学徒：术士")
- [魔法学徒：邪术师](Magic_Initiate_colon__Warlock.md "魔法学徒：邪术师")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

其他学习方式：

- 没有可供 [法师](Wizard.md "法师") [抄录](Transcribing_scrolls.md "抄录卷轴") 到其法术书中的卷轴。

## 备注

- 由于此戏法使用武器攻击掷骰，它符合 [额外攻击](Extra_Attack.md "额外攻击") 的条件。每当施法者可以进行一次正常近战攻击时，可以改为施放此戏法；尽管它限制为每次动作施放一次。
  - 通过 [哨兵：复仇](Sentinel_colon__Vengeance.md "哨兵：复仇") 被动在已经开始其驱散的角色上获得额外攻击，将允许该角色使用轰鸣剑攻击一次，然后再次使用动作攻击，从而规避每次动作施放一次的限制。
- 与游戏中所有其他戏法不同，轰鸣剑在等级 11 获得最终升级，而不是等级 10。
- 由于其伤害包含武器伤害，此法术允许触发关心法术伤害类型的效果（例如 [投毒者的长袍](Poisoner's_Robe.md "投毒者的长袍")、[悼霜](Mourning_Frost.md "悼霜")）与武器伤害结合。
- 轰鸣剑导致 [奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠") 授予 [奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）")，因为它施加了一个状态。
- 它也通过作为伤害戏法触发 [奥术协同戒指](Ring_of_Arcane_Synergy.md "奥术协同戒指")。

## 错误

- 尽管其描述中未显示，轰鸣剑可以在 [沉默](Silenced_(Condition).md "沉默（状态）") 状态下施放。
- 此戏法未被正确归类为 ⁠[雷鸣](Thunder.md "雷鸣") 法术，因此它不适用于以下效果：
  - [震骨雷鸣](Bone-shaking_Thunder.md "震骨雷鸣")
  - [毁灭狂怒](Destructive_Wrath.md "毁灭狂怒")
  - [元素导师：雷鸣](Elemental_Adept_colon__Thunder.md "元素导师：雷鸣")
  - [风暴之心：雷鸣](Heart_of_the_Storm_colon__Thunder.md "风暴之心：雷鸣")
  - [元素强化项链](Necklace_of_Elemental_Augmentation.md "元素强化项链")
  - [至上真神力量之戒](Ring_of_Absolute_Force.md "至上真神力量之戒")
- [预言：雷鸣掌声](Prophecy_colon__Thunderous_Applause_(Condition).md "预言：雷鸣掌声（状态）")
- 一些其他元素效果的实现方式不同，并且适用于轰鸣剑在等级 5 获得的 ⁠[雷鸣](Thunder.md "雷鸣") 伤害。这些效果包括：
  - [元素亢奋之靴](Boots_of_Elemental_Momentum.md "元素亢奋之靴")
  - [天崩手套](Gloves_of_Belligerent_Skies.md "天崩手套")
  - [风暴之子力量之帽](Hat_of_Storm_Scion's_Power.md "风暴之子力量之帽")
  - [元素注能戒指](Ring_of_Elemental_Infusion.md "元素注能戒指")
    - 由于一个额外的错误，这些物品在荣誉模式下不_起作用，除非武器本身造成元素伤害（例如来自 [元素武器](Elemental_Weapon.md "元素武器") 或任何固有元素伤害加成）。

## 外部链接

⁠[轰鸣剑](https://forgottenrealms.fandom.com/wiki/Booming_blade) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Booming Blade](https://bg3.wiki/wiki/Booming_Blade)*