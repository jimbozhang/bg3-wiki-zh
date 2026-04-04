# 高等隐形术

**高等隐形术** 是一个 [法术](Spells.md "法术")。它允许施法者为盟友提供更持久的[隐形](Invisibility_(spell).md "隐形")形态。

## 描述

使一个生物隐形。攻击它的攻击掷骰具有[劣势](Disadvantage.md "劣势")。它进行的攻击掷骰具有[优势](Advantage.md "优势")。

当在攻击、施法或与物品互动时，进行越来越难的[隐匿](Stealth.md "隐匿")[属性检定](Ability_Check.md "属性检定")失败时，隐形状态会解除。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")
详情
射程：1.5米（5英尺）
[专注](Concentration.md "专注")

## 更高环阶施法

以更高环阶施法此法术不会获得额外收益。

## 技术细节

UID

`Target_Invisibility_Greater`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：高等隐形术

**[高等隐形术](Greater_Invisibility_(Condition).md "高等隐形术 (状态)")**

持续时间：10驱散

- 实体在[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[优势](Advantage.md "优势")。针对它的攻击掷骰具有[劣势](Disadvantage.md "劣势")
- 当与物品互动、施法或攻击时，实体需要成功通过一次[隐匿](Stealth.md "隐匿")[属性检定](Ability_Check.md "属性检定")以维持隐形。每次成功尝试后，检定难度会增加。

## 如何习得

职业：

- 职业等级7：[吟游诗人](Bard.md "吟游诗人")、[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[大地结社](Circle_of_the_Land.md "大地结社")（幽暗地域）、[至高妖精](The_Archfey.md "至高妖精")和[脆弱诅咒](The_Hexblade.md "脆弱诅咒")

其他习得方式：

- 拥有[4级法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[高等隐形术卷轴](Scroll_of_Greater_Invisibility.md "高等隐形术卷轴")到他们的法术书中。

## 备注

- 此法术的[隐匿](Stealth.md "隐匿")检定[难度等级](Difficulty_Class.md "难度等级")起始为15，并随着成功次数增加而增加，具体缩放比例由难度决定：
  - 在[荣誉](Honour.md "荣誉")模式之外，DC线性缩放：DC=15+（先前成功隐匿检定的次数）
  - 在荣誉模式下，DC二次方缩放：DC=15+（先前成功隐匿检定的次数）2
- 具有`[Invisible](Invisible_(spell_flag).md)`标志的动作可以无需进行此隐匿检定即可执行。它们也不会增加后续动作的隐匿检定DC。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Greater_Invisibility_Visuals.mp4>

## 外部链接

- ⁠[高等隐形术](https://forgottenrealms.fandom.com/wiki/Greater_invisibility) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Greater Invisibility](https://bg3.wiki/wiki/Greater_Invisibility)*