# 简易毒素

**简易毒素**是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合；或者作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")，在区域内造成其效果。

这种毒素的翠绿色调如同沼泽上空的日出般鲜明而凶险。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：普通
- 重量：0.2 千克（0.4 磅）
- 价格：25 金币
- UID `Solution_Toxin_Basic` UUID `8b5f7965-6cd1-42c1-8449-c6562a270ad9` Stats `Solution_Toxin_Basic` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用简易毒素涂抹你的主动武器。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒素。
  - 范围：18 米（60 英尺）
  - 创造区域：简易毒素

## 状态：涂抹毒素

**[涂抹毒素](Coated_in_Toxin_(Condition).md "涂抹毒素 (状态)")**

持续时间：10 回合

- 目标在其下一回合结束时受到 1d4⁠⁠[中毒](Poison.md "中毒")伤害，除非他们成功通过[DC](Dice_rolls.md#Save_DCs "掷骰") 11 的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")。

## 区域：简易毒素

**[简易毒素](Simple_Toxin_(surface).md "简易毒素 (地表)")**

持续时间：1 回合

范围效果：1 米（3 英尺）半径

施加中毒。

类型：[地表](Area.md#Surface "区域")

### 状态：简易毒素

**[简易毒素](Simple_Toxin_(Condition).md "简易毒素 (状态)")**

[体质](Constitution.md "体质")[豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 11）

- 受影响实体在其下一回合结束时受到 1d4⁠⁠[中毒](Poison.md "中毒")伤害。

## 获取地点

- 在整个游戏中的各种商人、敌人和地点均可获得
- 通过结合[狂蛙人的小号悬液](Suspension_of_Bullywug_Trumpet.md "狂蛙人的小号悬液")（从[狂蛙人的小号](Bullywug_Trumpet.md "狂蛙人的小号")获取）和任意[升华物](Alchemy.md#Extractions "炼金术")制作而成

## 备注

- 在大多数情况下，购买原料的成本远高于直接从商人处购买毒素。
- 当多个目标同时被使用涂抹了此毒素的武器的范围效果攻击击中时，一次只能有一个目标受到毒素影响。

## 错误

- 由于代码行错误，对抗[中毒](Poisoned_(Condition).md "中毒 (状态)")的[豁免检定](Saving_throw.md "豁免检定")上的[优势](Advantage.md "优势")（例如来自[矮人活力](Dwarven_Resilience.md "矮人活力")、[壮心体魄](Strongheart_Resilience.md "壮心体魄")和[防护毒素](Protection_from_Poison_(Condition).md "防护毒素 (状态)")）对对抗此毒素影响的豁免检定无效。

## 被动特性

简易毒素拥有 1 点[生命值](Hit_Points.md "生命值")。

## 图库

- 道具设计：Cliff Laureys

- 游戏内模型

---
*Source: [Simple Toxin](https://bg3.wiki/wiki/Simple_Toxin)*