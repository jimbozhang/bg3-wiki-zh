# 隐形（法术）

另见：[隐形（消歧义）](Invisibility_(disambiguation).md)

**隐形**是一个[2级幻术学派法术](Spells.md "Spells")。它允许施法者让自己和其他生物对肉眼[隐形](Invisible_(Condition).md "Invisible (Condition)")。

## 描述

触摸一个生物使其[隐形](Invisible_(Condition).md "Invisible (Condition)")。攻击它的攻击掷骰具有[劣势](Disadvantage.md "Disadvantage")。它的攻击具有[优势](Advantage.md "Advantage")。

[隐形](Invisible_(Condition).md) 如果隐形实体攻击、施放另一个法术、与物体互动、采取动作或附赠动作，或受到伤害，则会提前结束。_\[[参见注释](#notes)\]_

如果生物攻击或施法，状态会提前结束。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [2级法术位](Spells.md#Spell_slots "Spells")
细节
近战：1.5米（5英尺）
[专注](Concentration.md "Concentration")

## 升环施法

[升环施法](Upcasting.md "Upcasting")：每比2级法术位高一级，影响一个额外目标。

## 技术细节

UID

`Target_Invisibility`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[UnavailableInDialogs](https://bg3.wiki/w/index.php?title=UnavailableInDialogs_\(spell_flag\)&action=edit&redlink=1) "UnavailableInDialogs \(spell flag\) \(page does not exist\)")`

## 状态：隐形

**[隐形](Invisible_(Condition).md "Invisible (Condition)")**

持续时间：10回合

- 在[攻击掷骰](Attack_roll.md "Attack Roll")上具有[优势](Advantage.md "Advantage")，并对敌人的攻击掷骰施加[劣势](Disadvantage.md "Disadvantage")。

如果隐形实体攻击、施放另一个法术、与物体互动、变得[濡湿](Wet_(Condition).md "Wet (Condition)")、采取动作或附赠动作，或受到伤害，隐形会提前结束。

## 如何习得

职业：

- 职业等级3：[吟游诗人](Bard.md "Bard")、[术士](Sorcerer.md "Sorcerer")、[邪术师](Warlock.md "Warlock")、[法师](Wizard.md "Wizard")，以及[大地结社](Circle_of_the_Land.md "Circle of the Land")（草原）
- 职业等级7：[诡术师](Arcane_Trickster.md "Arcane Trickster")
- 职业等级8：[奥法骑士](Eldritch_Knight.md "Eldritch Knight")

物品授予：

- [移形换影之戒指](Shifting_Corpus_Ring.md "Shifting Corpus Ring")（充能：[长休](Long_Rest.md "Long rest")）
- [卡勒杜兰·滑手的物像](Fetish_of_Callarduran_Smoothhands.md "Fetish of Callarduran Smoothhands")（充能：[长休](Long_Rest.md "Long rest")）

## 注释

- 具有`[Invisible](Invisible_(spell_flag).md)`法术标志的动作可以安全执行而不破坏隐形。这些包括：
  - 许多移动动作，如[疾走](Dash.md "Dash")和[跳跃](Jump.md "Jump")。
  - 使用某些物品，包括药水。
  - 打开大多数容器而不添加或移除任何东西。
  - 施放某些法术，如[初级幻影](Minor_Illusion.md "Minor Illusion")。
- 变得[濡湿](Wet_(Condition).md "Wet (Condition)")会破坏隐形。
- [灰矮人](Duergar.md "Duergar")在角色等级5时获得此法术的[戏法](Invisibility_(Duergar)版本.md)。
- 隐形有两种咒语：**Evanesco**（拉丁语，意为“我消失/消逝”）和**Invisiblis**（拉丁语，意为“隐形”）。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Invisibility_Visuals.mp4>

## 外部链接

⁠[隐形](https://forgottenrealms.fandom.com/wiki/Invisibility) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Invisibility (spell)](https://bg3.wiki/wiki/Invisibility_(spell)*