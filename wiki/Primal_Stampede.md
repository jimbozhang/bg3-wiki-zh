# 原始践踏

**原始践踏**是[荒蛮之心](Wildheart.md "荒蛮之心")野蛮人的职业动作，仅在使用[狂暴：麋鹿之心](Rage_colon__Elk_Heart.md "狂暴：麋鹿之心")时可用，允许你沿直线冲锋，对所有敌人造成伤害并将其击倒。

## 描述

向前冲锋，攻击路径上的所有敌人，并可能将其击倒[倒伏](Prone_(Condition).md "倒伏（状态）")。

仅在[狂暴](Rage_(Condition).md "狂暴（状态）")时可用。

不会引发[借机攻击](Opportunity_Attacks.md "借机攻击")。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [移动速度](Resources.md#Movement_speed "移动速度")
伤害：1~4 + 调整值

1d4 + [力量调整值](Strength.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击")

详情
近战徒手[攻击掷骰](Attack_roll.md "攻击掷骰")
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 10 + 力量调整值）
范围：9米（30英尺）直线
目标：路径上所有非盟友生物

## 技术细节

UID

`Rush_Primal_Stampede`

法术标志

`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`, `[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

持续时间：2回合

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 10 + 力量调整值）

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "反应")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 对倒伏生物的攻击，若在3米（10英尺）内进行，则具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）的移动速度即可站起。

## 如何习得

职业：

- 职业等级3：[荒蛮之心](Wildheart.md "荒蛮之心")

由法术授予：

- [狂暴：麋鹿之心](Rage_colon__Elk_Heart.md "狂暴：麋鹿之心")

## 备注

- 会击中冲锋路径上2米（7英尺）半径内的所有敌人、友方NPC和物体。
- 此动作会触发[额外攻击](Extra_Attack.md "额外攻击")，并且可以与额外攻击一起使用。
- 原始践踏被编码为近战徒手攻击。以下加成适用于或不适用于此攻击。
  - **攻击加成有效**，无论它们是针对徒手、武器还是未指定的攻击。例如，来自[酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")、[碾压手套](Gloves_of_Crushing.md "碾压手套")、[大师的遗产](Legacy_of_the_Masters.md "大师的遗产")和[残缺甲壳](Mutilated_Carapace.md "残缺甲壳")的攻击加成有效。
  - **伤害加成**有以下情况：
- 对*武器*攻击的伤害加成*无效*。例如，[大师的遗产](Legacy_of_the_Masters.md "大师的遗产")。
- 对*徒手*攻击的伤害加成*无效*。这包括[酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")或[黯狱手套](Helldusk_Gloves.md "黯狱手套")的伤害部分。
- 对*徒手和武器*攻击均有效的伤害加成*有效*。这包括：
      - [狂战士的号角](Horns_of_the_Berserker.md "狂战士的号角")
- [突触能量过载](Overloaded_With_Synaptic_Power_(Condition).md "突触能量过载（状态）")（来自灵能过载）
      - [蔽影戒指](Shadow-Cloaked_Ring.md "蔽影戒指")
      - [蜜蜂军团：攻击](Legion_of_Bees_colon__Attack.md "蜜蜂军团：攻击")（以及类似的蜂群守护者反应）
  - 其他类型的加成往往有效。这包括但不限于以下内容：
- [流血](Bleeding_(Condition).md "流血（状态）")（来自[黯狱手套](Helldusk_Gloves.md "黯狱手套")）
- [精华攫取](Grasp_Essence_(Condition).md "精华攫取（状态）")（来自[灵魂捕捉手套](Gloves_of_Soul_Catching.md "灵魂捕捉手套")）。
- [致命武器](Lethal_Weapon_(Bludgeoning).md "致命武器（钝击）")
    - [精神抑制之戒](Ring_of_Mental_Inhibition.md "精神抑制之戒")：精神疲劳
- 以下加成与原始践踏**无效**：
    - [狂暴：麋鹿之心](Rage_colon__Elk_Heart.md "狂暴：麋鹿之心")：徒手攻击的伤害加成
    - [孢子守护者护甲](Armour_of_the_Sporekeeper.md "孢子守护者护甲")：黯蚀伤害加成（对来自[狂战士的号角](Horns_of_the_Berserker.md "狂战士的号角")的黯蚀伤害）
    - [女妖之弓](Bow_of_the_Banshee.md "女妖之弓")：对恐慌生物的伤害加成
    - [多洛的凄凉](Dolor_Amarus.md "多洛的凄凉")：重击的伤害加成
- [地狱之怒](Infernal_Fury_(Condition).md "地狱之怒（状态）")：火焰伤害加成
    - [狂想曲](Rhapsody.md "狂想曲")：伤害加成
    - [吸血鬼至尊](Vampire_Ascendant.md "吸血鬼至尊")：黯蚀伤害加成

---
*Source: [Primal Stampede](https://bg3.wiki/wiki/Primal_Stampede)*