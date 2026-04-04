# 手酸臂软 (状态)

**手酸臂软**

- 从遭受重击或击中坚硬金属中恢复。每剩余一回合，[攻击掷骰](Attack_rolls.md "Attack Rolls")有-1的惩罚。
- **手酸臂软**的最大持续时间：10回合。

## 属性

[堆叠ID](Stack_ID.md "Stack ID"): `MAG_ATTACK_DEBUFF` [持续时间结束](Conditions.md#Duration "Conditions"): 回合结束

[堆叠优先级](Stack_priority.md "Stack priority"): 1

[更多属性](Status_properties.md "Status properties"):

- [MultiplyEffectsByDuration](Status_properties/MultiplyEffectsByDuration.md "Status properties/MultiplyEffectsByDuration")

## 备注

- **手酸臂软**会在被施加状态的生物进行下一次攻击时移除。
- 手酸臂软的持续时间应用方式取决于来源：
- [巨人扫荡者](Giantbreaker.md "Giantbreaker")：使用此武器命中目标时，*总是*为目标增加2回合，最多10回合。这是将状态持续时间延长至3回合以上的唯一方法。
  - [精金盾牌](Adamantine_Shield.md "Adamantine Shield")：对佩戴此盾牌的角色攻击未命中时，会移除攻击者身上的任何现有手酸臂软状态，然后施加一个新的2回合手酸臂软状态。命中时，任何现有手酸臂软状态都会被移除，且不会施加新状态。因此，仅来自盾牌的最大持续时间为2回合。
  - [精金鳞甲](Adamantine_Scale_Mail.md "Adamantine Scale Mail") 或 [精金板条甲](Adamantine_Splint_Armour.md "Adamantine Splint Armour")：对佩戴其中一种护甲的角色攻击未命中时，会移除手酸臂软状态。命中时，效果取决于攻击者是否已受手酸臂软影响：
    - 如果攻击者没有手酸臂软状态，命中佩戴这些护甲的角色会分别增加2和3回合。因此，仅来自这些护甲的最大持续时间分别为2和3。
- 如果生物具有多重攻击动作，攻击惩罚会在持续时间改变前适用于多重攻击中的所有攻击。

## 手酸臂软的来源

- [精金反冲](Adamantine_Backlash.md "Adamantine Backlash")
- [精金盾牌](Adamantine_Shield_(passive_feature).md "精金盾牌 (被动技能)")
- [沉重打击](Heavy_Hitter.md "Heavy Hitter")
- [高等精金反冲](Intense_Adamantine_Backlash.md "高等精金反冲")

## 具有手酸臂软的生物

*维基数据库中未定义*

## 具有相同堆叠ID的状态

- 从遭受重击或击中坚硬金属中恢复。每剩余一回合，[攻击掷骰](Attack_rolls.md "Attack Rolls")有-1的惩罚。
- **手酸臂软**的最大持续时间：10回合。

---
*Source: [Reeling (Condition)](https://bg3.wiki/wiki/Reeling_(Condition)*