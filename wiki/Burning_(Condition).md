# 燃烧 (状态)

| 状态 | 效果 |
| --- | --- |
| [燃烧](Burning_(Orthonic)_(Condition).md "燃烧 (奥托尼克) (状态)") | 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。**无法**通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。 |
| 燃烧 | 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。如果处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态则免疫。[蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。 |
| [灼烧](Burning_Fiercely_(Condition).md "灼烧 (状态)") | 每回合受到 1d10⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [圣火](Holy_Fire_(Condition).md "圣火 (状态)") | 每回合受到 1~4⁠⁠[光耀](Radiant.md "光耀") 伤害。 |
| [熔化](Melting_(Condition).md "熔化 (状态)") | 每回合受到 10d6⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火 (状态)") | 来自阿弗纳斯核心的火焰吞噬此实体，每回合造成 6d6⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [灼热光环](Scorching_Aura_(Condition).md "灼热光环 (状态)") | 此实体的攻击额外造成 1d6⁠⁠[火焰](Fire.md "火焰") 伤害，除非目标处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态。 |

不要与[邪魔火焰 (状态)](Infernal_Burning_(Condition).md) 和 [燃烧 (奥托尼克) (状态)](Burning_(Orthonic)_(Condition).md) 混淆。

- [蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `BURNING` [状态组](Status_groups.md "状态组"): [SG_Surface](SG_Surface.md "SG Surface"), [SG_Light](SG_Light.md "SG Light")

[持续时间损失](Conditions.md#Duration "状态"): 回合开始时

[更多属性](Status_properties.md "状态属性"):

- [InitiateCombat](Status_properties/InitiateCombat.md "状态属性/InitiateCombat")
- [Burning](Status_properties/Burning.md "状态属性/Burning")
- [DisableOverhead](Status_properties/DisableOverhead.md "状态属性/DisableOverhead")
- [IgnoreResting](Status_properties/IgnoreResting.md "状态属性/IgnoreResting")

## 注释

| 状态 | 效果 |
| --- | --- |
| [燃烧](Burning_(Orthonic)_(Condition).md "燃烧 (奥托尼克) (状态)") | 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。**无法**通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。 |
| 燃烧 | 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。如果处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态则免疫。[蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。 |
| [灼烧](Burning_Fiercely_(Condition).md "灼烧 (状态)") | 每回合受到 1d10⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [圣火](Holy_Fire_(Condition).md "圣火 (状态)") | 每回合受到 1~4⁠⁠[光耀](Radiant.md "光耀") 伤害。 |
| [熔化](Melting_(Condition).md "熔化 (状态)") | 每回合受到 10d6⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火 (状态)") | 来自阿弗纳斯核心的火焰吞噬此实体，每回合造成 6d6⁠⁠[火焰](Fire.md "火焰") 伤害。 |
| [灼热光环](Scorching_Aura_(Condition).md "灼热光环 (状态)") | 此实体的攻击额外造成 1d6⁠⁠[火焰](Fire.md "火焰") 伤害，除非目标处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态。 |

- 共享相同堆叠ID的状态会阻止这些状态的额外应用，直到原始状态持续时间结束。因此，受燃烧影响的角色不会同时受[熔化](Melting_(Condition).md "熔化 (状态)")影响，这意味着该角色可以在熔岩中自由行走，仅受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害，而不是 10d6⁠⁠[火焰](Fire.md "火焰") 伤害。
- 燃烧的生物受到[火元素](Fire_Elemental.md "火元素")的[多重攻击](Multiattack_(Fire_Elemental).md "多重攻击 (火元素)")双倍伤害，并被[水元素](Water_Elemental.md "水元素")的[寒冬吹息](Winter's_Breath.md "寒冬吹息")施加[易碎](Brittle_(Condition).md "易碎 (状态)")。
- 燃烧的生物在被[巨龙之握](Dragon's_Grasp.md "巨龙之握")或[引火者](Firestoker.md "引火者")攻击时，会额外受到 1d4⁠⁠[武器](Weapon.md "武器") 伤害。

## 燃烧来源

- [火焰](Fire_(surface).md "火焰 (地表)")
- [火墙术](Wall_of_Fire_(area).md "火墙术 (区域)")
- [炼金火焰](Alchemist's_Fire.md "炼金火焰")
- [火焰箭](Arrow_of_Fire.md "火焰箭")
- [烬蛾披风](Cindermoth_Cloak.md "烬蛾披风")
- [易燃粘液炸弹](Flammable_Slime_Bomb.md "易燃粘液炸弹")
- [土黄果冻怪粘液](Ochre_Jelly_Slime.md "土黄果冻怪粘液")
- [燃烧兽皮](Blazing_Hide.md "燃烧兽皮")
- [烧灼器](Cauteriser.md "烧灼器")
- [时代元素](Elements_of_an_Epoch.md "时代元素")
- [火焰回收](Fiery_Return.md "火焰回收")
- [火焰护罩](Flaming_Shroud.md "火焰护罩")
- [地狱潜行者](Hellstalker.md "地狱潜行者")
- [炙热小手](Hot_Little_Hands.md "炙热小手")
- [传奇动作：巨龙之怒](Legendary_Action_colon__Draconic_Fury.md "传奇动作：巨龙之怒")
- [自然的复仇](Nature's_Vengeance.md "自然的复仇")
- [无羁烈焰](Unfettered_Fire.md "无羁烈焰")
- [炼金火焰 (动作)](Alchemist's_Fire_(action).md "炼金火焰 (动作)")
- [燃烧溢出](Burning_Overflow.md "燃烧溢出")
- [火焰吐息 (龙)](Fire_Breath_(Dragons).md "火焰吐息 (龙)")
- [爆燃火花](Igniting_Spark.md "爆燃火花")
- [多重攻击 (红龙)](Multiattack_(Red_Dragon).md "多重攻击 (红龙)")
- [闷燃之触](Smouldering_Touch.md "闷燃之触")
- [重新施展炫目射线](Recast_Dazzling_Ray.md "重新施展炫目射线")
- [炽热打击](Scorching_Strike.md "炽热打击")
- [灼热血液](Searing_Blood.md "灼热血液")

## 拥有燃烧状态的生物

- [立式火炬](Standing_Torch.md "立式火炬")

## 具有相同堆叠ID的状态

- 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- **无法**通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。

燃烧
|

- 每回合受到 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
- 可通过[协助](Help.md "协助")动作、使用[治疗药水](Potion_of_Healing.md "治疗药水")或获得[濡湿](Wet_(Condition).md "濡湿 (状态)")来移除。
- 如果处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态则免疫。
- [蘸取](Dip.md "蘸取")动作可用于燃烧的角色或物体。

[灼烧](Burning_Fiercely_(Condition).md "灼烧 (状态)")
|

- 每回合受到 1d10⁠⁠[火焰](Fire.md "火焰") 伤害。

[圣火](Holy_Fire_(Condition).md "圣火 (状态)")
|

- 每回合受到 1~4⁠⁠[光耀](Radiant.md "光耀") 伤害。

[熔化](Melting_(Condition).md "熔化 (状态)")
|

- 每回合受到 10d6⁠⁠[火焰](Fire.md "火焰") 伤害。

[翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火 (状态)")
|

- 来自阿弗纳斯核心的火焰吞噬此实体，每回合造成 6d6⁠⁠[火焰](Fire.md "火焰") 伤害。

[灼热光环](Scorching_Aura_(Condition).md "灼热光环 (状态)")
|

- 此实体的攻击额外造成 1d6⁠⁠[火焰](Fire.md "火焰") 伤害，除非目标处于[濡湿](Wet_(Condition).md "濡湿 (状态)")状态。

---
*Source: [Burning (Condition)](https://bg3.wiki/wiki/Burning_(Condition)*