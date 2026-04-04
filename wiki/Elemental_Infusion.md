# 元素注能

**元素注能**是一项被动特性，可在使用者对敌人造成法术元素伤害后，为其下一次武器攻击附加元素伤害。

## 描述

当你使用[法术](Spell.md "法术")或[戏法](Cantrip.md "戏法")造成[强酸](Acid.md "强酸")、[寒冷](Cold.md "寒冷")、[火焰](Fire.md "火焰")、[闪电](Lightning.md "闪电")或[雷鸣](Thunder.md "雷鸣")伤害时，该元素会灌注你的武器。

直到你的下一回合结束，你的第一次成功武器攻击将额外造成 **1d4** 点该元素伤害。

## 学习方式

由装备提供：

- [元素注能戒指](Ring_of_Elemental_Infusion.md "元素注能戒指")

由生物使用：

- [乌姆拉阿克](Umr'a'ac.md "乌姆拉阿克")

## 备注

- 元素注能可将其伤害加成[多次](Damage_rider_as_source.md "伤害附加源")应用于单次武器攻击。
- 各个元素灌注状态共享相同的 `StackID`，这意味着同一时间只能有一个状态对角色生效。然而，这些状态也使用 `Overwrite` 的 `StackType`，这意味着被动特性最后施加的状态将实际影响使用者的下一次近战武器攻击。由于被动特性的编写方式，这会产生优先级效果，状态按以下优先级顺序排列（后施加的状态会覆盖先施加的状态）：
- [强酸灌注](Acid_Infusion_(Condition).md "强酸灌注（状态）") < [寒冷灌注](Cold_Infusion_(Condition).md "寒冷灌注（状态）") < [火焰灌注](Fire_Infusion_(Condition).md "火焰灌注（状态）") < [闪电灌注](Lightning_Infusion_(Condition).md "闪电灌注（状态）") < [雷鸣灌注](Thunder_Infusion_(Condition).md "雷鸣灌注（状态）")
    - 这意味着，如果一个角色使用主要造成火焰伤害但附加雷鸣伤害的法术攻击敌人，该角色将保留雷鸣灌注。

## 状态：强酸灌注

**[强酸灌注](Acid_Infusion_(Condition).md "强酸灌注（状态）")**

持续时间：2 驱散

- 受影响实体下一次使用武器造成伤害时，额外造成 1d4⁠⁠[强酸](Acid.md "强酸") 伤害。

## 状态：寒冷灌注

**[寒冷灌注](Cold_Infusion_(Condition).md "寒冷灌注（状态）")**

持续时间：2 驱散

- 受影响实体下一次使用武器造成伤害时，额外造成 1d4⁠⁠[寒冷](Cold.md "寒冷") 伤害。

## 状态：火焰灌注

**[火焰灌注](Fire_Infusion_(Condition).md "火焰灌注（状态）")**

持续时间：2 驱散

- 受影响实体下一次使用武器造成伤害时，额外造成 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。

## 状态：闪电灌注

**[闪电灌注](Lightning_Infusion_(Condition).md "闪电灌注（状态）")**

持续时间：2 驱散

- 受影响实体下一次使用武器造成伤害时，额外造成 1d4⁠⁠[闪电](Lightning.md "闪电") 伤害。

## 状态：雷鸣灌注

**[雷鸣灌注](Thunder_Infusion_(Condition).md "雷鸣灌注（状态）")**

持续时间：2 驱散

- 受影响实体下一次使用武器造成伤害时，额外造成 1d4⁠⁠[雷鸣](Thunder.md "雷鸣") 伤害。

---
*Source: [Elemental Infusion](https://bg3.wiki/wiki/Elemental_Infusion)*