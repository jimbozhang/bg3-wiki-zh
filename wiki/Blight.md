# 枯萎术

关于植物类生物的种族，请参见 [枯萎术（种族）](Blight_(race)..md)

**枯萎术** 是一个 [4环死灵学派法术](Spells.md "Spells")。它允许施法者使用死灵能量吸取目标生物的水分和活力。它对植物尤其有效。

## 描述

对目标造成 8d8⁠⁠[黯蚀](Necrotic.md "Necrotic") 伤害。植物受到此法术的伤害为最大值，并且在对抗它的 [豁免检定](Saving_throw.md "Saving Throw") 上具有 [劣势](Disadvantage.md "Disadvantage")。

对不死生物和构装生物无效。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [4环法术位](Spells.md#Spell_slots "Spells")
伤害：8~64

8d8⁠[黯蚀](Necrotic.md "Necrotic")（对植物为 64⁠[黯蚀](Necrotic.md "Necrotic")）

详情
[体质](Constitution.md "Constitution") [豁免](Saving_throws.md "Saving throws")（[法术豁免 DC](Dice_rolls.md#Spell_save_DC "Dice rolls")）（豁免成功：目标仍承受一半伤害。）
射程：9米（30英尺）

## 升环施法

[升环施法](Upcasting.md "Upcasting")：以更高环位施放此法术时，每比4环高一环，额外造成 1d8⁠⁠[黯蚀](Necrotic.md "Necrotic") 伤害。

## 技术细节

UID

`Target_Blight`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 学习方式

职业：

- 职业等级 7：[德鲁伊](Druid.md "Druid")、[术士](Sorcerer.md "Sorcerer")、[邪术师](Warlock.md "Warlock")、[法师](Wizard.md "Wizard")、[孢子结社](Circle_of_the_Spores.md "Circle of the Spores")（结社法术）和 [死亡领域](Death_Domain.md "Death Domain")（领域法术）
- 职业等级 10：[吟游诗人](Bard.md "Bard")（通过 [魔法秘密](Magical_Secrets.md "Magical Secrets")）

由物品提供：

- [悲伤](Woe.md "Woe")（充能：[长休](Long_Rest.md "Long rest")）

其他学习方式：

- 拥有 [4环法术位](Spells.md#Spell_slots "Spells") 的 [法师](Wizard.md "Wizard") 可以 [抄录](Transcribing_scrolls.md "Transcribing scrolls") [枯萎术卷轴](Scroll_of_Blight.md "Scroll of Blight") 到他们的法术书中。

## 注释

- 游戏中 [植物](Plant.md "Plant") 非常少。当获得此法术时，队伍很可能处于 [第二幕](Act_Two.md "Act Two")，那里的所有植物都对黯蚀伤害有 [抗性](Resistances.md "Resistances")，降低了可能的最大伤害。然而，在等级 6 时，[死亡领域](Death_Domain.md "Death Domain") 牧师的 [无法逃避的毁灭](Inescapable_Destruction.md "Inescapable Destruction") 允许此法术无视抗性。
  - 即使第二幕的植物有黯蚀伤害抗性，枯萎术在数学上仍然是伤害这些植物最有效的方法之一。
- 枯萎术的咒语是 **Perē**，拉丁语命令 _“消失/被摧毁！”_
- [德尔韦登](Delverdenn.md "Delverdenn")、[莱姆利奇](Limeleech.md "Limeleech") 和 [维康妮亚·迪佛](Viconia_DeVir.md "Viconia DeVir") 可以使用此法术的一个独特 5环变体，该变体可以以 [构装生物](Construct.md "Construct") 和 [不死生物](Undead.md "Undead") 为目标。

## 错误

- 此法术缺少 `[IsHarmful](IsHarmful_(spell_flag).md)` [法术标志](Spell_flags.md "Spell flags")，因此能够以受 [庇护术](Sanctuary_(Condition).md "Sanctuary (Condition)") 影响的生物为目标。
- 当以4环法术位施放于非植物敌人且豁免失败时，枯萎术会错误地造成非魔法伤害。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Blight_Visuals.mp4>

## 外部链接

- > )⁠[枯萎术（法术）](https://forgottenrealms.fandom.com/wiki/Blight_(spell)) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Blight](https://bg3.wiki/wiki/Blight)*