# 法术反制

**法术反制**是一个[法术](Spells.md "法术")。它允许施法者打断另一位施法者的施法，使其失败且没有任何效果。

## 描述

尝试阻止一个正在施放的法术。

如果该法术的环级高于你用于[法术反制](Counterspell.md "法术反制")的法术位环级，你必须使用你的[属性检定](Ability_Check.md "属性检定")进行一次[检定](#notes)来阻止它。检定的难度等于10加上你试图反制的法术环级。

此法术可以在你处于[沉默](Silenced_(Condition).md "沉默（状态）")状态时施放。

## 属性

消耗
[反应](Actions.md#Reactions "动作") + [3环法术位](Spells.md#Spell_slots "法术")

## 升环施法

法术反制可以升环施法，以反制更高环级的法术，而无需进行检定。

## 学习方式

职业：

- 职业等级5：[术士](Sorcerer.md "术士")、[邪术师](Warlock.md "邪术师")和[法师](Wizard.md "法师")
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

物品授予：

- [干扰法杖](Staff_of_Interruption.md "干扰法杖")（充能：[长休](Long_Rest.md "长休")）

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书中的卷轴。

## 备注

- 当尝试反制一个更高环级的法术时，使用[法术反制](Counterspell.md "法术反制")施法者的[智力](Intelligence.md "智力")调整值，而不是其施法关键属性调整值。<sup>[\[1\]](#cite_note-1)</sup>
- 即使[法术反制](Counterspell.md "法术反制")失败，也会为[防护学派](Abjuration_School.md "防护学派")法师的[奥术守御](Arcane_Ward.md "奥术守御")提供能量。
- 当卷轴被成功反制时，卷轴不会被吞噬。
- 戏法也可以被反制。

## 错误

- 无论使用什么环级的法术，[奥术守御](Arcane_Ward.md "奥术守御")最多只能被提供3点冲锋，这是由于基于成功/失败会施放一个额外的隐藏[法术反制](Counterspell.md "法术反制")。

## 外部链接

- ⁠[法术反制](https://forgottenrealms.fandom.com/wiki/Counterspell) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

## 参考资料

1. [↑](#cite_ref-1) 源自 `Mods/Shared/Scripts/thoth/helpers/CommonConditions.khn` 中 `TryCounterspellHigherLevel(level)` 的定义：显示代码

function TryCounterspellHigherLevel(level)
local spellPowerLevel = SpellPowerLevelEqualOrLessThan(level)
if not spellPowerLevel.Result then
local counterspellDC = 10 + context.HitDescription.SpellPowerLevel
local st = AbilityCheck(Ability.Intelligence, counterspellDC, false, false, 0, context.Observer, context.Observer)
return ConditionResult(st.Result,{},{},st.Chance)
end
return ConditionResult(true,{},{},1.0)
end

---
*Source: [Counterspell](https://bg3.wiki/wiki/Counterspell)*