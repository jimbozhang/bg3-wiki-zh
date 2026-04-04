# 动作

"Action" 重定向至此。关于资源，请参阅 [资源#动作](Resources.md#Action "资源")。

**动作** 是 _博德之门3_ 中 [生物](Creatures.md "生物") 在其回合内采取的行为。动作通常用于造成 [伤害](Damage.md "伤害") 或施加有害的 [状态](Conditions.md "状态")，但也可以用于 [治疗](Healing.md "治疗") 或援助盟友。

一种特殊形式的动作——称为 **反应**——可用于响应特定触发条件，包括在 _其他_ 生物的回合中。

采取动作通常需要行动生物消耗三种 [资源](Resources.md "资源") 之一：

- 动作
- 附赠动作
- 反应

## 目录

- [1 概述](#概述)
- [2 资源](#资源)
  - [2.1 例外情况](#例外情况)
- [3 反应](#反应)
  - [3.1 反应标签页](#反应标签页)
  - [3.2 限制](#限制)
    - [3.2.1 反应忽略的事件](#反应忽略的事件)
    - [3.2.2 阻止反应](#阻止反应)
  - [3.3 反应示例](#反应示例)
    - [3.3.1 法术](#法术)
    - [3.3.2 职业动作](#职业动作)
- [4 常见动作列表](#常见动作列表)
  - [4.1 动作](#动作)
  - [4.2 附赠动作](#附赠动作)
- [5 错误](#错误)
- [6 另见](#另见)
- [7 注释](#注释)

## 概述

动作按其来源分类：

常见动作
所有生物均可使用的动作。
职业动作
通过 [特性](Features.md "特性") 可用的动作，例如从 [职业](Classes.md "Classes") 或 [装备](Equipment.md "装备") 获得的动作。许多 [NPC](Non-player_characters.md "非玩家角色") 采取的动作也被视为职业动作。
种族动作
通过种族特性可用的动作，且仅从 [种族](Race.md "种族") 获得。
情境动作
因其他能力、特性或状态而解锁的动作。它会保留在角色的热键栏侧面，直到创建它的条件过期。一个这样的例子是 [强制策动](Forced_Manoeuvre.md "强制策动")，这是 [策动攻击（近战）](Manoeuvring_Attack_(Melee).md "策动攻击（近战）") 的结果。
武器动作
[武器动作](Weapon_actions.md "武器动作") 是通过装备 [武器](Weapons.md "武器") 可用的动作。
法术
[法术](Spells.md "法术") 由施法者和其他生物通过使用 [卷轴](Scrolls.md "卷轴") 施放。

## 资源

生物在 [回合制模式](Turn-based_mode.md "回合制模式") 中通过消耗两种 [资源](Resources.md "资源") 之一来采取动作：动作或附赠动作。

此外，一些动作需要消耗 _两种_ 资源。

额外的资源——反应——用于在其他生物的回合中采取有条件的 [反应](Reactions.md "反应")。

所有生物在每回合开始时拥有每种资源各 1 点，但可以从 [各种来源](Sources_of_additional_actions.md "额外动作来源") 获得额外的点数。

### 例外情况

额外动作

- 允许生物每回合采取 _额外_ 动作的动作——例如 [动作如潮](Action_Surge.md "动作如潮")——_不会_ 消耗它们提供的资源。

自由攻击

- 拥有 [额外攻击](Extra_Attack.md "额外攻击") 特性的职业可以在其回合内采取一次攻击动作后，再进行一次自由攻击动作，而无需消耗动作资源。
- 11 级 [战士](Fighter.md "战士") 拥有 [精通额外攻击](Improved_Extra_Attack.md "精通额外攻击") 特性，可以在其回合内采取一次攻击动作后，再进行两次自由攻击动作，而无需消耗动作资源。

## 反应

图 1 - 激活的反应。每个图标上的对话气泡表示这些反应设置为“询问”。

反应是响应触发条件而采取的动作，即使在其他生物的回合中被触发也可以采取。

一些反应要求行动生物消耗 [反应](#reactions) 资源，而其他反应则不需要。不需要消耗的通常是使用反应系统的职业特性，例如 [至圣斩](Divine_Smite.md "至圣斩")、[鲁莽攻击](Reckless_Attack.md "鲁莽攻击") 或 [偷袭](Sneak_Attack.md "偷袭")。<sup>[\[1\]](#cite_note-1)</sup>

### 反应标签页

图 2 - 反应标签页。每个反应都可以通过左侧的复选框启用或禁用。可以使用“询问”设置进行进一步配置，以便在每次触发反应时提示玩家确认。

反应通过 _反应标签页_ 为每个角色进行管理，该标签页位于角色表的法术书页面上。也可以通过按下热键栏上的激活反应之一或按下快捷键（默认：L）立即访问该标签页。

反应可以设置为自动采取，或者可以将游戏设置为首先提示玩家。

如果采取反应会消耗任何资源，它们会列在反应名称下方。

### 限制

如果任何反应提示确认，角色无法对同一事件应用多个反应；UI 会阻止为每个角色选择多个反应。

事件触发的反应集在它们生效之前就已确定。这意味着，如果攻击掷骰或豁免检定通常会忽略某个反应（例如，因为掷骰成功而反应是来自盟友的掷骰加值），即使掷骰结果被另一个反应改变，也会忽略该反应。

#### 反应忽略的事件

大多数反应只“看到”直接攻击或法术，因此通常只在动作的即时效果上触发。如果伤害和豁免检定源自以下来源，反应系统会忽略它们：

- 次要或延迟效果：来自地表、环境危害或持续状态的伤害（例如，内置在 [区域](Areas.md "区域") 效果、[人类定身术](Hold_Person.md "人类定身术") 等状态、反应或爆炸物品（箭矢和发射的烟花除外）中的豁免检定或伤害）
- 间接动作：由单独的反应（[炼狱叱喝](Hellish_Rebuke.md "炼狱叱喝")）或被动特性（[火焰护盾](Fire_Shield.md "火焰护盾") 或 [荆棘丛生](Spike_Growth.md "荆棘丛生")）发起的动作

**例外情况**：有关特定触发条件的完整列表——例如 [专注](Concentration.md "专注") 豁免检定或 [死亡豁免检定](Death_Saving_Throw.md "死亡豁免检定")——请参见下面列出的例外情况：<sup>[\[2\]](#cite_note-2)</sup>

被动特性的豁免检定会被忽略，但以下情况除外：

- [残响](Reverberation_(Condition).md "残响（状态）")<sup>[\[3\]](#cite_note-hiddenpassive-3)</sup>
- [灾祸油](Oil_of_Bane.md "灾祸油") 和 [收缩油](Oil_of_Diminution.md "收缩油") 涂层<sup>[\[3\]](#cite_note-hiddenpassive-3)</sup>
- [简易毒素](Simple_Toxin.md "简易毒素")、[蛇牙毒素](Serpent_Fang_Toxin.md "蛇牙毒素")、[翼龙毒素](Wyvern_Toxin.md "翼龙毒素") 和 [紫虫毒素](Purple_Worm_Toxin.md "紫虫毒素") 涂层<sup>[\[3\]](#cite_note-hiddenpassive-3)</sup>
- 由以下装备授予的被动特性：
  - [烬蛾披风](Cindermoth_Cloak.md "烬蛾披风")
  - [小丑之锤](Clown_Hammer.md "小丑之锤")
  - [黑暗移位手套](Dark_Displacement_Gloves.md "黑暗移位手套")
  - [残缺的黯狱护甲](Flawed_Helldusk_Armour.md "残缺的黯狱护甲")
  - [锻神旋涡](Gontr_Mael.md "锻神旋涡")
  - [腐液手套](Ichorous_Gloves.md "腐液手套")
  - [暗夜法官弯刀](Justiciar's_Scimitar.md "暗夜法官弯刀")
  - [玛科赫什基](Markoheshkir.md "玛科赫什基")（[酸性](Adrip_with_Kereska's_Acid_(Condition).md "克雷斯卡的酸液滴落（状态）")）
  - [悼霜](Mourning_Frost.md "悼霜")
  - [自然陷阱](Nature's_Snare.md "自然陷阱")
  - [投毒者的手套](Poisoner's_Gloves.md "投毒者的手套")
- 以下 NPC 被动特性：
  - [波尔的忠诚](BOOOAL's_Faithful.md "波尔的忠诚")
  - [腐蚀攻击](Caustic_Strikes.md "腐蚀攻击")
  - [炫目连击](Dazzling_Blows.md "炫目连击")
  - [鱼人忠诚](Fishfolk_Faithful.md "鱼人忠诚")
  - [恐惧形态](Form_of_Dread.md "恐惧形态")<sup>[\[3\]](#cite_note-hiddenpassive-3)</sup>
  - [森林之握](Grasp_of_the_Forest.md "森林之握")
  - [传染疯狂](Infectious_Madness.md "传染疯狂")
  - [感染](Infested.md "感染")
  - [缠绕藤蔓形态](Tanglevine_Form.md "缠绕藤蔓形态")

#### 阻止反应

许多状态可以阻止生物采取反应。这些包括：<sup>[\[4\]](#cite_note-4)</sup>

- 任何 [逃跑状态](Fleeing_(status_group).md) 例如 [恐惧](Fearful_(Condition).md "恐惧（状态）")
- 任何 [失能状态](Incapacitated_(status_group).md) 例如 [人类定身术](Hold_Person_(Condition).md "人类定身术（状态）")
- 任何 [隐形状态](SG_Invisible.md "隐形状态组")，这会阻止除 [受诅咒的幽鬼](Accursed_Spectre_(reaction).md "受诅咒的幽鬼（反应）")、[致盲伏击](Blinding_Ambush.md "致盲伏击") 和 [怪异魔法涌动](Weird_Magic_Surge.md "怪异魔法涌动") 之外的所有反应
- 任何 [变形状态](Polymorphed_(status_group).md) 除了 [伪装](SG_Disguise.md "伪装") 和 [星形形态](Starry_Form.md "星形形态") _\[[参见：错误](#bugs)\]_
- 任何 [束缚状态](Restrained_(status_group).md) 例如 [诱捕](Ensnared_(Condition).md "诱捕（状态）")
- 任何 [震慑状态](Stunned_(status_group).md), 即 [震慑](Stunned_(Condition).md "震慑（状态）")
- 任何 [昏迷状态](Unconscious_(status_group).md) 例如 [倒伏](Prone_(Condition).md "倒伏（状态）")

其他状态会阻止生物消耗 [反应](#reactions) 资源。这些包括：

- [哈达之臂](Arms_of_Hadar_(Condition).md "哈达之臂（状态）")
- [眩晕](Dazed_(Condition).md "眩晕（状态）")
- [电爪](Shocking_Grasp_(Condition).md "电爪（状态）")
- [减速](Slowed_(Condition).md "减速（状态）")
- [受惊](Surprised_(Condition).md "受惊（状态）")

后一组状态不会阻止受影响的生物采取不消耗 [反应](#reactions) 资源的反应。此类反应尤其包括 [传奇动作](Legendary_actions.md "传奇动作")，由 [荣誉模式](Honour_Mode.md "荣誉模式") 中的BOSS执行。这些动作像反应一样触发，但使用不同的资源，因此不受这些状态的影响。

### 反应示例

#### 法术

- [法术反制](Counterspell.md "法术反制")
- [炼狱叱喝](Hellish_Rebuke.md "炼狱叱喝")
- [护盾术](Shield_(spell).md "护盾术（法术）")

#### 职业动作

- [语出惊人](Cutting_Words.md "语出惊人")
- [拨挡飞弹](Deflect_Missiles.md "拨挡飞弹")
- [毁灭狂怒](Destructive_Wrath.md "毁灭狂怒")
- [熵光结界](Entropic_Ward.md "熵光结界")
- [真菌感染](Fungal_Infestation.md "真菌感染")
- [巨人杀手](Giant_Killer.md "巨人杀手")
- [吉斯洋基招架](Githyanki_Parry.md "吉斯洋基招架")
- [异界幸运](Luck_of_the_Far_Realms.md "异界幸运")
- [雾遁](Misty_Escape.md "雾遁")
- [借机攻击](Opportunity_Attack.md "借机攻击")
- [反击](Riposte.md "反击")
- [极效吉斯洋基招架](Supreme_Githyanki_Parry.md "极效吉斯洋基招架")
- [韧性](Tenacity.md "韧性")
- [守御闪光](Warding_Flare.md "守御闪光")
- [风暴狂怒](Wrath_of_the_Storm.md "风暴狂怒")

## 常见动作列表

### 动作

- [疾走](Dash.md "疾走")
- [撤离](Disengage.md "撤离")
- [协助](Help.md "协助")
- [即兴近战武器](Improvised_Melee_Weapon.md "即兴近战武器")
- [主手攻击](Main_Hand_Attack.md "主手攻击")
- [表演](Perform.md "表演")
- [远程攻击](Ranged_Attack.md "远程攻击")
- [投掷](Throw.md "投掷")
- [徒手打击](Unarmed_Strike.md "徒手打击")

### 附赠动作

- [蘸取](Dip.md "蘸取")
- [跳跃](Jump.md "跳跃")
- [副手攻击（近战）](Off-Hand_Attack_(Melee).md "副手攻击（近战）")
- [副手攻击（远程）](Off-Hand_Attack_(Ranged).md "副手攻击（远程）")
- [推击](Shove.md "推击")

## 错误

- 对豁免检定的反应会忽略 [惊惧斩](Staggering_Smite.md "惊惧斩")、[雷鸣打击](Thunderous_Smite.md "雷鸣打击") 和 [激愤斩](Wrathful_Smite.md "激愤斩") 以及 [推翻大个](Topple_the_Big_Folk.md "推翻大个") 的豁免检定。
- 大多数通常因非伪装、非星形形态的变形状态（例如其他荒野形态）而被禁用的反应，如果生物同时具有伪装或星形形态状态，则会被错误地启用。

## 另见

- [类别：附赠动作](Category_colon_Bonus_actions.md "类别：附赠动作")，所有附赠动作的类别。

## 注释

1. [↑](#cite_ref-1) 许多在 _博德之门3_ 中作为反应实现的职业特性，在基于 D&D 5 版的 _博德之门3_ 中并非反应。这一改变可能是因为反应在游戏开发后期才添加。
2. [↑](#cite_ref-2) 此限制是 `InterruptContext` 标志 `OnPostRoll` 和 `OnPreDamage` 固有的。`OnPostRoll` 反应可以在被动特性 `StatsFunctors` 的 `SavingThrow()` 调用上触发，但不能在其 `Conditions` 上触发。`OnPostRoll` 反应会忽略嵌套在函数参数中的 `SavingThrow()` 调用。
3. ↑ [3.0](#cite_ref-hiddenpassive_3-0) [3.1](#cite_ref-hiddenpassive_3-1) [3.2](#cite_ref-hiddenpassive_3-2) [3.3](#cite_ref-hiddenpassive_3-3) 相关的豁免检定由隐藏的被动特性执行。
4. [↑](#cite_ref-4) 源自 `Mods/Shared/Scripts/thoth/helpers/CommonConditions.khn` 中 `IsAbleToReact` 的定义、`EnableCondition` 字段数据（用于变形）和 `InterruptWhileInvisible` 标志。反应可能同时检查变形和 `IsAbleToReact`，只检查其中一个，或都不检查。

---
*Source: [Actions](https://bg3.wiki/wiki/Actions)*