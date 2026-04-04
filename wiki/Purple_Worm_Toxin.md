# 紫虫毒素

紫虫毒素是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合，或作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")，在区域内造成其效果。

如果这种毒素[足够强效](https://forgottenrealms.fandom.com/wiki/Purple_worm_toxin)，即使是最微小的针孔也能使大脑陷入谵妄，并使毛细血管萎缩成干瘪的管道。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：非常稀有
- 重量：0.2 千克 (0.4 磅)
- 价格：160 金币
- UID `CONS_Poison_Purple_Worm` UUID `56e531e9-78e4-430b-bc98-611c1b1ccd08` Stats `OBJ_PurpleWormPoison` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用紫虫毒素涂抹你的主动武器。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒素
  - 范围：18 米 (60 英尺)
  - 创造区域：紫虫毒素

## 状态：涂抹了紫虫毒素

**[涂抹了紫虫毒素](Coated_in_Purple_Worm_Toxin_(Condition).md "涂抹了紫虫毒素 (状态)")**

持续时间：10 回合

- 目标在其下一回合结束时受到 1d10⁠⁠[中毒](Poison.md "中毒")伤害，除非他们成功通过[DC](Dice_rolls.md#Save_DCs "掷骰") 19 的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")。

## 区域：紫虫毒素

**[紫虫毒素](Purple_Worm_Poison.md "紫虫毒素")**

范围效果：1 米 (3 英尺) 半径

造成中毒伤害。

类型：[地表](Area.md#Surface "区域")

### 状态：紫虫毒素

**[紫虫毒素](Purple_Worm_Toxin_(Condition).md "紫虫毒素 (状态)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 19)

- 受影响实体在其下一回合结束时受到 1d10⁠⁠[中毒](Poison.md "中毒")伤害。

## 获取地点

- 由以下角色出售：
  - [德里丝·骨篷](Derryth_Bonecloak.md "德里丝·骨篷")，位于[幽暗地域](Underdark.md "幽暗地域")的[蕈人栖息地](Myconid_Colony.md "蕈人栖息地")
  - [弗格·德罗戈](Ferg_Drogher.md "弗格·德罗戈")，位于[利文顿](Rivington.md "利文顿")
  - [丽德雯姐妹](Anna_Lidwin.md "安娜·丽德雯")，位于[治疗中心](House_of_Healing.md "治疗中心")
  - [阿拉吉·欧布罗扎](Araj_Oblodra.md "阿拉吉·欧布罗扎")，位于[月出之塔](Moonrise_Towers.md "月出之塔")主层
- 通过组合从[紫虫食道](Purple_Worm_Gullet.md "紫虫食道")获取的[紫虫粘液悬液](Suspension_of_Purple_Worm_Slime.md "紫虫粘液悬液")和任意[酸解物](Alchemy.md#Extractions "炼金术")合成

## 备注

- 当多个目标同时被使用涂抹了此毒素的武器的范围效果攻击击中时，一次只能有一个目标受到毒素影响。

## 错误

- 由于一行错误的代码，对抗[中毒](Poisoned_(Condition).md "中毒")的[豁免检定](Saving_throw.md "豁免检定")上的[优势](Advantage.md "优势")（例如来自[矮人活力](Dwarven_Resilience.md "矮人活力")、[壮心体魄](Strongheart_Resilience.md "壮心体魄")和[防护毒素](Protection_from_Poison_(Condition).md "防护毒素")）对对抗此毒素影响的豁免检定无效。
- 当使用涂抹了此毒素的武器伤害目标时，战斗日志中一个隐藏的技术性被动效果描述会说明受影响实体如果通过体质豁免检定则受到一半伤害。这并不正确；如果豁免成功，它根本不会受到施加伤害的状态。

## 画廊

- 由 Konstantin Melnik 渲染

---
*Source: [Purple Worm Toxin](https://bg3.wiki/wiki/Purple_Worm_Toxin)*