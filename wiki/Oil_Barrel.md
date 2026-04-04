# 油桶

**油桶**是一种常见的[消耗品](Consumables.md "消耗品")，可以被[投掷攻击](Thrown.md "投掷攻击")，如果被点燃则会[爆炸](Explosives.md "爆炸品")。它破裂时会创建一个易燃的地表。

闪亮的黑色油脂从木头的裂缝中缓缓渗出。

## 属性

- [消耗品](Consumables.md "消耗品")
- 单次使用
- 稀有度：普通
- 重量：40 kg (80 lb)
- 价格：5 gp
- UID `CONT_Barrel_Oil_A` UUID `72e3f454-5a68-4bb2-acef-7b8d595b5015` Stats `OBJ_Barrel_Filled_Oil` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")一个桶

- 范围：18 m (60 ft)

- 如果破裂，创建区域：[油](Oil.md "油")

- 1 [生命值](Hit_Points.md "生命值")

- 如果被点燃 - 变成[火焰](Fire_(surface).md "火焰 (地表)")地表（立即施加[燃烧](Burning_(Condition).md "燃烧 (状态)")状态）

- 如果受到任何[火焰](Fire.md "火焰")伤害，桶会爆炸

- 爆炸时：

  - 范围效果：6 m (20 ft) 半径

- 6d6 (6~36) [火焰](Fire.md "火焰")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")可减半）

  - 被爆炸波及的目标会被击退 3 m (10 ft)（无豁免检定）

## 区域：油

**[油](Oil.md "油")**

范围效果：6 m (20 ft) 半径

易燃。

类型：[地表](Area.md#Surface "地表")

## 获取地点

- 游戏中的各个地点，包括：
  - [地精营地](Goblin_Camp.md "地精营地")
  - [渥金的休眠地](Waukeen's_Rest.md "渥金的休眠地")，在[萨拉祖恩](Salazon.md "萨拉祖恩")所在的谷仓里
  - [塞伦涅信徒哨站](Sel%C3%BBnite_Outpost.md "塞伦涅信徒哨站")

## 备注

- 如果桶被投掷到[火焰](Fire_(surface).md "火焰 (地表)")地表上而破裂，或者被放置在火焰地表上，桶会爆炸。

---
*Source: [Oil Barrel](https://bg3.wiki/wiki/Oil_Barrel)*