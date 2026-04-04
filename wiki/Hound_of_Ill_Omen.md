# 厄兆猎犬

**厄兆猎犬**是[暗影魔法](Shadow_Magic.md "暗影魔法")术士的类动作，允许他们召唤[宁布斯](Nimbus.md "宁布斯")，一只幽影獒犬。

## 描述

召唤一个黑暗生物。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + 3 [术法点](Sorcery_Point.md "术法点")
详情
范围：18米（60英尺）
充能：[短休](Short_rest.md "短休")

## 技术细节

UID

`Target_HoundOfIllOmen`

法术标志

`[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`

## 生物：宁布斯

| [力量](Strength.md "力量") 16 (+3) | [敏捷](Dexterity.md "敏捷") 14 (+2) | [体质](Constitution.md "体质") 13 (+1) | [智力](Intelligence.md "智力") 5 (-3) | [感知](Wisdom.md "感知") 12 (+1) | [魅力](Charisma.md "魅力") 5 (-3) |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| 持续时间 | 永久 |  |  |  |  |
| 生命值 | 33 |  |  |  |  |
| 护甲等级 | 18 |  |  |  |  |
| 移动速度 | 15米（50英尺） |  |  |  |  |

[厄兆啃咬](Ominous_Bite.md "厄兆啃咬") ()
啃咬一个目标，并可能在其身上施加[厄兆](Hound's_Omen_(Condition).md "猎犬的厄兆（状态）")。

[暗影缠绕](Umbral_Tangle.md "暗影缠绕") ()
用暗影藤蔓困住你的敌人。

[暗影裂片](Splinter_Shadow.md "暗影裂片") ()
当你受到不造成[光耀伤害](Radiant_damage.md "光耀伤害")的近战攻击时，分裂出自己的一部分，从暗影中生成一个新的版本。

**仅在特殊情况下：**

[紧随其后](Right_Behind_You.md "紧随其后") ()
在你的召唤者的受害者旁边实体化。

## 学习方式

职业：

- 职业等级 6：[暗影魔法](Shadow_Magic.md "暗影魔法")

## 备注

- 尽管未在任何地方明确说明，但宁布斯可以在魔法黑暗中视物。这意味着它不会受到[失明术](Blindness_(Condition).md "失明术（状态）")的影响，并且在施法者的[黑暗术](Darkness_(cloud).md "黑暗术（云）")云中攻击时具有优势。

## 错误

- 此召唤生物的 `CharacterStats` 未正确设置 `DifficultyStatuses`，因此该生物会因[探索者难度](Difficulty.md#Explorer_mode "难度")调整值而损失 30% 生命值，仿佛它是一个敌对 NPC。

---
*Source: [Hound of Ill Omen](https://bg3.wiki/wiki/Hound_of_Ill_Omen)*