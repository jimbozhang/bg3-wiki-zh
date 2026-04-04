# 共生实体

**共生实体**是[孢子结社](Circle_of_the_Spores.md "孢子结社")德鲁伊的职业动作。这些德鲁伊不是变形为野兽，而是可以消耗一个[荒野形态充能](Druid.md#Level_2 "德鲁伊")来进入[共生实体](Symbiotic_Entity_(Condition).md "共生实体（状态）")形态。在此形态下，他们获得临时生命值，并在使用武器或徒手攻击以及[环形孢子](Halo_of_Spores.md "环形孢子")时造成额外的[黯蚀](Necrotic.md "黯蚀")伤害。当临时生命值耗尽时，该形态消失。

## 描述

每[德鲁伊](Druid.md "德鲁伊")等级获得4点[临时生命值](Temporary_Hit_Points.md "临时生命值")，并在拥有它们时，使用武器或徒手攻击造成额外的1d6点[黯蚀](Necrotic.md "黯蚀")伤害。施放[环形孢子](Halo_of_Spores.md "环形孢子")时伤害翻倍。

如果使用[荒野形态](Wild_Shape.md "荒野形态")，共生实体会提前结束。
只能拥有来自一个来源的临时生命值。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [荒野形态充能](Druid.md#Level_2 "德鲁伊")
详情
范围：自身
持续时间：直至[长休](Long_Rest.md "长休")

## 更高等级

在10级时，可以在该形态下施放[传播孢子](Spreading_Spores.md "传播孢子")。

## 状态：共生实体

**[共生实体](Symbiotic_Entity_(Condition).md "共生实体（状态）")**

持续时间：直至[长休](Long_Rest.md "长休")

- 受影响实体每[德鲁伊](Druid.md "德鲁伊")等级获得4点临时生命值，其近战武器或徒手攻击造成额外的1d6点[黯蚀](Necrotic.md "黯蚀")伤害，并且其[环形孢子](Halo_of_Spores.md "环形孢子")造成双倍伤害。_\[[参见：错误](Symbiotic_Entity_(Condition).md#Bugs).md#Bugs> "共生实体（状态）")\]_
- 如果实体使用[荒野形态](Wild_Shape.md "荒野形态")，则提前结束。

## 学习方式

职业：

- 职业等级2：[孢子结社](Circle_of_the_Spores.md "孢子结社")

## 备注

- 共生实体不被视为处于荒野形态，因此对于[荒野打击](Wild_Strike.md "荒野打击")而言，它不会在此形态下提供额外攻击。
- 在激活期间，其他来源的临时生命值（例如[生命通道之靴](Vital_Conduit_Boots.md "生命通道之靴")）会补充共生实体缺失的生命值，但不能超过其上限。
- [变形者的恩赐之戒](Shapeshifter's_Boon_Ring.md "变形者的恩赐之戒")不会被共生实体触发，因此不会提供属性检定加成。

## 错误

- 尽管工具提示有警告，但提供临时生命值的状态并未使用“TEMPORARY_HP”`StackId`，因此可能与其他临时生命值来源同时激活于一个角色身上。在这种情况下，角色将从最高来源获得临时生命值，而任何较低来源将用于补充最高来源损失的任何临时生命值。

## 相关物品

- [孢子守护者护甲](Armour_of_the_Sporekeeper.md "孢子守护者护甲") - 仅在共生实体形态下可使用额外动作。

---
*Source: [Symbiotic Entity](https://bg3.wiki/wiki/Symbiotic_Entity)*