# 国王匕首

**国王匕首**是[灰矮人](Duergar.md "灰矮人")对常见[长剑](Longsword.md "Longsword")的变体。它在所有方面都与[长剑](Longsword.md "Longsword")相同，除了外观。

锻造粗糙，部件不匹配，几乎生锈，但非常锋利。

## 属性

单手伤害

1d8 (1~8) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[挥砍](Slashing.md "挥砍")

双手伤害

1d10 (1~10) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[挥砍](Slashing.md "挥砍")

详情
[长剑](Longswords.md "长剑")
稀有度：普通
惑控学派：无
[两用](Versatile.md "两用")
[可蘸取](Dippable.md "可蘸取")
近战：1.5 米 (5 英尺)
重量：1.35 千克 (2.7 磅)
价格：40 金币
UID `WPN_Duergar_Sword_KingsKnife` UUID `5908898d-5d9e-40de-ab07-3f8fb5f0174c` Stats `MAG_Duergar_Sword_KingsKnife` ### 武器动作

_如果你拥有[熟练项](Proficiency.md "熟练项")，装备在**主手**以获得：_

[剑柄打击](Pommel_Strike.md "剑柄打击") ()
对敌人进行一次非致命攻击，并可能使其[眩晕](Dazed_(Condition).md "眩晕（状态）")。（充能：[短休](Short_rest.md "短休")。）

[割裂](Lacerate.md "割裂") ()
劈砍目标要害部位，使其[流血](Bleeding_(Condition).md "流血（状态）")。（充能：[短休](Short_rest.md "短休")。）

[突进攻击](Rush_Attack.md "突进攻击") ()
向前冲锋并攻击路径上的第一个敌人，可能将其推至[失衡](Off_Balance_(Condition).md "失衡（状态）")。（充能：[短休](Short_rest.md "短休")。）

## 获取地点

- [复仇之炉](Grymforge.md "复仇之炉") X: -643 Y: 411：由[石卫兵奥加斯](Orgarth.md "奥加斯")携带

## 错误

- 在游戏文件中，这把剑的_根模板_（UUID `5908898d-5d9e-40de-ab07-3f8fb5f0174c`）实际上描述的是一把短剑，该模板也被用作[山下国王之刃](Knife_of_the_Undermountain_King.md "山下国王之刃")的基础。事实上，那把剑的魔法属性也通过`<Stats>`标签添加到了这个根模板中，这意味着这个物品也应该拥有这些属性，并且如果通过控制台生成，它确实会拥有。然而，游戏中生成的武器并非直接基于_根模板_，而是基于一个名为`WPN_KingsKnife`的_统计条目_，该条目继承自`WPN_Longsword`。这最终导致该物品在功能上与普通长剑相同。
- 为雇佣兵装备此武器，然后解雇并重新雇佣他们，会将此武器的属性和武器动作更改为[山下国王之刃](Knife_of_the_Undermountain_King.md "山下国王之刃")的属性，因为其根模板具有相同的属性。

## 图库

- 3D 模型由 Gino Luka Kolling 制作

---
*Source: [King's Knife](https://bg3.wiki/wiki/King's_Knife)*