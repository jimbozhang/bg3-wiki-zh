# 烟粉挎包

**烟粉挎包**是一种[消耗品](Consumables.md "消耗品")，可以[投掷](Throw.md "投掷")，如果被点燃会[爆炸](Explosives.md "爆炸物")，并在破损时产生高度易燃的地表。

这个皮袋里塞满了气味刺鼻的黑色颗粒。

## 属性

- [消耗品](Consumables.md "消耗品")
- 单次使用
- 稀有度：普通
- 重量：0.3 千克 (0.6 磅)
- 价格：90 金币
- UID `UNI_Bag_Blackpowder` UUID `08c75e58-6e70-469a-a22e-44c184995e6c` Stats `OBJ_Bag_BlackPowder` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")挎包

- 范围：18 米 (60 英尺)

- 如果破损，产生区域：[烟粉](Smokepowder_(surface).md "烟粉 (地表)")

- 4 [生命值](Hit_Points.md "生命值")

  - 如果被点燃：

- 2d6 (2~12) ⁠[火焰](Fire.md "火焰")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")以豁免）

- 2d6 (2~12) ⁠[力场](Force.md "力场")

伤害

- 烟粉地表变为[火焰](Fire_(surface).md "火焰 (地表)")地表（立即施加[燃烧](Burning_(Condition).md "燃烧 (状态)")状态）

- 如果受到任何 ⁠⁠[火焰](Fire.md "火焰")伤害，即使挎包仍有生命值也会爆炸

- 爆炸时：

  - 范围效果：3 米 (10 英尺) 半径

- 3d4 + 9 (12~21) ⁠[力场](Force.md "力场")

伤害（[DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")以减半）

  - 自动[重击](Critical_Hit.md "重击")物体和环境
  - 被爆炸波及的目标会被击退 3 米 (10 英尺)（无豁免检定）
  - 产生烟粉地表并立即点燃，造成上述伤害

## 区域：烟粉

**[烟粉](Smokepowder_(surface).md "烟粉 (地表)")**

范围效果：6 米 (20 英尺) 半径

爆炸性。

类型：[地表](Area.md#Surface "区域")

## 获取地点

- 由[巴克斯·鲁特](Barcus_Wroot.md "巴克斯·鲁特")携带
- [复仇之炉](Grymforge.md "复仇之炉")内隐藏房间中，坐标 X: -585 Y: 388
- 风车地下室的“沉重的背包”内，通过[染疫村落](Blighted_Village.md "染疫村落")的木制舱口进入
- 唯一物品 - 无法购买或通过[炼金术](Alchemy.md "炼金术")制作

## 备注

- 对爆炸和烟粉地表点燃的豁免检定共享相同的 DC，但独立掷骰。
- 独立于火焰，仅力场伤害也会点燃烟粉地表。
- 如果将挎包投掷或放置在火焰地表上，它会爆炸。
- 位于爆炸半径外缘的生物可能不会受到烟粉点燃的伤害，但仍可能被击退并受到爆炸伤害。

---
*Source: [Smokepowder Satchel](https://bg3.wiki/wiki/Smokepowder_Satchel)*