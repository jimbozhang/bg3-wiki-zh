# 闪现术

**闪现术** 是一个 [法术](Spells.md "法术")。它允许施法者前往虚无形态位面，在返回之前无法被攻击或看见。

## 描述

在你的回合结束时，投掷一个d20。若结果为11或更高，你将消失进入虚无形态位面。在此期间，你在这个世界中无法被伤害或看见。

当你消失时，你在此处的存在代表了你将返回的位置。你可以选择将其传送至最多6米（20尺）外。

仅在战斗中可用。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
范围：自身

## 高阶施法

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Shout_Blink`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：闪现术

**[闪现术](Blink_(Condition).md "闪现术 (状态)")**

持续时间：10驱散

- 在每个回合结束时，受影响实体有几率[闪现至虚无形态位面](Blinked_to_the_Ethereal_Plane_(Condition).md "闪现至虚无形态位面 (状态)")，在那里它无法被伤害、看见或影响。

- 在虚无形态位面期间，实体无法移动或与世界中的任何事物互动。它只能选择传送至最多6米（20尺）外。当战斗结束时，此效果也会结束。

## 状态：闪现至虚无形态位面

**[闪现至虚无形态位面](Blinked_to_the_Ethereal_Plane_(Condition).md "闪现至虚无形态位面 (状态)")**

持续时间：直至战斗结束

- 受影响实体位于虚无形态位面，在那里它无法被伤害、看见或影响。
- 在虚无形态位面期间，实体无法移动或与世界中的任何事物互动。它可以选择传送至最多6米（20尺）外。
- 在每个回合结束时，它有几率重新出现在物质位面。当战斗结束时，此效果也会结束。
- 免疫[流血](Bleeding_(Condition).md "流血 (状态)")。

## 学习方式

职业：

- 职业等级5：[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[至高妖精](The_Archfey.md "至高妖精") 和 [脆弱诅咒](The_Hexblade.md "脆弱诅咒")

由物品提供：

- [闪烁之戒](Ring_of_Blink.md "闪烁之戒")（充能：[长休](Long_Rest.md "长休")）

其他学习方式：

- 拥有[3级法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[闪现术卷轴](Scroll_of_Blink.md "闪现术卷轴")至其法术书。

## 错误

- 尽管有意忽略会打断[专注](Concentration.md "专注")的函数器，但状态组错误仍会在消失时打断专注。
- 当消失进入虚无形态位面时，装备的物品会暂时失效。这会导致包含 `OnRemoveFunctors` 的物品技术状态（例如[玛科赫什基](Markoheshkir.md "玛科赫什基")使用的状态）触发，移除这些物品提供的任何效果。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Blink_Visuals.mp4>

## 外部链接

- ⁠[闪现术](https://forgottenrealms.fandom.com/wiki/Blink) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Blink](https://bg3.wiki/wiki/Blink)*