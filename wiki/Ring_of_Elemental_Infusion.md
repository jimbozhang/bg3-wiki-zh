# 元素注能戒指

元素注能戒指是一个[戒指](Rings.md "Rings")，它能将你的法术或戏法的元素灌注到你的武器中，造成额外伤害。

这枚戒指上镶嵌的神秘宝石似乎在你不注意时会改变色调。

## 属性

- [戒指](Rings.md "Rings")
- 稀有度：普通
- 重量：0.05 千克 (0.1 磅)
- 价格：40 gp
- UID `MAG_ElementalGish_ElementalInfusion_Ring` UUID `9ce563ca-82b0-4c28-bd82-8640fd0a5be3` Stats `MAG_ElementalGish_ElementalInfusion_Ring` ### 特殊

佩戴此物品的角色获得：

[元素注能](Elemental_Infusion.md "Elemental Infusion")
当你使用[法术](Spell.md "Spell")或[戏法](Cantrip.md "Cantrip")造成[强酸](Acid.md "Acid")、[寒冷](Cold.md "Cold")、[火焰](Fire.md "Fire")、[闪电](Lightning.md "Lightning")或[雷鸣](Thunder.md "Thunder")伤害时，该元素会灌注你的武器。直到你的下一个回合结束，你在第一次成功的武器攻击中造成该元素的额外 **1d4** 伤害。

## 获取地点

- [伊雷珂养育间](Cr%C3%A8che_Y'llek.md "Crèche Y'llek") X: 1303 Y: -798：由医疗区南部的[熟手乌姆拉阿克](Umr'a'ac.md "Umr'a'ac")佩戴

## 备注

_关于元素注能：_

- 元素注能可以将其伤害加成[多次](Damage_rider_as_source.md "Damage rider as source")应用于单次武器攻击。
- 各个元素伤害提升状态共享相同的 `StackID`，这意味着一个角色同时只能激活一个状态。然而，这些状态也使用 `Overwrite` 的 `StackType`，这意味着被动技能施加的最后一个状态将实际影响佩戴者的下一次近战武器攻击。由于被动技能的编写方式，这会产生优先级效果，状态遵循以下优先级顺序（后面的状态会覆盖前面的状态）：
- [强酸灌注](Acid_Infusion_(Condition).md "Acid Infusion (Condition)") < [寒冷灌注](Cold_Infusion_(Condition).md "Cold Infusion (Condition)") < [火焰灌注](Fire_Infusion_(Condition).md "Fire Infusion (Condition)") < [闪电灌注](Lightning_Infusion_(Condition).md "Lightning Infusion (Condition)") < [雷鸣灌注](Thunder_Infusion_(Condition).md "Thunder Infusion (Condition)")
    - 这意味着，如果一个角色使用主要造成火焰伤害但同时造成额外雷鸣伤害的法术攻击敌人，该角色将保留雷鸣灌注。

---
*Source: [Ring of Elemental Infusion](https://bg3.wiki/wiki/Ring_of_Elemental_Infusion)*