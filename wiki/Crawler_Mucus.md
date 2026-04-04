# 爬行者粘液

爬行者粘液是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十[驱散](Turn.md "驱散")，或作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")，在区域内造成其效果。

这种粘稠的膜状毒药的基底是从[食腐虫](https://forgottenrealms.fandom.com/wiki/carrion_crawler)的甲壳上刮下来的。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：稀有
- 重量：0.2 千克 (0.4 磅)
- 价格：50 金币
- UID `CONS_Poison_Crawler_Mucus` UUID `5865caed-4a5d-45b7-b365-1113334a8e7b` Stats `OBJ_CrawlerMucus` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用爬行者粘液涂抹你的主动武器

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒药。
  - 范围：18 米 (60 英尺)
  - 创建区域：爬行者粘液

## 状态：涂抹了爬行者粘液

**[涂抹了爬行者粘液](Coated_in_Crawler_Mucus_(Condition).md "涂抹了爬行者粘液 (状态)")**

持续时间：10 驱散

- 目标必须通过一次 [DC](Dice_rolls.md#Save_DCs "掷骰") 13 的 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，否则将[感染爬行者粘液](Stricken_with_Crawler_Mucus_(Condition).md "感染爬行者粘液 (状态)")。
- 如果豁免成功，目标将获得 [接种：爬行者粘液](Inoculated_colon__Crawler_Mucus_(Condition).md "接种：爬行者粘液 (状态)")，持续 2 驱散

## 区域：爬行者粘液

**[爬行者粘液](Crawler_Mucus_(cloud).md "爬行者粘液 (云)")**

持续时间：1 驱散

范围：1 米 (3 英尺) 半径

[中毒](Poisoned_(Condition).md "中毒 (状态)") 和 [麻痹](Paralysed_(Condition).md "麻痹 (状态)")。

类型：[云](Area.md#Cloud "区域")

### 状态：感染爬行者粘液

**[感染爬行者粘液](Stricken_with_Crawler_Mucus_(Condition).md "感染爬行者粘液 (状态)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 11)

- 受影响实体将[中毒](Poisoned_(Condition).md "中毒 (状态)") 和 [麻痹](Paralysed_(Condition).md "麻痹 (状态)")
- 持续到受影响实体成功通过一次 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 为止。

## 获取地点

- 由以下角色出售：
  - [阿巴济戈的回声](Echo_of_Abazigal.md "阿巴济戈的回声") 在 [谋杀裁判所](Murder_Tribunal.md "谋杀裁判所")，坐标 X: -1263 Y: 512
  - [弗格·德罗戈](Ferg_Drogher.md "弗格·德罗戈") 在 [利文顿](Rivington.md "利文顿")
  - [炮仗菲兹](Fytz.md "炮仗菲兹") 在 [下城区](Lower_City.md "下城区") 中央城墙传送点以南
- 通过 [炼金术](Alchemy.md "炼金术") 制作，将 [食腐虫触手盐](Salts_of_Carrion_Crawler_Tentacle.md "食腐虫触手盐")（从[食腐虫触手](Carrion_Crawler_Tentacle.md "食腐虫触手")获取）与任意[酸解物](Vitriol.md "酸解物")结合

## 备注

- 移除此状态的豁免检定发生在受影响角色的驱散结束时。这意味着，如果一个角色在驱散开始时带有此状态，他们将首先失去驱散，然后才能进行豁免检定以移除状态。
- 物品 [噩梦毒药](Karabasan's_Poison.md "噩梦毒药") 与此物品具有相同效果，使用时会施加“涂抹了爬行者粘液”状态。

## 图库

- 由 Konstantin Melnik 渲染

- 游戏内模型

---
*Source: [Crawler Mucus](https://bg3.wiki/wiki/Crawler_Mucus)*