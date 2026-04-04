# 烟粉桶

**烟粉桶**是一种常见的[消耗品](Consumables.md "消耗品")，可以被[投掷](Throw.md "投掷")，并在点燃时[爆炸](Explosives.md "爆炸物")。破裂时会产生高度易燃的地表。

鉴于其内容的挥发性，此桶应小心开启。

## 属性

- [消耗品](Consumables.md "消耗品")
- 单次使用
- 稀有度：普通
- 重量：26 千克 (52 磅)
- 价格：5 金币
- UID `CONT_Barrel_Smokepowder_A` UUID `9c875b66-4024-487f-b67c-0c175538eb5c` Stats `OBJ_Barrel_Filled_Smokepowder` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")桶

- 范围：18 米 (60 英尺)

- 如果破裂，创建区域：[烟粉](Smokepowder_(surface).md "烟粉 (地表)")

- 1 [生命值](Hit_Points.md "生命值")

  - 如果点燃：

- 2d6 (2~12) ⁠[火焰](Fire.md "火焰")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 以豁免）

- 2d6 (2~12) ⁠[力场](Force.md "力场")

伤害

- 烟粉地表变为[火焰](Fire_(surface).md "火焰 (地表)")地表（立即施加[燃烧](Burning_(Condition).md "燃烧 (状态)")状态）

- 如果受到任何 ⁠⁠[火焰](Fire.md "火焰")伤害，桶会爆炸。任何其他伤害类型会使其破裂，产生烟粉地表。

- 爆炸时：

  - 范围效果：6 米 (20 英尺) 半径

- 4d4 + 18 (22~34) ⁠[力场](Force.md "力场")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 以减半）

  - 自动[重击](Critical_Hit.md "重击")物体和环境。
  - 被爆炸波及的目标会被击退 6 米 (20 英尺)（无豁免检定）。
  - 创建烟粉地表并立即点燃，造成如上所述的伤害。

## 区域：烟粉

**[烟粉](Smokepowder_(surface).md "烟粉 (地表)")**

范围效果：6 米 (20 英尺) 半径

爆炸性。

类型：[地表](Area.md#Surface "区域")

## 获取地点

- 遍布游戏中的多个地点，包括：
  - 在 ⁠[破碎圣所](Shattered_Sanctum.md "破碎圣所")
  - 在 ⁠[散塔林会窝点](Zhentarim_Hideout.md "散塔林会窝点")
  - 在 ⁠[费洛杰尔烟花铺](Felogyr's_Fireworks.md "费洛杰尔烟花铺")
  - 在 ⁠[钢铁卫士铸造厂](Steel_Watch_Foundry.md "钢铁卫士铸造厂") 前方的轨道上

## 备注

- 对抗爆炸和烟粉地表点燃的豁免检定共享相同的 DC，但独立进行掷骰。
- 如果桶被投掷或放置在火焰地表上，它会爆炸。
- 处于爆炸半径外缘的生物可能不会因烟粉点燃而受到伤害，但会被击退并承受爆炸伤害。
- 如果桶被投掷到火焰地表边缘附近（即使落在其外部），它会爆炸。
- 如果桶被投掷到火焰地表外部很远的地方，它不会爆炸，但如果其区域与火焰地表重叠，烟粉会点燃。
- 如果桶撞击点离投掷者足够近，即使直接落在火焰地表上也不会爆炸，但烟粉仍会点燃。

---
*Source: [Smokepowder Barrel](https://bg3.wiki/wiki/Smokepowder_Barrel)*