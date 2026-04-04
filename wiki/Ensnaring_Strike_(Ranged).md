# 诱捕攻击（远程）

关于此法术的近战版本，请参见 [诱捕打击（近战）](Ensnaring_Strike_(Melee).md "诱捕打击（近战）").

**诱捕攻击（远程）** 是一个 [1级咒法学派法术](Spells.md "法术"). 它允许施法者使用远程武器攻击，用荆棘藤蔓诱捕敌人，并每回合对其造成穿刺伤害。

## 描述

你的攻击会召唤荆棘藤蔓，可能使目标陷入 \_(状态)[诱捕](Ensnared_(Ensnaring_Strike)_(Condition).md "诱捕（诱捕攻击）（状态）") 状态。

被诱捕的生物无法移动，并在每回合开始时受到 1d6⁠⁠[穿刺](Piercing.md "穿刺") 伤害。盟友可以使用其 [协助](Help.md "协助") 动作尝试撕开藤蔓。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中后消耗
[附赠动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：1~6

正常武器伤害

\+ 1d6⁠[穿刺](Piercing.md "穿刺")（每回合）

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
范围：18米（60英尺）
[专注](Concentration.md "专注")

## 升环施法

[升环施法](Upcasting.md "升环施法")：\_(状态)[诱捕](Ensnared_(Ensnaring_Strike)_(Condition).md "诱捕（诱捕攻击）（状态）") 状态每升一级额外造成 1d6⁠⁠[穿刺](Piercing.md "穿刺") 伤害。

## 技术细节

UID

`Projectile_EnsnaringStrike`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：诱捕（诱捕攻击）

**\_(状态)[诱捕](Ensnared_(Ensnaring_Strike)_(Condition).md "诱捕（诱捕攻击）（状态）")**

持续时间：10回合

- 无法移动，每回合受到 1d6⁠⁠[穿刺](Piercing.md "穿刺") 伤害。
- 对该生物的 [攻击掷骰](Attack_roll.md "攻击掷骰") 具有 [优势](Advantage.md "优势")，而该生物的攻击掷骰和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 具有 [劣势](Disadvantage.md "劣势")。
- 当被 [协助](Help.md "协助") 时移除。

## 如何习得

此法术是以下法术的变体：
[诱捕攻击](Ensnaring_Strike.md "诱捕攻击")

## 备注

- 此法术与游侠的 [宿敌](Favoured_Enemy.md "宿敌") 被动 [赏金猎人](Bounty_Hunter.md "赏金猎人") 搭配良好。

## 错误

- 当升环至4级时，诱捕攻击（远程）错误地在使用时消耗 [动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")，并在命中时消耗 [附赠动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")。

## 外部链接

- ⁠[诱捕攻击](https://forgottenrealms.fandom.com/wiki/Ensnaring_strike) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Ensnaring Strike (Ranged)](https://bg3.wiki/wiki/Ensnaring_Strike_(Ranged)*