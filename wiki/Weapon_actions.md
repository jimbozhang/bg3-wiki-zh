# 武器动作

**武器动作**是根据角色装备的武器而授予的[动作](Action.md "Action")。通常，这些动作是特殊攻击，在某些方面优于普通攻击。每种武器类型都有其独特的武器动作，这有助于区分武器类别。例如，[长剑](Longswords.md "Longswords")授予[割裂](Lacerate.md "Lacerate")、[突进攻击](Rush_Attack.md "Rush Attack")和[剑柄打击](Pommel_Strike.md "Pommel Strike")动作。此外，许多特殊武器除了武器类型授予的动作外，还具有独特的武器动作。

为了获得武器的武器动作，生物必须[重甲的](Proficient.md "Proficient")该武器类型，并将其装备在主手或双手。副手武器不会授予武器动作。

每个武器动作每[短休](Short_rest.md "Short rest")可使用一次，除非另有说明，并且此限制是角色特定的，而非武器特定的。因此，已消耗的武器动作无法通过装备新武器来恢复，但同一武器动作可由不同角色在不进行短休的情况下使用。即使攻击未命中，武器动作也会被消耗。

## 目录

- [1 武器动作DC](#武器动作DC)
- [2 基础武器动作](#基础武器动作)
  - [2.1 基础近战武器动作](#基础近战武器动作)
  - [2.2 基础远程武器动作](#基础远程武器动作)
- [3 独特武器动作](#独特武器动作)
  - [3.1 独特近战武器动作](#独特近战武器动作)
  - [3.2 独特远程武器动作](#独特远程武器动作)
  - [3.3 NPC专属武器动作](#NPC专属武器动作)
  - [3.4 无法获取的武器动作](#无法获取的武器动作)
- [4 武器动作施加的状态](#武器动作施加的状态)
- [5 注释](#注释)

## 武器动作DC

许多武器动作是攻击，可以对目标施加衰弱状态。对于这些攻击，目标可以进行[豁免检定](Saving_throw.md "Saving throw")以避免遭受该状态。[难度等级](Difficulty_Class.md "Difficulty Class")（或DC）的计算方式与[法术豁免DC](Spells.md#Spell_saves "Spells")类似，但有两个区别：首先，[施法关键属性](Spells.md#Spellcasting_ability "Spells")被替换为[力量](Strength.md "Strength")或[敏捷](Dexterity.md "Dexterity")中较高的[属性调整值](Abilities.md#Ability_score_modifiers "Abilities")。其次，每个武器动作可以授予其自身固有的奖励DC，该DC未在任何地方列出，但最常见的是+2。用数学表达如下：

武器动作DC = 8 + [熟练项加值](Proficiency_Bonus.md "Proficiency bonus") + [力量](Strength.md "Strength")或[敏捷](Dexterity.md "Dexterity")调整值 + 武器动作固有奖励DC

某些武器动作使用**混合DC**，允许使用者使用其法术豁免DC或武器动作DC（+2奖励），以较高者为准。其他独特武器动作始终使用法术豁免DC。在所有情况下，DC类型和任何固有奖励均在下面的表格中列出。

在补丁5之前，武器动作的基础DC为10，但未将熟练项加值添加到DC中，导致在5级后熟练项加值增加时总体DC较低。补丁5之后已更改为上述公式。

## 基础武器动作

以下武器动作由不同武器类型授予。给定类别中的所有武器都将具有指定的武器动作。

### 基础近战武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [摔翻打击](Backbreaker.md "Backbreaker") | [战锤](Warhammers.md "Warhammers") / [巨锤](Mauls.md "Mauls") | [动作](Actions#Resources.md#Resources "Actions") | 施加[倒地](Prone_(Condition).md "Prone (Condition)") [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 |
| [备战（近战）](Brace_(Melee).md "Brace (Melee)") | [长柄刀](Glaives.md "长柄刀") / [长矛](Pikes.md "Pikes") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "Resources") | 重掷近战伤害骰并取较高值 持续时间：1回合 | - |
| [劈砍](Cleave.md "Cleave") | [战斧](Battleaxes.md "Battleaxes") / [巨斧](Greataxes.md "Greataxes") / [长戟](Halberds.md "Halberds") / [巨剑](Greatswords.md "Greatswords") | [动作](Actions#Resources.md#Resources "Actions") | 攻击最多3个目标 范围：2米（7英尺）锥形 | 武器伤害减半 任何额外伤害（如来自[至圣斩](Divine_Smite.md "Divine Smite")或[巨武器大师：全力一击](Great_Weapon_Master_colon__All_In.md "Great Weapon Master: All In")）不会减半 |
| [震荡猛击](Concussive_Smash.md "Concussive Smash") | [钉头锤](Morningstars.md "Morningstars") / [短棒](Clubs.md "Clubs") / [轻锤](Light_Hammers.md "Light Hammers") / [硬头锤](Maces.md "Maces") / [战锤](Warhammers.md "Warhammers") / [巨棒](Greatclubs.md "Greatclubs") / [巨锤](Mauls.md "Mauls") [链枷](Flails.md "Flails") | [动作](Actions#Resources.md#Resources "Actions") | 施加[晕眩](Dazed_(Condition).md "Dazed (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 混合DC 持续时间：2回合 | 武器伤害 |
| [跛足打击](Maiming_Strike.md "Maiming Strike") | [战镐](War_Picks.md "War Picks") / [战斧](Battleaxes.md "Battleaxes") | [动作](Actions#Resources.md#Resources "Actions") | 施加[跛足](Maimed_(Condition).md "Maimed (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 |
| [缴械打击](Disarming_Strike.md "Disarming Strike") | [三叉戟](Tridents.md "Tridents") | [动作](Actions#Resources.md#Resources "Actions") | 目标掉落武器 [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 |
| [华舞](Flourish.md "华舞") | [弯刀](Scimitars.md "Scimitars") / [短剑](Shortswords.md "Shortswords") / [刺剑](Rapiers.md "Rapiers") | [附赠动作](Actions#Resources.md#Resources "Actions") | 施加[失衡](Off_Balance_(Condition).md "Off Balance (Condition)") [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 1d4⁠⁠[钝击](Bludgeoning.md "Bludgeoning") 非致命伤害 |
| [惊心打击](Heartstopper.md "Heartstopper") | [钉头锤](Morningstars.md "Morningstars") | [动作](Actions#Resources.md#Resources "Actions") | 施加[胸外伤](Chest_Trauma_(Condition).md "Chest Trauma (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 |
| [割裂](Lacerate.md "Lacerate") | [手斧](Handaxes.md "Handaxes") / [镰刀](Sickles.md "Sickles") / [弯刀](Scimitars.md "Scimitars") / [战斧](Battleaxes.md "Battleaxes") / [长剑](Longswords.md "Longswords") / [长柄刀](Glaives.md "长柄刀") / [巨斧](Greataxes.md "Greataxes") / [巨剑](Greatswords.md "Greatswords") / [长戟](Halberds.md "Halberds") | [动作](Actions#Resources.md#Resources "Actions") | 施加[流血](Bleeding_(Condition).md "Bleeding (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [穿刺打击](Piercing_Strike.md "Piercing Strike") | [匕首](Daggers.md "Daggers") / [刺剑](Rapiers.md "Rapiers") / [短剑](Shortswords.md "Shortswords") / [三叉戟](Tridents.md "Tridents") / [长矛](Pikes.md "Pikes") / [标枪](Javelins.md "Javelins") | [动作](Actions#Resources.md#Resources "Actions") | 施加[开放伤口](Gaping_Wounds_(Condition).md "Gaping Wounds (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [剑柄打击](Pommel_Strike.md "Pommel Strike") | [长剑](Longswords.md "Longswords") / [巨剑](Greatswords.md "Greatswords") | [附赠动作](Actions#Resources.md#Resources "Actions") | 施加[晕眩](Dazed_(Condition).md "Dazed (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 1d4⁠⁠[钝击](Bludgeoning.md "Bludgeoning") 非致命伤害 |
| [准备](Prepare.md "Prepare") | [巨斧](Greataxes.md "Greataxes") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "Resources") | 本回合近战攻击造成额外伤害 | [力量调整值](Ability_score_modifier.md "Ability Score Modifier") ⁠[挥砍](Slashing.md "Slashing") |
| [突进攻击](Rush_Attack.md "Rush Attack") | [长剑](Longswords.md "Longswords") / [短矛](Spears.md "Spears") / [三叉戟](Tridents.md "Tridents") / [长柄刀](Glaives.md "长柄刀") / [长戟](Halberds.md "Halberds") / [长矛](Pikes.md "Pikes") | [动作](Actions#Resources.md#Resources "Actions") / + / [移动速度](Resources#Movement_speed.md#Movement_speed "Resources") | 冲锋最多9米（30英尺）远 / 施加[失衡](Off_Balance_(Condition).md "Off Balance (Condition)") [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 |
| [韧性](Tenacity.md "Tenacity") | [钉头锤](Morningstars.md "Morningstars") / [巨棒](Greatclubs.md "Greatclubs") / [巨锤](Mauls.md "Mauls") [链枷](Flails.md "Flails") | [反应](Actions#Reactions.md#Reactions "Actions") | 未命中时造成伤害 重充：无限使用 | [力量调整值](Ability_score_modifier.md "Ability Score Modifier") ⁠[钝击](Bludgeoning.md "Bludgeoning") 最低1点伤害 |
| [摔绊](Topple.md "Topple") | [长棍](Quarterstaves.md "Quarterstaves") | [动作](Actions#Resources.md#Resources "Actions") | 施加[倒地](Prone_(Condition).md "Prone (Condition)") [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：1回合 | 1d4⁠⁠[钝击](Bludgeoning.md "Bludgeoning") 非致命伤害 |
| [弱化打击](Weakening_Strike.md "Weakening Strike") | [刺剑](Rapiers.md "Rapiers") / [战镐](War_Picks.md "War Picks") / [战锤](Warhammers.md "Warhammers") [链枷](Flails.md "Flails") | [动作](Actions#Resources.md#Resources "Actions") | 施加[弱腕](Weak_Grip_(Condition).md "Weak Grip (Condition)") [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "Damage Roll") 继承武器伤害类型 非致命伤害 |

### 基础远程武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [备战（远程）](Brace_(Ranged).md "Brace (Ranged)") | [重弩](Heavy_Crossbows.md "Heavy Crossbows") / [长弓](Longbows.md "Longbows") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "Resources") | 重掷远程伤害骰并取较高值 持续时间：1回合 | - |
| [腿筋射击](Hamstring_Shot.md "Hamstring Shot") | [短弓](Shortbows.md "Shortbows") / [长弓](Longbows.md "Longbows") | [动作](Actions#Resources.md#Resources "Actions") | 施加[腿筋受伤](Hamstrung_(Condition).md "Hamstrung (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [移动射击](Mobile_Shot.md "Mobile_Shot") | [手弩](Hand_Crossbows.md "Hand Crossbows") | [附赠动作](Actions#Resources.md#Resources "Actions") | 在使用[疾走](Dash.md "Dash")或[撤离](Disengage.md "Disengage")后进行一次附赠动作攻击 | 武器伤害 |
| [穿刺射击](Piercing_Shot.md "Piercing Shot") | [重弩](Heavy_Crossbows.md "Heavy Crossbows") / [轻弩](Light_Crossbows.md "Light Crossbows") / [手弩](Hand_Crossbows.md "Hand Crossbows") | [动作](Actions#Resources.md#Resources "Actions") | 施加[开放伤口](Gaping_Wounds_(Condition).md "Gaping Wounds (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |

## 独特武器动作

以下武器动作仅在特定武器上可用。这些动作在武器类别关联的基础武器动作之外授予。

### 独特近战武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [至上力量](Absolute_Power.md "Absolute Power") | [破誓者](Faithbreaker.md "Faithbreaker") | [动作](Actions#Resources.md#Resources "Actions") | 将目标推回5米（17英尺） [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 法术豁免DC | 武器伤害 / + 力量调整值 / + 1d6⁠⁠[力场](Force.md "Force") |
| [血钱](Blood_Money.md "Blood Money") | [扭曲幸运](Twist_of_Fortune.md "Twist of Fortune") | [动作](Actions#Resources.md#Resources "Actions") | 根据目标携带的金币数量造成额外伤害 目标的金币会被此攻击消耗 | 武器伤害 / + 熟练项加值（每300金币） |
| [血祭](Blood_Sacrifice.md "Blood Sacrifice") | [仪式匕首](Ritual_Dagger.md "Ritual Dagger") | [附赠动作](Actions#Resources.md#Resources "Actions") | 对自身造成1d4⁠⁠[挥砍](Slashing.md "Slashing")伤害。对自身施加[祝福](Bless_(Condition).md "Bless (Condition)")。 持续时间：1回合 | - |
| [巨大冲击](Colossal_Onslaught.md "Colossal Onslaught") | [乔戈拉尔的巨剑](Jorgoral's_Greatsword.md "Jorgoral's Greatsword") | [动作](Actions#Resources.md#Resources "Actions") | 攻击一条直线上的多个目标 范围：6米（20英尺）直线 | 武器伤害 / + 熟练项加值 |
| [腐蚀打击](Corrosive_Strike.md "Corrosive Strike") | [腐蚀链枷](Corrosive_Flail.md "Corrosive Flail") | [动作](Actions#Resources.md#Resources "Actions") | 在目标周围创造一滩[酸液](Acid_(surface).md "Acid (surface)") 降低[护甲等级](Armour_Class.md "Armour Class") 2点 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[强酸](Acid.md "强酸") |
| [至高打击](Crowning_Strike.md "Crowning Strike") | [压迫灵魂之剑](Blade_of_Oppressed_Souls.md "Blade of Oppressed Souls") | [动作](Actions#Resources.md#Resources "Actions") | 施加[疯狂](Crown_of_Madness_(Condition).md "Crown of Madness (Condition)") [智力](Intelligence.md "Intelligence") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[心灵](Psychic.md "Psychic") |
| [黎明爆裂打击](Dawnburst_Strike.md "Dawnburst Strike") | [圣星](The_Sacred_Star.md "The Sacred Star") | [动作](Actions#Resources.md#Resources "Actions") | 在范围内施加[致盲](Blinded_(Condition).md "Blinded (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[光耀](Radiant.md "Radiant") |
| [决斗者的热枕](Dueller's_Enthusiasm.md "Dueller's Enthusiasm") | [决斗者的特权](Duellist's_Prerogative.md "Duellist's Prerogative") | [附赠动作](Actions#Resources.md#Resources "Actions") | 如果未双持，则使用此武器进行一次附赠攻击 重充：每回合 | 武器伤害 |
| [黑暗之刃](Edge_of_Darkness.md "Edge of Darkness") | [莎尔的黄昏短矛](Shar's_Spear_of_Evening.md "Shar's Spear of Evening") | [动作](Actions#Resources.md#Resources "Actions") | 创造一片[黑暗术](Darkness_(cloud).md "Darkness (cloud)")云雾并攻击范围内的所有目标 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 |
| [巨像切割者](Gargantuan_Cleave.md "Gargantuan Cleave") | [沉重巨斧](Very_Heavy_Greataxe.md "Very Heavy Greataxe") | [动作](Actions#Resources.md#Resources "Actions") | 攻击最多3个目标 范围：2米（7英尺）锥形 对自身施加[失衡](Off_Balance_(Gargantuan_Cleave)_(Condition).md "Off Balance (Gargantuan Cleave) (Condition)") 持续时间：1回合 | 武器伤害减半 / + 1d6⁠⁠[挥砍](Slashing.md "Slashing") 来自[巨武器大师](Great_Weapon_Master.md "Great Weapon Master")等的额外伤害不会减半 |
| [全垒打](Grand_Slam.md "Grand Slam") | [绞尸机](Corpsegrinder.md "Corpsegrinder") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 在范围内伤害并推开敌人 推力等于正常[推击](Shove.md "推击")距离 [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 范围：3米（10英尺）半径 | 武器伤害 / + 熟练项加值⁠⁠[雷鸣](Thunder.md "Thunder") |
| [地狱火撕裂](Hellflame_Cleave.md "Hellflame Cleave") | [地狱火巨斧](Hellfire_Greataxe.md "Hellfire Greataxe") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 攻击多个目标并施加[翻腾地狱火](Roiling_Hellfire_(Condition).md "Roiling Hellfire (Condition)") [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 法术豁免DC 范围：3米（10英尺）锥形 创造[地狱火](Hellfire.md "Hellfire")表面 | 武器伤害 / + 2d6⁠⁠[火焰](Fire.md "Fire") |
| [肃静！](Hush_You!.md "Hush You!") | [巫术破除](Witchbreaker.md "Witchbreaker") | [动作](Actions#Resources.md#Resources "Actions") | 施加[沉默](Silenced_(Condition).md "Silenced (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 |
| [月光蝴蝶](Moonlight_Butterflies.md "Moonlight Butterflies") | [月光](Moonlight_Glaive.md "Moonlight Glaive") | [动作](Actions#Resources.md#Resources "Actions") | 创造[月光蝴蝶](Moonlight_Butterflies_(area).md "Moonlight Butterflies (area)")区域 对范围内的生物提供[优势](Advantage.md "Advantage") 范围：2米（7英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值 / + 熟练项加值⁠⁠[心灵](Psychic.md "Psychic") |
| [血肉分离](Part_the_Flesh.md "Part the Flesh") | [血肉裁决者](Fleshrender.md "Fleshrender") | [动作](Actions#Resources.md#Resources "Actions") | 施加[撕裂血肉](Rended_Flesh_(Condition).md "Rended Flesh (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[黯蚀](Necrotic.md "Necrotic") |
| [完美平衡打击](Perfectly_Balanced_Strike.md "Perfectly Balanced Strike") | [贝尔姆](Belm.md "Belm") | [附赠动作](Actions#Resources.md#Resources "Actions") | 使用主手武器进行一次攻击 如果贝尔姆装备在副手，攻击将不会使用贝尔姆。 重充：每回合 | 武器伤害 |
| [生离死别：尖啸](Phalar_Aluve_colon__Shriek.md "Phalar Aluve: Shriek") | [生离死别](Phalar_Aluve.md "Phalar Aluve") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 创造一个使附近敌人减益的光环 受影响的敌人在被攻击时承受1d4⁠⁠[雷鸣](Thunder.md "Thunder")额外伤害 受影响的敌人所有豁免检定承受-1d4惩罚 范围：6米（20英尺）半径 持续时间：5回合 | - |
| [生离死别：歌唱](Phalar_Aluve_colon__Sing.md "Phalar Aluve: Sing") | [生离死别](Phalar_Aluve.md "Phalar Aluve") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 创造一个使附近盟友增益的光环 受影响的盟友攻击掷骰和豁免检定获得1d4奖励 范围：6米（20英尺）半径 持续时间：5回合 | - |
| [毒雾](Poison_Mist.md "Poison Mist") | [争端解决者](Argument_Solver.md "Argument Solver") | [动作](Actions#Resources.md#Resources "Actions") | 创造一片[毒云](Poison_Cloud.md "Poison Cloud")，施加[中毒](Poisoned_(Condition).md "Poisoned (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 法术豁免DC 范围：1.5米（5英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值 / + 熟练项加值⁠⁠[中毒](Poison.md "中毒") |
| [亵渎灾祸](Profane_Scourge.md "Profane Scourge") | [不死灾祸](The_Undead_Bane.md "The Undead Bane") | [动作](Actions#Resources.md#Resources "Actions") | 对[不死生物](Undead.md "Undead")和[恶魔](Fiends.md "Fiends")施加[灾祸](Bane_(Condition).md "Bane (Condition)") [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：3回合 对其他生物类型无效 | 武器伤害 / + 熟练项加值 / + 2d6⁠⁠[挥砍](Slashing.md "Slashing")（仅对不死生物和恶魔） |
| [剃刀狂风](Razor_Gale.md "Razor Gale") | [拉瑞斯安之怒](Larethian's_Wrath.md "Larethian's Wrath") | [动作](Actions#Resources.md#Resources "Actions") | 攻击大锥形范围内的所有敌人 范围：4米（13英尺）锥形 | 武器伤害 / + 熟练项加值 |
| [再生打击](Revitalising_Strike.md "Revitalising Strike") | [跳跳](Hoppy.md "Hoppy") | [动作](Actions#Resources.md#Resources "Actions") | 治疗自身1d6⁠⁠[治疗](Healing.md "治疗") | 武器伤害 / + 熟练项加值⁠⁠[黯蚀](Necrotic.md "Necrotic") |
| [灼热血液](Searing_Blood.md "Searing Blood") | [断裂之刃](Rupturing_Blade.md "Rupturing Blade") | [动作](Actions#Resources.md#Resources "Actions") | 施加[燃烧](Burning_(Condition).md "Burning (Condition)")和[流血](Bleeding_(Condition).md "Bleeding (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 两种状态有独立的豁免检定 对自身造成1d6⁠⁠[挥砍](Slashing.md "Slashing")伤害 | 武器伤害 / + 熟练项加值⁠⁠[火焰](Fire.md "Fire") / + 1d6⁠⁠[火焰](Fire.md "Fire") |
| [碎魂者](Soulbreaker.md "Soulbreaker") | [碎魂者巨剑](Soulbreaker_Greatsword.md "Soulbreaker Greatsword") / [星界银剑](Silver_Sword_of_the_Astral_Plane.md "Silver Sword of the Astral Plane") | [动作](Actions#Resources.md#Resources "Actions") | 施加[震慑](Stunned_(Condition).md "Stunned (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值⁠⁠[心灵](Psychic.md "Psychic") |
| [浸影打击](Shadowsoaked_Blow.md "Shadowsoaked Blow") | [阴影之握](Sword_of_Clutching_Umbra.md "Sword of Clutching Umbra") / [暗夜法官弯刀](Justiciar's_Scimitar.md "Justiciar's Scimitar") | [动作](Actions#Resources.md#Resources "Actions") | 可在不失去[潜行](Hiding_(Condition).md "Hiding (Condition)")的情况下攻击 | 武器伤害 / + 熟练项加值 / + 1d6⁠⁠[心灵](Psychic.md "Psychic") |
| [推翻大个](Topple_the_Big_Folk.md "Topple the Big Folk") | [博德安的巨人杀手](Balduran's_Giantslayer.md "Balduran's Giantslayer") | [动作](Actions#Resources.md#Resources "Actions") | 对大型或更大的目标施加[倒地](Prone_(Condition).md "Prone (Condition)") [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 / + 2d6（如果目标是大型或更大） |
| [解缚打击](Unshackling_Strike.md "Unshackling Strike") | [俄耳甫斯之锤](Orphic_Hammer.md "Orphic Hammer") | [动作](Actions#Resources.md#Resources "Actions") | 移除[束缚](Restrained_(Condition).md "Restrained (Condition)")、[麻痹](Paralysed_(Condition).md "Paralysed (Condition)")和[震慑](Stunned_(Condition).md "Stunned (Condition)") 重充：无限使用 | - |
| [旋风斩](Whirlwind_Attack_(Weapon_Action).md "Whirlwind Attack (Weapon Action)") | [蹁跹清风](The_Dancing_Breeze.md "The Dancing Breeze") / [贝尔姆](Belm.md "Belm") | [动作](Actions#Resources.md#Resources "Actions") | 攻击半径内的所有敌人 范围：2米（7英尺）半径 | 武器伤害 |
| [西风破裂](Zephyr_Break.md "Zephyr Break") | [尼鲁纳](Nyrulna.md "Nyrulna") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 攻击一条直线上的所有生物。施加[失衡](Off_Balance_(Condition).md "Off Balance (Condition)")并将目标推回5米（17英尺） [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 法术豁免DC 范围：12米（40英尺）直线 持续时间：2回合 成功豁免时造成一半伤害 | 6d6⁠⁠[雷鸣](Thunder.md "Thunder") |
| [西风闪](Zephyr_Flash.md "Zephyr Flash") | [尼鲁纳](Nyrulna.md "Nyrulna") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 向前冲锋最多12米（40英尺），攻击路径上的所有敌人。施加[流血](Bleeding_(Condition).md "Bleeding (Condition)")并将目标推回2米（7英尺） [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 15 [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 持续时间：3回合 成功豁免时造成一半伤害 | 6d8⁠⁠[雷鸣](Thunder.md "Thunder") |

### 独特远程武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [奥术弹药](Arcane_Ammunition.md "Arcane Ammunition") | [奥术力场之弩](Crossbow_of_Arcane_Force.md "Crossbow of Arcane Force") | [附赠动作](Actions#Resources.md#Resources "Actions") | 使此武器的伤害增加1d4⁠⁠[力场](Force.md "Force") 持续时间：1回合 | - |
| [致盲射击](Blinding_Shot.md "Blinding Shot") | [出敌不意](Least_Expected.md "Least Expected") | [动作](Actions#Resources.md#Resources "Actions") | 施加[致盲](Blinded_(Condition).md "Blinded (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 |
| [天界光箭](Bolt_of_Celestial_Light.md "Bolt of Celestial Light") | [锻神旋涡](Gontr_Mael.md "Gontr Mael") | [动作](Actions#Resources.md#Resources "Actions") | 使此武器的伤害增加1d4⁠⁠[光耀](Radiant.md "Radiant") 持续时间：10回合 施加[恐慌](Frightened_(Condition).md "Frightened (Condition)") [感知](Wisdom.md "Wisdom") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC 持续时间：2回合 | 武器伤害 / + 熟练项加值 / + 1d8⁠⁠[光耀](Radiant.md "Radiant") |
| [照亮射击](Illuminating_Shot.md "Illuminating Shot") | [组装劲弩](Fabricated_Arbalest.md "Fabricated Arbalest") | [附赠动作](Actions#Resources.md#Resources "Actions") | 施加[光耀法球](Radiating_Orb_(Condition).md "Radiating Orb (Condition)") 持续时间：2回合 重充：无限使用 | 1d4⁠⁠[穿刺](Piercing.md "Piercing") 不受益于大多数伤害加成，包括[神射手](Sharpshooter.md "Sharpshooter") |
| [推撞攻击](Pushing_Attack_(Titanstring_Bow).md "Pushing Attack (Titanstring Bow)") | [泰坦弦弓](Titanstring_Bow.md "Titanstring Bow") | [动作](Actions#Resources.md#Resources "Actions") | 将目标推回4.5米（15英尺） [力量](Strength.md "Strength") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC | 武器伤害 |
| [回头是岸](Reposition_Malefactor.md "Reposition Malefactor") | [地狱火引擎弩](Hellfire_Engine_Crossbow.md "Hellfire Engine Crossbow") | [动作](Actions#Resources.md#Resources "Actions") / [[](#cite_note-fullaction-1 "[")注1] | 将目标拉向你9米（30英尺） [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 15 [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 重充：无限使用 | 武器伤害减半 不受益于大多数伤害加成，包括[神射手](Sharpshooter.md "Sharpshooter") |
| [神圣弹药](Sacred_Munitions.md "Sacred Munitions") | [根德莱尔的渴望](Gandrel's_Aspiration.md "Gandrel's Aspiration") | [附赠动作](Actions#Resources.md#Resources "Actions") | 附魔此武器，对[不死生物](Undead.md "Undead")施加[驱退](Turned_(Condition).md "Turned (Condition)") 增益持续1回合 [驱退](Turned_(Condition).md "Turned (Condition)")持续3回合 拥有[摧毁不死生物](Destroy_Undead.md "Destroy Undead")时，攻击对不死生物造成4d6⁠⁠[光耀](Radiant.md "Radiant")额外伤害 | - |

### NPC专属武器动作

这些武器动作附着在通常仅对特定生物可用的武器上。因此，玩家在不使用漏洞的情况下访问这些武器动作的唯一方法是召唤一个装备相关武器的生物。

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [电气猛击](Electrified_Flail.md "Electrified Flail") | [旋涡链枷](Flail_of_the_Vortex.md "Flail of the Vortex") | [动作](Actions#Resources.md#Resources "Actions") | 施加[震慑](Stunned_(Condition).md "Stunned (Condition)") [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 13 [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[闪电](Lightning.md "Lightning") |
| [寒冬打击](Hiemal_Strike.md "Hiemal Strike") | [深海三叉戟](Trident_of_the_Depths.md "Trident of the Depths") | [动作](Actions#Resources.md#Resources "Actions") | 施加[冻伤](Chilled_(Condition).md "Chilled (Condition)") [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 13 [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[寒冷](Cold.md "寒冷") |
| [过热](Overheat.md "Overheat") | [火矮人战锤](Azer_Warhammer.md "Azer Warhammer") | [附赠动作](Actions#Resources.md#Resources "Actions") | 在范围内施加[灼烧](Burning_Fiercely_(Condition).md "Burning Fiercely (Condition)") [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 15 [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 范围：2米（7英尺）半径 持续时间：3回合 | 1d10⁠⁠[火焰](Fire.md "Fire") |
| [炽热打击](Scorching_Strike.md "Scorching Strike") | [灰烬弯刀](Scimitar_of_Cinder.md "Scimitar of Cinder") | [动作](Actions#Resources.md#Resources "Actions") | 施加[燃烧](Burning_(Condition).md "Burning (Condition)") [DC](Dice_rolls#Save_DCs.md#Save_DCs "Dice rolls") 13 [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[火焰](Fire.md "Fire") |

### 无法获取的武器动作

这些武器动作附着在无法通过正常游戏获取的武器上。它们仍然可以通过第三方工具访问。

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [瞬息飞矢](Blink-of-an-eye_Bolt.md "Blink-of-an-eye Bolt") | [疾速轻弩](Light_Crossbow_of_Speed.md "Light Crossbow of Speed") | [附赠动作](Actions#Resources.md#Resources "Actions") | 使用此武器进行一次附赠攻击 重充：每回合 | 武器伤害 |
| [血腥高歌](Bloodrender.md "Bloodrender") | [穿刺者](The_Impaler.md "The Impaler") | [动作](Actions#Resources.md#Resources "Actions") | 对自身施加[血腥高歌](Bloodrender_(Condition).md "Bloodrender (Condition)") 持续时间：3回合 | 武器伤害 / + 熟练项加值 |
| [夜刃](Frigid_Blade.md "Frigid Blade") | [阿兰德拉的浪涛](Allandra's_Whelm.md "Allandra's Whelm") | [动作](Actions#Resources.md#Resources "Actions") | 施加[冻伤](Frostbitten_(Condition).md "Frostbitten (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[寒冷](Cold.md "寒冷") |
| [裂颅碎击](Headcrack.md "Headcrack") | [投石索](Sling.md "Sling") | [动作](Actions#Resources.md#Resources "Actions") | 施加[晕眩](Dazed_(Condition).md "Dazed (Condition)") [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 武器动作DC 持续时间：2回合 | 武器伤害 非致命伤害 |
| [乘胜追击](Press_the_Advantage.md "Press the Advantage") | [合成斧](Combination_Axe.md "Combination Axe") | [附赠动作](Actions#Resources.md#Resources "Actions") | 在造成[重击](Critical_Hit.md "Critical hit")后，可用主手武器进行一次附赠攻击 | 武器伤害 |
| [坚定打击](Steadfast_Strike.md "Steadfast Strike") | [坚毅巨锤](Steadfast_Maul.md "Steadfast Maul") | [动作](Actions#Resources.md#Resources "Actions") | 附加效果未实现 | 武器伤害 / + 熟练项加值 |

## 武器动作施加的状态

| 状态 | 施加者 / 豁免检定 | 豁免检定惩罚 | 附加效果 | 移除方式 |
| --- | --- | --- | --- | --- |
| [流血](Bleeding_(Condition).md "Bleeding (Condition)") | [割裂](Lacerate.md "Lacerate") (体质) | [体质](Constitution.md "Constitution") | 每回合造成2点⁠⁠[挥砍](Slashing.md "Slashing")伤害，持续2回合 | 治疗 |
| [胸外伤](Chest_Trauma_(Condition).md "Chest Trauma (Condition)") | [惊心打击](Heartstopper.md "Heartstopper") (体质) | [体质](Constitution.md "Constitution") | 2回合内少一个[动作](Actions#Resources.md#Resources "Actions") | 治疗 |
| [跛足](Maimed_(Condition).md "Maimed (Condition)") | [致残打击](Crippling_Strike.md "Crippling Strike") (体质) | [敏捷](Dexterity.md "Dexterity") | [移动速度](Movement_speed.md "Movement Speed")降至0 | 治疗 |
| [晕眩](Dazed_(Condition).md "Dazed (Condition)") | [震荡猛击](Concussive_Smash.md "Concussive Smash") (体质) [剑柄打击](Pommel_Strike.md "Pommel Strike") (体质) | [感知](Wisdom.md "Wisdom") | 无法进行反应，失去敏捷对[护甲等级](Armour_Class.md "Armour Class")的加值 | 盟友[协助](Help.md "Help") |
| [开放伤口](Gaping_Wounds_(Condition).md "Gaping Wounds (Condition)") | [穿刺射击](Piercing_Shot.md "Piercing Shot") (体质) [穿刺打击](Piercing_Strike.md "Piercing Strike") (体质) | - | 2回合内受到攻击时承受额外2点⁠⁠[穿刺](Piercing.md "Piercing")伤害 | 治疗 |
| [腿筋受伤](Hamstrung_(Condition).md "Hamstrung (Condition)") | [腿筋射击](Hamstring_Shot.md "Hamstring Shot") (体质) | - | [移动速度](Movement_speed.md "Movement Speed")减半 | 治疗 |
| [失衡](Off_Balance_(Condition).md "Off Balance (Condition)") | [突进攻击](Rush_Attack.md "Rush Attack") (力量) [华舞](Flourish.md "华舞") (敏捷) | [力量](Strength.md "Strength") [敏捷](Dexterity.md "Dexterity") | 攻击者获得[优势](Advantage.md "Advantage") | 盟友[协助](Help.md "Help")或受到伤害 |
| [倒地](Prone_(Condition).md "Prone (Condition)") | [摔绊](Topple.md "Topple") (力量) [摔翻打击](Backbreaker.md "Backbreaker") (敏捷) | [力量](Strength.md "Strength") [敏捷](Dexterity.md "Dexterity") | 附近攻击者获得[优势](Advantage.md "Advantage") | 使用一半[移动速度](Movement_speed.md "Movement Speed") |
| [弱腕](Weak_Grip_(Condition).md "Weak Grip (Condition)") | [弱化打击](Weakening_Strike.md "Weakening Strike") (力量) | [力量](Strength.md "Strength") [敏捷](Dexterity.md "Dexterity") | 攻击时具有[劣势](Disadvantage.md "Disadvantage") | 盟友[协助](Help.md "Help") |

## 注释

1. ↑ [1.0](#cite_ref-fullaction_1-0) [1.1](#cite_ref-fullaction_1-1) [1.2](#cite_ref-fullaction_1-2) [1.3](#cite_ref-fullaction_1-3) [1.4](#cite_ref-fullaction_1-4) [1.5](#cite_ref-fullaction_1-5) [1.6](#cite_ref-fullaction_1-6) 这些武器动作不计入[额外攻击](Extra_Attack.md "Extra Attack")，并且需要消耗完整的[动作](Actions.md#Resources "Actions")才能使用。

---
*Source: [Weapon actions](https://bg3.wiki/wiki/Weapon_actions)*