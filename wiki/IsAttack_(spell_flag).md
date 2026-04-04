# IsAttack (法术标识)

**IsAttack** 是一个基本未使用的[法术标识](Spell_flag.md "法术标识")。它*不*决定哪些动作被归类为攻击，以用于[额外攻击](Extra_Attack.md "额外攻击")和类似特性。相反，决定哪些动作是攻击的标准是基于攻击掷骰的类型（例如近战武器、徒手等）。

与 `[IsSpell](IsSpell_(法术标识).md)`（它实际决定哪些动作是真正的法术）相比，此标识对游戏玩法的影响极小。

## 拥有 IsAttack 的动作列表

| 名称 | 类型 | 消耗/充能 | 范围/区域 | 掷骰 | 效果 |
| --- | --- | --- | --- | --- | --- |
| [至上力量](Absolute_Power.md "至上力量") | 武器动作 | [短休](Short_rest.md "短休") | 武器 | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[武器](Weapon.md "武器") + 1d6⁠[力场](Force.md "力场") |
| [奥术射击：放逐箭](Arcane_Shot_colon__Banishing_Arrow.md "奥术射击：放逐箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [魅力](Charisma.md "魅力") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害施加 [流放](Banished_(Condition).md "流放 (状态)") |
| [奥术射击：魅惑箭](Arcane_Shot_colon__Beguiling_Arrow.md "奥术射击：魅惑箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 2d6⁠[心灵](Psychic.md "心灵")施加 [魅惑](Charmed_(Condition).md "魅惑 (状态)") |
| [奥术射击：爆裂箭](Arcane_Shot_colon__Bursting_Arrow.md "奥术射击：爆裂箭") | 武器动作 | + | 武器 5 m (17 ft) (半径) | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 正常武器伤害 + 2d6⁠[力场](Force.md "力场") |
| [奥术射击：衰弱箭](Arcane_Shot_colon__Enfeebling_Arrow.md "奥术射击：衰弱箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 2d6⁠[黯蚀](Necrotic.md "黯蚀")施加 [虚弱](Feeble_(Condition).md "虚弱 (状态)") |
| [奥术射击：缠绕箭](Arcane_Shot_colon__Grasping_Arrow.md "奥术射击：缠绕箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 2d6⁠[中毒](Poison.md "中毒") + 2d6⁠[挥砍](Slashing.md "挥砍") (移动时每回合)施加 [缠绕箭：缠绕](Grasping_Arrow_colon__Entangled_(Condition).md "缠绕箭：缠绕 (状态)") |
| [奥术射击：穿透箭](Arcane_Shot_colon__Piercing_Arrow.md "奥术射击：穿透箭") | 武器动作 | + | 自身 10 m (33 ft) (直线) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 1d6⁠[武器](Weapon.md "武器") |
| [奥术射击：追踪箭](Arcane_Shot_colon__Seeking_Arrow.md "奥术射击：追踪箭") | 武器动作 | + | 武器 | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 1d6⁠[力场](Force.md "力场")施加 [妖火](Faerie_Fire_(Condition).md "妖火 (状态)") |
| [奥术射击：暗影箭](Arcane_Shot_colon__Shadow_Arrow.md "奥术射击：暗影箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 正常武器伤害 + 2d6⁠[心灵](Psychic.md "心灵")施加 [目盲](Blinded_(Condition).md "目盲 (状态)") |
| [刺藤](Barbed_Vine.md "刺藤") | 动作 |  | 6 m (20 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[挥砍](Slashing.md "挥砍") |
| [喙啄攻击 (恐鸦)](Beak_Attack_(Dire_Raven).md "喙啄攻击 (恐鸦)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [喙啄攻击 (渡鸦魔宠)](Beak_Attack_(Raven_Familiar).md "喙啄攻击 (渡鸦魔宠)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [喙啄攻击 (幽影诅咒渡鸦)](Beak_Attack_(Shadow-Cursed_Raven).md "喙啄攻击 (幽影诅咒渡鸦)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (獾)](Bite_(Badger).md "啃咬 (獾)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (恐狼)](Bite_(Dire_Wolf).md "啃咬 (恐狼)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (蜘蛛)](Bite_(Spider).md "啃咬 (蜘蛛)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1⁠[穿刺](Piercing.md "穿刺") + 1d4⁠[中毒](Poison.md "中毒") (豁免失败时) |
| [啃咬 (黑豹)](Bite_(Panther).md "啃咬 (黑豹)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 3d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (相位幼蛛)](Bite_(Phase_Spiderling).md "啃咬 (相位幼蛛)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") + 1d4⁠[中毒](Poison.md "中毒") |
| [啃咬 (双脊龙)](Bite_(Dilophosaurus).md "啃咬 (双脊龙)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d10 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") + 1d8⁠[强酸](Acid.md "强酸") |
| [啃咬 (剑齿虎)](Bite_(Sabre-Toothed_Tiger).md "啃咬 (剑齿虎)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺")施加 [倒伏](Prone_(Condition).md "倒伏 (状态)") |
| [啃咬 (狼)](Bite_(Wolf).md "啃咬 (狼)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (观察者眼魔)](Bite_(Spectator).md "啃咬 (观察者眼魔)") | 动作 |  | 2 m (7 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d8 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (老鼠战斗者)](Bite_(Rat_Combatant).md "啃咬 (老鼠战斗者)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (蛰伏伪怪)](Bite_(Cloaker).md "啃咬 (蛰伏伪怪)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 3d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺")施加 [开放伤口](Gaping_Wounds_(Condition).md "开放伤口 (状态)") |
| [啃咬 (鲨蜥兽)](Bite_(Bulette).md "啃咬 (鲨蜥兽)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 4d12 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺")施加 [强酸](Acid_(Condition).md "强酸 (状态)") |
| [啃咬 (幽魂犬)](Bite_(Ghost_Dogs).md "啃咬 (幽魂犬)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 3d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[黯蚀](Necrotic.md "黯蚀") |
| [啃咬 (分支龙)](Bite_(Alioramus).md "啃咬 (分支龙)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 2d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺")施加 [流血](Bleeding_(Condition).md "流血 (状态)") 和 [开放伤口](Gaping_Wounds_(Condition).md "开放伤口 (状态)") |
| [啃咬 (拟形怪)](Bite_(Mimic).md "啃咬 (拟形怪)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 2d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺")施加 [武器被偷！](Weapon_Stolen!_(Condition).md "武器被偷！ (状态)") |
| [啃咬 (豺狼人)](Bite_(Gnoll).md "啃咬 (豺狼人)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (小法妖)](Bite_(Gremishka).md "啃咬 (小法妖)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") + 1d6⁠[力场](Force.md "力场") |
| [啃咬 (老鼠)](Bite_(Rat).md "啃咬 (老鼠)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (蝙蝠)](Bite_(Bat).md "啃咬 (蝙蝠)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (剑刃蜘蛛)](Bite_(Sword_Spider).md "啃咬 (剑刃蜘蛛)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d8 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (波尼)](Bite_(Squire).md "啃咬 (波尼)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺")施加 [冻僵](Bone_Chilled_(Condition).md "冻僵 (状态)") |
| [啃咬 (座狼)](Bite_(Worg).md "啃咬 (座狼)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 4d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (微型蜘蛛)](Bite_(Tiny_Spider).md "啃咬 (微型蜘蛛)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") + 1d4⁠[中毒](Poison.md "中毒") (豁免失败时) |
| [啃咬 (鬣狗)](Bite_(Hyena).md "啃咬 (鬣狗)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (狗)](Bite_(dog).md "啃咬 (狗)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (熊)](Bite_(Bear).md "啃咬 (熊)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (基础)](Bite_(Base).md "啃咬 (基础)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") |
| [致盲伏击 (近战)](Blinding_Ambush_(melee).md "致盲伏击 (近战)") | 武器动作 | 每回合 | 3 m (10 ft) | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 5d10⁠[光耀](Radiant.md "光耀")施加 [目盲](Blinded_(Condition).md "目盲 (状态)") |
| [瞬息飞矢](Blink-of-an-eye_Bolt.md "瞬息飞矢") | 武器动作 |  | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 正常武器伤害 |
| [血骷髅猛击](Blood_Skeleton_Slam.md "血骷髅猛击") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[钝击](Bludgeoning.md "钝击")施加 [流血](Bleeding_(Condition).md "流血 (状态)") |
| [蛙毒](Bufotoxin.md "蛙毒") | 动作 |  | 1.5 m (5 ft) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1⁠[强酸](Acid.md "强酸")施加 [蛙毒](Bufotoxin_(Condition).md "蛙毒 (状态)") |
| [燃烧爪](Burning_Claws.md "燃烧爪") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[挥砍](Slashing.md "挥砍") + 1d4⁠[火焰](Fire.md "火焰") |
| [腐蚀爪](Caustic_Claws.md "腐蚀爪") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 4d8⁠[强酸](Acid.md "强酸") |
| [爪击 (熊荒野形态)](Claws_(Bear_Wild_Shape).md "爪击 (熊荒野形态)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[挥砍](Slashing.md "挥砍") |
| [爪击 (猫)](Claws_(Cat).md "爪击 (猫)") | 动作 |  | 1.5 m (5 ft) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2⁠[挥砍](Slashing.md "挥砍") |
| [爪击 (小魔鬼)](Claws_(Imp).md "爪击 (小魔鬼)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[挥砍](Slashing.md "挥砍") |
| [爪击 (噬脑怪)](Claws_(Intellect_Devourer).md "爪击 (噬脑怪)") | 动作 |  | 1.5 m (5 ft) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[挥砍](Slashing.md "挥砍") |
[查看全部](https://bg3.wiki/w/index.php?title=Special:ViewData&tables=actions&fields=_pageName%3Dlink%2C%0Atype%2C%0Aname%2C%0Acontroller_icon%2C%0Aspell_level%2C+spell_school%2C%0Acost%2C+hit_cost%2C%0Afeature_range%2C%0Aaoe%2C+aoe_m%2C%0Aattack_roll%2C%0Asave%2C%0Arecharge%2C%0Adamage_1%2C+damage_1_type%2C+damage_1_info%2C%0Adamage_2%2C+damage_2_type%2C+damage_2_info%2C%0Adamage_3%2C+damage_3_type%2C+damage_3_info%2C%0Adamage_4%2C+damage_4_type%2C+damage_4_info%2C%0Aconditions%2C%0Acreatures%2C%0Aarea%2C%0ACONCAT%28%22name%2C+type%2C+cost-recharge%2C+range-aoe%2C+roll%2C+effects%22%29%3Dcolumns%2C&where=spell_flags+HOLDS+%22IsAttack%22&order_by=name&format=template&offset=50&limit=100&intro=%3Ctable+class%3D%22wikitable+sortable%22+style%3D%22width%3A100%25%3B%22%3E%0A%0A%3Ctr%3E%0A%0A%3Cth%3EName%3C%2Fth%3E%3Cth%3EType%3C%2Fth%3E%3Cth%3ECost%2FRecharge%3C%2Fth%3E%3Cth%3ERange%2FArea%3C%2Fth%3E%3Cth%3ERoll%3C%2Fth%3E%3Cth%3EEffect%3C%2Fth%3E%0A%3C%2Ftr%3E&outro=%3C%2Ftable%3E&more+results+text=View+all&template=Action+table%2Frow&named+args=yes)

---
*Source: [IsAttack (spell flag)](https://bg3.wiki/wiki/IsAttack_(spell_flag)*