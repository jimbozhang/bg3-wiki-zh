# 武器动作

**武器动作**是根据角色装备的武器而授予的[动作](Action.md "动作")。通常，这些动作是特殊攻击，在某些方面优于普通攻击。每种武器类型都有其独特的武器动作，这有助于区分武器类别。例如，[长剑](Longswords.md "长剑")授予[割裂](Lacerate.md "割裂")、[突进攻击](Rush_Attack.md "突进攻击")和[剑柄打击](Pommel_Strike.md "剑柄打击")动作。此外，许多特殊武器在武器类型授予的动作之外，还拥有独特的武器动作。

为了获得武器的武器动作，生物必须[重甲的](Proficient.md "重甲的")该武器类型，并将其装备在主手或双手。副手武器不会授予武器动作。

每个武器动作每[短休](Short_rest.md "短休")可使用一次，除非另有说明，并且此限制是角色特定的，而非武器特定的。因此，已消耗的武器动作无法通过装备新武器来恢复，但同一武器动作可由不同角色在不进行短休的情况下使用。即使攻击未命中，武器动作也会被消耗。

## 目录

- [1 武器动作难度等级](#武器动作难度等级)
- [2 基本武器动作](#基本武器动作)
  - [2.1 基本近战武器动作](#基本近战武器动作)
  - [2.2 基本远程武器动作](#基本远程武器动作)
- [3 独特武器动作](#独特武器动作)
  - [3.1 独特近战武器动作](#独特近战武器动作)
  - [3.2 独特远程武器动作](#独特远程武器动作)
  - [3.3 NPC专属武器动作](#NPC专属武器动作)
  - [3.4 无法获取的武器动作](#无法获取的武器动作)
- [4 武器动作施加的状态](#武器动作施加的状态)
- [5 备注](#备注)

## 武器动作难度等级

许多武器动作是攻击，可以对目标施加衰弱状态。对于这些攻击，目标可以进行[豁免检定](Saving_throw.md "豁免检定")以避免承受该状态。豁免检定的[难度等级](Difficulty_Class.md "难度等级")（或DC）计算方式类似于[法术豁免DC](Spells.md#Spell_saves "法术")，但有两个不同之处：首先，[施法关键属性调整值](Spells.md#Spellcasting_ability "施法")被替换为[力量](Strength.md "力量")或[敏捷](Dexterity.md "敏捷")中较高的[属性值调整值](Abilities.md#Ability_score_modifiers "属性")。其次，每个武器动作可以授予其自身固有的奖励DC，该DC未在任何地方列出，但最常见的是+2。用数学表达如下：

武器动作DC = 8 + [熟练项加值](Proficiency_Bonus.md "熟练项加值") + [力量](Strength.md "力量")或[敏捷](Dexterity.md "敏捷")调整值 + 固有武器动作奖励DC

某些武器动作使用**混合DC**，允许使用者使用其法术豁免DC或武器动作DC（+2奖励），以较高者为准。其他独特武器动作始终使用法术豁免DC。在所有情况下，DC类型和任何固有奖励均在下面的表格中列出。

在补丁5之前，武器动作的基础DC为10，但不将熟练项加值添加到DC中，导致在5级后熟练项加值增加时总体DC较低。补丁5后已更改为上述公式。

## 基本武器动作

以下武器动作由不同武器类型授予。给定类别中的所有武器都将拥有指定的武器动作。

### 基本近战武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [摔翻打击](Backbreaker.md "摔翻打击") | [战锤](Warhammers.md "战锤") / [巨锤](Mauls.md "巨锤") | [动作](Actions#Resources.md#Resources "动作") | 施加[倒地](Prone_(Condition).md "倒地") [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 |
| [备战（近战）](Brace_(Melee).md "备战（近战）") | [长柄刀](Glaives.md "长柄刀") / [长矛](Pikes.md "长矛") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "资源") | 重掷近战伤害掷骰并取较高值 持续时间：1回合 | - |
| [劈砍](Cleave.md "劈砍") | [战斧](Battleaxes.md "战斧") / [巨斧](Greataxes.md "巨斧") / [长戟](Halberds.md "长戟") / [巨剑](Greatswords.md "巨剑") | [动作](Actions#Resources.md#Resources "动作") | 攻击最多3个目标 范围：2米（7英尺）锥形 | 武器伤害减半 任何额外伤害（如[至圣斩](Divine_Smite.md "至圣斩")或[巨武器大师](Great_Weapon_Master.md "巨武器大师")）不会减半 |
| [震荡猛击](Concussive_Smash.md "震荡猛击") | [钉头锤](Morningstars.md "钉头锤") / [短棒](Clubs.md "短棒") / [轻锤](Light_Hammers.md "轻锤") / [硬头锤](Maces.md "硬头锤") / [战锤](Warhammers.md "战锤") / [巨棒](Greatclubs.md "巨棒") / [巨锤](Mauls.md "巨锤") [链枷](Flails.md "链枷") | [动作](Actions#Resources.md#Resources "动作") | 施加[晕眩](Dazed_(Condition).md "晕眩") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 混合DC 持续时间：2回合 | 武器伤害 |
| [跛足打击](Maiming_Strike.md "跛足打击") | [战镐](War_Picks.md "战镐") / [战斧](Battleaxes.md "战斧") | [动作](Actions#Resources.md#Resources "动作") | 施加[跛足](Maimed_(Condition).md "跛足") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 |
| [缴械打击](Disarming_Strike.md "缴械打击") | [三叉戟](Tridents.md "三叉戟") | [动作](Actions#Resources.md#Resources "动作") | 目标掉落武器 [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 |
| [华舞](Flourish.md "华舞") | [弯刀](Scimitars.md "弯刀") / [短剑](Shortswords.md "短剑") / [刺剑](Rapiers.md "刺剑") | [附赠动作](Actions#Resources.md#Resources "动作") | 施加[失衡](Off_Balance_(Condition).md "失衡") [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 1d4⁠⁠[钝击](Bludgeoning.md "钝击") 非致命伤害 |
| [惊心打击](Heartstopper.md "惊心打击") | [钉头锤](Morningstars.md "钉头锤") | [动作](Actions#Resources.md#Resources "动作") | 施加[胸外伤](Chest_Trauma_(Condition).md "胸外伤") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 |
| [割裂](Lacerate.md "割裂") | [手斧](Handaxes.md "手斧") / [镰刀](Sickles.md "镰刀") / [弯刀](Scimitars.md "弯刀") / [战斧](Battleaxes.md "战斧") / [长剑](Longswords.md "长剑") / [长柄刀](Glaives.md "长柄刀") / [巨斧](Greataxes.md "巨斧") / [巨剑](Greatswords.md "巨剑") / [长戟](Halberds.md "长戟") | [动作](Actions#Resources.md#Resources "动作") | 施加[流血](Bleeding_(Condition).md "流血") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [穿刺打击](Piercing_Strike.md "穿刺打击") | [匕首](Daggers.md "匕首") / [刺剑](Rapiers.md "刺剑") / [短剑](Shortswords.md "短剑") / [三叉戟](Tridents.md "三叉戟") / [长矛](Pikes.md "长矛") / [标枪](Javelins.md "标枪") | [动作](Actions#Resources.md#Resources "动作") | 施加[开放伤口](Gaping_Wounds_(Condition).md "开放伤口") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [剑柄打击](Pommel_Strike.md "剑柄打击") | [长剑](Longswords.md "长剑") / [巨剑](Greatswords.md "巨剑") | [附赠动作](Actions#Resources.md#Resources "动作") | 施加[晕眩](Dazed_(Condition).md "晕眩") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 1d4⁠⁠[钝击](Bludgeoning.md "钝击") 非致命伤害 |
| [准备](Prepare.md "准备") | [巨斧](Greataxes.md "巨斧") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "资源") | 本回合近战攻击造成额外伤害 | [力量调整值](Ability_score_modifier.md "属性值调整值") ⁠[挥砍](Slashing.md "挥砍") |
| [突进攻击](Rush_Attack.md "突进攻击") | [长剑](Longswords.md "长剑") / [短矛](Spears.md "短矛") / [三叉戟](Tridents.md "三叉戟") / [长柄刀](Glaives.md "长柄刀") / [长戟](Halberds.md "长戟") / [长矛](Pikes.md "长矛") | [动作](Actions#Resources.md#Resources "动作") / + / [移动速度](Resources#Movement_speed.md#Movement_speed "资源") | 冲锋最多9米（30英尺）远 / 施加[失衡](Off_Balance_(Condition).md "失衡") [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 |
| [韧性](Tenacity.md "韧性") | [钉头锤](Morningstars.md "钉头锤") / [巨棒](Greatclubs.md "巨棒") / [巨锤](Mauls.md "巨锤") [链枷](Flails.md "链枷") | [反应](Actions#Reactions.md#Reactions "动作") | 未命中时造成伤害 重充：无限使用 | [力量调整值](Ability_score_modifier.md "属性值调整值") ⁠[钝击](Bludgeoning.md "钝击") 最低1点伤害 |
| [摔绊](Topple.md "摔绊") | [长棍](Quarterstaves.md "长棍") | [动作](Actions#Resources.md#Resources "动作") | 施加[倒地](Prone_(Condition).md "倒地") [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：1回合 | 1d4⁠⁠[钝击](Bludgeoning.md "钝击") 非致命伤害 |
| [弱化打击](Weakening_Strike.md "弱化打击") | [刺剑](Rapiers.md "刺剑") / [战镐](War_Picks.md "战镐") / [战锤](Warhammers.md "战锤") [链枷](Flails.md "链枷") | [动作](Actions#Resources.md#Resources "动作") | 施加[弱腕](Weak_Grip_(Condition).md "弱腕") [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 1d4 + [力量或敏捷调整值](Damage_Roll#Modifiers.md#Modifiers "伤害掷骰") 继承武器伤害类型 非致命伤害 |

### 基本远程武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [备战（远程）](Brace_(Ranged).md "备战（远程）") | [重弩](Heavy_Crossbows.md "重弩") / [长弓](Longbows.md "长弓") | 6米（20英尺）[移动速度](Resources#Movement_speed.md#Movement_speed "资源") | 重掷远程伤害掷骰并取较高值 持续时间：1回合 | - |
| [腿筋射击](Hamstring_Shot.md "腿筋射击") | [短弓](Shortbows.md "短弓") / [长弓](Longbows.md "长弓") | [动作](Actions#Resources.md#Resources "动作") | 施加[腿筋受伤](Hamstrung_(Condition).md "腿筋受伤") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |
| [移动射击](Mobile_Shot.md "移动射击") | [手弩](Hand_Crossbows.md "手弩") | [附赠动作](Actions#Resources.md#Resources "动作") | 在使用[疾走](Dash.md "疾走")或[撤离](Disengage.md "撤离")后进行一次附赠动作攻击 | 武器伤害 |
| [穿刺射击](Piercing_Shot.md "穿刺射击") | [重弩](Heavy_Crossbows.md "重弩") / [轻弩](Light_Crossbows.md "轻弩") / [手弩](Hand_Crossbows.md "手弩") | [动作](Actions#Resources.md#Resources "动作") | 施加[开放伤口](Gaping_Wounds_(Condition).md "开放伤口") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 |

## 独特武器动作

以下武器动作仅在特定武器上可用。这些动作在武器类别关联的基本武器动作之外授予。

### 独特近战武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [至上力量](Absolute_Power.md "至上力量") | [破誓者](Faithbreaker.md "破誓者") | [动作](Actions#Resources.md#Resources "动作") | 将目标推回5米（17英尺） [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 法术豁免DC | 武器伤害 / + 力量调整值 / + 1d6⁠⁠[力场](Force.md "力场") |
| [血钱](Blood_Money.md "血钱") | [扭曲幸运](Twist_of_Fortune.md "扭曲幸运") | [动作](Actions#Resources.md#Resources "动作") | 根据目标携带的金币数量造成额外伤害 目标的金币会被此攻击消耗 | 武器伤害 / + 每300金币的熟练项加值 |
| [血祭](Blood_Sacrifice.md "血祭") | [仪式匕首](Ritual_Dagger.md "仪式匕首") | [附赠动作](Actions#Resources.md#Resources "动作") | 对自身造成1d4⁠⁠[挥砍](Slashing.md "挥砍")伤害。对自身施加[祝福](Bless_(Condition).md "祝福")。 持续时间：1回合 | - |
| [巨大冲击](Colossal_Onslaught.md "巨大冲击") | [乔戈拉尔的巨剑](Jorgoral's_Greatsword.md "乔戈拉尔的巨剑") | [动作](Actions#Resources.md#Resources "动作") | 攻击一条线上的多个目标 范围：6米（20英尺）直线 | 武器伤害 / + 熟练项加值 |
| [腐蚀打击](Corrosive_Strike.md "腐蚀打击") | [腐蚀链枷](Corrosive_Flail.md "腐蚀链枷") | [动作](Actions#Resources.md#Resources "动作") | 在目标周围创造一滩[酸液](Acid_(surface).md "酸液") 降低[护甲等级](Armour_Class.md "护甲等级")2点 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[强酸](Acid.md "强酸") |
| [至高打击](Crowning_Strike.md "至高打击") | [压迫灵魂之剑](Blade_of_Oppressed_Souls.md "压迫灵魂之剑") | [动作](Actions#Resources.md#Resources "动作") | 施加[疯狂](Crown_of_Madness_(Condition).md "疯狂") [智力](Intelligence.md "智力") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[心灵](Psychic.md "心灵") |
| [黎明爆裂打击](Dawnburst_Strike.md "黎明爆裂打击") | [圣星](The_Sacred_Star.md "圣星") | [动作](Actions#Resources.md#Resources "动作") | 在范围内施加[致盲](Blinded_(Condition).md "致盲") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[光耀](Radiant.md "光耀") |
| [决斗者的热枕](Dueller's_Enthusiasm.md "决斗者的热枕") | [决斗者的特权](Duellist's_Prerogative.md "决斗者的特权") | [附赠动作](Actions#Resources.md#Resources "动作") | 如果未双持，则使用此武器进行一次附赠攻击 重充：每回合 | 武器伤害 |
| [黑暗之刃](Edge_of_Darkness.md "黑暗之刃") | [莎尔的黄昏短矛](Shar's_Spear_of_Evening.md "莎尔的黄昏短矛") | [动作](Actions#Resources.md#Resources "动作") | 创造一团[黑暗术](Darkness_(cloud).md "黑暗术")并攻击范围内的每个目标 范围：3米（10英尺）半径 持续时间：3回合 | 武器伤害 |
| [巨像切割者](Gargantuan_Cleave.md "巨像切割者") | [沉重巨斧](Very_Heavy_Greataxe.md "沉重巨斧") | [动作](Actions#Resources.md#Resources "动作") | 攻击最多3个目标 范围：2米（7英尺）锥形 施加[失衡](Off_Balance_(Gargantuan_Cleave)_(Condition).md "失衡（巨像切割者）")于自身 持续时间：1回合 | 武器伤害减半 / + 1d6⁠⁠[挥砍](Slashing.md "挥砍") 来自[巨武器大师](Great_Weapon_Master.md "巨武器大师")等的额外伤害不会减半 |
| [全垒打](Grand_Slam.md "全垒打") | [绞尸机](Corpsegrinder.md "绞尸机") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 在范围内伤害并推开敌人 推力等于正常[推击](Shove.md "推击")距离 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 范围：3米（10英尺）半径 | 武器伤害 / + 熟练项加值⁠⁠[雷鸣](Thunder.md "雷鸣") |
| [地狱火撕裂](Hellflame_Cleave.md "地狱火撕裂") | [地狱火巨斧](Hellfire_Greataxe.md "地狱火巨斧") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 攻击多个目标并施加[翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火") [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 法术豁免DC 范围：3米（10英尺）锥形 创造[地狱火](Hellfire.md "地狱火")表面 | 武器伤害 / + 2d6⁠⁠[火焰](Fire.md "火焰") |
| [肃静！](Hush_You!.md "肃静！") | [巫术破除](Witchbreaker.md "巫术破除") | [动作](Actions#Resources.md#Resources "动作") | 施加[沉默](Silenced_(Condition).md "沉默") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 |
| [月光蝴蝶](Moonlight_Butterflies.md "月光蝴蝶") | [月光](Moonlight_Glaive.md "月光") | [动作](Actions#Resources.md#Resources "动作") | 创造[月光蝴蝶](Moonlight_Butterflies_(area).md "月光蝴蝶")区域 为范围内的生物提供[优势](Advantage.md "优势") 范围：2米（7英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值 / + 熟练项加值⁠⁠[心灵](Psychic.md "心灵") |
| [血肉分离](Part_the_Flesh.md "血肉分离") | [血肉裁决者](Fleshrender.md "血肉裁决者") | [动作](Actions#Resources.md#Resources "动作") | 施加[撕裂血肉](Rended_Flesh_(Condition).md "撕裂血肉") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[黯蚀](Necrotic.md "黯蚀") |
| [完美平衡打击](Perfectly_Balanced_Strike.md "完美平衡打击") | [贝尔姆](Belm.md "贝尔姆") | [附赠动作](Actions#Resources.md#Resources "动作") | 使用主手武器进行一次攻击 如果贝尔姆装备在副手，攻击将不会使用贝尔姆。 重充：每回合 | 武器伤害 |
| [生离死别：尖啸](Phalar_Aluve_colon__Shriek.md "生离死别：尖啸") | [生离死别](Phalar_Aluve.md "生离死别") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 创造一个使附近敌人减益的光环 受影响的敌人在被攻击时承受1d4⁠⁠[雷鸣](Thunder.md "雷鸣")额外伤害 受影响的敌人所有豁免检定承受-1d4惩罚 范围：6米（20英尺）半径 持续时间：5回合 | - |
| [生离死别：歌唱](Phalar_Aluve_colon__Sing.md "生离死别：歌唱") | [生离死别](Phalar_Aluve.md "生离死别") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 创造一个使附近盟友增益的光环 受影响的盟友攻击掷骰和豁免检定获得1d4奖励 范围：6米（20英尺）半径 持续时间：5回合 | - |
| [毒雾](Poison_Mist.md "毒雾") | [争端解决者](Argument_Solver.md "争端解决者") | [动作](Actions#Resources.md#Resources "动作") | 创造一团[毒云](Poison_Cloud.md "毒云")，施加[中毒](Poisoned_(Condition).md "中毒") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 法术豁免DC 范围：1.5米（5英尺）半径 持续时间：3回合 | 武器伤害 / + 熟练项加值 / + 熟练项加值⁠⁠[中毒](Poison.md "中毒") |
| [亵渎灾祸](Profane_Scourge.md "亵渎灾祸") | [不死灾祸](The_Undead_Bane.md "不死灾祸") | [动作](Actions#Resources.md#Resources "动作") | 对[不死生物](Undead.md "不死生物")和[恶魔](Fiends.md "恶魔")施加[灾祸](Bane_(Condition).md "灾祸") [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：3回合 对其他生物类型无效 | 武器伤害 / + 熟练项加值 / + 2d6⁠⁠[挥砍](Slashing.md "挥砍")（仅对亡灵和恶魔） |
| [剃刀狂风](Razor_Gale.md "剃刀狂风") | [拉瑞斯安之怒](Larethian's_Wrath.md "拉瑞斯安之怒") | [动作](Actions#Resources.md#Resources "动作") | 攻击大锥形范围内的所有敌人 范围：4米（13英尺）锥形 | 武器伤害 / + 熟练项加值 |
| [再生打击](Revitalising_Strike.md "再生打击") | [跳跳](Hoppy.md "跳跳") | [动作](Actions#Resources.md#Resources "动作") | 治疗自身1d6⁠⁠[治疗](Healing.md "治疗") | 武器伤害 / + 熟练项加值⁠⁠[黯蚀](Necrotic.md "黯蚀") |
| [灼热血液](Searing_Blood.md "灼热血液") | [断裂之刃](Rupturing_Blade.md "断裂之刃") | [动作](Actions#Resources.md#Resources "动作") | 施加[灼烧](Burning_(Condition).md "灼烧")和[流血](Bleeding_(Condition).md "流血") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 两种状态有独立的豁免检定 对自身造成1d6⁠⁠[挥砍](Slashing.md "挥砍") | 武器伤害 / + 熟练项加值⁠⁠[火焰](Fire.md "火焰") / + 1d6⁠⁠[火焰](Fire.md "火焰") |
| [碎魂者](Soulbreaker.md "碎魂者") | [碎魂者巨剑](Soulbreaker_Greatsword.md "碎魂者巨剑") / [星界银剑](Silver_Sword_of_the_Astral_Plane.md "星界银剑") | [动作](Actions#Resources.md#Resources "动作") | 施加[震慑](Stunned_(Condition).md "震慑") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值⁠⁠[心灵](Psychic.md "心灵") |
| [浸影打击](Shadowsoaked_Blow.md "浸影打击") | [阴影之握](Sword_of_Clutching_Umbra.md "阴影之握") / [暗夜法官弯刀](Justiciar's_Scimitar.md "暗夜法官弯刀") | [动作](Actions#Resources.md#Resources "动作") | 可在不失去[潜行](Hiding_(Condition).md "潜行")的情况下攻击 | 武器伤害 / + 熟练项加值 / + 1d6⁠⁠[心灵](Psychic.md "心灵") |
| [推翻大个](Topple_the_Big_Folk.md "推翻大个") | [博德安的巨人杀手](Balduran's_Giantslayer.md "博德安的巨人杀手") | [动作](Actions#Resources.md#Resources "动作") | 对大型或更大的目标施加[倒地](Prone_(Condition).md "倒地") [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 / + 2d6（如果目标是大型或更大） |
| [解缚打击](Unshackling_Strike.md "解缚打击") | [俄耳甫斯之锤](Orphic_Hammer.md "俄耳甫斯之锤") | [动作](Actions#Resources.md#Resources "动作") | 移除[束缚](Restrained_(Condition).md "束缚")、[麻痹](Paralysed_(Condition).md "麻痹")和[震慑](Stunned_(Condition).md "震慑") 重充：无限使用 | - |
| [旋风斩](Whirlwind_Attack_(Weapon_Action).md "旋风斩（武器动作）") | [蹁跹清风](The_Dancing_Breeze.md "蹁跹清风") / [贝尔姆](Belm.md "贝尔姆") | [动作](Actions#Resources.md#Resources "动作") | 攻击半径内的所有敌人 范围：2米（7英尺）半径 | 武器伤害 |
| [西风破裂](Zephyr_Break.md "西风破裂") | [尼鲁纳](Nyrulna.md "尼鲁纳") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 攻击一条线上的所有生物。施加[失衡](Off_Balance_(Condition).md "失衡")并将目标推回5米（17英尺） [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 法术豁免DC 范围：12米（40英尺）直线 持续时间：2回合 成功豁免时造成一半伤害 | 6d6⁠⁠[雷鸣](Thunder.md "雷鸣") |
| [西风闪](Zephyr_Flash.md "西风闪") | [尼鲁纳](Nyrulna.md "尼鲁纳") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 向前冲锋最多12米（40英尺），击中路径上的所有敌人。施加[流血](Bleeding_(Condition).md "流血")并将目标推回2米（7英尺） [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 15 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 持续时间：3回合 成功豁免时造成一半伤害 | 6d8⁠⁠[雷鸣](Thunder.md "雷鸣") |

### 独特远程武器动作

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [奥术弹药](Arcane_Ammunition.md "奥术弹药") | [奥术力场之弩](Crossbow_of_Arcane_Force.md "奥术力场之弩") | [附赠动作](Actions#Resources.md#Resources "动作") | 将此武器的伤害提高1d4⁠⁠[力场](Force.md "力场") 持续时间：1回合 | - |
| [致盲射击](Blinding_Shot.md "致盲射击") | [出敌不意](Least_Expected.md "出敌不意") | [动作](Actions#Resources.md#Resources "动作") | 施加[致盲](Blinded_(Condition).md "致盲") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：2回合 | 武器伤害 / + 熟练项加值 |
| [天界光箭](Bolt_of_Celestial_Light.md "天界光箭") | [锻神旋涡](Gontr_Mael.md "锻神旋涡") | [动作](Actions#Resources.md#Resources "动作") | 将此武器的伤害提高1d4⁠⁠[光耀](Radiant.md "光耀") 持续时间：10回合 施加[恐慌](Frightened_(Condition).md "恐慌") [感知](Wisdom.md "感知") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC 持续时间：2回合 | 武器伤害 / + 熟练项加值 / + 1d8⁠⁠[光耀](Radiant.md "光耀") |
| [照亮射击](Illuminating_Shot.md "照亮射击") | [组装劲弩](Fabricated_Arbalest.md "组装劲弩") | [附赠动作](Actions#Resources.md#Resources "动作") | 施加[光耀法球](Radiating_Orb_(Condition).md "光耀法球") 持续时间：2回合 重充：无限使用 | 1d4⁠⁠[穿刺](Piercing.md "穿刺") 不受益于大多数伤害加成，包括[神射手](Sharpshooter.md "神射手") |
| [推撞攻击](Pushing_Attack_(Titanstring_Bow).md "推撞攻击（泰坦弦弓）") | [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓") | [动作](Actions#Resources.md#Resources "动作") | 将目标推回4.5米（15英尺） [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC | 武器伤害 |
| [回头是岸](Reposition_Malefactor.md "回头是岸") | [地狱火引擎弩](Hellfire_Engine_Crossbow.md "地狱火引擎弩") | [动作](Actions#Resources.md#Resources "动作") / [[](#cite_note-fullaction-1 "[")注1] | 将目标拉向你9米（30英尺） [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 15 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 重充：无限使用 | 武器伤害减半 不受益于大多数伤害加成，包括[神射手](Sharpshooter.md "神射手") |
| [神圣弹药](Sacred_Munitions.md "神圣弹药") | [根德莱尔的渴望](Gandrel's_Aspiration.md "根德莱尔的渴望") | [附赠动作](Actions#Resources.md#Resources "动作") | 为武器附魔，对[不死生物](Undead.md "不死生物")施加[驱退](Turned_(Condition).md "驱退") 增益持续1回合 [驱退](Turned_(Condition).md "驱退")持续3回合 拥有[摧毁不死生物](Destroy_Undead.md "摧毁不死生物")时，攻击对亡灵造成4d6⁠⁠[光耀](Radiant.md "光耀")额外伤害 | - |

### NPC专属武器动作

这些武器动作附着在通常仅对某些生物可用的武器上。因此，玩家在不使用漏洞的情况下获取这些武器动作的唯一方法是召唤一个装备相关武器的生物。

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [电气猛击](Electrified_Flail.md "电气猛击") | [旋涡链枷](Flail_of_the_Vortex.md "旋涡链枷") | [动作](Actions#Resources.md#Resources "动作") | 施加[震慑](Stunned_(Condition).md "震慑") [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[闪电](Lightning.md "闪电") |
| [寒冬打击](Hiemal_Strike.md "寒冬打击") | [深海三叉戟](Trident_of_the_Depths.md "深海三叉戟") | [动作](Actions#Resources.md#Resources "动作") | 施加[冻伤](Chilled_(Condition).md "冻伤") [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[寒冷](Cold.md "寒冷") |
| [过热](Overheat.md "过热") | [火矮人战锤](Azer_Warhammer.md "火矮人战锤") | [附赠动作](Actions#Resources.md#Resources "动作") | 在范围内施加[灼烧](Burning_Fiercely_(Condition).md "灼烧") [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 15 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 范围：2米（7英尺）半径 持续时间：3回合 | 1d10⁠⁠[火焰](Fire.md "火焰") |
| [炽热打击](Scorching_Strike.md "炽热打击") | [灰烬弯刀](Scimitar_of_Cinder.md "灰烬弯刀") | [动作](Actions#Resources.md#Resources "动作") | 施加[灼烧](Burning_(Condition).md "灼烧") [DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 持续时间：2回合 重充：无限使用 | 武器伤害 / + 1d10⁠⁠[火焰](Fire.md "火焰") |

### 无法获取的武器动作

这些武器动作附着在无法通过正常游戏玩法获取的武器上。它们仍然可以通过第三方工具访问。

| 武器动作 | 关联武器 | 消耗 | 效果 | 伤害 |
| --- | --- | --- | --- | --- |
| [瞬息飞矢](Blink-of-an-eye_Bolt.md "瞬息飞矢") | [疾速轻弩](Light_Crossbow_of_Speed.md "疾速轻弩") | [附赠动作](Actions#Resources.md#Resources "动作") | 使用此武器进行一次附赠攻击 重充：每回合 | 武器伤害 |
| [血腥高歌](Bloodrender.md "血腥高歌") | [穿刺者](The_Impaler.md "穿刺者") | [动作](Actions#Resources.md#Resources "动作") | 对自身施加[血腥高歌](Bloodrender_(Condition).md "血腥高歌") 持续时间：3回合 | 武器伤害 / + 熟练项加值 |
| [夜刃](Frigid_Blade.md "夜刃") | [阿兰德拉的浪涛](Allandra's_Whelm.md "阿兰德拉的浪涛") | [动作](Actions#Resources.md#Resources "动作") | 施加[冻伤](Frostbitten_(Condition).md "冻伤") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC + 2 持续时间：3回合 | 武器伤害 / + 熟练项加值⁠⁠[寒冷](Cold.md "寒冷") |
| [裂颅碎击](Headcrack.md "裂颅碎击") | [投石索](Sling.md "投石索") | [动作](Actions#Resources.md#Resources "动作") | 施加[晕眩](Dazed_(Condition).md "晕眩") [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 武器动作DC 持续时间：2回合 | 武器伤害 非致命伤害 |
| [乘胜追击](Press_the_Advantage.md "乘胜追击") | [合成斧](Combination_Axe.md "合成斧") | [附赠动作](Actions#Resources.md#Resources "动作") | 在造成[重击](Critical_Hit.md "重击")后，可用主手武器进行一次附赠攻击 | 武器伤害 |
| [坚定打击](Steadfast_Strike.md "坚定打击") | [坚毅巨锤](Steadfast_Maul.md "坚毅巨锤") | [动作](Actions#Resources.md#Resources "动作") | 附加效果未实现 | 武器伤害 / + 熟练项加值 |

## 武器动作施加的状态

| 状态 | 施加者 / 豁免检定 | 豁免检定惩罚 | 附加效果 | 移除方式 |
| --- | --- | --- | --- | --- |
| [流血](Bleeding_(Condition).md "流血") | [割裂](Lacerate.md "割裂") (体质) | [体质](Constitution.md "体质") | 每回合造成2点⁠⁠[挥砍](Slashing.md "挥砍")伤害，持续2回合 | 治疗 |
| [胸外伤](Chest_Trauma_(Condition).md "胸外伤") | [惊心打击](Heartstopper.md "惊心打击") (体质) | [体质](Constitution.md "体质") | 2回合内少一个[动作](Actions#Resources.md#Resources "动作") | 治疗 |
| [跛足](Maimed_(Condition).md "跛足") | [致残打击](Crippling_Strike.md "致残打击") (体质) | [敏捷](Dexterity.md "敏捷") | [移动速度](Movement_speed.md "移动速度")降至0 | 治疗 |
| [晕眩](Dazed_(Condition).md "晕眩") | [震荡猛击](Concussive_Smash.md "震荡猛击") (体质) [剑柄打击](Pommel_Strike.md "剑柄打击") (体质) | [感知](Wisdom.md "感知") | 无法进行反应，失去敏捷对[护甲等级](Armour_Class.md "护甲等级")的加值 | 盟友[协助](Help.md "协助") |
| [开放伤口](Gaping_Wounds_(Condition).md "开放伤口") | [穿刺射击](Piercing_Shot.md "穿刺射击") (体质) [穿刺打击](Piercing_Strike.md "穿刺打击") (体质) | - | 2回合内受到攻击时承受额外2点⁠⁠[穿刺](Piercing.md "穿刺")伤害 | 治疗 |
| [腿筋受伤](Hamstrung_(Condition).md "腿筋受伤") | [腿筋射击](Hamstring_Shot.md "腿筋射击") (体质) | - | [移动速度](Movement_speed.md "移动速度")减半 | 治疗 |
| [失衡](Off_Balance_(Condition).md "失衡") | [突进攻击](Rush_Attack.md "突进攻击") (力量) [华舞](Flourish.md "华舞") (敏捷) | [力量](Strength.md "力量") [敏捷](Dexterity.md "敏捷") | 攻击者获得[优势](Advantage.md "优势") | 盟友[协助](Help.md "协助")或受到伤害 |
| [倒地](Prone_(Condition).md "倒地") | [摔绊](Topple.md "摔绊") (力量) [摔翻打击](Backbreaker.md "摔翻打击") (敏捷) | [力量](Strength.md "力量") [敏捷](Dexterity.md "敏捷") | 附近攻击者获得[优势](Advantage.md "优势") | 使用一半[移动速度](Movement_speed.md "移动速度") |
| [弱腕](Weak_Grip_(Condition).md "弱腕") | [弱化打击](Weakening_Strike.md "弱化打击") (力量) | [力量](Strength.md "力量") [敏捷](Dexterity.md "敏捷") | 攻击时具有[劣势](Disadvantage.md "劣势") | 盟友[协助](Help.md "协助") |

## 备注

1. ↑ [1.0](#cite_ref-fullaction_1-0) [1.1](#cite_ref-fullaction_1-1) [1.2](#cite_ref-fullaction_1-2) [1.3](#cite_ref-fullaction_1-3) [1.4](#cite_ref-fullaction_1-4) [1.5](#cite_ref-fullaction_1-5) [1.6](#cite_ref-fullaction_1-6) 这些武器动作不计入[额外攻击](Extra_Attack.md "额外攻击")的攻击次数，并且需要消耗完整的[动作](Actions.md#Resources "动作")来使用。

---
*Source: [Weapon actions](https://bg3.wiki/wiki/Weapon_actions)*