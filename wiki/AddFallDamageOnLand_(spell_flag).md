# AddFallDamageOnLand (法术标志)

**AddFallDamageOnLand** 是一个 [法术标志](Spell_flag.md "法术标志")，用于确定动作是否能造成 [坠落伤害](Fall_damage.md "坠落伤害")。如果设置，足够的垂直位移将根据坠落伤害规则造成坠落伤害。此标志设置在大多数跳跃能力以及大多数强制移动目标的动作上。

由没有此标志的动作引起的移动（无论是否强制）都不会触发坠落伤害。此类移动能力的例子包括 [俯冲突袭](Diving_Strike.md "俯冲突袭") 或任何形式的 [飞行](Fly_(class_action).md "飞行（职业动作）")。对于强制移动能力，此标志的应用相当一致，但也有少数例外，例如：

- [黑洞](Black_Hole.md "黑洞")
- [清流鞭：拉扯](Water_Whip_colon__Pull.md "清流鞭：拉扯")
- [风暴之怒](Storm's_Fury.md "风暴之怒")
- [爪击（獾）](Claws_(Badger).md "爪击（獾）")
- [爪击（枭熊）](Claws_(Owlbear).md "爪击（枭熊）")
- [西风闪](Zephyr_Flash.md "西风闪")
- [全垒打](Grand_Slam.md "全垒打")

由于缺少此法术标志，这些动作在将目标推下或拉下悬崖时_无法_造成坠落伤害。

深渊的行为不受此标志影响。

## 拥有 AddFallDamageOnLand 的动作列表

| 名称 | 类型 | 消耗/充能 | 范围/区域 | 掷骰 | 效果 |
| --- | --- | --- | --- | --- | --- |
| [至上力量](Absolute_Power.md "至上力量") | 武器动作 | [短休](Short_rest.md "短休") | 武器 | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[武器](Weapon.md "武器") + 1d6⁠[力场](Force.md "力场") |
| [粘稠之鞭](Adhesive_Whip.md "粘稠之鞭") | 动作 |  | 15 m (50 ft) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [巨人之靴](Boot_of_the_Giants.md "巨人之靴") | 动作 |  | 1.5 m (5 ft) | - | 徒手⁠[钝击](Bludgeoning.md "钝击") |
| [凶蛮跳跃](Brutal_Leap.md "凶蛮跳跃") | 动作 | + 每回合 | 9 m (30 ft) 3 m (10 ft) (半径) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [公牛冲锋](Bull_Rush.md "公牛冲锋") | 动作 | + 每回合 | 9 m (30 ft) (直线) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") |  |
| [冲锋（牛头人）](Charge_(Minotaur).md "冲锋（牛头人）") | 动作 | + 每回合 | 12 m (40 ft) (直线) | [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 4d8 + 4⁠[穿刺](Piercing.md "穿刺") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [冲锋：推击](Charger_colon__Shove.md "冲锋：推击") | 武器动作 | + | 9 m (30 ft) | - |  |
| [震荡爆炸](Concussive_Burst.md "震荡爆炸") | 动作 | 每回合 | 1.5 m (5 ft) 8 m (27 ft) (锥形) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 5d8⁠[雷鸣](Thunder.md "雷鸣") |
| [废黜](Dethrone.md "废黜") | 5级法术 | + [长休](Long_Rest.md "长休") | 30 m (100 ft) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 10d6 + 20⁠[黯蚀](Necrotic.md "黯蚀") |
| [醉意龙卷](Drunken_Inhale.md "醉意龙卷") | 1级法术 |  | 自身 5 m (17 ft) (锥形) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 4d8⁠[中毒](Poison.md "中毒") 施加 [醉酒](Drunk_(Condition).md "醉酒（状态）") |
| [魔能爆](Eldritch_Blast.md "魔能爆") | 戏法 |  | 18 m (60 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d10⁠[力场](Force.md "力场") |
| [强化跳跃](Enhanced_Jump.md "强化跳跃") | 动作 | + | 13 m (43 ft) | - |  |
| [愤怒投掷](Enraged_Throw.md "愤怒投掷") | 动作 |  | 18 m (60 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 正常武器伤害 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [四雷拳](Fist_of_Four_Thunders.md "四雷拳") | 动作 | + 2 | 5 m (17 ft) (立方体) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 2d8⁠[雷鸣](Thunder.md "雷鸣") |
| [凝气刚拳](Fist_of_Unbroken_Air.md "凝气刚拳") | 动作 | + 2 | 9 m (30 ft) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 3d10⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [疾风连击：推击](Flurry_of_Blows_colon__Push.md "疾风连击：推击") | 动作 | + | 1.5 m (5 ft) | 徒手近战 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 徒手⁠[钝击](Bludgeoning.md "钝击") + 徒手⁠[钝击](Bludgeoning.md "钝击") |
| [卸力](Force_Tunnel.md "卸力") | 动作 | [短休](Short_rest.md "短休") | 9 m (30 ft) (直线) | - |  |
| [强力投掷](Forceful_Throw.md "强力投掷") | 动作 |  | 18 m (60 ft) 1 m (3 ft) (半径) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 1d10⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [盖尔（职业动作）](Gale_(class_action).md "盖尔（职业动作）") | 动作 |  | 6 m (20 ft) (锥形) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [顶撞（牛头人）](Gore_(Minotaur).md "顶撞（牛头人）") | 动作 |  | 1.5 m (5 ft) | 徒手近战 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 2d10 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [抓攫触手](Grasping_Appendage.md "抓攫触手") | 动作 | 每回合 | 18 m (60 ft) | - |  |
| [坟墓斥力](Grave_Repulsion.md "坟墓斥力") | 1级法术 | - | 1.5 m (5 ft) 5 m (17 ft) (立方体) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 3d8⁠[黯蚀](Necrotic.md "黯蚀") ( [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 减半) |
| [造风术](Gust_of_Wind.md "造风术") | 2级法术 | + | 自身 12 m (40 ft) (直线) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 施加 [失衡](Off_Balance_(Condition).md "失衡（状态）") |
| [钩子（职业动作）](Hook_(class_action).md "钩子（职业动作）") | 动作 |  | 1.5 m (5 ft) | 徒手近战 [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 2d6 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") 施加 [流血](Bleeding_(Condition).md "流血（状态）") |
| [集群打击](Hordestrike.md "集群打击") | 4级法术 | 每回合 | 16 m (53 ft) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 4d8⁠[力场](Force.md "力场") 施加 [灾祸术](Bane_(Condition).md "灾祸术（状态）") |
| [即兴近战武器](Improvised_Melee_Weapon.md "即兴近战武器") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 物品⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [即兴近战武器（附赠动作）](Improvised_Melee_Weapon_(Bonus_Action).md "即兴近战武器（附赠动作）") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 物品⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [铁意追击](Ironbound_Pursuit.md "铁意追击") | 动作 |  | 1.5 m (5 ft) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 3d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [跳跃](Jump.md "跳跃") | 动作 | + | 4.5 m (15 ft) | - |  |
| [跳跃（奔跑）](Jump_(Running).md "跳跃（奔跑）") | 动作 | 每回合 | [跳跃](Jump.md "跳跃") | - |  |
| [移动华舞（近战）](Mobile_Flourish_(Melee).md "移动华舞（近战）") | 武器动作 | + | 武器 | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 正常武器伤害 + 1d6⁠[武器](Weapon.md "武器") 施加 [移动华舞的目标](Mobile_Flourish_Target_(Condition).md "移动华舞的目标（状态）") 和 [移动华舞](Mobile_Flourish_(Condition).md "移动华舞（状态）") |
| [移动华舞（远程）](Mobile_Flourish_(Ranged).md "移动华舞（远程）") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 正常武器伤害 + 1d6⁠[武器](Weapon.md "武器") 施加 [移动华舞的目标](Mobile_Flourish_Target_(Condition).md "移动华舞的目标（状态）") 和 [移动华舞](Mobile_Flourish_(Condition).md "移动华舞（状态）") |
| [攫取灵魂](Pluck_Soul.md "攫取灵魂") | 动作 |  | 18 m (60 ft) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1d6 + 召唤者魅力调整值⁠[黯蚀](Necrotic.md "黯蚀") |
| [原始践踏](Primal_Stampede.md "原始践踏") | 动作 | + | 9 m (30 ft) (直线) | 徒手近战 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 1d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [灵能牵引](Psionic_Pull.md "灵能牵引") | 动作 | [短休](Short_rest.md "短休") | 18 m (60 ft) | - |  |
| [拉扯之网](Pulling_Web.md "拉扯之网") | 戏法 |  | 9 m (30 ft) | - | 1d6⁠[穿刺](Piercing.md "穿刺") |
| [推撞攻击（近战）](Pushing_Attack_(Melee).md "推撞攻击（近战）") | 武器动作 | + | 武器 | [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + [卓越骰子](Battlemaster#Superiority_dice.md#卓越骰子 "战大师") |
| [推撞攻击（远程）](Pushing_Attack_(Ranged).md "推撞攻击（远程）") | 武器动作 | + | 武器 | [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + [卓越骰子](Battlemaster#Superiority_dice.md#卓越骰子 "战大师") |
| [推撞攻击（泰坦弦弓）](Pushing_Attack_(Titanstring_Bow).md "推撞攻击（泰坦弦弓）") | 武器动作 | [短休](Short_rest.md "短休") | 武器 | [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 |
| [回头是岸（钢铁卫士）](Reposition_Malefactor_(Steel_Watcher).md "回头是岸（钢铁卫士）") | 动作 |  | 14 m (47 ft) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 3d8⁠[钝击](Bludgeoning.md "钝击") |
| [回头是岸](Reposition_Malefactor.md "回头是岸") | 武器动作 |  | 武器 | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 1/2 正常武器伤害 |
| [冲击之力（德罗尔·拉格兹林）](Repulsor_(Dror_Ragzlin).md "冲击之力（德罗尔·拉格兹林）") | 动作 | 每回合 | 自身 6 m (20 ft) (半径) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 1d6⁠[力场](Force.md "力场") |
| [冲击之力（灵吸怪能力）](Repulsor_(Illithid_Power).md "冲击之力（灵吸怪能力）") | 动作 | [短休](Short_rest.md "短休") | 6 m (20 ft) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 2d6⁠[力场](Force.md "力场") |
| [罗兰的雷鸣波](Rolan's_Thunderwave.md "罗兰的雷鸣波") | 1级法术 | + | 1.5 m (5 ft) 5 m (17 ft) (立方体) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 2d6⁠[雷鸣](Thunder.md "雷鸣") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
| [盖尔之灵急冲](Rush_of_the_Gale_Spirits.md "盖尔之灵急冲") | 动作 | + 2 | 12 m (40 ft) (直线) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 施加 [失衡](Off_Balance_(Condition).md "失衡（状态）") |
| [攫取灵魂](Seize_Soul.md "攫取灵魂") | 动作 |  | 18 m (60 ft) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1d6 + 召唤者魅力调整值⁠[黯蚀](Necrotic.md "黯蚀") |
| [幽影狂潮](Shadow_Torrent.md "幽影狂潮") | 动作 |  | 18 m (60 ft) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") |  |
| [盾牌推击](Shield_Shove.md "盾牌推击") | 动作 |  | 1.5 m (5 ft) | - |  |
| [推击](Shove.md "推击") | 动作 |  | 1.5 m (5 ft) | - |  |
| [猛击（食人魔）](Slam_(Ogre).md "猛击（食人魔）") | 动作 |  | 3 m (10 ft) | 徒手近战 [攻击掷骰](Attack_roll.md "攻击掷骰") [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 2d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏（状态）") |
[查看全部](https://bg3.wiki/w/index.php?title=Special:ViewData&tables=actions&fields=_pageName%3Dlink%2C%0Atype%2C%0Aname%2C%0Acontroller_icon%2C%0Aspell_level%2C+spell_school%2C%0Acost%2C+hit_cost%2C%0Afeature_range%2C%0Aaoe%2C+aoe_m%2C%0Aattack_roll%2C%0Asave%2C%0Arecharge%2C%0Adamage_1%2C+damage_1_type%2C+damage_1_info%2C%0Adamage_2%2C+damage_2_type%2C+damage_2_info%2C%0Adamage_3%2C+damage_3_type%2C+damage_3_info%2C%0Adamage_4%2C+damage_4_type%2C+damage_4_info%2C%0Aconditions%2C%0Acreatures%2C%0Aarea%2C%0ACONCAT%28%22name%2C+type%2C+cost-recharge%2C+range-aoe%2C+roll%2C+effects%22%29%3Dcolumns%2C&where=spell_flags+HOLDS+%22AddFallDamageOnLand%22&order_by=name&format=template&offset=50&limit=100&intro=%3Ctable+class%3D%22wikitable+sortable%22+style%3D%22width%3A100%25%3B%22%3E%0A%0A%3Ctr%3E%0A%0A%3Cth%3EName%3C%2Fth%3E%3Cth%3EType%3C%2Fth%3E%3Cth%3ECost%2FRecharge%3C%2Fth%3E%3Cth%3ERange%2FArea%3C%2Fth%3E%3Cth%3ERoll%3C%2Fth%3E%3Cth%3EEffect%3C%2Fth%3E%0A%3C%2Ftr%3E&outro=%3C%2Ftable%3E&more+results+text=View+all&template=Action+table%2Frow&named+args=yes)

---
*Source: [AddFallDamageOnLand (spell flag)](https://bg3.wiki/wiki/AddFallDamageOnLand_(spell_flag)*