# 昼明术：附魔物品

**昼明术：附魔物品** 是一个 [3级塑能学派法术](Spells.md "Spells")。此法术是 [昼明术](Daylight.md "昼明术") 的一个变体。此变体允许施法者附魔一件物品，使其像太阳一样发光。

## 描述

附魔一件物品或武器，使其散发太阳般的光芒，并驱散周围所有黑暗。目标必须在主手中持有一件武器。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术位")
详情
射程：18米（60英尺）
范围：15米（50英尺）半径

## 高等施法

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_Daylight_Enchantment`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：昼明术

**[昼明术](Daylight_(Condition).md "昼明术 (状态)")**

持续时间：20驱散

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "骰子检定"))

- 散发太阳般的光芒。在15米（50英尺）半径内驱散 [黑暗术](Darkness_(cloud).md "黑暗术 (云)")。
- 此法术的附魔物品版本要求目标生物主手中持有一件 [武器](Weapons.md "武器")。

## 如何习得

此法术是以下法术的变体：
[昼明术](Daylight.md "昼明术")

## 备注

- 范围内的黑暗云仅在法术初始施放于目标时被驱散。
- 将 [轻语树花](Sussur_Bloom.md "轻语树花") 暴露于此法术的光芒下，在 [幽暗地域](Underdark.md "幽暗地域") 中不会导致其枯萎。

## 错误

- 尽管游戏内此法术和 [法术容器](Daylight.md "昼明术") 的描述均列出了此变体的20驱散限制，但如果应用于角色，效果将应用于其手持的主手武器，直到 [长休](Long_Rest.md "长休")，并且即使施法者不再处于活跃队伍中，效果也会持续。
- 尽管将 [灰矮人](Duergar.md "灰矮人")、[卓尔](Drow.md "卓尔") 和其他NPC暴露于此法术范围内的光芒会触发 [日照敏感](Sunlight_Sensitivity.md "日照敏感")，但不会向玩家显示任何状态效果（例如，作为被动或状态在其角色表上，如果检查），但可以检查战斗日志以查看 [劣势](Disadvantage.md "劣势") 应用的效果。
- 由于编码错误，此法术无法施放于非盟友生物，否则将要求他们进行一次 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")，DC等于施法者的 [法术豁免DC](Spell_save_DC.md "法术豁免DC") 以避免效果。

## 图库

- 未使用图像

- 工具提示图像

- 控制器UI图标

- 图标

## 外部链接

- ⁠[昼明术](https://forgottenrealms.fandom.com/wiki/Daylight) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Daylight: Enchant Item](https://bg3.wiki/wiki/Daylight:_Enchant_Item)*