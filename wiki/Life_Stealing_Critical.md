# 生命窃取重击

**生命窃取重击** 是一个被动特性，可在重击时造成额外伤害并为你提供临时生命值。

## 描述

在 [重击](Critical_Hit.md "重击") 时，只要目标不是构装生物或不死生物，就会受到额外的 10⁠⁠[黯蚀](Necrotic.md "黯蚀")[DRS](Damage_rider_as_source.md "伤害来源") 伤害。你还会获得 10 点 [临时生命值](Temporary_Hit_Points.md "临时生命值")。

只能拥有来自一个来源的临时生命值。

## 状态：临时生命值 (10)

**\_(状态)[临时生命值](Temporary_Hit_Points_(10)_(Condition).md "临时生命值 (10) (状态)")**

- 被短暂的魔法增益从死亡边缘拉回。获得 10 点 [临时生命值](Temporary_Hit_Points.md "临时生命值")。

## 如何习得

由以下武器提供：

- [偷生之剑](Sword_of_Life_Stealing.md "偷生之剑")

## 备注

- 尽管描述存在歧义，但只有持有生命窃取重击的武器发动的重击才会触发其效果；它不会影响其他已装备的武器。

## 错误

- 临时生命值的 `StackPriority` 仅为 1，因此会被任何其他 `StackPriority` 为 1 或更高的临时生命值来源覆盖，即使新来源的值更低。

---
*Source: [Life Stealing Critical](https://bg3.wiki/wiki/Life_Stealing_Critical)*