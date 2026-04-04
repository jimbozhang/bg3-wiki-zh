# 血甲魔炸弹

不要与 [血甲魔炸药](Orthon_Explosive.md "血甲魔炸药") 混淆

**血甲魔炸弹**是一种 [消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")），可以被 [投掷](Throw.md "投掷") 并在撞击时 [爆炸](Explosives.md "爆炸")。

对附近的物体造成火焰和力场伤害，并将其击退。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 千克 (0.6 磅)
- 价格：16 金币
- UID `GRN_Bomb_Orthon` UUID `29d32b36-390f-4fe8-b27b-931393d76c2a` Stats `OBJ_Bomb_Orthon` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷") 一枚在撞击时爆炸的炸弹

- 范围：18 米 (60 英尺)
- 范围效果：2 米 (7 英尺) 半径
- 4d8 (4~32) ⁠[力场](Force.md "力场")

伤害

- 4d8 (4~32) ⁠[火焰](Fire.md "火焰")

伤害

- [DC](Dice_rolls.md#Save_DCs "掷骰") 17 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 以减半所有伤害，并消除燃烧状态

## 状态：燃烧（血甲魔）

**\_(状态)[燃烧](Burning_(Orthonic)_(Condition).md "燃烧（血甲魔）（状态）")**

持续时间：2 驱散

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 17)

- 每驱散受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- **无法**通过 [协助](Help.md "协助") 动作、使用 [治疗药水](Potion_of_Healing.md "治疗药水") 或获得 [濡湿](Wet_(Condition).md "濡湿（状态）") 来移除。

## 获取地点

- 由 [尤格](Yurgir.md "尤格") 在 [莎尔铁手神殿](Gauntlet_of_Shar.md "莎尔铁手神殿") 携带并使用

## 备注

- 此手雷在地面停留一驱散后会获得 [快速计时地雷](Quickly_Ticking_Mine_(Condition).md "快速计时地雷（状态）") 状态。会添加一个红色圆圈作为视觉提示，表示其爆炸半径。如果在此状态下拾取，它会在所有者的物品栏中爆炸。
- 如果立即拾取，即使在战斗结束后也可以安全地用作手雷。如果物品提示中仍有 [快速计时地雷](Quickly_Ticking_Mine_(Condition).md "快速计时地雷（状态）") 状态，将其丢弃在地面上会导致它在 2 驱散后自动爆炸。
- 由于 `物品模板` 中使用的脚本，使用此手雷击杀敌人不会奖励 [经验值](Experience.md "经验值")。

## 错误

- 使用 [投掷](Throw.md "投掷") 时，半径看起来是 4 米 / 13 英尺，但实际半径仅为 2 米 / 7 英尺，与投掷水瓶产生的 [水](Water_(surface).md "水（地表）") 地表相同。
- 大多数角色在盟友被此物品爆炸伤害甚至击杀时不会做出反应或变得敌对，包括由它引起的连锁爆炸。
- 游戏内描述提到了雷鸣伤害和击退，但两者均未实现。
- 此手雷的法术描述称应施加 [邪魔火焰](Infernal_Burning_(Condition).md "邪魔火焰（状态）")，但实际施加的是 \_(状态)[燃烧（血甲魔）](Burning_(Orthonic)_(Condition).md "燃烧（血甲魔）（状态）")。

---
*Source: [Orthonic Handbomb](https://bg3.wiki/wiki/Orthonic_Handbomb)*