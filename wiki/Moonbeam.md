# 月华之光

**月华之光**是一个[法术](Spells.md "法术")。它允许施法者召唤一道月光光束，对任何进入光束或在其内开始其回合的生物造成光耀伤害。

## 描述

召唤一道光束，对任何进入光束或在其内开始其回合的生物造成伤害。你可以使用一个[动作](Action.md "动作")将光束移动18米（60英尺）。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
伤害：2~20

2d10⁠[光耀](Radiant.md "光耀")（每回合）

详情
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：目标仍承受一半伤害。）
范围：18米（60英尺）
范围效果：1米（3英尺）半径
创造区域：月华之光
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：当法术以3环或更高环级施放时，每比2环高1环，伤害增加1d10⁠⁠[光耀](Radiant.md "光耀")。

## 技术细节

UID

`Target_Moonbeam`

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell_flag\) \(页面不存在\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 赋予

- [移动月华之光](Move_Moonbeam.md "移动月华之光")

## 区域：月华之光

**[月华之光](Moonbeam_(area).md "月华之光 (区域)")**

持续时间：10回合

范围效果：1米（3英尺）半径

类型：[召唤](Area.md#Summoned "区域")

### 状态：月华之光（光环）

**\_(状态)[月华之光](Moonbeam_(Aura)_(Condition).md "月华之光 (光环) (状态)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 幽灵般的火焰吞噬任何进入这银色光芒或在其内开始其回合的生物。它们造成2d10⁠⁠[光耀](Radiant.md "光耀")。豁免成功时，目标仍承受一半伤害。

## 如何习得

职业：

- 职业等级3：[德鲁伊](Druid.md "德鲁伊")
- 职业等级5：[古贤之誓](Oath_of_the_Ancients.md "古贤之誓")（誓言法术）

由物品赋予：

- [塞伦涅的暗夜短矛](Sel%C3%BBne's_Spear_of_Night.md "塞伦涅的暗夜短矛")（充能：[长休](Long_Rest.md "长休")）

其他习得方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书的卷轴。

## 注释

- 月华之光被视为一个召唤实体，与施法者分离。这有以下影响：
  - 施放月华之光或[移动月华之光](Move_Moonbeam.md "移动月华之光")不会打破[庇护术](Sanctuary.md "庇护术")，即使成功造成伤害。
  - [光耀报复](Radiant_Retort.md "光耀报复")以光束本身为目标，使施法者免受伤害；由于月华之光实际上没有生命值，它也不会受到伤害。
- 自补丁6起，在[幽影诅咒之地](Shadow-Cursed_Lands.md "幽影诅咒之地")的枯萎区域施放月华之光会导致施法者失去对该法术的[专注](Concentration.md "专注")并使其消散，但仍会造成伤害。
- [移动月华之光](Move_Moonbeam.md "移动月华之光")是一个“赋予”法术。*赋予*法术在施放原始法术后授予施法者，并且只要[专注](Concentration.md "专注")未被打破，就可以[重施](Category_colon_Recastable_spells.md "类别：可重施法术")而无需消耗另一个法术位。像这样的赋予法术与施法者的已知法术列表（即游戏中的法术书图标）没有直接关联。因此，如果在身兼多职时施放赋予法术，后续的重施（在本例中为[移动月华之光](Move_Moonbeam.md "移动月华之光")）将使用最近获得的施法职业的施法调整值，而不是初始施放月华之光时使用的施法调整值。在这种情况下，可能会导致法术豁免DC意外地低。
- 月华之光的咒语是 **Ex Textura**，拉丁语，意为“来自织网”。

## 错误

- 尽管是塑能学派法术，月华之光不与[法术塑形](Sculpt_Spells.md "法术塑形")互动。

## 外部链接

- ⁠[月华之光](https://forgottenrealms.fandom.com/wiki/Moonbeam) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Moonbeam](https://bg3.wiki/wiki/Moonbeam)*