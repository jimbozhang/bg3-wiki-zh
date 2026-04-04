# 备战（近战）

另请参阅：[备战（远程）](Brace_(Ranged).md)

**备战（近战）**是一种[武器动作](Weapon_action.md "武器动作")，可供[重甲的](Proficient.md "重甲的")使用并手持[长柄刀](Glaives.md "长柄刀")或[长矛](Pikes.md "长矛")作为主手武器的角色使用。

## 描述

消耗6米（20英尺）的[移动](Movement_speed.md "移动速度")。在你的剩余回合中，掷两次近战伤害骰并使用最高结果。

## 属性

消耗
6米（20英尺）[移动速度](Resources.md#Movement_speed "资源")
详情
充能：[短休](Short_rest.md "短休")
持续时间：1驱散

## 技术细节

UID

`Shout_Steady`

法术标志

`[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`

## 状态：备战

**[备战](Braced_(Condition).md "备战（状态）")**

持续时间：1驱散

- 在伤害掷骰时，掷两次并使用较高结果。

## 如何习得

通过[熟练](Proficiency.md "熟练项")使用以下武器类型获得：

- [长柄刀](Glaives.md "长柄刀")
- [长矛](Pikes.md "长矛")

## 备注

- 备战的效果等同于[凶蛮打手](Savage_Attacker.md "凶蛮打手")专长，并与之叠加。两者同时使用时，每个伤害骰掷3次并取最高值。
- 当与[凶蛮打手](Savage_Attacker.md "凶蛮打手")和[巨武器战斗](Great_Weapon_Fighting.md "巨武器战斗")同时使用时，备战会先掷一次骰子，如果结果是1或2则重掷，然后额外掷两次并使用最高结果。以这种方式使用时，凶蛮打手和巨武器战斗的效果仍会共同生效，但收益递减（[见表格](#math)）。
- 备战会打破[隐藏](Hiding_(Condition).md "隐藏（状态）")和[隐形](Invisible_(Condition).md "隐形（状态）")。

## 错误

- 当与其他重掷骰子的特性结合时，战斗日志可能显示错误的重掷次数。

## 数学

### 备战的平均额外伤害

### 备战和凶蛮打手的平均额外伤害

1d12 | 2.98 | 9.48 | 0.99 2d6 | 2.92 | 9.92 | 0.98

### 备战、凶蛮打手和巨武器战斗的平均额外伤害

| 伤害骰 | 平均额外伤害 | 平均伤害掷骰 |
| --- | --- | --- |
| 1d4 | 1.08 | 3.58 | 0.14 | 0.21 |
| 1d6 | 1.62 | 5.12 | 0.16 | 0.35 |
| 1d8 | 2.13 | 6.63 | 0.16 | 0.51 |
| 1d10 | 2.64 | 8.14 | 0.17 | 0.67 |
| 1d12 | 3.14 | 9.64 | 0.16 | 0.83 |
| 2d6 | 3.24 | 10.24 | 0.32 | 0.70 |

## 外部链接

- [凶蛮打手和巨武器战斗计算](https://docs.google.com/spreadsheets/d/1ebI3SACmQFpC82tSN5UOQEI4HwizHDOPZDofTJqh9Hs/edit#gid=781019269) by Kalaeman

---
*Source: [Brace (Melee)](https://bg3.wiki/wiki/Brace_(Melee)*