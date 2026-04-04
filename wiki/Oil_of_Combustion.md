# 燃烧油

燃烧油是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合。

“看，这很简单。你只需要把油涂在人身上，像这样。然后划一根火柴，像这——哦该死。”——不走运的巴福特·伊格尔斯

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：稀有
- 重量：0.1 千克（0.2 磅）
- 价格：30 金币
- UID `ALCH_Solution_Oil_Combustion` UUID `bb750807-895b-468d-81e1-4378797d11ca` Stats `ALCH_Solution_Oil_Combustion` ### 效果

[附赠动作](Actions.md#Resources "动作") 涂抹你的主动武器以附上油。

## 状态：涂抹燃烧油

**[涂抹燃烧油](Coated_in_Oil_of_Combustion_(Condition).md "涂抹燃烧油（状态）")**

持续时间：10 回合

- 涂抹了易燃油。
- 命中时，目标被油浸湿，持续 2 回合。如果它受到[火焰](Fire.md "火焰")伤害，油会燃烧，在其周围区域造成 3d6[火焰](Fire.md "火焰")伤害。

## 状态：燃烧油

**[燃烧油](Oil_of_Combustion_(Condition).md "燃烧油（状态）")**

持续时间：2 回合

- 如果受影响实体受到[火焰](Fire.md "火焰")伤害，它会在 3 米（10 英尺）半径范围内造成 3d6[火焰](Fire.md "火焰")伤害。

## 获取地点

- 通过[炼金术](Alchemy.md "炼金术")合成，将[魔蝠岩浆灰](Ashes_of_Mephit_Magma.md "魔蝠岩浆灰")（从[心形石头](Heart-Shaped_Rock.md "心形石头")获得）与任意[精华](Alchemy.md#Extractions "炼金术")结合。

## 备注

- 此物品*不能*作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")以在区域中施加其效果。
- 状态：燃烧油在受到火焰伤害后结束。
- 造成火焰伤害的武器攻击可以施加燃烧油，但不会在同一攻击中点燃它。只有在先前攻击施加后，它们才会点燃它。一些为武器攻击添加火焰伤害的例子包括：
  - [炽焰斩](Searing_Smite.md "炽焰斩")
- [地狱之怒](Infernal_Fury_(Condition).md "地狱之怒（状态）")
  - [残缺的黯狱手套](Flawed_Helldusk_Gloves.md "残缺的黯狱手套")
  - [黯狱手套](Helldusk_Gloves.md "黯狱手套")
  - [龙息](Drakethroat_Glaive.md "龙息")（可以灌注另一把武器）
  - [传古链枷](Flail_of_Ages.md "传古链枷")（可以灌注主手近战武器）
- 造成火焰伤害的武器攻击不能同时点燃先前施加的燃烧油并施加新的燃烧油。一次攻击（无论是否造成火焰伤害）需要施加它，另一次攻击（造成火焰伤害）需要点燃它；然后第三次攻击可以再次施加它，依此类推。
- 作为上述规则的例外：[[_验证_](bg3wiki_colon_Verification.md "bg3wiki:验证")]
- 如果[反应](Reaction_(Combat).md) 在施加油的原始攻击后立即造成火焰伤害，它会立即点燃它。
  - 造成火焰伤害并击中多个目标的武器攻击可以将油施加到一个目标上，然后点燃另一个目标上先前施加的油（由另一次攻击施加），其爆炸又会点燃刚刚施加到第一个目标上的油。
- 炼金术创造所需的成分名称与提取物不同。

## 图库

- 游戏内模型

---
*Source: [Oil of Combustion](https://bg3.wiki/wiki/Oil_of_Combustion)*