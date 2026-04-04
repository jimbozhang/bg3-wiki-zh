# 雷鸣打击

**雷鸣打击**是一个[法术](Spells.md "法术")。它允许施法者在攻击时让近战武器发出[雷鸣](Thunder.md "雷鸣")声，将目标推开并可能使其[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 描述

你的近战武器在攻击时发出雷鸣声，将目标推开3米（10英尺），并可能使其[倒伏](Prone_(Condition).md "倒伏（状态）")。

## 属性

消耗
[动作](Actions.md#Resources "动作")
命中时消耗
[附赠动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
伤害：2~12

正常武器伤害

\+ 2d6[雷鸣](Thunder.md "雷鸣")

详情
近战武器[攻击掷骰](Attack_roll.md "攻击掷骰")
[力量](Strength.md "力量")[豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）（豁免成功：目标承受全额伤害但不会被[击倒](Prone_(Condition).md "倒伏（状态）")）
射程：正常武器射程

## 升环施法

以更高环位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_Smite_Thunderous`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：1回合

[力量](Strength.md "力量")[豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）范围内对倒伏生物进行的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）的移动速度即可站起。

## 学习方式

职业：

- 职业等级2：[圣武士](Paladin.md "圣武士")
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

物品授予：

- [不和谐音](Cacophony.md "不和谐音")

## 备注

- 参见[至圣斩](Smite.md "至圣斩")以获取更多功能信息。
- 目标仅在豁免倒伏检定失败时才会被推开。
- 与大多数通过力量移动目标的攻击不同，此法术不会显示目标将被移动到的位置的轨迹线。

## 错误

- [1级法术位](Spells.md#Spell_slots "法术")版本的此动作在荣誉模式下会因代码覆盖而改变攻击动画。
- 由于编码错误，角色在荣誉模式下会收到两个[2级法术位](Spells.md#Spell_slots "法术")版本的此动作，其中一个具有DRS更改，而另一个没有。
- 升环至[3级法术位](Spells.md#Spell_slots "法术")或[4级法术位](Spells.md#Spell_slots "法术")的雷鸣打击不会为击退效果添加坠落伤害。

## 外部链接

- [雷鸣打击](https://forgottenrealms.fandom.com/wiki/Thunderous_smite) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Thunderous Smite](https://bg3.wiki/wiki/Thunderous_Smite)*