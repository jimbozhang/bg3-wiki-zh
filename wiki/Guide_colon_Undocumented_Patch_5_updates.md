# 指南：未记录的5号补丁更新

这是一个[社区指南](Guide_colon_Index.md "Guide:Index")，任何人都可以编辑。请参阅[样式手册](Help_colon_Style_manual.md "Help:Style manual")了解指南。

5号补丁发布时附带了巨大的更新日志，其中包含重大更改，例如引入[荣誉模式](Difficulty.md#Honour "Difficulty")和新的结局。它还包括数百项游戏玩法更改和修复，最后写道：

> _以及更多、更多的修复、改进、调整和充满爱意的劳作！_

本文旨在记录这些未列出的修复、改进和调整。

## 目录

- [1 荣誉模式](#荣誉模式)
  - [1.1 动作经济](#动作经济)
  - [1.2 伤害机制简化](#伤害机制简化)
  - [1.3 物品稀有度与价格更改](#物品稀有度与价格更改)
  - [1.4 杂项平衡更改](#杂项平衡更改)
- [2 通用更改](#通用更改)
  - [2.1 法术更改](#法术更改)
  - [2.2 属性更改](#属性更改)
  - [2.3 物品更改](#物品更改)
  - [2.4 效果更改](#效果更改)
  - [2.5 微小更改](#微小更改)

## 荣誉模式

### 动作经济

荣誉模式包含多项更改以收紧动作经济。

- 通过[加速](Hastened_(Condition).md "Hastened (Condition)")或[嗜血灵药](Elixir_of_Bloodlust.md "Elixir of Bloodlust")获得的额外动作不再受益于[额外攻击](Extra_Attack.md "Extra Attack")。
  - 例如，如果你处于[加速](Hastened_(Condition).md "Hastened (Condition)")状态并拥有[额外攻击](Extra_Attack.md "Extra Attack")，你可以用第一个动作攻击两次，但第二个动作只能攻击一次。
  - [动作如潮](Action_Surge.md "Action Surge")的额外动作仍然受益于[额外攻击](Extra_Attack.md "Extra Attack")。
- [加深魔契](Deepened_Pact.md "加深魔契")不再与[额外攻击](Extra_Attack.md "Extra Attack")叠加。以前，兼职[邪术师](Warlock.md "Warlock")和任何战斗职业的角色每动作可以获得3次攻击，并且比[战士](Fighter.md "Fighter")的[精通额外攻击](Improved_Extra_Attack.md "Improved Extra Attack")更早获得。

这些更改更接近[桌面游戏使用的规则](D&D_5e_rule_changes.md#Action_Economy "D&D 5e rule changes")。

此外，荣誉模式中的[心灵庇护](Mind_Sanctuary.md "Mind Sanctuary")仅[加速](Hastened_(Condition)其内的角色.md)，而不是允许他们互换使用动作和附赠动作。

### 伤害机制简化

有关详细信息，请参阅[伤害机制](Damage_mechanics.md "Damage mechanics")。

不同伤害增益之间的相互作用可能导致意外（且可利用）的行为。特别是，伤害附加物（damage riders）可能在单次攻击中多次应用，而伤害附加物来源（DRS）导致攻击造成远超预期的伤害。

荣誉模式对许多物品和效果进行了全面更改，以阻止伤害增益相互作用。现在，所有（或大多数）伤害加成都表现良好且不相互作用。这实际上消除了荣誉模式中的DRS概念。许多围绕利用DRS机制每回合造成数百（甚至数千）伤害的构建在荣誉模式中将不起作用。

具体更改如下：

- [生离死别：尖啸](Phalar_Aluve_colon__Shriek.md "Phalar Aluve: Shriek")不再为每个伤害来源创建单独的伤害实例（DRS）。相反，它为每个伤害来源添加额外伤害。
- [酒馆殴斗者](Tavern_Brawler.md "Tavern Brawler")在投掷时不再创建单独的伤害实例。
- 武器[刺客之触](Assassin's_Touch.md "Assassin's Touch")、[深度挖掘](Deep_Delver.md "Deep Delver")、[巨龙之握](Dragon's_Grasp.md "Dragon's Grasp")、[剿灭者之斧](Exterminator's_Axe.md "Exterminator's Axe")、[引火者](Firestoker.md "Firestoker")、[第一滴血短剑](Shortsword_of_First_Blood.md "Shortsword of First Blood")、[染血的巨斧](Blooded_Greataxe.md "Blooded Greataxe")、[身心粉碎者](Render_of_Mind_and_Body.md "Render of Mind and Body")、[偷生之剑](Sword_of_Life_Stealing.md "Sword of Life Stealing")、[猩红诡计](Crimson_Mischief.md "Crimson Mischief")、[决斗者的特权](Duellist's_Prerogative.md "Duellist's Prerogative")和[卑劣短棒](Rat_Bat.md "Rat Bat")都已移除其DRS额外伤害，并替换为普通伤害增益。
- 能力[偷袭](Sneak_Attack.md "Sneak Attack")、[巨像屠夫](Colossus_Slayer.md "Colossus Slayer")、[至圣斩](Divine_Smite.md "Divine Smite")、[神圣打击](Divine_Strike.md "Divine Strike")已添加检查，以确保它们不会获得本应仅应用于基础攻击的额外伤害增益。\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
- [当锤棒喝](Hamarhraft.md "Hamarhraft")的跳跃范围伤害效果不会获得*任何*其他伤害附加物。它是固定的1d4。\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]

### 物品稀有度与价格更改

荣誉模式中，几个物品的稀有度已更改。这些物品是：

- [界限突破手套](Martial_Exertion_Gloves.md "Martial Exertion Gloves")：稀有度：珍稀 / 荣誉模式极稀有
- [腐蚀指环](Caustic_Band.md "Caustic Band")：稀有度：不常见 / 荣誉模式极稀有
- [回旋长矛](Returning_Pike.md "Returning Pike")：稀有度：不常见 / 荣誉模式珍稀
- [投掷之戒](Ring_of_Flinging.md "Ring of Flinging")：稀有度：不常见 / 荣誉模式珍稀
  - 以前总是珍稀，但现在在荣誉模式外是不常见。
  - [珍珠力量护符](Pearl_of_Power_Amulet.md "Pearl of Power Amulet")：稀有度：不常见 / 荣誉模式珍稀
- [遮蔽施法饰环](The_Shadespell_Circlet.md "The Shadespill Circlet")：稀有度：不常见 / 荣誉模式珍稀

此外，大约100个物品的价格已调整，有时幅度很大。一些例子包括：

- [闪避之鞋](Evasive_Shoes.md "Evasive Shoes")：价格：95 gp / 荣誉模式1050 gp
- [破拳头盔](Fistbreaker_Helm.md "Fistbreaker Helm")：价格：60 gp / 荣誉模式420 gp
- [轻声承诺](The_Whispering_Promise.md "The Whispering Promise")：价格：40 gp / 荣誉模式85 gp

### 杂项平衡更改

- [孤注一掷](Perilous_Stakes.md "Perilous Stakes")现在只能以盟友为目标。不能再对敌人施加简单的伤害[易伤](Vulnerability.md "Vulnerability")。

## 通用更改

以下更改适用于所有难度和模式。

### 法术更改

- [治疗](Heal.md "Heal")的范围从范围：1.5米（5英尺）增加到范围：18米（60英尺）。
- [欧提路克弹力法球](Otiluke's_Resilient_Sphere.md "Otiluke's Resilient Sphere")现在只能对大型或更小的目标施放。
- [冰墙](Wall_of_Ice.md "Wall of Ice")现在在被破坏时正确造成其10d6⁠⁠[寒冷](Cold.md "Cold")伤害爆炸。以前，只有残留的冷空气造成伤害。
- 作为[防护学派](Abjuration.md "Abjuration")施放[护盾术](Shield_(spell).md "Shield (spell)")不再获得[奥术守御](Arcane_Ward_(Condition).md "Arcane Ward (Condition)")层数。（*这曾经是这样吗？*\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]）。
- 撬锁和解除陷阱现在会打破[隐形](Invisible_(Condition).md "Invisible (Condition)")，并有几率打破[高等隐形术](Greater_Invisibility_(Condition).md "Greater Invisibility (Condition)")。\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
- [获得魔宠](Find_Familiar.md "Find Familiar")现在每次短休只能施放一次。

### 属性更改

- [原始践踏](Primal_Stampede.md "Primal Stampede")现在允许进行体质豁免检定以避免[倒伏](Prone_(Condition).md "Prone (Condition)")。DC为10 + 力量调整值。
- [野兽形态（黑猩猩）](Aspect_of_the_Beast_(Chimpanzee).md "Aspect of the Beast (Chimpanzee)")现在有体质豁免检定以避免被[目盲](Blinded_(Condition).md "Blinded (Condition)")。DC为8 + [熟练项加值](Proficiency_Bonus.md "Proficiency bonus") + 敏捷调整值。

### 物品更改

- [狂想曲](Rhapsody.md "Rhapsody")的猩红叠加层数现在仅通过杀死敌人获得。以前，你可以通过摧毁无生命物体（如板条箱）轻松达到最大层数。
- [奥术协同王冠](Diadem_of_Arcane_Synergy.md "Diadem of Arcane Synergy")现在仅当你对敌人施加效果时才给予[奥术协同](Arcane_Synergy_(Condition).md "Arcane Synergy (Condition)")（[受威胁](Threatened_(Condition).md "Threatened (Condition)")不计数）。以前，它会在你对任何事物施加任何效果时激活。
- 潜在的新物品。这些物品列在与[阿拉吉·欧布罗扎](Araj_Oblodra.md "Araj Oblodra")相关的宝藏表中，但尚不清楚它们是否可以通过正常方式在游戏中获得。\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
- 积聚法杖（[长棍](Quarterstaves.md "Quarterstaves")）：用近距离法术（范围⁠6米（20英尺）或更小的法术）造成伤害时获得[奥术充能](Arcane_Charge_(Condition).md "Arcane Charge (Condition)")。
  - 吸脑斗篷（[披风](Cloaks.md "Cloaks")）：每当你成功通过法术的[豁免检定](Saving_throw.md "Saving Throw")时，对施法者施加2层[精神疲劳](Mental_Fatigue_(Condition).md "Mental Fatigue (Condition)")。
  - [奥术吸收匕首](Arcane_Absorption_Dagger.md "Arcane Absorption Dagger")
  - [闪亮的碎颅锤](Shining_Staver-of-Skulls.md "Shining Staver-of-Skulls")现在具有永久的光亮术戏法效果，范围7.5米。\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]

### 效果更改

- [奥术充能](Arcane_Charge_(Condition).md "Arcane Charge (Condition)")已大幅重做。
  - 以前它提供等于你的[熟练项加值](Proficiency_Bonus.md "Proficiency bonus")的额外伤害，用于对抗[受威胁](Threatened_(Condition).md "Threatened (Condition)")目标的*所有*伤害。激活时还会施加50%[移动速度](Movement_speed.md "Movement speed")惩罚。
  - 现在，它为法术对抗受威胁目标提供2点额外伤害。没有移动速度惩罚。
  - [静待良机](Bided_Time.md "Bided Time")现在仅在被敌人近战攻击击中时激活。以前，它可以被盟友攻击触发（例如，如果你使用[法师之手](Mage_Hand.md "Mage Hand")攻击自己）。
  - [奥术敏锐](Arcane_Acuity_(Condition).md "Arcane Acuity (Condition)")已略微重做。
  - 现在最多可叠加10层（原为7层）。
  - 当受到伤害时，你会失去2层奥术敏锐。
  - 这适用于任何伤害，包括自我伤害，如[灼热](Heat.md "Heat")。这意味着灼热物品和[火焰敏锐之帽](Hat_of_Fire_Acuity.md "Hat of Fire Acuity")可能无法很好地协同工作。
  - [光耀法球](Radiating_Orb_(Condition).md "Radiating Orb (Condition)")已略微重做。
  - 现在最多可叠加10层（原为7层）。
  - 当受影响的实体进行攻击掷骰时（无论命中或未命中），将移除2层。
  - [发光护甲](Luminous_Armour.md "Luminous Armour")以前有一个错误，可以超过正常的叠加限制。这已修复。
  - [精神疲劳](Mental_Fatigue_(Condition).md "Mental Fatigue (Condition)")已大幅重做。
  - 现在最多可叠加7层（以前无法叠加）。
  - 当受影响的实体在至少有5层时精神[豁免检定](Saving_throw.md "Saving Throw")失败时，它们会释放，造成1d4⁠⁠[心灵](Psychic.md "Psychic")伤害。
  - [亢奋](Momentum_(Condition).md "Momentum (Condition)")现在最多可叠加5层（原为4层）。

### 微小更改

- [召唤魔像铃铛](Summon_Golem_Bell.md "Summon Golem Bell")现在需要一个动作来使用，并且不再算作“疾走”以激活[奥术强化之靴](Boots_of_Arcane_Bolstering.md "Boots of Arcane Bolstering")等物品。以前，它是激活疾走物品的完全免费方式。
- [永恒玻璃酒瓶（有时是强酸）](Eternal_Carafe_of_Wine_(Or_Sometimes_Acid).md "Eternal Carafe of Wine (Or Sometimes Acid)")现在使用需要[附赠动作](Resources.md#Common_resources "Resources")。以前，它是[酒精](Alcohol_(Condition).md "Alcohol (Condition)")（或有时[强酸](Acid_(Condition).md "Acid (Condition)")）的完全免费来源。
- [岁月知识](Knowledge_of_the_Ages.md "岁月知识")现在给予[驯兽](Animal_Handling.md "Animal Handling")、[洞悉](Insight.md "Insight")、[察觉技能](Perception.md "Perception")、[医药](Medicine.md "Medicine")和[求生](Survival.md "Survival")的熟练项。它以前给予[驯兽](Animal_Handling.md "Animal Handling")、[历史的](History.md "History")、[调查](Investigation.md "Investigation")、[自然](Nature.md "Nature")和[宗教](Religion.md "Religion")的熟练项。

---
*Source: [Guide:Undocumented Patch 5 updates](https://bg3.wiki/wiki/Guide:Undocumented_Patch_5_updates)*