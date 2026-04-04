# 吞噬智力

本文介绍的是灵吸怪威能。关于升级版的[完整的灵吸怪](Full-illithid.md "完整的灵吸怪")版本，请参见[突触吞噬](Synaptic_Consumption.md "突触吞噬")。

**吞噬智力**是一种[灵吸怪威能](Illithid_powers.md "灵吸怪威能")，它会吸取目标的[智力](Intelligence.md "智力")，并随时间治疗使用者。每回合的治疗量和智力减少量起始分别为1d8⁠⁠[生命值](Healing.md "治疗")和-1，随后每回合叠加增加1d8⁠⁠[生命值](Healing.md "治疗")和-1的减少量，持续5回合。

## 描述

吞噬敌人的智力，每回合降低其[智力](Intelligence.md "智力")1点，并在5回合内治疗你的伤口。

## 属性

消耗
[动作](Actions.md#Resources "动作")
治疗：15~120

1d8⁠[治疗](Healing.md "治疗")（初始施加时）

\+ 2d8⁠[治疗](Healing.md "治疗")（1回合后）

\+ 3d8⁠[治疗](Healing.md "治疗")（2回合后）

\+ 4d8⁠[治疗](Healing.md "治疗")（3回合后）

\+ 5d8⁠[治疗](Healing.md "治疗")（4回合后）

详情
[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）
范围：9米（30英尺）
充能：[短休](Short_rest.md "短休")
持续时间：5回合

## 技术细节

UID

`Target_TAD_AbsorbIntellect`

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[CannotTargetTerrain](https://bg3.wiki/w/index.php?title=CannotTargetTerrain_\(spell_flag\)&action=edit&redlink=1) "CannotTargetTerrain \(spell flag\) \(page does not exist\)")`, `[DisableBlood](https://bg3.wiki/w/index.php?title=DisableBlood_\(spell_flag\)&action=edit&redlink=1) "DisableBlood \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：被吞噬的智力

**[被吞噬的智力](Absorbed_Intellect_(Condition).md "被吞噬的智力（状态）")**

持续时间：5回合

[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- [智力](Intelligence.md "智力")正被降低1点。

## 学习方式

其他学习途径：

- 在获得以下任一物品后，使用[夺心魔寄生虫标本](Mind_Flayer_Parasite_Specimen.md "夺心魔寄生虫标本")从[灵吸怪威能](Illithid_powers.md "灵吸怪威能")技能树中解锁：
  - [孤注一掷](Perilous_Stakes.md "孤注一掷")
  - [移位兽形态](Displacer_Beast_Shape.md "移位兽形态")

## 备注

- [被吞噬的智力](Absorbed_Intellect_(Condition).md "被吞噬的智力（状态）")状态在初始豁免检定失败后，每回合都会丢失并重新获得。效果的每一回合，智力损失量增加1点，第一回合以-1惩罚开始，最后一回合以-5惩罚结束。
- 当受影响实体的智力降至2时，吞噬智力会施加[萎缩](Atrophied_(Condition).md "萎缩（状态）")，而非降至0。

---
*Source: [Absorb Intellect](https://bg3.wiki/wiki/Absorb_Intellect)*