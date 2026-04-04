# 猩红炸药

**猩红炸药**是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")），可以[投掷](Throw.md "投掷")并在撞击时[爆炸](Explosives.md "爆炸")。

创造一片血迹地表。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 千克（0.6 磅）
- 价格：16 金币
- UID `WPN_Grenade_BloodSurface` UUID `7821978d-c720-4651-9693-936960145636` Stats `OBJ_Bomb_Orthon` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")一个在撞击时爆炸的药瓶

- 范围：18 米（60 英尺）
- 范围效果：2 米（7 英尺）半径
- 4d8（4~32）⁠[力场](Force.md "力场")

伤害

- 4d8（4~32）⁠[火焰](Fire.md "火焰")

伤害

- 施加 \_(状态)[燃烧（血甲魔）](Burning_(Orthonic)_(Condition).md "燃烧（血甲魔）（状态）")，持续 2 驱散
- [DC](Dice_rolls.md#Save_DCs "掷骰") 17 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 可使所有伤害减半，并消除燃烧状态

## 状态：燃烧（血甲魔）

**\_(状态)[燃烧](Burning_(Orthonic)_(Condition).md "燃烧（血甲魔）（状态）")**

持续时间：2 驱散

- 每驱散受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- **无法**通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿（状态）")来移除。

## 获取地点

- 在[下城区](Lower_City.md "下城区")从[阿拉吉·欧布罗扎](Araj_Oblodra.md "阿拉吉·欧布罗扎")处购买，前提是角色在饮用[神秘药剂](Mysterious_Potion.md "神秘药剂")后允许她取血。

## 备注

- 每次长休只能向阿拉吉·欧布罗扎捐献一次血液。虽然阿拉吉不会提及此事，但每次捐献后她会获得两个猩红炸药用于出售；捐献后这些炸药会出现在她的交易列表中。
- 此物品在功能上与[血甲魔炸弹](Orthonic_Handbomb.md "血甲魔炸弹")相似，但缺少[快速计时地雷](Quickly_Ticking_Mine_(Condition).md "快速计时地雷（状态）")状态。

## 错误

- 由于`物品模板`中使用的脚本，使用此手雷击杀敌人不会奖励[经验值](Experience.md "经验值")。
- 使用[投掷](Throw.md "投掷")时，半径显示为 4 米 / 13 英尺，但实际半径仅为 2 米 / 7 英尺。
- 大多数角色在盟友被此物品的爆炸伤害甚至击杀时不会做出反应或变得敌对，包括由其引起的连锁爆炸。

---
*Source: [Sanguine Explosive](https://bg3.wiki/wiki/Sanguine_Explosive)*