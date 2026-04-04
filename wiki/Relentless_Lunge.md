# 无情猛扑

**无情猛扑**是仅限[杀戮者](Slayer.md "杀戮者")使用的特殊职业动作。它允许杀戮者跃过空中，在落地时碾压其敌人。

## 描述

蜿蜒跃起并猛撞向你的敌人，有可能将其击至[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + 3米（10英尺）[移动速度](Resources.md#Movement_speed "资源")
伤害：2~12 + 调整值

2d6 + [力量调整值](Strength.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击")

详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
范围：[跳跃](Jump.md "跳跃")范围
范围效果：5米（17英尺）半径
充能：每回合

## 更高等级

在10级时，伤害变为4d6 + [力量调整值](Strength.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击")

## 技术细节

UID

`Projectile_TerrifyingLunge_Slayer`

造成2d6伤害的基础版本

`Projectile_TerrifyingLunge_Slayer_10`

10级升级版，造成4d6伤害

法术标志

`[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsJump](https://bg3.wiki/w/index.php?title=IsJump_\(spell_flag\)&action=edit&redlink=1) "IsJump \(spell flag\) \(page does not exist\)")`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：2回合

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）范围内对倒伏生物的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）移动速度即可站起。

## 如何习得

由以下生物使用：[杀戮者](Slayer.md "杀戮者")

## 备注

- 范围等于正常[跳跃](Jump.md "跳跃")范围，且所有适用于跳跃范围的调整值也适用于此攻击的范围。在10级之前，范围为9.5米（32英尺）（由于杀戮者的力量调整值为+5）。在10级之后，范围增加到11.5米（38英尺）（由于杀戮者的力量调整值为+7）。
- 自补丁6起，此攻击现在可以打破[庇护术](Sanctuary_(Condition).md "庇护术（状态）")。

## 错误

- 杀戮者动作的[法术豁免DC](Spell_save_DC.md "法术豁免DC")使用你首次就职的*第一个*职业的[施法关键属性](Spells.md#Spellcasting_ability "法术")，但使用杀戮者的属性值。这导致由于杀戮者较低的精神属性值而产生非常低的DC。特别是，战士、游荡者、法师、牧师、德鲁伊、武僧和游侠在杀戮者形态下，来自智力或感知的[施法调整值](Spells.md#Spellcasting_modifier "施法调整值")为+0，而野蛮人、吟游诗人、圣武士、术士和邪术师在杀戮者形态下，来自魅力的施法调整值为-1。

- `AreaRadius`被错误地设置为18米（60英尺），导致范围效果半径看起来比实际大得多。

---
*Source: [Relentless Lunge](https://bg3.wiki/wiki/Relentless_Lunge)*