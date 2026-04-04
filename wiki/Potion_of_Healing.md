# 治疗药水

另请参阅：[高等治疗药水](Potion_of_Greater_Healing.md "高等治疗药水")、[特效治疗药水](Potion_of_Superior_Healing.md "特效治疗药水")和[极效治疗药水](Potion_of_Supreme_Healing.md "极效治疗药水")

**治疗药水**是一种[消耗品](Consumables.md "消耗品")（[药水](Potions.md "药水")）。吞噬或使用时可恢复[生命值](Hit_Points.md "生命值")。

用于治疗轻微割伤和瘀伤的药剂。

## 属性

- [药水](Potions.md "药水")
- 单次使用
- 稀有度：普通
- 重量：0.1 千克 (0.2 磅)
- 价格：10 金币
- UID `CONS_Potion_Healing_A` UUID `d47006e9-8a51-453d-b200-9e0d42e9bbab` Stats `OBJ_Potion_Healing` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 吞噬药水
  - 恢复 2d4+2⁠⁠[治疗](Healing.md "治疗")
- 移除[燃烧](Burning_(Condition).md "燃烧（状态）")

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")药水。
  - 范围：18 米 (60 英尺)
  - 创建区域：治疗药水

## 区域：治疗药水

**[治疗药水](Potion_of_Healing_(cloud).md "治疗药水（云）")**

范围效果：1 米 (3 英尺) 半径

恢复 2d4+2⁠⁠[治疗](Healing.md "治疗")并停止[燃烧](Burning_(Condition).md "燃烧（状态）")。

类型：[云](Area.md#Cloud "区域")

## 获取地点

- 可从游戏中的各种商人、敌人和地点获得
- 可通过[炼金术](Alchemy.md "炼金术")制作，将[游荡者的零嘴盐](Salts_of_Rogue's_Morsel.md "游荡者的零嘴盐")（从[游荡者的零嘴](Rogue's_Morsel.md "游荡者的零嘴")获取）与任意[悬液](Alchemy.md#Extractions "炼金术")结合

## 备注

- 当投掷治疗药水以治疗友方生物时，建议将其投掷在它们附近的地面上，而不是直接投向它们：
  - 投掷的**治疗药水**在落地时会治疗小范围内的所有存活实体，而直接投向目标通常会导致目标受到投掷物的伤害，从而有效降低治疗效果，并可能引发战斗。
  - 如果直接命中目标，投掷伤害会在治疗*之前*应用，可能杀死濒死目标而非治疗他们。

## 图库

- 游戏内模型

---
*Source: [Potion of Healing](https://bg3.wiki/wiki/Potion_of_Healing)*