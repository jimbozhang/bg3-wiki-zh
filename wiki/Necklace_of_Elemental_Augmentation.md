# 元素强化项链

元素强化项链是一件[护符](Amulets.md "Amulets")，当佩戴者使用元素伤害的戏法时，会将施法调整值添加到伤害中。

这项链中的电气石几乎热得令人不适，被一种自身的热量所温暖。

## 属性

- [护符](Amulets.md "Amulets")
- 稀有度：普通
- 重量：0.05 千克 (0.1 磅)
- 价格：65 金币
- UID `MAG_ElementalGish_CantripBooster_Amulet` UUID `a92cec2f-3a86-4aa1-a7e9-1d6dc9e12957` ### 特殊

佩戴此物品获得：

[元素强化](Elemental_Augmentation.md "元素强化")
当你的一个[戏法](List_of_cantrips.md "List of cantrips")造成[强酸](Acid.md "强酸")、[寒冷](Cold.md "寒冷")、[火焰](Fire.md "火焰")、[闪电](Lightning.md "闪电")或[雷鸣](Thunder.md "雷鸣")伤害时，将你的[施法调整值](Spellcasting_Modifier.md "施法调整值")添加到造成的伤害中。

## 获取地点

- [伊雷珂养育间](Cr%C3%A8che_Y'llek.md "伊雷珂养育间") X: 1379 Y: -662：在[审判官的房间](Cr%C3%A8che_Y'llek.md#Inquisitor's_Chamber "伊雷珂养育间")的一个展示柜内
- [飞龙关](Wyrm's_Crossing.md "飞龙关") X: -97 Y: 107：在[南翼检查点](South_Span_Checkpoint.md "南翼检查点")西北方向一艘失事船只上的[旅行者的箱子](Traveller's_Chest.md "旅行者的箱子")内

## 备注

_关于元素强化：_

- 元素强化实际上并不检查造成的伤害是否匹配所列元素之一，而是检查是否匹配 `DamageType` 标志。然而，添加的元素伤害（例如来自[闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")等来源）不被视为源自戏法，这导致两种方法在功能上没有区别。

- 元素强化与大多数[龙族血脉](Draconic_Bloodline.md "龙族血脉")[术士](Sorcerer.md "术士")的[元素亲和：伤害](Elemental_Affinity_colon__Damage.md "元素亲和：伤害")特性叠加（但绿色龙血统的术士除外，因为此物品不提升中毒伤害）。在这种情况下，魅力调整值将被添加到相关戏法的伤害中两次。

- 元素强化对非元素伤害的戏法无效，如[魔能爆](Eldritch_Blast.md "魔能爆")，即使它们通过[闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")或[生离死别：尖啸](Phalar_Aluve_colon__Shriek.md "生离死别：尖啸")等效果造成额外的元素伤害。

- 当身兼多职时，元素强化使用_最后_添加的职业的[施法关键属性](Spells.md#Item_spellcasting_ability "法术")调整值，而不是授予戏法的职业的施法关键属性。

  - 最小额外伤害为1，即使角色的施法关键属性调整值为0或负数。

- [地狱火撕裂](Hellflame_Cleave.md "地狱火撕裂")造成两次伤害，_两者_都获得元素强化的额外伤害。

- 以下戏法获得元素强化的额外伤害：

| 名称 | 等级 | 施法时间 | 持续时间 | 范围/区域 | 攻击/豁免 | 伤害/效果 |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [酸液飞溅](Acid_Splash.md "酸液飞溅") | 戏法 |  |  | - | 18 米 / 60尺 / 2米 / 7尺 (半径) | [敏捷](Dexterity.md "敏捷") [豁免](Saving_throw.md "豁免检定") | 1d6[强酸](Acid.md "强酸") |
| [激活巫术箭](Activate_Witch_Bolt.md "激活巫术箭") | 戏法 |  |  | - | 30 米 / 100尺 | - | 1d12[闪电](Lightning.md "闪电") |
| [诱捕电击](Ensnaring_Shock.md "诱捕电击") | 戏法 |  |  | 4 驱散 | 18 米 / 60 尺 | [敏捷](Dexterity.md "敏捷") [豁免](Saving_throw.md "豁免检定") | 1d4[闪电](Lightning.md "闪电") |
| [火焰箭](Fire_Bolt.md "火焰箭") | 戏法 |  |  | - | 18 米 / 60尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d10[火焰](Fire.md "火焰") |
| [火焰箭?](Firebolt_q_.md "火焰箭?") | 戏法 |  |  | - | 18 米 / 60尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d10[火焰](Fire.md "火焰") |
| [地狱火撕裂](Hellflame_Cleave.md "地狱火撕裂") | 戏法 |  |  | 1 驱散 | 3米 / 10尺 (锥形) | [敏捷](Dexterity.md "敏捷") [豁免](Saving_throw.md "豁免检定") | 正常武器伤害 / 2d6[火焰](Fire.md "火焰") |
| [燃火术](Produce_Flame.md "燃火术") | 戏法 |  |  | 长休 | 自身 | - | 1d8[火焰](Fire.md "火焰") |
| [燃火术：投掷](Produce_Flame_colon__Hurl.md "燃火术：投掷") | 戏法 |  |  | - | 9 米 / 30尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d8[火焰](Fire.md "火焰") |
| [冷冻射线](Ray_of_Frost.md "冷冻射线") | 戏法 |  |  | 1 驱散 | 18 米 / 60尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d8[寒冷](Cold.md "寒冷") |
| [火焰射线](Rays_of_Fire_(Cantrip).md "火焰射线 (戏法)") | 戏法 |  |  | - | 18 米 / 60 尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 3d6[火焰](Fire.md "火焰") / 3d6[火焰](Fire.md "火焰") / 3d6[火焰](Fire.md "火焰") |
| [电爪](Shocking_Grasp.md "电爪") | 戏法 |  |  | 1 驱散 | 1.5 米 / 5 尺 | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d8[闪电](Lightning.md "闪电") |

---
*Source: [Necklace of Elemental Augmentation](https://bg3.wiki/wiki/Necklace_of_Elemental_Augmentation)*