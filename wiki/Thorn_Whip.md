# 荆棘之鞭

**荆棘之鞭** 是一个 [法术](Spells.md "法术")。它对目标造成伤害并将其拉向施法者。

## 描述

将生物拉近 3 米 (10 英尺)。

如果目标体型为 [巨型](Creature_size.md "生物体型")，则无法拉动。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害: 1~6

1d6⁠[穿刺](Piercing.md "穿刺")

详情
近战法术 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程: 9 米 (30 英尺)
拉动: 3 米 (10 英尺)

## 升环效应

- 在 [角色等级](Character_level.md "角色等级") 5 时，伤害增加至 2d6⁠⁠[穿刺](Piercing.md "穿刺")。
- 在角色等级 10 时，伤害增加至 3d6⁠⁠[穿刺](Piercing.md "穿刺")。

## 技术细节

UID

`Target_ThornWhip`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 学习方式

职业:

- 职业等级 1: [德鲁伊](Druid.md "德鲁伊") 和 [自然领域](Nature_Domain.md "自然领域") (领域法术)
- 职业等级 3: [邪术师](Warlock.md "邪术师") (通过 [书之魔契](Pact_of_the_Tome.md "书之魔契"))

由特性授予:

- [魔法学徒：德鲁伊](Magic_Initiate_colon__Druid.md "魔法学徒：德鲁伊")
- [法术狙击](Spell_Sniper.md "法术狙击")

生物使用: [哈弗·威洛比 (自然的复仇)](Harvard_Willoughby_(Nature's_Vengeance).md)

其他学习方式:

- 没有可供 [法师](Wizard.md "法师") [抄录](Transcribing_scrolls.md "抄录卷轴") 到其法术书中的卷轴。

## 备注

- 尽管射程为 9 米 (30 英尺)，但此戏法实际上使用近战法术攻击掷骰。这意味着施法者在近距离攻击时不会遭受 [劣势](Disadvantage.md "劣势")。它也可以触发反应和被动，这些被动在近战攻击时激活，例如 [盾牌猛击](Shield_Blow.md "盾牌猛击")。
- 荆棘之鞭的咒语是 **Fragilo**，拉丁语意为 _“易碎”_ 或 _“脆弱”_。

## 错误

- 此法术缺少 `[IsHarmful](IsHarmful_(spell_flag).md)` [法术标志](Spell_flags.md "法术标志")，因此能够以受 [庇护术](Sanctuary_(Condition).md "庇护术 (状态)") 影响的生物为目标。

## 外部链接

- ⁠[荆棘之鞭](https://forgottenrealms.fandom.com/wiki/Thorn_whip) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Thorn Whip](https://bg3.wiki/wiki/Thorn_Whip)*