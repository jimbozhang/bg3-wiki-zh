# 真菌迷药

真菌迷药是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")），可[投掷](Thrown.md "投掷")以散播[鬼头蘑菇孢子](Timmask_Spores_(cloud).md "鬼头蘑菇孢子（云）")。

吸入错误的孢子甚至能将最敏锐的智力溶解成滋滋作响的困惑。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：罕见
- 重量：0.3 千克（0.6 磅）
- 价格：20 金币
- UID `ALCH_Solution_Grenade_SporesConfusion` UUID `cbc47f2b-b88a-4bd8-99cd-aacc2dc2ea44` Stats `ALCH_Solution_Grenade_SporesConfusion` ### 效果

[动作](Actions.md#Resources "动作")

- 投掷此蒸汽状药剂以使附近敌人[昏沉](Befuddle.md "昏沉")
  - 范围：18 米（60 英尺）
  - 创建区域：鬼头蘑菇孢子

## 区域：鬼头蘑菇孢子

**[鬼头蘑菇孢子](Timmask_Spores_(cloud).md "鬼头蘑菇孢子（云）")**

持续时间：2 驱散

范围效果：2 米（7 英尺）半径

使生物有几率[昏沉](Befuddled_(Condition).md "昏沉（状态）")。

类型：[云](Area.md#Cloud "区域")

### 状态：昏沉

**[昏沉](Befuddled_(Condition).md "昏沉（状态）")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 10）

- 受影响实体无法控制其动作，并漫无目的地游荡。

## 获取地点

- 通过[炼金术](Alchemy.md "炼金术")制作，将[鬼头蘑菇孢子精华](Essence_of_Timmask_Spores.md "鬼头蘑菇孢子精华")（从[鬼头蘑菇孢子（原料）](Timmask_Spores_(ingredient).md "鬼头蘑菇孢子（原料）")获取）与任意[盐](Alchemy.md#Extractions "炼金术")结合。

## 备注

- 工具提示信息可能令人困惑，使得[昏沉](Befuddled_(Condition).md "昏沉（状态）")的持续时间显示为 2 驱散；实际上，_鬼头蘑菇孢子云_的持续时间为 2 驱散，而_昏沉_仅持续到受影响角色的驱散结束。
- 当手雷爆炸时，还会产生爆炸，可造成 2d4 + 1⁠⁠[中毒](Poison.md "中毒")伤害。这是一个法术攻击。
- 已处于鬼头蘑菇孢子云中的角色不会受到另一枚手雷的昏沉影响，但爆炸伤害仍会影响他们。然而，如果他们离开云层，则可能受到另一枚手雷的昏沉影响。
- 在驱散结束和开始时均需进行豁免检定；任一掷骰都可能导致昏沉。

---
*Source: [Fungal Bamboozler](https://bg3.wiki/wiki/Fungal_Bamboozler)*