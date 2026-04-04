# 军团魔药水

军团魔药水是一种[消耗品](Consumables.md "消耗品")([手雷](Grenades.md "手雷"))物品，可以使用[投掷](Throw.md "投掷")动作投掷。

由军团魔酿造的药水，用于魅惑移位兽。这一批似乎效力较弱，可能只会使心智昏沉。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 kg (0.6 lb)
- 价格：9 gp
- UID `UNI_Throwable_Grenade_MerregonPotion` UUID `11600b5b-999b-4444-b9a1-f3aa110c7604` ### 效果

[动作](Actions.md#Resources "动作")

- 将此雾状药剂投向附近敌人，使其[昏沉](Befuddled_(Condition).md "昏沉 (状态)")

- 范围：18 m (60 ft)

- 创建区域：[鬼头蘑菇孢子](Timmask_Spores_(cloud).md "鬼头蘑菇孢子 (云)")

## 状态：昏沉

**[昏沉](Befuddled_(Condition).md "昏沉 (状态)")**

持续时间：1 驱散

- 受影响实体无法控制其动作，并在无方向地游荡。

## 区域：鬼头蘑菇孢子

**[鬼头蘑菇孢子](Timmask_Spores_(cloud).md "鬼头蘑菇孢子 (云)")**

持续时间：2 驱散

范围效果：2 m (7 ft) 半径

有几率使生物[昏沉](Befuddled_(Condition).md "昏沉 (状态)")。

类型：[云](Area.md#Cloud "区域")

### 状态：昏沉

**[昏沉](Befuddled_(Condition).md "昏沉 (状态)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 10)

- 受影响实体无法控制其动作，并在无方向地游荡。

## 获取地点

- 通过在[军团魔囤宝者](Hoarding_Merregon.md "军团魔囤宝者")身上通过 DC 11 [侦测思想](Detect_Thoughts.md "侦测思想") [属性检定](Ability_Check.md "属性检定")，并告知它你负责喂养[移位兽](Displacer_Beast.md "移位兽")后获得。

## 备注

- 游戏内工具提示显示持续时间为 2 驱散，但实际为 1 驱散。
- 当手雷爆炸时，还会产生一次爆炸，可造成 2d4 + 1⁠⁠[中毒](Poison.md "中毒")伤害。此攻击为法术攻击。
- 已处于鬼头蘑菇孢子云中的角色不会受到另一枚手雷的昏沉效果影响。爆炸伤害仍会影响他们。然而，如果他们离开云层，则可能受到另一枚手雷的昏沉效果影响。
- 豁免检定在驱散结束和开始时各进行一次，任一掷骰都可能导致昏沉。

---
*Source: [Merregon Potion](https://bg3.wiki/wiki/Merregon_Potion)*