# 简易毒药

**简易毒药**是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合；或者作为[手雷](Grenades.md "手雷")投掷，在区域内生效。

即使瓶盖紧闭，这瓶药水仍散发出刺鼻的气味。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：普通
- 重量：0.2 千克（0.4 磅）
- 价格：20 金币
- UID `CONS_Poison_Basic` UUID `28645376-e6e8-436a-8e9a-c62877fae07d` Stats `OBJ_BasicPoison` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 对你的主动武器施加[涂抹简易毒药](Coated_in_Basic_Poison_(Condition).md "涂抹简易毒药（状态）")。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒药。
  - 范围：18 米（60 英尺）
  - 创造区域：[毒云](Poison_Cloud.md "毒云")

## 状态：涂抹简易毒药

**[涂抹简易毒药](Coated_in_Basic_Poison_(Condition).md "涂抹简易毒药（状态）")**

持续时间：10 回合

- 目标必须通过一次[DC](Dice_rolls.md#Save_DCs "掷骰") 11 的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，否则将[中毒](Poisoned_(Condition).md "中毒（状态）")。
- 如果豁免成功，目标将获得[免疫：简易毒药](Inoculated_colon__Basic_Poison_(Condition).md "免疫：简易毒药（状态）")，持续 2 回合。

## 区域：毒云

**[毒云](Poison_Cloud.md "毒云")**

持续时间：1 回合

范围效果：1 米（3 英尺）半径

有几率使目标中毒。

类型：[云](Area.md#Cloud "区域")

### 状态：中毒

**[中毒](Poisoned_(Condition).md "中毒（状态）")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 11）

- 在[攻击掷骰](Attack_roll.md "攻击掷骰")和[检定](Checks.md "检定")上承受[劣势](Disadvantage.md "劣势")。

## 获取地点

- 在游戏中的各种商人、敌人和地点均可获得
- 通过[炼金术](Alchemy.md "炼金术")制作：将[骨帽酸解物](Vitriol_of_Bonecap.md "骨帽酸解物")（从[骨帽菇](Bonecap.md "骨帽菇")获取）与任意[灰烬](Alchemy.md#Extractions "炼金术")结合

## 备注

- 如果使用涂抹武器施加[中毒](Poisoned_(Condition).md "中毒（状态）")状态，该状态具有以下特性：
  - 除了施加时的原始豁免检定外，每回合结束时还会进行一次额外的豁免检定。
  - 该状态将持续到成功通过（DC 11）豁免检定为止。
- 投掷此药水可导致两种不同的中毒状态：
  - 毒云可导致持续时间为 1 的中毒状态，该状态在回合开始时失去持续时间（使用 DC 11）。
  - 爆炸可导致与用涂抹简易毒药的武器击中敌人类似的中毒状态。在这种情况下，战斗日志在计算中（但不是在结果中）错误地显示为使用了角色的 DC。然而，结果始终显示为 11，这是正确的值。
  - 两种状态使用相同的图标，但来自毒云的状态还会显示持续时间数字（1）和计时器（图标周围的棕色弧线），而另一个则不会。
- 在大多数情况下，购买原料比直接从商人处购买毒药要贵得多。

## 被动特性

简易毒药有 1 点[生命值](Hit_Points.md "生命值")。

## 图库

- 道具设计：Cliff Laureys

- 游戏内模型

---
*Source: [Basic Poison](https://bg3.wiki/wiki/Basic_Poison)*