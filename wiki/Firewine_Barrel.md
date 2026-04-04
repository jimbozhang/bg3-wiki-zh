# 火酒桶

**火酒桶**是一种常见的[消耗品](Consumables.md "消耗品")，可以被[投掷](Throw.md "投掷")，如果被点燃则会[爆炸](Explosives.md "爆炸物")。破裂时会创建一个可燃的地表。

尽管密封严密，但桶内仍散发出酒类甜美的气味。

## 属性

- [消耗品](Consumables.md "消耗品")
- 单次使用
- 稀有度：普通
- 重量：40 kg (80 lb)
- 价格：5 gp
- UID `CONT_Barrel_Alcohol_A` UUID `79050068-7ce3-43f9-a9a3-1646f5eb39c3` Stats `OBJ_Barrel_Filled_Alcohol` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")一个桶

- 范围：18 m (60 ft)

- 如果破裂，创建区域：[酒](Alcohol_(surface).md "酒 (地表)")

- 1 [生命值](Hit_Points.md "生命值")

- 如果被点燃 - 变成[火焰](Fire_(surface).md "火焰 (地表)")地表（立即施加[燃烧](Burning_(Condition).md "燃烧 (状态)")状态）

- 如果受到任何[火焰](Fire.md "火焰")伤害，桶会爆炸

- 爆炸时：

  - 范围效果：6 m (20 ft) 半径

- 4d6 (4~24) [火焰](Fire.md "火焰")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 14 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 以减半）

  - 被爆炸波及的目标会被击退 3 m (10 ft)（无豁免检定）

## 区域：酒

**[酒](Alcohol_(surface).md "酒 (地表)")**

范围效果：6 m (20 ft) 半径

可燃。

类型：[地表](Area.md#Surface "区域")

## 获取地点

- 在游戏中的各个地点，包括[渥金的休眠地](Waukeen's_Rest.md "渥金的休眠地")和[地精营地](Goblin_Camp.md "地精营地")

## 备注

- 如果被投掷或放置在火焰地表上，桶会爆炸。

---
*Source: [Firewine Barrel](https://bg3.wiki/wiki/Firewine_Barrel)*