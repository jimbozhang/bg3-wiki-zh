# 深邃浅眠药水

深邃浅眠药水是一种[消耗品](Consumables.md "消耗品")（[药水](Potions.md "药水")）。它具有有益的实用效果。

瓶中闪烁液体来回流动的景象令人昏昏欲睡——你知道饮用它会带来温暖、包裹般的毯子般的舒适感。

## 属性

- [药水](Potions.md "Potions")
- 单次使用
- 稀有度：稀有
- 重量：0.1 千克（0.2 磅）
- 价格：90 金币
- UID `ALCH_Solution_Potion_Rest_Lesser` UUID `b0ff8d30-5825-49d4-8cd4-ebf3a3d0a024` Stats `ALCH_Solution_Potion_Rest_Lesser` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 消耗药水，对自己施加[天使恢复药水](Potion_of_Angelic_Relief_(Condition).md "天使恢复药水 (状态)")。

## 状态：天使恢复药水

**[天使恢复药水](Potion_of_Angelic_Relief_(Condition).md "天使恢复药水 (状态)")**

持续时间：2 驱散

- 受影响实体入睡 2 回合。当它醒来时，会获得[短休](Short_rest.md "短休")的效果，并且所有 1 级和 2 级法术位都会恢复。
- 如果在持续时间结束前被打断，效果将不会生效。

## 获取地点

- 由以下角色出售：
  - [兰恩·塔夫](Lann_Tarv.md "兰恩·塔夫") 在[月出之塔](Moonrise_Towers.md "月出之塔")（[幽影诅咒之地](Shadow-Cursed_Lands.md "幽影诅咒之地")）
  - [卢克修斯](Lucretious.md "卢克修斯") 在[终焉马戏团](Circus_of_the_Last_Days.md "终焉马戏团")（[利文顿](Rivington.md "利文顿")）
- 通过[炼金术](Alchemy.md "炼金术")制作，组合[独角兽角金属箔](Essence_of_Unicorn_Horn.md "独角兽角金属箔")（从[独角兽角](Unicorn_Horn.md "独角兽角")获取）和任意[盐](Alchemy.md#Extractions "炼金术")

## 备注

- 这种药水对[邪术师](Warlock.md "邪术师")特别有用，因为该职业在[短休](Short_rest.md "短休")后会恢复所有法术位。
- 这种药水允许[术士](Sorcerer.md "术士")将其 1 级和 2 级法术位转化为术法点，以便稍后使用——用于创造更多法术位或超魔——具体步骤如下。获得的术法点确切数量取决于消耗的法术位数量。

1. 重复使用[1 级法术位](Spells.md#Spell_slots "法术")和[2 级法术位](Spells.md#Spell_slots "法术")[创造术法点](Create_Sorcery_Points.md "创造术法点")，直到全部用完。
1. 消耗此药水以恢复所有 1 级和 2 级法术位。
1. 只要你有药水，就可以重复步骤 1 和 2。
1. 随意使用你囤积的[术法点](Sorcery_Point.md "术法点")。

## 错误

- 该药水未被编程为恢复预言学派法师的[预言](Prophecy.md "预言")，这可能是一个疏忽。
- 此药水不会恢复使用 `OncePerShortRestPerItem` 冷却类型的物品所赋予的能力，但*会*恢复使用 `OncePerShortRest` 冷却类型的物品所赋予的能力，这与[深邃沉眠药水](Potion_of_Angelic_Slumber.md "深邃沉眠药水")相反，后者会恢复物品上两种类型的长休和短休冷却能力。

## 图库

- 游戏内模型

---
*Source: [Potion of Angelic Reprieve](https://bg3.wiki/wiki/Potion_of_Angelic_Reprieve)*