# 自然恢复

另请参阅：[奥术回想](Arcane_Recovery.md "奥术回想") 和 [创造法术位](Create_Spell_Slot.md "创造法术位")

**自然恢复**是[大地结社](Circle_of_the_Land.md "大地结社")德鲁伊的职业动作。此能力允许这些德鲁伊在每次长休时补充一定数量的法术位。

## 描述

在非战斗状态下补充已消耗的[法术位](Spells.md#Spell_slots "法术位")。

仅在非战斗状态下可用。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 自然恢复充能
详情
范围：自身

## 更高等级

- 在3级时，解锁消耗1个[动作](Actions.md#Resources "动作") + 2点自然恢复充能来补充一个[2级法术位](Spells.md#Spell_slots "法术位")的能力。
- 在5级时，解锁消耗1个[动作](Actions.md#Resources "动作") + 3点自然恢复充能来补充一个[3级法术位](Spells.md#Spell_slots "法术位")的能力。
- 在7级时，解锁消耗1个[动作](Actions.md#Resources "动作") + 4点自然恢复充能来补充一个[4级法术位](Spells.md#Spell_slots "法术位")的能力。
- 在9级时，解锁消耗1个[动作](Actions.md#Resources "动作") + 5点自然恢复充能来补充一个[5级法术位](Spells.md#Spell_slots "法术位")的能力。

## 技术细节

UID

`Shout_NaturalRecovery`

容器能力

`Shout_NaturalRecovery_1`

恢复1级法术位的版本

`Shout_NaturalRecovery_2`

恢复2级法术位的版本

`Shout_NaturalRecovery_3`

恢复3级法术位的版本

`Shout_NaturalRecovery_4`

恢复4级法术位的版本

`Shout_NaturalRecovery_5`

恢复5级法术位的版本

法术标志

`[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`

## 学习方式

职业：

- 职业等级2：[大地结社](Circle_of_the_Land.md "大地结社")

## 备注

- 大地结社德鲁伊获得的自然恢复充能数量等于职业等级除以二并向上取整。例如，一个5级德鲁伊将总共有3点自然恢复充能。
- 这些充能在长休后恢复。
- 恢复一个法术位消耗的充能数量等于法术等级。例如，恢复一个[3级法术位](Spells.md#Spell_slots "法术位")消耗3点自然恢复充能。
- 可恢复的最高等级法术位上限为5级，即使11级或12级德鲁伊总共有6点充能。
- 与[创造法术位](Create_Spell_Slot.md "创造法术位")不同，此动作不能添加新的法术位，只能补充已消耗的法术位。

---
*Source: [Natural Recovery](https://bg3.wiki/wiki/Natural_Recovery)*