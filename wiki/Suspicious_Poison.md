# 可疑的毒药

**可疑的毒药**是一种[药水](Potions.md "药水")，其外观旨在模仿[治疗药水](Potion_of_Healing.md "治疗药水")，但实际饮用时会施加[中毒](Poisoned_(Condition).md "中毒 (状态)")状态。当投掷时，它会造成比预期更强大的效果。_\[[参见注释](#notes)\]_

不要被欺骗——这种“药水”会让你状况更糟。

## 属性

- [杂物](Miscellaneous.md "杂物")
- 单次使用
- 稀有度：普通
- 重量：0.1 千克 (0.2 磅)
- 价格：10 金币
- UID `S_FOR_ThayanCellar_FakeHealingPotion` UUID `b6f7f39f-9809-4f08-a2d9-73821e372da5` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 造成

3d6 (3~18) ⁠[中毒](Poison.md "中毒")

伤害，如果使用者未通过[DC](Dice_rolls.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，则施加 \_(状态)[中毒](Poisoned_(Suspicious_Poison)_(Condition).md "中毒 (可疑的毒药) (状态)") 状态，持续 10 回合。

  - 在回合结束时自动重新尝试豁免检定以移除中毒状态。

**可疑的毒药**也可以投掷。[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒药以制造小型[毒云](Poison_Cloud.md "毒云")。
  - 范围：1 米 (3 英尺) 半径
  - 持续时间：1 回合
- 对[毒云](Poison_Cloud.md "毒云")中的所有生物造成

3d6 (3~18) ⁠[中毒](Poison.md "中毒")

伤害。

- 对它们施加 \_(状态)[中毒](Poisoned_(Suspicious_Poison)_(Condition).md "中毒 (可疑的毒药) (状态)") 状态，持续 3 回合。此外，它们必须进行 [DC](Dice_rolls.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")：否则将获得 \_(状态)[中毒](Poisoned_(Suspicious_Poison)_(Condition).md "中毒 (可疑的毒药) (状态)") 状态，持续 1 回合。
- 受 \_(状态)[中毒](Poisoned_(Suspicious_Poison)_(Condition).md "中毒 (可疑的毒药) (状态)") 状态影响的生物必须在回合开始时进行 [DC](Dice_rolls.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，否则受到

3d6 (3~18) ⁠[中毒](Poison.md "中毒")

伤害。此伤害效果持续 10 回合，或直到成功通过豁免检定。

## 状态：中毒 (可疑的毒药)

**\_(状态)[中毒](Poisoned_(Suspicious_Poison)_(Condition).md "中毒 (可疑的毒药) (状态)")**

持续时间：10 回合

[体](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 13)

- 在[攻击掷骰](Attack_roll.md "攻击掷骰")和[检定](Checks.md "检定")上承受[劣势](Disadvantage.md "劣势")。
- 每回合造成 3d6⁠⁠[中毒](Poison.md "中毒")伤害，直到成功通过 [DC](Dice_rolls.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")。

## 获取地点

- 在[药剂师地窖](Apothecary's_Cellar.md "药剂师地窖")

## 注释

- 物品栏图标与[治疗药水](Potion_of_Healing.md "治疗药水")完全相同，并且共享 `饮用` 选项作为其主要菜单动作。这种欺骗很可能是游戏设计意图。
  - 此物品最有益的用途实际上是将其用作（出奇强大的）[手雷](Grenades.md "手雷")。
  - 尽管与其他同类物品共享常见属性，但它不能用作[涂层](Coatings.md "涂层")。
  - 在复仇之炉，它可以与啤酒桶一起使用，以杀死在复仇之炉码头骚扰[斯奇皮特](Skickpit.md "斯奇皮特")的 2 名[灰矮人](Duergar.md "灰矮人")，而无需战斗，不过需要一点时间才能杀死他们。

---
*Source: [Suspicious Poison](https://bg3.wiki/wiki/Suspicious_Poison)*