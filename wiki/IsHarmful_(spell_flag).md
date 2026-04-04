# IsHarmful (法术标识)

**IsHarmful** 是一个 [法术标识](Spell_flag.md "法术标识")，用于指示某个动作在特定情境下是否被视为有害。此标识主要由 [庇护术](Sanctuary_(Condition).md "庇护术 (状态)") 和 [魅惑](Charmed_(Condition).md "魅惑 (状态)") 检查，以确定哪些动作会打破这些状态。

此标识不一定会影响中立 NPC 对动作的反应。有些法术如 [疫病术](Contagion.md "疫病术") 被标记为有害，但对 NPC 使用时 _不会_ 引发反应。

## 拥有 IsHarmful 标识的动作列表

| 名称 | 类型 | 消耗/充能 | 范围/区域 | 掷骰 | 效果 |
| --- | --- | --- | --- | --- | --- |
| [破胆斥喝](Abjure_Enemy.md "破胆斥喝") | 动作 | + | 18 米 (60 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [破胆斥喝：恐慌](Abjure_Enemy_colon__Frightened_(Condition).md "破胆斥喝：恐慌 (状态)") 和 [破胆斥喝：缓慢](Abjure_Enemy_colon__Slow_(Condition).md "破胆斥喝：缓慢 (状态)") |
| [吞噬智力](Absorb_Intellect.md "吞噬智力") | 动作 | [短休](Short_rest.md "短休") | 9 米 (30 英尺) | [智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定") | 1d8⁠[治疗](Healing.md "治疗") (初始施加时) + 2d8⁠[治疗](Healing.md "治疗") (1 回合后) + 3d8⁠[治疗](Healing.md "治疗") (2 回合后) + 4d8⁠[治疗](Healing.md "治疗") (3 回合后) 施加 [被吞噬智力](Absorbed_Intellect_(Condition).md "被吞噬智力 (状态)") |
| [酸液飞溅](Acid_Splash.md "酸液飞溅") | 戏法 |  | 18 米 (60 英尺) 2 米 (7 英尺) (半径) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 1d6⁠[强酸](Acid.md "强酸") ( [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 以豁免) |
| [强酸回流](Acidic_Regurgitation.md "强酸回流") | 动作 | 每回合 | 4 米 (13 英尺) | [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 6d8 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[强酸](Acid.md "强酸") 施加 [中度醉酒](Moderately_Inebriated_(Condition).md "中度醉酒 (状态)") |
| [激活巫术箭](Activate_Witch_Bolt.md "激活巫术箭") | 戏法 |  | 30 米 (100 英尺) | - | 1d12⁠[闪电](Lightning.md "闪电") |
| [粘稠之鞭](Adhesive_Whip.md "粘稠之鞭") | 动作 |  | 15 米 (50 英尺) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 施加 [倒伏](Prone_(Condition).md "倒伏 (状态)") |
| [敌意尖啸](Animus_Screech.md "敌意尖啸") | 动作 |  | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 4d6⁠[心灵](Psychic.md "心灵") 施加 [困惑](Confused_(Condition).md "困惑 (状态)") |
| [阿拉贝尔之影纠缠术](Arabella's_Shadow_Entangle.md "阿拉贝尔之影纠缠术") | 1 级法术 |  | 18 米 (60 英尺) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") |  |
| [奥术射击：放逐箭](Arcane_Shot_colon__Banishing_Arrow.md "奥术射击：放逐箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [魅力](Charisma.md "魅力") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 施加 [流放](Banished_(Condition).md "流放 (状态)") |
| [奥术射击：魅惑箭](Arcane_Shot_colon__Beguiling_Arrow.md "奥术射击：魅惑箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 2d6⁠[心灵](Psychic.md "心灵") 施加 [魅惑](Charmed_(Condition).md "魅惑 (状态)") |
| [奥术射击：爆裂箭](Arcane_Shot_colon__Bursting_Arrow.md "奥术射击：爆裂箭") | 武器动作 | + | 武器 5 米 (17 英尺) (半径) | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 普通武器伤害 + 2d6⁠[力场](Force.md "力场") |
| [奥术射击：衰弱箭](Arcane_Shot_colon__Enfeebling_Arrow.md "奥术射击：衰弱箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 2d6⁠[黯蚀](Necrotic.md "黯蚀") 施加 [虚弱](Feeble_(Condition).md "虚弱 (状态)") |
| [奥术射击：缠绕箭](Arcane_Shot_colon__Grasping_Arrow.md "奥术射击：缠绕箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 2d6⁠[中毒](Poison.md "中毒") + 2d6⁠[挥砍](Slashing.md "挥砍") (移动时每回合) 施加 [缠绕箭：缠绕](Grasping_Arrow_colon__Entangled_(Condition).md "缠绕箭：缠绕 (状态)") |
| [奥术射击：穿透箭](Arcane_Shot_colon__Piercing_Arrow.md "奥术射击：穿透箭") | 武器动作 | + | 自身 10 米 (33 英尺) (直线) | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 1d6⁠[武器](Weapon.md "武器") |
| [奥术射击：寻的箭](Arcane_Shot_colon__Seeking_Arrow.md "奥术射击：寻的箭") | 武器动作 | + | 武器 | [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 1d6⁠[力场](Force.md "力场") 施加 [妖火](Faerie_Fire_(Condition).md "妖火 (状态)") |
| [奥术射击：暗影箭](Arcane_Shot_colon__Shadow_Arrow.md "奥术射击：暗影箭") | 武器动作 | + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 2d6⁠[心灵](Psychic.md "心灵") 施加 [目盲](Blinded_(Condition).md "目盲 (状态)") |
| [哈达之臂](Arms_of_Hadar.md "哈达之臂") | 1 级法术 | + | 自身 3 米 (10 英尺) (半径) | [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 2d6⁠[黯蚀](Necrotic.md "黯蚀") 施加 [哈达之臂](Arms_of_Hadar_(Condition).md "哈达之臂 (状态)") |
| [至尊噬咬](Ascendant_Bite.md "至尊噬咬") | 动作 | [短休](Short_rest.md "短休") | 1.5 米 (5 英尺) | - | 6d6⁠[黯蚀](Necrotic.md "黯蚀") (对目标) 6d6⁠[治疗](Healing.md "治疗") (对自身) 施加 [高兴](Happy_(Condition).md "高兴 (状态)") 和 [贫血](Bloodless_(Condition).md "贫血 (状态)") |
| [摔翻打击](Backbreaker.md "摔翻打击") | 武器动作 | [短休](Short_rest.md "短休") | 武器 | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定") | 1d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[钝击](Bludgeoning.md "钝击") 施加 [倒伏](Prone_(Condition).md "倒伏 (状态)") |
| [不祥之兆](Bad_Omen.md "不祥之兆") | 动作 | 每回合 | 9 米 (30 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 2d8⁠[穿刺](Piercing.md "穿刺") 施加 [恐鸦诅咒](Curse_of_the_Dire_Raven_(Condition).md "恐鸦诅咒 (状态)") |
| [灾祸术 (法术)](Bane_(spell).md "灾祸术 (法术)") | 1 级法术 | + | 9 米 (30 英尺) | [魅力](Charisma.md "魅力") [豁免检定](Saving_throws.md "豁免检定") | 施加 [灾祸术](Bane_(Condition).md "灾祸术 (状态)") |
| [班恩之怒](Bane's_Wrath.md "班恩之怒") | 4 级法术 |  | 1.5 米 (5 英尺) | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 普通武器伤害 + 6d6⁠[心灵](Psychic.md "心灵") 施加 [恐慌](Frightened_(Condition).md "恐慌 (状态)") |
| [放逐斩(近战)](Banishing_Smite_(Melee).md "放逐斩(近战)") | 5 级法术 | + + | 武器 | 近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 普通武器伤害 + 5d10⁠[力场](Force.md "力场") 施加 [流放](Banished_(Condition).md "流放 (状态)") |
| [放逐斩(远程)](Banishing_Smite_(Ranged).md "放逐斩(远程)") | 5 级法术 | + + | 武器 | 远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰") | 普通武器伤害 + 5d10⁠[力场](Force.md "力场") 施加 [流放](Banished_(Condition).md "流放 (状态)") |
| [刺藤](Barbed_Vine.md "刺藤") | 动作 |  | 6 米 (20 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[挥砍](Slashing.md "挥砍") |
| [喙啄攻击 (恐鸦)](Beak_Attack_(Dire_Raven).md "喙啄攻击 (恐鸦)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [喙啄攻击 (渡鸦魔宠)](Beak_Attack_(Raven_Familiar).md "喙啄攻击 (渡鸦魔宠)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [喙啄攻击 (幽影诅咒渡鸦)](Beak_Attack_(Shadow-Cursed_Raven).md "喙啄攻击 (幽影诅咒渡鸦)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [降咒](Bestow_Curse.md "降咒") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") |  |
| [降咒：额外伤害](Bestow_Curse_colon__Additional_Damage.md "降咒：额外伤害") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 1d8⁠[黯蚀](Necrotic.md "黯蚀") (施法者每次攻击) 施加 [被诅咒：额外伤害](Cursed_colon__Additional_Damage_(Condition).md "被诅咒：额外伤害 (状态)") |
| [降咒：攻击劣势](Bestow_Curse_colon__Attack_Disadvantage.md "降咒：攻击劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：攻击劣势](Cursed_colon__Attack_Disadvantage_(Condition).md "被诅咒：攻击劣势 (状态)") |
| [降咒：魅力劣势](Bestow_Curse_colon__Charisma_Disadvantage.md "降咒：魅力劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：魅力](Cursed_colon__Charisma_(Condition).md "被诅咒：魅力 (状态)") |
| [降咒：体质劣势](Bestow_Curse_colon__Constitution_Disadvantage.md "降咒：体质劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：体质](Cursed_colon__Constitution_(Condition).md "被诅咒：体质 (状态)") |
| [降咒：敏捷劣势](Bestow_Curse_colon__Dexterity_Disadvantage.md "降咒：敏捷劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：敏捷](Cursed_colon__Dexterity_(Condition).md "被诅咒：敏捷 (状态)") |
| [降咒：恐惧](Bestow_Curse_colon__Dread.md "降咒：恐惧") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：恐惧](Cursed_colon__Dread_(Condition).md "被诅咒：恐惧 (状态)") |
| [降咒：智力劣势](Bestow_Curse_colon__Intelligence_Disadvantage.md "降咒：智力劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：智力](Cursed_colon__Intelligence_(Condition).md "被诅咒：智力 (状态)") |
| [降咒：力量劣势](Bestow_Curse_colon__Strength_Disadvantage.md "降咒：力量劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：力量](Cursed_colon__Strength_(Condition).md "被诅咒：力量 (状态)") |
| [降咒：感知劣势](Bestow_Curse_colon__Wisdom_Disadvantage.md "降咒：感知劣势") | 3 级法术 | + | 1.5 米 (5 英尺) | [感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") | 施加 [被诅咒：感知](Cursed_colon__Wisdom_(Condition).md "被诅咒：感知 (状态)") |
| [啃咬 (獾)](Bite_(Badger).md "啃咬 (獾)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (恐狼)](Bite_(Dire_Wolf).md "啃咬 (恐狼)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (蜘蛛)](Bite_(Spider).md "啃咬 (蜘蛛)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") [体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") | 1⁠[穿刺](Piercing.md "穿刺") + 1d4⁠[中毒](Poison.md "中毒") (豁免检定失败时) |
| [啃咬 (黑豹)](Bite_(Panther).md "啃咬 (黑豹)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 3d6 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (相位幼蛛)](Bite_(Phase_Spiderling).md "啃咬 (相位幼蛛)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") + 1d4⁠[中毒](Poison.md "中毒") |
| [啃咬 (双脊龙)](Bite_(Dilophosaurus).md "啃咬 (双脊龙)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d10 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") + 1d8⁠[强酸](Acid.md "强酸") |
| [啃咬 (剑齿虎)](Bite_(Sabre-Toothed_Tiger).md "啃咬 (剑齿虎)") | 动作 |  | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d6 + [力量调整值](Strength#Strength_modifier_chart.md#Strength_modifier_chart "力量")⁠[穿刺](Piercing.md "穿刺") 施加 [倒伏](Prone_(Condition).md "倒伏 (状态)") |
| [啃咬 (狼)](Bite_(Wolf).md "啃咬 (狼)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [敏捷调整值](Dexterity#Dexterity_modifier_chart.md#Dexterity_modifier_chart "敏捷")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (观察者眼魔)](Bite_(Spectator).md "啃咬 (观察者眼魔)") | 动作 |  | 2 米 (7 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d8 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (吸血鬼衍体)](Bite_(Vampire_Spawn).md "啃咬 (吸血鬼衍体)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 1d6 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") + 2d6⁠[黯蚀](Necrotic.md "黯蚀") 施加 [被吸血](Blood-Sapped_(Condition).md "被吸血 (状态)") |
| [啃咬 (母之憎恨)](Bite_(Mother's_Loathing).md "啃咬 (母之憎恨)") | 动作 | 每回合一次 | 1.5 米 (5 英尺) | 近战徒手 [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4⁠[穿刺](Piercing.md "穿刺") |
| [啃咬 (鼠人战士)](Bite_(Rat_Combatant).md "啃咬 (鼠人战士)") | 动作 |  | 1.5 米 (5 英尺) | [攻击掷骰](Attack_roll.md "攻击掷骰") | 2d4 + [力量或敏捷调整值](Finesse.md "灵巧")⁠[穿刺](Piercing.md "穿刺") |
[查看全部](https://bg3.wiki/w/index.php?title=Special:ViewData&tables=actions&fields=_pageName%3Dlink%2C%0Atype%2C%0Aname%2C%0Acontroller_icon%2C%0Aspell_level%2C+spell_school%2C%0Acost%2C+hit_cost%2C%0Afeature_range%2C%0Aaoe%2C+aoe_m%2C%0Aattack_roll%2C%0Asave%2C%0Arecharge%2C%0Adamage_1%2C+damage_1_type%2C+damage_1_info%2C%0Adamage_2%2C+damage_2_type%2C+damage_2_info%2C%0Adamage_3%2C+damage_3_type%2C+damage_3_info%2C%0Adamage_4%2C+damage_4_type%2C+damage_4_info%2C%0Aconditions%2C%0Acreatures%2C%0Aarea%2C%0ACONCAT%28%22name%2C+type%2C+cost-recharge%2C+range-aoe%2C+roll%2C+effects%22%29%3Dcolumns%2C&where=spell_flags+HOLDS+%22IsHarmful%22&order_by=name&format=template&offset=50&limit=100&intro=%3Ctable+class%3D%22wikitable+sortable%22+style%3D%22width%3A100%25%3B%22%3E%0A%0A%3Ctr%3E%0A%0A%3Cth%3EName%3C%2Fth%3E%3Cth%3EType%3C%2Fth%3E%3Cth%3ECost%2FRecharge%3C%2Fth%3E%3Cth%3ERange%2FArea%3C%2Fth%3E%3Cth%3ERoll%3C%2Fth%3E%3Cth%3EEffect%3C%2Fth%3E%0A%3C%2Ftr%3E&outro=%3C%2Ftable%3E&more+results+text=View+all&template=Action+table%2Frow&named+args=yes)

---
*Source: [IsHarmful (spell flag)](https://bg3.wiki/wiki/IsHarmful_(spell_flag)*