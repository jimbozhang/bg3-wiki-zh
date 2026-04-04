# 休息

**休息**是一种游戏机制，用于恢复失去的[生命值](Hit_Points.md "生命值")和耗尽的[资源](Resources.md "资源")。

## 目录

- [1 概述](#概述)
- [2 长休](#长休)
  - [2.1 完全休息](#完全休息)
  - [2.2 部分休息](#部分休息)
  - [2.3 长休的后果](#长休的后果)
- [3 短休](#短休)
- [4 其他类型](#其他类型)

## 概述

休息可以是长休或短休。**长休**恢复所有失去的生命值和已消耗的资源，而**短休**恢复有限的生命值和较少种类的资源。

## 长休

在营地开始长休

长休主要在[营地](Campsite.md "营地")进行。进行长休会度过夜晚，并消耗40（在硬核或荣誉难度下为80，在自定义难度下最多为120）[营地补给](Camp_supplies.md "营地补给")。

### 完全休息

如果拥有所需的[补给](Camp_supplies.md "营地补给")，队伍可以进行长休，恢复以下内容：

- [生命值](Hit_Points.md "生命值") - 全部
- [法术位](Spells.md#Spell_Slots "法术") - 全部
- [资源](Resources.md "资源") - 全部
- 某些物品动作的使用
- [灵吸怪威能](Illithid_power.md "灵吸怪威能")对话选项
- 两次短休次数

### 部分休息

如果缺乏所需的补给，队伍可以改为进行_部分休息_，恢复以下内容：

- 生命值 - 最多恢复其最大值的一半，向下取整
- 资源 - 最多恢复角色最大值的一半，向下取整
  - 包括职业特定资源，如法术位、[气点](Ki_Point.md "气点")和[卓越骰](Battle_Master.md#Level_3 "战斗大师")
- 冷却时间的刷新，包括物品和职业特性，如[休憩曲](Song_of_Rest.md "休憩曲")、[预兆](Portent.md "预兆")和大多数[灵吸怪威能](Illithid_powers.md "灵吸怪威能")
  - [远域幸运](Luck_of_the_Far_Realms.md "远域幸运")不会恢复，因为它消耗一个隐藏资源，该资源最大值为1，并且从一半向下取整为零（0）。

进行部分长休时，短休次数_不会_恢复。

### 长休的后果

许多[出身](Origin.md "出身")、[伙伴](Companions.md "伙伴")和[营地随从](Camp_Followers.md "营地随从")互动发生在长休时。长休也可以推进某些[时间敏感内容](Time-sensitive_activities.md "时间敏感内容")；此外，每幕都有少数[任务](Quests.md "任务")会在长休时推进。

任何具有“持续时间：直到长休”的[临时加成](Temporary_bonuses.md "临时加成")都会结束。

任何[灵药](Elixirs.md "灵药")的效果都会结束。

## 短休

每长休两次，队伍可以在不前往营地的情况下进行短休。不在活跃队伍中的角色不会从短休中受益，也不会恢复生命值或资源。短休恢复以下内容：

- 生命值 - 最多恢复其最大值的一半，向下取整
- 资源：
  - 5级或以上的[吟游诗人](Bard.md "吟游诗人")恢复其[诗人激励](Bardic_Inspiration_(resource).md) charges
  - [牧师](Cleric.md "牧师")恢复其[引导神力充能](Channel_Divinity_Charge.md "引导神力充能")
  - [德鲁伊](Druid.md "德鲁伊")恢复其[荒野形态充能](Druid.md#Level_2 "德鲁伊")
  - [战士](Fighter.md "战士")恢复其[动作如潮](Action_Surge.md "动作如潮")和[回气](Second_Wind.md "回气")能力的使用，以及其[卓越骰](Battle_Master.md#Level_3 "战斗大师")和[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")。
  - [武僧](Monk.md "武僧")恢复其[气点](Ki_Point.md "气点")
  - [圣武士](Paladin.md "圣武士")恢复其[引导誓言充能](Channel_Oath_Charge.md "引导誓言充能")
  - [邪术师](Warlock.md "邪术师")恢复其[邪术师法术位](Spells.md#Pact_Magic "法术")
- [武器动作](Weapon_actions.md "武器动作")的使用
- [灵吸怪威能](Illithid_powers.md "灵吸怪威能")：
  - [灵能过载](Psionic_Overload.md "灵能过载")
  - [卸力](Force_Tunnel.md "卸力")
  - [怯场](Stage_Fright.md "怯场")
- [冲击之力](Repulsor.md "冲击之力")
  - [隶属之盾](Shield_of_Thralls.md "隶属之盾")
- [黑洞](Black_Hole.md "黑洞")
  - [吞噬智力](Absorb_Intellect.md "吞噬智力")
  - [灵魂受挫](Fracture_Psyche.md "灵魂受挫")

## 其他类型

游戏中还有其他功能类似于休息；

- 2级[吟游诗人](Bard.md "吟游诗人")特性[休憩曲](Song_of_Rest.md "休憩曲")功能与短休相同。
- [深邃浅眠药水](Potion_of_Angelic_Reprieve.md "深邃浅眠药水")功能如同短休（除了恢复所有已消耗的和[法术位](Spell_Slot.md "法术位")），如果消耗它的角色保持睡眠且不受干扰，持续2回合。
- [深邃沉眠药水](Potion_of_Angelic_Slumber.md "深邃沉眠药水")功能如同长休，如果消耗它的角色保持睡眠且不受干扰，持续2回合。
- [神圣干预：光耀复苏](Divine_Intervention_colon__Opulent_Revival.md "神圣干预：光耀复苏")恢复队伍如同他们进行了长休，复活任何倒地的队伍成员，甚至可以在战斗中使用。然而，任何形式的神圣干预在整个游戏中每个角色只能使用一次。
- 使用在序幕中[鹦鹉螺](Nautiloid.md "鹦鹉螺")上或[第二幕](Act_Two.md "第二幕")中[夺心魔殖民地](Mind_Flayer_Colony.md "夺心魔殖民地")内的[恢复站](Restoration.md "恢复站")，[第三幕](Act_Three.md "第三幕")中[希望之邸](House_of_Hope.md "希望之邸")的内室，或同样在第三幕的[至高大殿](High_Hall.md "至高大殿")中的恢复站，也会恢复队伍如同他们进行了长休，_而不会_结束相关效果，如[神莓](Goodberry.md "神莓")或[灵药](Elixirs.md "灵药")。

---
*Source: [Resting](https://bg3.wiki/wiki/Resting)*