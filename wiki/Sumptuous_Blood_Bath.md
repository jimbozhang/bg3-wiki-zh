# 血浴盛宴

**血浴盛宴**是仅限[杀戮者](Slayer.md "杀戮者")使用的特殊职业动作。它允许杀戮者撕裂目标，使目标流血并覆盖杀戮者的血液，从而治疗杀戮者。

## 描述

切开敌人的要害动脉。他们开始[流血](Bleeding_(Condition).md "流血（状态）"), 随之而来的喷涌会持续治疗你的伤口。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~20

2d10⁠[挥砍](Slashing.md "挥砍")

治疗：2~12

2d6⁠[治疗](Healing.md "治疗")（对自身）

详情
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）（若豁免成功：目标仍承受一半伤害。）
近战：1.5米（5英尺）

## 更高等级

在10级时，伤害提升至3d10⁠[挥砍](Slashing.md "挥砍")，治疗提升至4d6⁠[治疗](Healing.md "治疗")。

## 技术细节

UID

`Target_BloodBath_Slayer`

基础版本

`Target_BloodBath_Slayer_10`

10级升级版本

法术标志

`[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：流血

**[流血](Bleeding_(Condition).md "流血（状态）")**

持续时间：3回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 生物每回合开始时承受2⁠⁠[挥砍](Slashing.md "挥砍")[DRS](Damage_rider_as_source.md "伤害来源驱动")伤害，并在[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 通过治疗移除。

## 状态：活力血肉

**[活力血肉](Revitalising_Gore_(Condition).md "活力血肉（状态）")**

持续时间：3回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响实体浸透在敌人的血液中。每回合恢复2d6⁠⁠[治疗](Healing.md "治疗")。
- 在10级时，治疗提升至4d6⁠⁠[治疗](Healing.md "治疗")每回合。

## 如何习得

由以下生物使用：[杀戮者](Slayer.md "杀戮者")

## 错误

- 杀戮者动作的[法术豁免DC](Spell_save_DC.md "法术豁免DC")使用你首次获得一级职业的最后一个职业的[施法关键属性](Spells.md#Spellcasting_ability "法术")，但使用杀戮者的属性值。这导致DC非常低，因为杀戮者的精神属性值很低。特别是，战士、游荡者、法师、牧师、德鲁伊、武僧和游侠在杀戮者形态下，智力或感知的施法调整值为+0，而野蛮人、吟游诗人、圣武士、术士和邪术师在杀戮者形态下，魅力的施法调整值为-1。

---
*Source: [Sumptuous Blood Bath](https://bg3.wiki/wiki/Sumptuous_Blood_Bath)*