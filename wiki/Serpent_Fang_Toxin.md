# 蛇牙毒素

蛇牙毒素是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合，或作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")，在区域内造成效果。

从政治暗杀到婚姻不和，[毒素](https://forgottenrealms.fandom.com/wiki/Poison)都能满足你的需求。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：普通
- 重量：0.2 千克 (0.4 磅)
- 价格：40 金币
- UID `CONS_Poison_Serpent_Venom` UUID `b0385b93-f525-4740-8126-471a76fa31a2` Stats `OBJ_SerpentVenom` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用蛇牙毒素涂抹你的主动武器。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒素。
  - 范围：18 米 (60 英尺)
  - 创建区域：蛇毒

## 状态：涂抹蛇牙毒素

**[涂抹蛇牙毒素](Coated_in_Serpent_Venom_Toxin_(Condition).md "涂抹蛇牙毒素 (状态)")**

持续时间：10 回合

- 目标在其下一回合结束时受到 1d6⁠⁠[中毒](Poison.md "中毒")伤害，除非他们成功通过[DC](Dice_rolls.md#Save_DCs "掷骰") 13 的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")。

## 区域：蛇毒

**[蛇毒](Serpent_Venom.md "蛇毒")**

范围效果：1 米 (3 英尺) 半径

造成中毒伤害。

类型：[地表](Area.md#Surface "区域")

### 状态：蛇牙毒素

**[蛇牙毒素](Serpent_Fang_Toxin_(Condition).md "蛇牙毒素 (状态)")**

[体质](Constitution.md "体质")[豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 13)

- 受影响实体在其下一回合结束时受到 1d6⁠⁠[中毒](Poison.md "中毒")伤害。

## 获取地点

- 通过结合[蛇毒悬液](Suspension_of_Snake_Venom.md "蛇毒悬液")（从[毒牙](Venomous_Fang.md "毒牙")获得）和任意[酸解物](Alchemy.md#Extractions "炼金术")制作而成。

## 备注

- 当多个目标同时被使用涂抹了此毒素的武器的范围效果攻击击中时，一次只能有一个目标受到毒素影响。

## 错误

- 由于一行错误代码，对[中毒](Poisoned_(Condition).md "中毒")的[豁免检定](Saving_throw.md "豁免检定")的[优势](Advantage.md "优势")（例如来自[矮人活力](Dwarven_Resilience.md "矮人活力")、[壮心体魄](Strongheart_Resilience.md "壮心体魄")和[防护毒素](Protection_from_Poison_(Condition).md "防护毒素")）对抵抗此毒素影响的豁免检定无效。
- 当用涂抹了此毒素的武器伤害目标时，战斗日志中隐藏的技术被动描述会说明受影响实体如果通过体质豁免检定则受到一半伤害。这并不正确；如果豁免成功，它根本不会受到施加伤害的状态。

## 图库

- 由 Konstantin Melnik 渲染

- 游戏内模型

---
*Source: [Serpent Fang Toxin](https://bg3.wiki/wiki/Serpent_Fang_Toxin)*