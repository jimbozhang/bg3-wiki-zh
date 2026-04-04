# 加速药水

加速药水是一种[消耗品](Consumables.md "消耗品")（[药水](Potions.md "药水")），具有有益的实用效果。

这种溶液会自行荡漾和飞溅，几乎像是在试图逃离瓶子。

## 属性

- [药水](Potions.md "Potions")
- 单次使用
- 稀有度：普通
- 重量：0.1 千克 (0.2 磅)
- 价格：20 金币
- UID `CONS_Potion_Speed` UUID `ad9f3f24-d755-48b6-aa7b-c34da068209f` Stats `OBJ_Potion_Of_Speed` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 饮用药水以使自身获得[加速](Hastened_(Condition).md "加速 (状态)")

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")药水以使区域内所有生物获得[加速](Hastened_(Condition).md "加速 (状态)")
  - 范围：18 米 (60 英尺)
  - 范围效果：1 米 (3 英尺) 半径

## 状态：加速

**[加速](Hastened_(Condition).md "加速 (状态)")**

持续时间：3 驱散

- 受影响的生物获得以下效果：
  - [护甲等级](Armour_Class.md "护甲等级") +2，且在[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[优势](Advantage.md "优势")
  - [移动速度](Movement_speed.md "移动速度")增加 9 米 (30 英尺)
  - 额外获得一个[动作](Actions.md#Resources "动作")
- 状态结束时，受影响的生物会变得[力竭](Lethargic_(Condition).md "力竭 (状态)")，并在 1 驱散内无法移动或进行[动作](Action.md "动作")。

## 获取地点

- 在整个游戏中由各种商人出售，带有[实用药水表](Utility_Potion_Table.md "实用药水表")；出售此物品的商人示例包括：
  - [晋升之路](The_Risen_Road.md "晋升之路")[收费站](The_Risen_Road.md#Toll_House "晋升之路")的[赛丽尔](Cyrel.md "赛丽尔")
  - [破碎圣所](Shattered_Sanctum.md "破碎圣所")的[罗阿·月光](Roah_Moonglow.md "罗阿·月光")
  - [蕈人殖民地](Myconid_Colony.md "蕈人殖民地")的[德里丝·骨篷](Derryth_Bonecloak.md "德里丝·骨篷")
- 在[疮痍的海滩](Ravaged_Beach.md "疮痍的海滩")上 X: 141 Y: 280 处，藏在磨光岩石下的哈珀储藏点中
- 由一些[夺心魔](Mind_flayer.md "夺心魔")携带
- 通过[炼金术](Alchemy.md "炼金术")制作，将任意[盐](Alchemy.md#Extractions "炼金术")与[鬣狗耳屎灰烬](Ashes_of_Hyena_Ear.md "鬣狗耳屎灰烬")（从[鬣狗耳朵](Hyena_Ear.md "鬣狗耳朵")中获取）结合

## 备注

- 当[加速](Hastened_(Condition).md "加速 (状态)")效果结束时，受影响的生物通常会获得[力竭](Lethargic_(Condition).md "力竭 (状态)")状态，导致其错过下一驱散。
- 在已经加速时使用另一瓶加速药水可以有效地延迟力竭状态。当使用新的加速药水时，旧加速药水的效果会立即结束，立即应用力竭状态，但力竭状态仅持续到当前驱散结束；如果生物在消耗第二瓶加速药水（例如使用最后一个附赠动作饮用新药水）之前已准备好结束其驱散（例如所有动作已用完），则不会有任何损失。
- [加速孢子](Haste_Spores_(Condition).md "加速孢子 (状态)")状态由[加速孢子弹](Haste_Spore_Grenade.md "加速孢子弹")授予，类似于加速药水授予的[加速](Hastened_(Condition).md "加速 (状态)")状态，但仅持续 1 驱散而非 3 驱散，并且在过期时不会使使用者留下[力竭](Lethargic_(Condition).md "力竭 (状态)")状态，这可能使加速孢子弹在[投掷攻击](Thrown.md "投掷攻击")时比加速药水更具实用性。
  - 加速孢子弹的价格比加速药水高 5 金币。

## 被动特性

加速药水拥有 1 点[生命值](Hit_Points.md "生命值")。

## 画廊

- 概念艺术：Ana Popescu

- 游戏内模型

## 外部链接

- ⁠[加速药水](https://forgottenrealms.fandom.com/wiki/Potion_of_speed) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Potion of Speed](https://bg3.wiki/wiki/Potion_of_Speed)*