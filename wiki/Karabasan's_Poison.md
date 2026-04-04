# 噩梦毒药

噩梦毒药是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合；或者作为[手雷](Grenades.md "手雷")投掷，在区域内造成效果。

这种粘稠的膜状毒药的基底是从食腐爬行者的甲壳上刮下来的。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：稀有
- 重量：0.2 千克 (0.4 磅)
- 价格：50 gp
- UID `TWN_Poison_Paralytic_A` UUID `a5d93495-c01c-4dd4-928c-3793f620121f` Stats `OBJ_CrawlerMucus` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用毒药涂抹你的主动武器。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒药。
  - 范围：18 米 (60 英尺)
  - 创建区域：爬行者粘液

## 状态：涂抹爬行者粘液

**[涂抹爬行者粘液](Coated_in_Crawler_Mucus_(Condition).md "涂抹爬行者粘液 (状态)")**

持续时间：10 回合

- 目标必须通过 [DC](Dice_rolls.md#Save_DCs "骰子掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，否则将[感染爬行者粘液](Stricken_with_Crawler_Mucus_(Condition).md "感染爬行者粘液 (状态)")。
- 如果豁免成功，目标将获得[接种：爬行者粘液](Inoculated_colon__Crawler_Mucus_(Condition).md "接种：爬行者粘液 (状态)")，持续 2 回合。

## 区域：爬行者粘液

**[爬行者粘液](Crawler_Mucus_(cloud).md "爬行者粘液 (云)")**

持续时间：1 回合

范围效果：1 米 (3 英尺) 半径

[中毒](Poisoned_(Condition).md "中毒 (状态)") 和 [麻痹](Paralysed_(Condition).md "麻痹 (状态)")。

类型：[云](Area.md#Cloud "区域")

### 状态：感染爬行者粘液

**[感染爬行者粘液](Stricken_with_Crawler_Mucus_(Condition).md "感染爬行者粘液 (状态)")**

[体](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 11)

- 受影响实体[中毒](Poisoned_(Condition).md "中毒 (状态)") 并 [麻痹](Paralysed_(Condition).md "麻痹 (状态)")
- 持续至受影响实体成功通过一次[体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")。

## 获取地点

- 由[丽德雯姐妹](Anna_Lidwin.md "安娜·丽德雯")在[治疗中心](House_of_Healing.md "治疗中心")出售

## 备注

- 此物品无法通过[炼金术](Alchemy.md "炼金术")制作。
- 尽管是不同的物品，但此物品与[爬行者粘液](Crawler_Mucus.md "爬行者粘液")具有相同的效果，并在使用时施加“[涂抹爬行者粘液](<Coated_in_Crawler_Mucus_(Condition)"状态。

## 图库

- 游戏内模型

---
*Source: [Karabasan's Poison](https://bg3.wiki/wiki/Karabasan's_Poison)*