# 照亮射击

**照亮射击**是一种由[组装劲弩](Fabricated_Arbalest.md "组装劲弩")赋予的[武器动作](Weapon_action.md "武器动作")。

## 描述

发射一道闪烁的箭矢，对目标造成1回合的[光耀法球](Radiating_Orb_(Condition).md "光耀法球 (状态)")状态。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作")
伤害：1~4

1d4⁠[穿刺](Piercing.md "穿刺")

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）

## 技术细节

UID

`Projectile_MAG_Automaton_LightTagging_Shot`

法术标志

`[CanDualWield](https://bg3.wiki/w/index.php?title=CanDualWield_\(spell_flag\)&action=edit&redlink=1) "CanDualWield \(spell_flag\) \(页面不存在\)")`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell_flag\) \(页面不存在\)")`

## 状态：光耀法球

**[光耀法球](Radiating_Orb_(Condition).md "光耀法球 (状态)")**

持续时间：1回合

- 受影响实体每剩余回合**攻击掷骰**[攻击掷骰](Attack_rolls.md "攻击掷骰")**-1**。同时在其周围区域散发明亮光线。

- 每次实体进行攻击时，持续时间减少2。

## 学习方式

由物品赋予：

- [组装劲弩](Fabricated_Arbalest.md "组装劲弩")

## 错误

- 伤害固定为1d4⁠⁠[穿刺](Piercing.md "穿刺")，无法受益于大多数原本会影响普通攻击的伤害加成。
  - 这包括[神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷")，该效果会施加命中率惩罚，但_不_添加伤害加成。

---
*Source: [Illuminating Shot](https://bg3.wiki/wiki/Illuminating_Shot)*