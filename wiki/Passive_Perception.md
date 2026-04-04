# 察觉技能

**察觉技能**是基于[感知](Wisdom.md "感知")的[技能](Skills.md "技能")。

生物的感知属性越高，就越有可能在察觉[检定](Checks.md "检定")中成功发现隐藏的物体或生物。

> “
>
> 观察你的环境。发现隐藏的细节。
>
> „

— 游戏内技能描述

## 目录

- [1 熟练项](#proficiency)
- [2 用途](#uses)
  - [2.1 世界察觉](#world-perception)
  - [2.2 被动察觉](#passive-perception)
  - [2.3 隐匿察觉](#stealth-perception)
- [3 提升或惩罚的方法](#ways-to-boost-or-penalize)

## 熟练项

在**察觉技能**上**熟练**的角色在进行[属性检定](Ability_Check.md "属性检定")时可以添加他们的[熟练项加值](Proficiency_Bonus.md "熟练项加值")。

以下职业可以在1级时选择将**察觉技能**作为熟练技能：

- [野蛮人](Barbarian.md "野蛮人")
- [吟游诗人](Bard.md "吟游诗人")
- [德鲁伊](Druid.md "德鲁伊")
- [战士](Fighter.md "战士")
- [游侠](Ranger.md "游侠")
- [游荡者](Rogue.md "游荡者")

以下[种族](Races.md "种族")在**察觉技能**上熟练：

- [精灵](Elf.md "精灵")
- [卓尔](Drow.md "卓尔")

## 用途

### 世界察觉

世界或环境察觉检定用于确定玩家角色是否成功探测到[陷阱](Traps.md "陷阱")、隐藏的容器或机关、伏击或环境中的其他细节。这些是常规的[技能检定](Skill_Check.md "技能检定")，当玩家角色足够接近可被探测的事物时会自动执行。

拥有[地城探索者：察觉](Dungeon_Delver_colon__Perception.md "地城探索者：察觉")专长（来自[地牢探索者](Dungeon_Delver.md "地牢探索者")专长）的角色在这些检定上具有[优势](Advantage.md "优势")。

_注意：_ 这些有时被错误地称为被动察觉检定，这在D&D桌面游戏中通常是，但在《博德之门3》中，它们被实现为自动掷骰。在游戏引擎中，它们被称为 `KnowledgeCheck`。

当进行此类掷骰时，会播放骰子音效，屏幕角落会显示一个小指示器，显示成功或失败。

### 被动察觉

[被动检定](Passive_checks.md "被动检定")是不涉及主动掷d20的属性或技能检定。相反，结果直接由公式决定。对于被动察觉检定：

10 + [感知](Wisdom.md "感知")调整值 + [熟练项加值](Proficiency_Bonus.md "熟练项加值")（如果熟练）+ 优势调整值 +（任何其他调整值）

在《博德之门3》中，被动察觉主要用于非玩家生物，以确定玩家角色需要进行的[隐匿](Stealth.md "隐匿")检定的[难度等级](Difficulty_Class.md "难度等级")，以保持[隐藏](Hide.md "隐藏")。玩家角色进行的掷骰在战斗日志中被列为_隐藏检定_。

许多生物还具有未列出的平坦察觉加值。例如，[枭熊](Owlbear.md "枭熊")有+5加值，[座狼](Worg.md "座狼")有+4加值。然而，由于在检视敌人时不显示技能，此信息在游戏中不易获得。

### 隐匿察觉

当玩家角色执行[隐匿攻击](Stealth_attack.md "隐匿攻击")时，他们会掷隐匿检定以保持不被发现。虽然没有明确显示，但战斗日志中显示的_隐匿检定_的[难度等级](Difficulty_Class.md "难度等级")是由目标或目击者进行的主动察觉检定决定的。上一节提到的特定生物平坦加值适用。

## 提升或惩罚的方法

提高或降低[感知](Wisdom.md "感知")也会在偶数时提升/惩罚感知调整值（因此也影响察觉技能），每2点变化1。

| 名称 | 加值或惩罚 | 备注 |
| --- | --- | --- |
| [伏击者](Ambusher.md "伏击者") | 优势 |  |
| [半身人幸运灵药](Elixir_of_Halfling_Luck.md "半身人幸运灵药") | 优势 | 所有属性检定 |
| [人类通才灵药](Elixir_of_Human_Versatility.md "人类通才灵药") | 熟练项 | 所有技能 |
| [踌躇意志](Faltering_Will.md "踌躇意志") | 劣势 | 所有感知属性检定 |
| [警觉长戟](Halberd_of_Vigilance.md "警觉长戟") | 优势 |  |
| [地狱骑士团长弓](Hellrider_Longbow.md "地狱骑士团长弓") | 优势 |  |
| [法官巨盾](Justiciar's_Greatshield.md "法官巨盾") | 优势 |  |
| [识魂面具](Mask_of_Soul_Perception.md "识魂面具") | +2 |  |
| [塞伦涅的暗夜短矛](Selûne's_Spear_of_Night.md "塞伦涅的暗夜短矛") | 优势 |  |
| [智能盾牌](Sentinel_Shield.md "智能盾牌") | 优势 |  |
| [变形者的恩赐之戒](Shapeshifter's_Boon_Ring.md "变形者的恩赐之戒") | +1d4 | 变形/伪装时的所有属性检定 |
| [变质的糖蜜馅饼](Spoiled_Treacle_Tart.md "变质的糖蜜馅饼") | 劣势 | 所有智力/感知属性检定 |
| [共鸣石](Resonance_Stone.md "共鸣石") | 劣势 | 所有精神属性检定 |
| [卫士盾牌](Watcher's_Shield.md "卫士盾牌") | 优势 |  |
| 名称 | 加值或惩罚 | 备注 |
| --- | --- | --- |
| [至尊噬咬](Ascendant_Bite.md "至尊噬咬") | -1（目标）/ +1（使用者） | 所有属性检定 |
| [星界知识：感知](Astral_Knowledge_colon__Wisdom.md "星界知识：感知") | 熟练项 |  |
| [诗人激励](Bardic_Inspiration_(class_action).md "诗人激励（职业动作）") / [战斗激励](Combat_Inspiration.md "战斗激励") | +1d6 / +1d8 / +1d10 | 下一次属性检定 |
| [扭曲幸运：属性检定加值](Bend_Luck_colon__Ability_Check_Bonus.md "扭曲幸运：属性检定加值") | +1d4 | 所有属性检定 |
| [降咒：感知劣势](Bestow_Curse_colon__Wisdom_Disadvantage.md "降咒：感知劣势") | 劣势 | 所有感知属性检定 |
| [强化魔法：恩赐](Bolstering_Magic_colon__Boon.md "强化魔法：恩赐") | +1d4 | 所有属性检定 |
| [疫病术：失明症](Contagion_colon__Blinding_Sickness.md "疫病术：失明症") | 劣势 | 所有感知属性检定 |
| [宇宙预兆：属性检定](Cosmic_Omen_colon__Ability_Check.md "宇宙预兆：属性检定") | +1d6 | 所有属性检定 |
| [语出惊人](Cutting_Words.md "语出惊人") | -1d6 | 所有属性检定 |
| [埃赛尔的虫群瘟疫](Ethel's_Insect_Plague.md "埃赛尔的虫群瘟疫") | 劣势 |  |
| [神导术](Guidance.md "神导术") | +1d4 | 所有属性检定 |
| [脆弱诅咒（感知）](Hex_(Wisdom).md "脆弱诅咒（感知）") | 劣势 | 所有感知属性检定 |
| [精通诗人激励](Improved_Bardic_Inspiration_(class_action).md "精通诗人激励（职业动作）") | +1d12 | 下一次属性检定 |
| [虫群瘟疫](Insect_Plague.md "虫群瘟疫") | 劣势 |  |
| [岁月知识：感知](Knowledge_of_the_Ages_colon__Wisdom.md "岁月知识：感知") | 熟练项 |  |
| [枭之感知](Owl's_Wisdom.md "枭之感知") | 优势 | 所有感知属性检定 |
| [心灵撕裂](Psychic_Rend.md "心灵撕裂") | 劣势 | 所有智力/感知属性检定 |
| [吸血鬼之噬](Vampire_Bite.md "吸血鬼之噬") | -1（目标）/ +1（使用者） | 所有属性检定 |

---
*Source: [Perception](https://bg3.wiki/wiki/Perception)*