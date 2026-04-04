# 鸣响丧钟

**鸣响丧钟**是一个[法术](Spells.md "法术")。它造成[黯蚀](Necrotic.md "黯蚀")伤害，并且如果目标已经受伤，伤害会增加。_\[[参见：错误](#bugs)\]_

## 描述

敲响预示厄运的丧钟。如果目标生命值全满，你将改为造成 1d8[黯蚀](Necrotic.md "黯蚀")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：1~12

1d12[黯蚀](Necrotic.md "黯蚀")（如果目标生命值全满，则为 1d8[黯蚀](Necrotic.md "黯蚀")）

详情
[WIS](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（豁免成功：伤害被抵消）
射程：18 米（60 英尺）

## 升级效果

- 在[角色等级](Character_level.md "角色等级") 5 时，伤害增加至 2d12[黯蚀](Necrotic.md "黯蚀")（如果未受伤，则为 2d8[黯蚀](Necrotic.md "黯蚀")）。
- 在角色等级 10 时，伤害增加至 3d12[黯蚀](Necrotic.md "黯蚀")（如果未受伤，则为 3d8[黯蚀](Necrotic.md "黯蚀")）。

## 技术细节

UID

`Target_TollTheDead`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 学习方式

职业：

- 职业等级 1：[牧师](Cleric.md "牧师")、[邪术师](Warlock.md "邪术师")、[法师](Wizard.md "法师")和[死亡领域](Death_Domain.md "死亡领域")（领域法术）
- 职业等级 3：[奥法骑士](Eldritch_Knight.md "奥法骑士")和[诡术师](Arcane_Trickster.md "诡术师")

种族：

- 角色等级 1：[高精灵](High_Elf.md "高精灵")和[半高精灵](High_Half-Elf.md "半高精灵")

（_角色等级_ 是多职业角色所有职业等级的总和。）

由特性授予：

- [魔法学徒：牧师](Magic_Initiate_colon__Cleric.md "魔法学徒：牧师")
- [魔法学徒：邪术师](Magic_Initiate_colon__Warlock.md "魔法学徒：邪术师")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到法术书中的卷轴。

## 注释

- 鸣响丧钟的咒语是 **Mortalis** ，拉丁语意为 _“凡人”_。

## 错误

- 该戏法关于伤害的功能描述可能具有误导性。该法术的代码测试目标的生命值是否小于或等于 _99%_ ，而不是 _100%_ 。因此，对于拥有大量生命值的目标，如果对手仅仅是轻微受伤，鸣响丧钟可能仍然只造成 d8 伤害（不会增加到 d12）。

## 外部链接

- [鸣响丧钟](https://forgottenrealms.fandom.com/wiki/Toll_the_dead) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Toll the Dead](https://bg3.wiki/wiki/Toll_the_Dead)*