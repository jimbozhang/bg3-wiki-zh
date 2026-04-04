# 操纵死尸

**操纵死尸**是一个[3级死灵学派法术](Spells.md "法术")。它允许施法者操纵一具尸体，创造一个[不死生物](Undead.md "不死生物")仆从。

## 描述

在非战斗状态下操纵一具尸体，创造一个不死生物仆从。

目标必须是一具中型或小型尸体。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
射程：3米（10英尺）

## 更高法术位效果

- 当以4级法术位施放此法术时，可以唤起最多3个[骷髅](Animate_Dead_colon__Skeleton_Squad.md "操纵死尸：骷髅小队")或[僵尸](Animate_Dead_colon__Zombie_Battalion.md "操纵死尸：僵尸大军")，而非1个。
- 当以5级法术位施放此法术时，可以唤起一个[食尸鬼](Animate_Dead_colon__Ghoul.md "操纵死尸：食尸鬼")或[飞行食尸鬼](Animate_Dead_colon__Flying_Ghoul.md "操纵死尸：飞行食尸鬼")。
- 当以6级法术位施放此法术时，可以唤起最多3个[食尸鬼](Animate_Dead_colon__Ghoul_Pack.md "操纵死尸：食尸鬼群")或[飞行食尸鬼](Animate_Dead_colon__Flying_Ghoul_Flock.md "操纵死尸：飞行食尸鬼群")，而非1个。

## 技术细节

UID

`Target_AnimateDead`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 变体

- [操纵死尸：骷髅](Animate_Dead_colon__Skeleton.md "操纵死尸：骷髅")
- [操纵死尸：僵尸](Animate_Dead_colon__Zombie.md "操纵死尸：僵尸")
- [操纵死尸：骷髅小队](Animate_Dead_colon__Skeleton_Squad.md "操纵死尸：骷髅小队")
- [操纵死尸：僵尸大军](Animate_Dead_colon__Zombie_Battalion.md "操纵死尸：僵尸大军")
- [操纵死尸：食尸鬼](Animate_Dead_colon__Ghoul.md "操纵死尸：食尸鬼")
- [操纵死尸：飞行食尸鬼](Animate_Dead_colon__Flying_Ghoul.md "操纵死尸：飞行食尸鬼")
- [操纵死尸：食尸鬼群](Animate_Dead_colon__Ghoul_Pack.md "操纵死尸：食尸鬼群")
- [操纵死尸：飞行食尸鬼群](Animate_Dead_colon__Flying_Ghoul_Flock.md "操纵死尸：飞行食尸鬼群")

## 学习方式

职业：

- 职业等级5：[牧师](Cleric.md "牧师")、[法师](Wizard.md "法师")、[孢子结社](Circle_of_the_Spores.md "孢子结社")（结社法术）、[邪术师](Warlock.md "邪术师")（通过[书之魔契](Pact_of_the_Tome.md "书之魔契")，长休一次）和[死亡领域](Death_Domain.md "死亡领域")（领域法术）
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）和[死灵法师](Necromancer.md "死灵法师")（通过[死灵学派](Necromancy_School.md "死灵学派")）
- 职业等级9：[弃誓者](Oathbreaker.md "弃誓者")（誓言法术）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

其他学习方式：

- 拥有[3级法术位](Spells.md#Spell_slots "法术")的[法师](Wizard.md "法师")可以将[操纵死尸卷轴](Scroll_of_Animate_Dead.md "操纵死尸卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 每个施法者一次只能拥有此法术的一个激活实例，无论使用哪个版本。当不死生物召唤物已存在时再次施放，会驱散前一个召唤物。
- 拥有死灵学派副职的法师可以为法术的每个等级和版本额外唤起一个不死生物。
- 这些召唤的不死生物都没有近战武器，因此不受弃誓者圣武士的[仇恨灵光](Aura_of_Hate.md "仇恨灵光")影响。
- 术士可以对卷轴施放的操纵死尸应用[成双法术](Metamagic_colon__Twinned_Spell.md "超魔：成双法术")，但只会唤起一个生物；另一个会立即被摧毁，如同施法者施放了两个实例，此过程会浪费[术法点](Sorcery_Point.md "术法点")。
- 如果施法者取消准备此法术，召唤的不死生物将保留。

## 视觉效果

<https://bg3.wiki/wiki/File:Animate_Dead_Visuals.mp4>

## 外部链接

- ⁠[操纵死尸](https://forgottenrealms.fandom.com/wiki/Animate_dead) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Animate Dead](https://bg3.wiki/wiki/Animate_Dead)*