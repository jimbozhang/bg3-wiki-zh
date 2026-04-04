# 印记斩

**印记斩**是一个[法术](Spells.md "法术")。它允许施法者让武器闪耀星界光耀，从而用光标记目标，阻止其变为[隐形](Invisible_(Condition).md "隐形（状态）")。

## 描述

你的武器在攻击时闪耀星界光耀，可能用光标记你的目标，阻止其变为[隐形](Invisible_(Condition).md "隐形（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中时消耗
[附赠动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
伤害：2~12

正常武器伤害

\+ 2d6⁠[光耀](Radiant.md "光耀")

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：正常武器射程
[专注](Concentration.md "专注")

## 更高环阶

每环阶额外造成1d6⁠⁠[光耀](Radiant.md "光耀")伤害。

## 技术细节

UID

`Target_Smite_Branding_Container`

法术标志

`[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 变体

- [印记斩（近战）](Branding_Smite_(Melee).md "印记斩（近战）")
- [印记斩（远程）](Branding_Smite_(Ranged).md "印记斩（远程）")

## 状态：印记斩

**[印记斩](Branding_Smite_(Condition).md "印记斩（状态）")**

持续时间：10 驱散

- 无法变为[隐形](Condition.md#Invisible "状态")。

## 学习方式

职业：

- 职业等级3：[魔契刃](The_Hexblade.md "魔契刃")
- 职业等级5：[圣武士](Paladin.md "圣武士")

种族：

- 角色等级5：[扎瑞尔的提夫林](Zariel_Tiefling.md "扎瑞尔的提夫林")

（_角色等级_ 是多职业角色所有职业等级的总和。）

## 备注

- 参见[至圣斩](Smite.md "至圣斩")获取更多功能信息。
- 与大多数其他至圣斩类法术不同，此法术可与远程武器配合使用。
- 扎瑞尔[提夫林](Tiefling.md "提夫林")获得的此法术种族版本只能每[长休](Long_Rest.md "长休")施放一次。
- 此法术与[印记斩（近战）](Branding_Smite_(Melee).md "印记斩（近战）")的不同之处在于，它有一个小半径1米（3英尺）的区域，可用于以地面为目标，仍能造成伤害并对单个目标施加[印记斩](Branding_Smite_(Condition).md "印记斩（状态）")，该目标可能是[隐形](Invisible_(Condition).md "隐形（状态）")因而无法直接瞄准。

## 错误

- 使用[4级法术位](Spells.md#Spell_slots "法术")施放印记斩时，工具提示伤害错误地列出了该法术的[2级法术位](Spells.md#Spell_slots "法术")。
- 印记斩的法术容器未正确显示邪术师的当前法术位等级。
- 此法术缺乏针对物品的瞄准限制，由于半径小且目标限制为1，可能瞄准生物但将[印记斩](Branding_Smite_(Condition).md "印记斩（状态）")施加到半径内的物品上。

## 外部链接

- ⁠[Branding smite](https://forgottenrealms.fandom.com/wiki/Branding_smite) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Branding Smite](https://bg3.wiki/wiki/Branding_Smite)*