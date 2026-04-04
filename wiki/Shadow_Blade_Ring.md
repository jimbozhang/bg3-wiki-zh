# 幽影之刃戒指

幽影之刃戒指是一个[戒指](Rings.md "Rings")，它能让佩戴者施展[破影利刃](Shadow_Blade.md "破影利刃")。完成任务[找到阿拉贝尔的父母](Find_Arabella's_Parents.md "找到阿拉贝尔的父母")后，即可获得此物品作为奖励。

这是⁠[深杜埃拉](https://forgottenrealms.fandom.com/wiki/Deep_Duerra)叛逆子嗣的遗物之一。很久以前，在一个名为锤墓的险恶领域，深杜埃拉——阴郁之神拉杜格的女儿——为她扭曲的刚玉王座诞下了众多子嗣。

## 属性

- [戒指](Rings.md "Rings")
- 稀有度：罕见
- 重量：0.05 千克 (0.1 磅)
- 价格：105 金币
- UID `MAG_Shadow_ShadowBlade_Ring` UUID `8cc165d7-0372-4f4b-b4ac-f424f4069af1` Stats `MAG_Shadow_ShadowBlade_Ring` ### 特殊

佩戴此物品者获得：

[破影利刃](Shadow_Blade.md "破影利刃") ()
以2级法术施展（充能：[短休](Short_rest.md "短休")。）

## 获取地点

- [营地（第二幕）](Campsite_(Act_Two).md): 由[阿拉贝尔](Arabella.md "阿拉贝尔")奖励，以完成任务[找到阿拉贝尔的父母](Find_Arabella's_Parents.md "找到阿拉贝尔的父母")

## 备注

截至补丁 8：

- 该法术不再需要专注，且召唤的利刃将持续到长休。
  - 因此，该戒指可产生多个幽影之刃——每次短休各一个。
- 召唤幽影之刃后，可卸下该戒指。
- 该戒指的幽影之刃可与使用法术位召唤的幽影之刃一同召唤并装备。

## 错误

- 只要幽影之刃当前处于召唤状态，卸下此戒指将打断角色当前的[专注](Concentration.md "专注")法术。
- 由于 `SummonInInventory` 函数编码错误，该戒指的幽影之刃可在角色间转移，并由队伍中任何人装备，且先前召唤的利刃不会在施放新法术时从施法者的物品栏中消失。

---
*Source: [Shadow Blade Ring](https://bg3.wiki/wiki/Shadow_Blade_Ring)*