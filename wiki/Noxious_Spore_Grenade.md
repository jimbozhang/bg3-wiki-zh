# 毒素孢子弹

毒素孢子弹是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")）物品，可以[投掷](Throw.md "投掷")以制造[有毒烟雾](Noxious_Fumes.md "有毒烟雾")。

一股浓烈翻滚的恶臭从这种炼金混合物中散发出来。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 kg (0.6 lb)
- 价格：16 gp
- UID `ALCH_Solution_Grenade_SporesToxic` UUID `9320005f-18c6-4c2b-be7f-e168d3b15573` Stats `ALCH_Solution_Grenade_SporesToxic` ### 效果

[动作](Actions.md#Resources "动作")

- 爆炸成一团剧毒云，可对范围内的生物施加有毒烟雾状态。
  - 范围：18 m (60 ft)
  - 创造区域：有毒烟雾

## 区域：有毒烟雾

**[有毒烟雾](Noxious_Fumes.md "有毒烟雾")**

持续时间：3 驱散

范围效果：2 m (7 ft) 半径

有几率影响生物，使其获得 \_(状态)[有毒烟雾](Noxious_Fumes_(Bibberbang)_(Condition).md "有毒烟雾 (噼啪砰) (状态)")。

类型：[云](Area.md#Cloud "区域")

### 状态：有毒烟雾 (噼啪砰)

**\_(状态)[有毒烟雾](Noxious_Fumes_(Bibberbang)_(Condition).md "有毒烟雾 (噼啪砰) (状态)")**

- 受影响实体每驱散受到 1d4⁠⁠[中毒](Poison.md "中毒") 伤害。它必须成功通过 难度等级 15 的 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，否则将额外受到 2d4⁠⁠[中毒](Poison.md "中毒") 伤害，成功时伤害减半。

## 获取地点

- 可通过[炼金术](Alchemy.md "炼金术")制作，将[毒素孢子升华物](Sublimate_of_Poison_Spores.md "毒素孢子升华物")（从[毒素孢子](Poison_Spore.md "毒素孢子")中获取）与任何[灰烬](Alchemy.md#Extractions "炼金术")结合。

## 备注

- 1d4⁠⁠[中毒](Poison.md "中毒") 伤害在第一驱散不会生效。
- 2d4⁠⁠[中毒](Poison.md "中毒") 伤害每驱散生效。其难度等级为 15，如果生物在烟雾中移动，可多次生效。
- 当手雷爆炸时，爆炸可造成 2d4 + 1⁠⁠[中毒](Poison.md "中毒") 伤害；这是一个法术攻击。

---
*Source: [Noxious Spore Grenade](https://bg3.wiki/wiki/Noxious_Spore_Grenade)*