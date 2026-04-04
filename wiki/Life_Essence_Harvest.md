# 获取生命精华

**获取生命精华** 是一项被动特性，当法术杀死生物时，会为使用者提供法术位。这些法术位只能用于死灵学派法术。

## 描述

当使用者用法术杀死敌对生物时，他们贪婪地吸收其能量，并获得 [生命精华](Life_Essence_(Condition).md "生命精华 (状态)")，直到下一次 [长休](Long_Rest.md "长休")。

## 状态：生命精华

**[生命精华](Life_Essence_(Condition).md "生命精华 (状态)")**

持续时间：直到 [长休](Long_Rest.md "长休")

- 受影响实体已吸收一个生物的精华。他们可以使用该精华来施放任何 [死灵学派](Necromancy.md "死灵学派")，而无需消耗 [法术位](Spells.md#Spell_slots "法术位")。

## 如何习得

由武器授予：

- [死灵珍爱法杖](Staff_of_Cherished_Necromancy.md "死灵珍爱法杖")

由生物使用：

- [秘术师卡里翁](Mystic_Carrion.md "秘术师卡里翁")

## 备注

- 获取生命精华没有冷却时间，可以无限触发。
- 使用 [生命精华](Life_Essence_(Condition).md "生命精华 (状态)") 提供的法术杀死生物，不会提供新的 [生命精华](Life_Essence_(Condition).md "生命精华 (状态)") 冲锋。
- 来自 [精魂守卫](Spirit_Guardians.md "精魂守卫") 等来源的间接法术伤害，在杀死敌对生物时不会提供 [生命精华](Life_Essence_(Condition).md "生命精华 (状态)") 冲锋。
- 根据 `GreaterNecromancySpellFilter() .khn` 脚本，此效果旨在仅当法术等级等于或低于使用者拥有的生命精华驱散数时，才允许施放额外的死灵学派法术。然而，此限制目前无法正常工作，任何等级的死灵学派法术都可以使用此效果施放。尽管工具提示均未明确提及此功能，但生命精华在其工具提示中显示了使用者拥有的驱散数。

## 错误

- 如果此被动效果在角色施放死灵学派的 [戏法](Cantrip.md "戏法") 时处于激活状态，即使该戏法未在角色的施法栏中高亮显示，该效果也会被消耗。

---
*Source: [Life Essence Harvest](https://bg3.wiki/wiki/Life_Essence_Harvest)*