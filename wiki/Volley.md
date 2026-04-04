# 疾速齐射

**疾速齐射**是[猎人](Hunter.md "猎人")游侠的武器动作。此能力允许猎人使用远程武器攻击一个大区域内的所有敌人，而非单一目标。

## 描述

向附近敌人倾泻一连串魔法阔头箭和锥头箭。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：

正常武器伤害

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
范围：正常武器范围
范围效果：3米（10英尺）半径
目标：所有非盟友生物和物体

## 技术细节

UID

`Target_Volley`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 学习方式

职业：

- 职业等级 11：[猎人](Hunter.md "猎人")

## 备注

- 在测试版中，描述为“向附近敌人倾泻一连串箭矢。”。在发布版（补丁#2）中，此技能的描述为空白，直到补丁8才更新为当前描述。
- 此技能本质上用于替代普通远程攻击。它无法击中队伍成员，但可以击中其他友方NPC。除此之外，使用它没有比普通远程攻击更多的缺点。
- 物品的某些属性会应用于每个被击中的生物，而有些则只应用于单个生物。
  - 如果只有一个生物受到影响，似乎没有简单的规则来确定哪个生物受到影响。
  - 哪些属性应用于每个生物，哪些只应用于单个生物，这并不明显。
  - 一些应用于每个被击中敌人的有用属性列表：
    - [巴尔护符](Amulet_of_Bhaal.md "巴尔护符")：流血
    - [女妖之弓](Bow_of_the_Banshee.md "女妖之弓")：恐慌
    - [脑力汲取手套](Braindrain_Gloves.md "脑力汲取手套")：精神疲劳
    - 所有[涂层](Coatings.md "涂层")，不包括：[收缩油](Oil_of_Diminution.md "收缩油")（仅一个生物缩小，-1武器惑控仍应用于每次掷骰）、[灾祸油](Oil_of_Bane.md "灾祸油")和所有毒素
- [冷冻](Encrusted_with_Frost_(Condition).md "冷冻（状态）")
    - [巨人扫荡者](Giantbreaker.md "巨人扫荡者")：手酸臂软
    - [恶毒手套](Gloves_of_Baneful_Striking.md "恶毒手套")：豁免检定-1d4惩罚
    - [威能手套](Gloves_of_Power.md "威能手套")：灾祸术
    - [哈罗德](Harold.md "哈罗德")：灾祸术
    - [战法师的骄傲](Helmet_of_Arcane_Acuity.md "战法师的骄傲")：奥术敏锐
- [光耀法球](Radiating_Orb_(Condition).md "光耀法球（状态）")
    - [恶之雷鸣戒指](Ring_of_Spiteful_Thunder.md "恶之雷鸣戒指")：眩晕
    - [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓")：额外伤害
  - 一些只应用于单个生物的有用属性列表：
    - 以下[涂层](Coatings.md "涂层")：[收缩油](Oil_of_Diminution.md "收缩油")（仅一个生物缩小，-1武器惑控仍应用于每次掷骰）、[灾祸油](Oil_of_Bane.md "灾祸油")和所有毒素
    - [火焰敏锐之帽](Hat_of_Fire_Acuity.md "火焰敏锐之帽")：奥术敏锐
    - [风暴之子力量帽](Hat_of_Storm_Scion's_Power.md "风暴之子力量帽")：奥术敏锐
- [残响](Reverberation_(Condition).md "残响（状态）")
    - [雪花迸射](Snowburst_Ring.md "雪花迸射")：冰地表

---
*Source: [Volley](https://bg3.wiki/wiki/Volley)*