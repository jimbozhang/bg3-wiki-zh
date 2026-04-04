# 隐形药水

隐形药水是一种[消耗品](Consumables.md "消耗品")（[药水](Potions.md "药水")）。饮用后使自身进入[隐形](Invisible_(Condition).md "隐形（状态）")状态。

你以为这瓶子是空的，但里面传来了液体晃动的声音。

## 属性

- [药水](Potions.md "药水")
- 单次使用
- 稀有度：稀有
- 重量：0.1 千克（0.2 磅）
- 价格：65 金币
- UID `CONS_Potion_Invisible_A` UUID `809d5026-4896-4b3a-986e-95da58da77e2` Stats `OBJ_Potion_Of_Invisibility` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 饮用药水，使自身获得[隐形](Invisible_(Condition).md "隐形（状态）")状态。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")药水，使区域内所有生物获得[隐形](Invisible_(Condition).md "隐形（状态）")状态。
  - 范围：18 米（60 英尺）
  - 范围效果：1 米（3 英尺）半径

## 状态：隐形

**[隐形](Invisible_(Condition).md "隐形（状态）")**

持续时间：10 驱散

- 在[攻击掷骰](Attack_roll.md "攻击掷骰")时具有[优势](Advantage.md "优势")，并对敌人的攻击掷骰施加[劣势](Disadvantage.md "劣势")。

如果隐形实体进行攻击、施放其他法术、与物体互动、变得[濡湿](Wet.md "濡湿")、执行动作或附赠动作，或受到伤害，则隐形状态会提前结束。

## 获取地点

- 在整个游戏中由各种[商人](Traders.md "商人")出售（前提是玩家角色等级足够高，通常为 6 级以上），包括：
  - [德鲁伊林地](Druid_Grove.md "德鲁伊林地")或[河边茶室](Riverside_Teahouse.md "河边茶室")中的[埃赛尔婶婶](Auntie_Ethel.md "埃赛尔婶婶")
  - [散塔林会窝点](Zhentarim_Hideout.md "散塔林会窝点")中的[布雷姆](Brem.md "布雷姆")
  - [蕈人巢穴](Myconid_Colony.md "蕈人巢穴")中的[德里丝·骨篷](Derryth_Bonecloak.md "德里丝·骨篷")
  - [破碎圣所](Shattered_Sanctum.md "破碎圣所")或主楼层或[月出之塔](Moonrise_Towers.md "月出之塔")中的[罗阿·月光](Roah_Moonglow.md "罗阿·月光")
- 通过[炼金术](Alchemy.md "炼金术")制作，将[小魔鬼翼膜灰](Ashes_of_Imp_Patagium.md "小魔鬼翼膜灰")（从[小魔鬼翼膜](Imp_Patagium.md "小魔鬼翼膜")中获取）与任意[精华](Alchemy.md#Extractions "炼金术")结合。

---
*Source: [Potion of Invisibility](https://bg3.wiki/wiki/Potion_of_Invisibility)*