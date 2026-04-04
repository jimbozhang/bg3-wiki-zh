# 愤怒投掷

**愤怒投掷**是[狂战士](Berserker.md "狂战士")[野蛮人](Barbarian.md "野蛮人")的附赠动作。此能力允许狂战士使用附近的物品或生物进行远程攻击。

## 描述

拾取一个物品或生物并将其投向目标，造成额外伤害并使其[倒伏](Prone_(Condition).md "倒伏（状态）")。

你的[力量](Strength.md "力量")影响额外伤害以及你能投掷的重量。更重的物品造成更多伤害。

具有[投掷攻击](Thrown.md "投掷攻击")属性的武器的伤害与该武器的近战伤害相同。

你还会基于你的[力量](Strength.md "力量")造成额外伤害。

仅在[狂乱](Frenzied_(Condition).md "狂乱（状态）")时可用。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作")
伤害：

普通武器伤害

详情
[攻击掷骰](Attack_roll.md "攻击掷骰")
范围：18米（60英尺）

范围效果：1.5米（5英尺）半径（用于拾取物品或生物）

## 技术细节

UID

`Throw_FrenziedThrow`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[CombatLogSetSingleLineRoll](https://bg3.wiki/w/index.php?title=CombatLogSetSingleLineRoll_\(spell_flag\)&action=edit&redlink=1) "CombatLogSetSingleLineRoll \(spell flag\) \(page does not exist\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IgnoreSilence](IgnoreSilence_(spell_flag).md)`, `[IgnoreVisionBlock](IgnoreVisionBlock_(spell_flag).md)`, `[InventorySelection](https://bg3.wiki/w/index.php?title=InventorySelection_\(spell_flag\)&action=edit&redlink=1) "InventorySelection \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：1驱散

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在3米（10英尺）范围内对倒伏生物进行的攻击具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）的移动速度即可站起。

## 如何习得

职业：

- 职业等级3：[狂战士](Berserker.md "狂战士")

生物使用：[艾比](Abby.md "艾比")、[伯姆巴托](Bombasto.md "伯姆巴托")、[欢乐的克朗](Gleeful_Clong.md "欢乐的克朗")、[因库·纳扎](Inku_Neza.md "因库·纳扎")和[迦纳斯勋爵的保镖](Lord_Jannath's_Bodyguard.md "迦纳斯勋爵的保镖")

## 备注

- 此攻击的[倒伏](Prone_(Condition).md "倒伏（状态）")效果无法通过豁免检定避免。
- 此能力与[快手](Fast_Hands.md "快手")和[勇气头盔](Helmet_of_Grit.md "勇气头盔")的额外[附赠动作](Extra_Bonus_Action_(Condition).md)（状态）")协同效果良好，每轮最多可进行三次愤怒投掷攻击，同时[酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")会使投掷攻击的力量加成翻倍。
- 有关也适用于此变体的详细信息，请参阅[投掷](Throw.md "投掷")。

---
*Source: [Enraged Throw](https://bg3.wiki/wiki/Enraged_Throw)*