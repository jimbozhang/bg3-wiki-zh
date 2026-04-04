# 掷骰

**掷骰**是《博德之门3》的核心游戏机制。当玩家角色尝试大多数动作时，会通过掷骰来根据相关的[难度等级](#d20_rolls)或[护甲等级](#armour-class)以及行动角色的任何[调整值](#modifiers)来解析结果。玩家的选择决定行动方式，而掷骰决定最终结果，例如[属性检定](#ability-checks)是否成功、[攻击](#attack-rolls)是否命中，或造成多少[伤害](#damage-rolls)。

## 目录

- [1 掷骰表示法](#掷骰表示法)
- [2 调整值](#调整值)
- [3 d20 掷骰](#d20-掷骰)
  - [3.1 自然点数 1 和 20](#自然点数-1-和-20)
  - [3.2 优势与劣势](#优势与劣势)
- [4 属性检定](#属性检定)
  - [4.1 技能](#技能)
    - [4.1.1 专精](#专精)
  - [4.2 属性检定类型](#属性检定类型)
- [5 豁免检定](#豁免检定)
  - [5.1 豁免熟练项](#豁免熟练项)
  - [5.2 豁免 DC](#豁免-DC)
  - [5.3 死亡豁免检定](#死亡豁免检定)
- [6 攻击掷骰](#攻击掷骰)
  - [6.1 攻击掷骰调整值](#攻击掷骰调整值)
  - [6.2 重击](#重击)
  - [6.3 攻击失败](#攻击失败)
  - [6.4 护甲等级](#护甲等级)
    - [6.4.1 基础公式](#基础公式)
    - [6.4.2 其他公式](#其他公式)
- [7 伤害掷骰](#伤害掷骰)
  - [7.1 伤害调整值](#伤害调整值)
- [8 其他掷骰](#其他掷骰)
- [9 业力骰子](#业力骰子)
- [10 数学](#数学)
  - [10.1 护甲等级数学](#护甲等级数学)
  - [10.2 伤害掷骰数学](#伤害掷骰数学)
  - [10.3 优势数学](#优势数学)
    - [10.3.1 优势对成功率的影响](#优势对成功率的影响)
    - [10.3.2 优势对掷骰平均值的影响](#优势对掷骰平均值的影响)
    - [10.3.3 优势对重击掷骰的影响](#优势对重击掷骰的影响)
- [11 外部资源](#外部资源)
- [12 注释](#注释)

## 掷骰表示法

骰子用 _d_ 后跟该特定骰子的面数来表示：

- d4
- d6
- d8
- d10
- d12
- d20

要掷的骰子数量在 _d_ 之前注明。任何适用于掷骰的[调整值](#modifiers)在骰子表示法之后以加法（奖励）或减法（惩罚）的形式给出。例如，当掷一个没有调整值的二十面骰时，表示为 1d20。当掷两个六面骰并带有 +3 调整值时，掷骰表示为 2d6+3。

潜在结果的范围通常在括号中给出，尤其是对于[伤害掷骰](#damage-rolls)。例如，[魔法飞弹](Magic_Missile.md "Magic_Missile")法术的单枚飞镖造成 1d4+1（2-5）力场伤害。这意味着掷 1d4 并将结果加 1，可能造成 2 到 5 点伤害。请注意，当掷多个骰子时，并非范围内的所有数字都是等可能的结果，如[伤害掷骰数学](#damage-roll-mathematics)中所述。

在某些情况下（例如[攻击掷骰](#attack-rolls)），游戏会显示一个百分比，表示成功率，该百分比根据调整值和其他因素计算得出，如本文所述。难度等级为 15 的检定和 1d20+4（范围 5 到 24）的掷骰显示 50% 的成功率（掷出 11 到 20 时至少得到 15）。

## 调整值

许多调整值可能会加到骰子掷骰上。调整值要么是加到结果上的奖励，要么是从结果中减去的惩罚。一次掷骰可能有来自多个来源的奖励和惩罚；在这种情况下，它们会相加并表示为单个调整值。例如，带有 +5 奖励和 -2 惩罚的 d20 掷骰表示为 1d20+3。

**属性值调整值**
大多数掷骰都有一个相关的[属性](Ability.md "Ability")，生物会将其相应的属性值调整值加到其掷骰结果中。某些特性会改变特定类型掷骰使用的调整值。例如，法术[橡棍术](Shillelagh.md "Shillelagh")让施法者在使用该武器进行攻击和伤害掷骰时，添加其施法关键属性调整值，而不是力量或敏捷调整值。
**熟练项加值**
生物在使用其熟练的武器、技能或豁免进行攻击掷骰、属性检定或豁免检定时，会添加其熟练项加值。熟练项加值也会加到所有法术攻击掷骰上。
**额外调整值**
某些特性和[状态](Conditions.md "Conditions")会为掷骰结果添加额外的调整值。例如，[神导术](Guidance.md "Guidance")为受术者进行的属性检定结果添加 1d4。

## d20 掷骰

每当生物尝试一个可能失败的动作时，它会掷一个 d20 对抗一个目标数字，以确定尝试是成功还是失败，然后添加任何适用的调整值。如果结果等于或超过目标数字，则尝试成功。如果结果低于目标数字（或者对于某些掷骰，如果未调整的骰子掷出 1），则尝试失败。

这些尝试分为攻击掷骰——对抗目标的[护甲等级](Armour_Class.md "Armour Class")（AC）、属性检定——对抗检定的难度等级（DC），或豁免检定——对抗[豁免 DC](#save-dcs)。一般来说，大多数 d20 掷骰遵循类似的公式：

d20 + 属性值调整值 + 熟练项加值（如果熟练）+ 其他调整值

**攻击掷骰**
当生物攻击目标时，它会进行攻击掷骰对抗目标的 AC，以确定攻击是命中还是未命中。他们使用的武器（或没有武器）决定了使用的属性值调整值，通常是力量或敏捷。<sup>[\[1\]](#cite_note-1)</sup> 如果攻击命中，攻击者会掷伤害。生物通常使用装备的[武器](Weapon.md "Weapon")进行攻击，但某些[法术](Spells.md "Spells")——例如[魔能爆](Eldritch_Blast.md "Eldritch_Blast")——要求施法者进行法术攻击掷骰；法术攻击的功能类似于武器攻击，但使用施法者的施法关键属性来确定属性值调整值。
**豁免检定**
陷阱、法术、状态和其他伤害来源可能允许生物有机会避免或减少其效果，称为豁免检定或豁免。为了尝试豁免，生物掷一个 d20 对抗目标[豁免 DC](#save-dcs)。与豁免相关的属性由伤害来源的类型决定。对于必须避免的物理威胁，进行敏捷豁免检定。对于中毒效果，进行体质豁免检定。对于魔法或非物质效果，豁免检定可能是智力、感知或魅力，但最常见的是感知。
**属性检定**
属性检定是尝试执行特定任务，相关的属性和 DC 由游戏为该任务设置。如果掷骰的最终结果等于或超过 DC，则尝试成功。

难度等级（或 DC）是在进行属性检定和豁免检定时对抗的数字。它表示任务完成的难度。

该数字由尝试的任务决定，或者——在豁免检定的情况下——由必须克服的法术、状态或动作决定。

### 自然点数 1 和 20

在 d20 掷骰中掷出未调整的 1 或 20 被称为“自然点数 1”或“自然点数 20”。在进行攻击掷骰或属性检定时，掷出自然点数 1 总是自动失败，<sup>[\[2\]](#cite_note-lucky_half-2)</sup> 而自然点数 20 总是自动成功，无论应用调整值后的最终结果如何。

与攻击掷骰和属性检定不同，大多数豁免检定在 d20 结果为自然点数 1 或 20 时并不保证失败或成功，除非是为了维持[专注](Concentration.md "Concentration")或在对话期间进行。

### 优势与劣势

许多情况和状态给予生物在 d20 掷骰上的[优势](Advantage.md "Advantage")或[劣势](Disadvantage.md "Disadvantage")。具有优势的生物掷两个 d20，并使用两者中较高的结果。如果具有劣势，则使用两者中较低的结果。

生物从拥有多个优势或劣势来源中不会获得额外的好处或惩罚，并且仍然只掷两次。此外，如果生物在一次掷骰上同时具有优势和劣势，这些条件会相互抵消，并且只掷一个 d20，即使它们有多个来源。

有关优势和劣势来源的详尽列表，请参见以下页面：

- 对于攻击掷骰：[优势](List_of_sources_of_advantage_and_disadvantage_on_attack_rolls.md#Advantage_on_attack_rolls "攻击掷骰的优势来源列表")和[劣势](List_of_sources_of_advantage_and_disadvantage_on_attack_rolls.md#Disadvantage_on_attack_rolls "攻击掷骰的劣势来源列表")
- 对于豁免检定：[优势](List_of_features_and_items_that_affect_saving_throws.md#Advantage_on_saving_throws "影响豁免检定的特性和物品列表")和[劣势](List_of_features_and_items_that_affect_saving_throws.md#Disadvantage_on_saving_throws "影响豁免检定的特性和物品列表")

在确定[被动技能分数](Passive_checks.md "被动检定")时，具有优势或劣势只需在结果上加或减 5。

## 属性检定

属性检定是掷骰以确定生物是否成功或失败完成任务。它们对抗任务的 DC 进行掷骰。这些检定的 DC 通常由游戏预先确定。每个属性检定使用游戏中的六个[属性](Abilities.md "Abilities")之一，生物会将其属性的相应属性值调整值加到他们进行的属性检定结果中。

### 技能

属性检定通常使用指定的技能进行。技能是特定的专业领域，每个技能与一个属性相关联，角色可以熟练掌握。

角色在使用其熟练的技能进行任何属性检定时，会添加其熟练项加值。<sup>[\[3\]](#cite_note-3)</sup>

[力量](Strength.md "Strength")
| 属性值 | 技能 |
| --- | --- |
| [魅力](Charisma.md "Charisma") | [欺瞒](Deception.md "Deception") [威吓](Intimidation.md "Intimidation") [表演](Performance.md "Performance") [游说](Persuasion.md "Persuasion") |
| [体质](Constitution.md "Constitution") | 无 |
| [敏捷](Dexterity.md "Dexterity") | [体操](Acrobatics.md "Acrobatics") [巧手](Sleight_of_Hand.md "Sleight of Hand") [隐匿](Stealth.md "Stealth") |
| [智力](Intelligence.md "Intelligence") | [奥秘](Arcana.md "Arcana") [历史的](History.md "History") [调查](Investigation.md "Investigation") [自然](Nature.md "Nature") [宗教](Religion.md "Religion") |
| [力量](Strength.md "Strength") | [运动](Athletics.md "Athletics") |
| [感知](Wisdom.md "Wisdom") | [驯兽](Animal_Handling.md "Animal Handling") [洞悉](Insight.md "Insight") [医药](Medicine.md "Medicine") [察觉技能](Perception.md "Perception") [求生](Survival.md "Survival") |

- [欺瞒](Deception.md "Deception")
- [威吓](Intimidation.md "Intimidation")
- [表演](Performance.md "Performance")
- [游说](Persuasion.md "Persuasion")

**[体质](Constitution.md "Constitution")**
|

- 无

**[敏捷](Dexterity.md "Dexterity")**
|

- [体操](Acrobatics.md "Acrobatics")
- [巧手](Sleight_of_Hand.md "Sleight of Hand")
- [隐匿](Stealth.md "Stealth")

**[智力](Intelligence.md "Intelligence")**
|

- [奥秘](Arcana.md "Arcana")
- [历史的](History.md "History")
- [调查](Investigation.md "Investigation")
- [自然](Nature.md "Nature")
- [宗教](Religion.md "Religion")

**[力量](Strength.md "Strength")**
|

- [运动](Athletics.md "Athletics")

**[感知](Wisdom.md "Wisdom")**
|

- [驯兽](Animal_Handling.md "Animal Handling")
- [洞悉](Insight.md "Insight")
- [医药](Medicine.md "Medicine")
- [察觉技能](Perception.md "Perception")
- [求生](Survival.md "Survival")

自定义角色在角色创建时根据其选择的[背景](Background.md "Background")获得两项技能熟练项，而[出身](Origin.md "Origin")角色具有预设的背景。所有角色都可以从其[职业](Class.md "Class")决定的技能列表中再选择 2 项技能来熟练掌握（[吟游诗人](Bard.md "Bard")和[游侠](Ranger.md "Ranger")选择 3 项，而[游荡者](Rogue.md "Rogue")选择 4 项）。

此外，某些[种族](Races.md "Races")、副职和[专长](Feats.md "Feats")也会授予特定技能的熟练项，而[吟游诗人](Bards.md "Bards")在 2 级时获得职业特性[多面手](Jack_of_All_Trades.md "Jack_of_All Trades")，允许他们在使用_不_熟练的技能进行属性检定时，添加其熟练项加值的一半（向下取整）。

熟练项不会叠加——为一项技能拥有多个熟练项来源没有额外好处。

#### 专精

角色还可以在技能上拥有专精，这允许他们在进行相应的属性检定时添加_双倍_的熟练项加值。虽然可以在一项技能上同时拥有熟练项和专精，但它们不会叠加。然而，某些专精来源要求角色已经熟练掌握该技能。

要求事先熟练掌握相应技能的专精来源包括：

- [吟游诗人](Bard.md "Bard")在 3 级和 10 级时获得其熟练的任意两项技能的专精。
- [游荡者](Rogue.md "Rogue")在 1 级和 6 级时获得其熟练的任意两项技能的专精。

不要求事先熟练掌握相应技能的专精来源包括：

- [岩侏儒](Gnome.md#Rock_gnome "Gnome")在[历史的](History.md "History")上的专精
- [知识领域](Knowledge_Domain.md "Knowledge Domain")[牧师](Cleric.md "Cleric")在 1 级时选择两项以下技能的专精：[奥秘](Arcana.md "Arcana")、[历史的](History.md "History")、[自然](Nature.md "Nature")或[宗教](Religion.md "Religion")
- 来自[演员](Actor.md "Actor")专长的[欺瞒](Deception.md "Deception")和[表演](Performance.md "Performance")专精
- 来自[灵吸怪专精](Illithid_Expertise.md "Illithid Expertise")特性的[欺瞒](Deception.md "Deception")、[威吓](Intimidation.md "Intimidation")和[游说](Persuasion.md "Persuasion")专精

### 属性检定类型

**自动掷骰**
某些属性检定是自动进行的。例如，当生物接近陷阱时，会掷一个[察觉技能](Perception.md "Perception")检定来确定他们是否注意到它。察觉技能是感知技能，因此生物会将其感知调整值以及（如果熟练察觉技能）其熟练项加值加到属性检定中。
**对话期间**
属性检定在对话中也很常见，一些回应需要属性检定来决定结果。例如使用魅力技能如[游说](Persuasion.md "Persuasion")、[欺瞒](Deception.md "Deception")或[威吓](Intimidation.md "Intimidation")来影响他人，或使用智力技能如[奥秘](Arcana.md "Arcana")、[历史的](History.md "History")或[宗教](Religion.md "Religion")来确定或回忆事实。在这些检定之前，屏幕底部会出现一个标记为“添加奖励”的按钮，<sup>[\[4\]](#cite_note-4)</sup> 允许玩家角色和其他队伍成员自由使用可用的法术和消耗品来授予检定奖励。在与物体互动时进行属性检定时（例如解除陷阱或开锁）也可以这样做。
**对抗**
对抗是两个生物都进行掷骰，掷骰结果更好的一方获胜的情况。也可以说一个生物进行掷骰以确定另一个生物掷骰的[难度等级](Difficulty_Class.md "Difficulty Class")。例如在[躲藏](Hide.md "躲藏")时攻击，此时目标掷察觉技能，攻击者掷隐匿技能来对抗它。
这可能还涉及[被动检定](Passive_check.md "Passive check")而不是主动掷骰。例如，一个隐藏的玩家角色在非盟友生物的视线内，必须进行隐匿检定对抗该生物的被动察觉技能分数。另一个例子是尝试[推击](Shove.md "推击")或[投掷](Throw.md "Throw")一个生物，此时尝试的生物掷[运动](Athletics.md "Athletics")检定，对抗另一个生物的被动运动或[体操](Acrobatics.md "Acrobatics")分数（取较高者）。

## 豁免检定

豁免检定代表生物试图“豁免”自己免受伤害。法术和其他生物采取的动作经常允许其目标尝试豁免，[陷阱](Traps.md "Traps")和[地表](Surface.md "Surface")等危险也是如此。每个豁免都有一个相关的属性和一个豁免 DC，尝试豁免的生物会对抗它进行掷骰。尝试豁免时，生物会添加该豁免相关属性的属性值调整值，如果他们熟练使用该属性进行豁免，则还会添加其熟练项加值。

虽然尝试豁免检定的结果总是二元的——成功或失败——但成功豁免的确切结果取决于相关效果。通常，相关效果造成伤害或状态的严重程度会降低，或者有时完全被抵消。

如上所述，豁免检定在自然点数 1 和 20 时不会自动失败或成功，除非是为了维持[专注](Concentration.md "Concentration")或在对话期间进行。

[许多特性](List_of_features_and_items_that_affect_saving_throws.md "影响豁免检定的特性和物品列表")会影响豁免检定，某些[种族](Races.md "Races")对特定类型的豁免具有优势。

### 豁免熟练项

每个职业授予两个属性的豁免熟练项。然而，当身兼多职时，只有第一个职业授予豁免熟练项（除非它们来自单独的特性，如[钢铁意志](Iron_Mind.md "Iron Mind")）。可以通过选择[坚如磐石](Resilient.md "Resilient")专长获得额外的豁免熟练项。

| 属性值 | 技能 |
| --- | --- |
| [魅力](Charisma.md "Charisma") | [欺瞒](Deception.md "Deception") [威吓](Intimidation.md "Intimidation") [表演](Performance.md "Performance") [游说](Persuasion.md "Persuasion") |
| [体质](Constitution.md "Constitution") | 无 |
| [敏捷](Dexterity.md "Dexterity") | [体操](Acrobatics.md "Acrobatics") [巧手](Sleight_of_Hand.md "Sleight of Hand") [隐匿](Stealth.md "Stealth") |
| [智力](Intelligence.md "Intelligence") | [感知](Wisdom.md "Wisdom") | [魅力](Charisma.md "Charisma") |
| [力量](Strength.md "Strength") | [运动](Athletics.md "Athletics") |
| [感知](Wisdom.md "Wisdom") | [驯兽](Animal_Handling.md "Animal Handling") [洞悉](Insight.md "Insight") [医药](Medicine.md "Medicine") [察觉技能](Perception.md "Perception") [求生](Survival.md "Survival") |

### 豁免 DC

尝试豁免时对抗的难度等级称为豁免 DC。成功豁免可能意味着完全避免负面效果、减少受到的伤害（通常减半），或两者兼有。例如，成功豁免尖刺陷阱可能意味着生物因为成功躲避尖刺而不受伤害。另一方面，如果陷入[火球术](Fireball.md "火球术")法术的效应区域，成功豁免仅使伤害减半。豁免[雷鸣波](Thunderwave.md "Thunderwave")法术既使受到的伤害减半，又防止生物被法术推开。

不同的机制以不同的方式计算豁免 DC：

**法术豁免 DC**
可以豁免的法术的难度等级通过以下公式确定：

8 + 熟练项加值 + 施法关键属性调整值

除战士和游荡者外，每个职业都有一个施法关键属性，用于其职业特性（出现在法术书职业标签下的特性）和需要施法关键属性调整值的法术。一些非职业特性也使用此施法关键属性，例如通过物品施放的法术（包括[卷轴](Scrolls.md "Scrolls")）、[可重施法术](Category_colon_Recastable_spells.md "Category:Recastable spells")的免费重施（无论来源），以及[灵吸怪威能](Illithid_powers.md "Illithid powers")。身兼多职的角色对非职业特性使用其最新职业（最近达到 1 级的职业）的施法关键属性。有些职业特性存在错误，会错误地使用最新职业的施法关键属性，如这些特性页面上所述。

战士和游荡者没有正确定义的施法关键属性，因此使用施法者的默认施法关键属性。默认施法关键属性对于自定义角色以及出身角色[阿斯代伦](Astarion.md "Astarion")、[邪念](The_Dark_Urge.md "The Dark Urge")、[盖尔](Gale.md "Gale")、[卡菈克](Karlach.md "Karlach")和[莱埃泽尔](Lae'zel.md "Lae'zel")是智力；[哈尔辛](Halsin.md "Halsin")、[贾希拉](Jaheira.md "Jaheira")、[明斯克](Minsc.md "Minsc")、[明萨拉](Minthara.md "Minthara")和[影心](Shadowheart.md "Shadowheart")使用感知；最后，[威尔](Wyll.md "Wyll")使用魅力。对于单职业角色，这按预期工作，但如果他们身兼多职，并且最近选择的职业是战士或游荡者，则将使用次新职业的施法关键属性。

然而，[诡术师](Arcane Trickster.md "Arcane Trickster")和[奥法骑士](Eldritch Knight.md "Eldritch Knight")副职正确定义了智力作为其施法关键属性，因此这两个副职在身兼多职角色上会按预期表现。即使这些副职的施法关键属性仅在 3 级后定义，最新职业仍然是最近达到 1 级的职业。

| 职业 | [力量](STR.md "力量") | [敏捷](DEX.md "敏捷") | [体质](CON.md "体质") | [智力](Int.md "Int") | [感知](WIS.md "感知") | [魅力](CHA.md "魅力") |
| --- | --- | --- | --- | --- | --- | --- |
| [野蛮人](Barbarian.md "Barbarian") | ✓ |  | ✓ |  |  |  |
| [吟游诗人](Bard.md "Bard") |  | ✓ |  |  |  | ✓ |
| [牧师](Cleric.md "Cleric") |  |  |  |  | ✓ | ✓ |
| [德鲁伊](Druid.md "Druid") |  |  |  | ✓ | ✓ |  |
| [战士](Fighter.md "Fighter") | ✓ |  | ✓ |  |  |  |
| [武僧](Monk.md "Monk") | ✓ | ✓ |  |  |  |  |
| [圣武士](Paladin.md "Paladin") |  |  |  |  | ✓ | ✓ |
| [游侠](Ranger.md "Ranger") | ✓ | ✓ |  |  |  |  |
| [游荡者](Rogue.md "Rogue") |  | ✓ |  | ✓ |  |  |
| [术士](Sorcerer.md "Sorcerer") |  |  | ✓ |  |  | ✓ |
| [邪术师](Warlock.md "Warlock") |  |  |  |  | ✓ | ✓ |
| [法师](Wizard.md "Wizard") |  |  |  | ✓ |  | ✓ |

施法职业可以在法术书（快捷键“K”）中查看其法术豁免 DC。可以通过检查目标（快捷键“T”）来查看其豁免检定。

**混合豁免 DC**

对于非施法者来源的威胁，例如陷阱或毒苹果，游戏会根据威胁的预期严重程度设置 DC。例如，一个轻微变质的馅饼在食用时可能施加 DC 5 体质豁免，而强效蛇毒可能对受害者施加 DC 15 体质豁免。许多消耗品物品，如元素[箭](Arrows.md "Arrows")、[手雷](Grenades.md "Grenades")和[涂层](Coatings.md "Coatings")，使用固定的豁免 DC。

### 死亡豁免检定

| 1d20 目标值 | 普通掷骰 | 具有优势的掷骰 | 具有劣势的掷骰 |
| --- | --- | --- | --- |
| 1 | 100% | 100% | 100% |
| 2 | 95% | 99.75% | 90.25% |
| 3 | 90% | 99% | 81% |
| 4 | 85% | 97.75% | 72.25% |
| 5 | 80% | 96% | 64% |
| 6 | 75% | 93.75% | 56.25% |
| 7 | 70% | 91% | 49% |
| 8 | 65% | 87.75% | 42.25% |
| 9 | 60% | 84% | 36% |
| 10 | 55% | 79.75% | 30.25% |
| 11 | 50% | 75% | 25% |
| 12 | 45% | 69.75% | 20.25% |
| 13 | 40% | 64% | 16% |
| 14 | 35% | 57.75% | 12.25% |
| 15 | 30% | 51% | 9% |
| 16 | 25% | 43.75% | 6.25% |
| 17 | 20% | 36% | 4% |
| 18 | 15% | 27.75% | 2.25% |
| 19 | 10% | 19% | 1% |
| 20 | 5% | 9.75% | 0.25% |

可玩角色在累积三次失败时[死亡](Dead.md "Dead")，或在累积三次成功时稳定，以先发生者为准。

死亡豁免检定不与属性值相关联，因此不会获得任何属性值调整值，也不会从熟练项加值中受益。它们仅受益于适用于所有豁免检定的奖励（例如[祝福术](Bless.md "Bless")）或专门针对死亡豁免的奖励（例如来自[家族戒指](Family_Ring.md "Family Ring")）。

## 攻击掷骰

生物在攻击目标时进行攻击掷骰，通常使用[武器](Weapon.md "Weapon")或[法术](Spell.md "Spell")。

如果攻击掷骰的结果等于或高于目标的 AC，则攻击命中，攻击者掷伤害，除非被[免疫](Immunity.md "Immunity")或其他特性阻止。如果结果低于目标的 AC，则攻击未命中，除非是[重击](Critical_Hit.md "Critical hit")。

### 攻击掷骰调整值

攻击掷骰总是使用相关的属性进行：

- 徒手攻击、近战武器攻击和投掷武器攻击通常添加攻击生物的[力量](Strength.md "Strength")调整值。
- 使用远程武器的攻击添加生物的[敏捷](Dexterity.md "Dexterity")调整值。
- 具有[灵巧](Finesse.md "Finesse")属性的武器或[武僧](Monk.md "Monk")武器的攻击，以及具有[ martial arts: dextrous attacks](Martial_Arts_colon__Dextrous_Attacks.md "Martial Arts: Dextrous Attacks")的生物的徒手攻击，添加攻击者的力量或敏捷调整值中较高者。
- 法术攻击添加施法者的[施法关键属性调整值](Spells.md#Spellcasting "Spells")，通常由其[职业](Class.md "Class")决定。

法术攻击、徒手攻击以及攻击者熟练的武器攻击还会添加其[熟练项](Proficiency.md "Proficiency")加值。某些攻击还会添加额外的调整值：

- 如果攻击者使用[惑控学派](Enchantment.md "Enchantment")武器，则添加附魔值，从 +1 到 +3。
- 根据[高地规则](High_ground_rules.md "High ground rules")，从至少 2.5 米（8 英尺）高处攻击会为攻击掷骰应用 +2 奖励，而从至少 2.5 米（8 英尺）低处攻击会应用 -2 惩罚。

攻击掷骰还受以下因素修改：

- [职业](Class.md "Class")[特性](Features.md "Features") - 例如[箭术](Archery.md "Archery")
- [涂层](Coatings.md "Coatings") - 例如[稀释的锐利之油](Diluted_Oil_of_Sharpness.md "Diluted Oil of Sharpness")
- [状态](Conditions.md "Conditions") - 例如[闪电充能](Lightning_Charges_(Condition).md "Lightning Charges (Condition)")
- [专长](Feats.md "Feats") - 例如[神射手](Sharpshooter.md "Sharpshooter")
- [物品](Items.md "Items") - 例如[敏捷手套](Gloves_of_Dexterity.md "Gloves of Dexterity")
- [法术](Spells.md "Spells") - 例如[祝福术](Bless.md "Bless")

有关完整列表，请参见[影响攻击掷骰的特性和物品列表](List_of_features_and_items_that_affect_attack_rolls.md "影响攻击掷骰的特性和物品列表")。

### 重击

使用 1d6 短剑进行重击的示例。

主文章：[重击](Critical_Hit.md "Critical hit")

当生物在攻击掷骰中掷出自然点数 20 时，攻击为重击。重击会自动命中，无论目标的 AC 如何，并且攻击者还会掷双倍正常数量的骰子来确定造成的伤害，包括来自[至圣斩](Smite.md "Smite")或[策略](Manoeuvres.md "Manoeuvres")的额外骰子。然而，某些物品（例如[精金盾牌](Adamantine_Shield.md "Adamantine Shield")）授予对重击的免疫，将其视为普通攻击掷骰。

调整值和平整奖励（即任何不涉及骰子的奖励）——包括生物的相关属性值调整值——不会翻倍。

某些专长、职业特性和物品[降低重击阈值](Critical_Hit_threshold_reduction.md "Critical Hit threshold reduction")1 点，允许攻击掷骰在掷出 19 或 20 时造成重击。多个此效果来源会叠加，允许重击阈值低于 19。

### 攻击失败

当生物在攻击掷骰中掷出自然点数 1 时，攻击为攻击失败。攻击失败会自动失败<sup>[\[2\]](#cite_note-lucky_half-2)</sup>，无论目标的 AC 或攻击掷骰调整值如何。

### 护甲等级

护甲等级（AC）是衡量生物被攻击命中的难易程度的指标。为了成功击中生物，攻击掷骰的结果必须等于或大于目标的护甲等级。AC 可以通过装备[护甲](Armour.md "Armour")和[盾牌](Shields.md "Shields")、在升级时选择某些[专长](Feats.md "Feats")或利用某些[法术](Spells.md "Spells")来提高。

#### 基础公式

不穿护甲时确定 AC 的公式为：

10 + 敏捷调整值 + 盾牌奖励 + 其他奖励和惩罚

如果装备了护甲，则使用其 AC 值代替 10。穿中甲时，敏捷提供的 AC 奖励通常上限为 +2，<sup>[\[5\]](#cite_note-5)</sup><sup>[\[6\]](#cite_note-6)</sup> 穿重甲时则完全移除。

大多数[盾牌](Shields.md "Shields")提供 +2 AC，但有些稀有盾牌提供 +3 AC。

其他奖励包括诸如[防御](Defence.md "Defence")战斗风格（在穿护甲时提供 +1 AC）和[守护披风](Cloak_of_Protection.md "Cloak of Protection")（始终提供 +1 AC）等。AC 奖励会相互叠加。

#### 其他公式

与 AC 奖励（它们都相互叠加）不同，某些法术和特性授予生物一个新的基础公式，用于在不穿护甲时确定 AC。一次只能激活其中一个公式，如果生物可以使用多个公式，则它将使用在给定时间产生最高 AC 的公式。任何标记为轻甲、中甲或重甲的装备在装备时都会阻碍使用这些公式中的任何一个，即使它本身不提供 AC 值。

[魔法护甲](Mage_Armour.md "Mage_Armour")和[龙族韧性](Draconic_Resilience.md "Draconic Resilience")：

13 + 敏捷调整值 + 盾牌奖励 + 其他奖励和惩罚

| 属性值 | 技能 |
| --- | --- |
| [魅力](Charisma.md "Charisma") | [欺瞒](Deception.md "Deception") [威吓](Intimidation.md "Intimidation") [表演](Performance.md "Performance") [游说](Persuasion.md "Persuasion") |
| [体质](Constitution.md "Constitution") | 无 |
| [敏捷](Dexterity.md "Dexterity") | [体操](Acrobatics.md "Acrobatics") [巧手](Sleight_of_Hand.md "Sleight of Hand") [隐匿](Stealth.md "Stealth") |
| [智力](Intelligence.md "Intelligence") | [奥秘](Arcana.md "Arcana") [历史的](History.md "History") [调查](Investigation.md "Investigation") [自然](Nature.md "Nature") [宗教](Religion.md "Religion") |
| [力量](Strength.md "Strength") | [运动](Athletics.md "Athletics") |
| [感知](Wisdom.md "Wisdom") | [驯兽](Animal_Handling.md "Animal Handling") [洞悉](Insight.md "Insight") [医药](Medicine.md "Medicine") [察觉技能](Perception.md "Perception") [求生](Survival.md "Survival") |

[无甲防御（野蛮人）](Unarmoured_Defence_(Barbarian).md "Unarmoured Defence (Barbarian)")：

[无甲防御（武僧）](Unarmoured_Defence_(Monk).md "Unarmoured Defence (Monk)")：

10 + 感知调整值 + 敏捷调整值 + 其他奖励和惩罚

法术[树肤术](Barkskin.md "Barkskin")将受影响生物的 AC 设置为 16（如果其原本低于此值）。穿护甲不会阻碍它。

## 伤害掷骰

[武器](Weapon.md "Weapon")、[法术](Spell.md "Spell")、职业[动作](Action.md "Action")或[状态](Condition.md "Condition")造成的基础伤害通常由伤害掷骰决定。伤害掷骰总是有一个相关的[伤害类型](Damage_type.md "Damage type")，以骰子表示法给出，例如 1d4⁠⁠[穿刺](Piercing.md "Piercing")或 2d6⁠⁠[火焰](Fire.md "Fire")。

### 伤害调整值

添加到伤害掷骰的调整值每个来源只添加_一次_，即使掷多个骰子。

属性值调整值是否添加到伤害掷骰取决于攻击：

- 进行武器攻击时，攻击生物通常将相同的属性值调整值添加到攻击掷骰和伤害掷骰中。
- 属性值调整值通常不会添加到法术和法术攻击的伤害掷骰中，除非由[苦痛魔爆](Agonising_Blast.md "Agonising Blast")等特性特别启用。虽然法术描述中未说明，但[破影利刃](Shadow_Blade.md "Shadow Blade")在进行武器攻击时，将施法者的力量或敏捷调整值中较高者添加到其伤害中，这与[火焰刀](Flame_Blade.md "Flame Blade")不同。

熟练项加值不会添加到伤害掷骰中，除非所使用的攻击另有说明，例如[浸影打击](Shadowsoaked_Blow.md "Shadowsoaked Blow")，或由特性启用，例如[魔刃诅咒](Hexblade's_Curse.md "Hexblade's Curse")。

## 其他掷骰

**治疗**
[治疗](Healing.md "Healing")以类似于伤害掷骰的方式恢复目标的[生命值](Hit_Points.md "Hit points")。治疗掷骰也可能添加调整值，但没有通用规则；任何奖励由治疗来源决定。例如，[治疗药水](Potion_of_Healing.md "Potion of Healing")恢复 2d4+2⁠⁠[治疗](Healing.md "治疗")。有魔法物品、职业特性和其他效果提供治疗奖励，例如[生命领域](Life_Domain.md "生命领域")的[生命门徒](Disciple_of_Life.md "Disciple of Life")特性。
**狂野魔法**
| 职业 | [力量](STR.md "力量") | [敏捷](DEX.md "敏捷") | [体质](CON.md "体质") | [智力](Int.md "Int") | [感知](WIS.md "感知") | [魅力](CHA.md "魅力") |
| --- | --- | --- | --- | --- | --- | --- |
| [野蛮人](Barbarian.md "Barbarian") | ✓ |  | ✓ |  |  |  |
| [吟游诗人](Bard.md "Bard") |  | ✓ |  |  |  | ✓ |
| [牧师](Cleric.md "Cleric") |  |  |  |  | ✓ | ✓ |
| [德鲁伊](Druid.md "Druid") |  |  |  | ✓ | ✓ |  |
| [战士](Fighter.md "Fighter") | ✓ |  | ✓ |  |  |  |
| [武僧](Monk.md "Monk") | ✓ | ✓ |  |  |  |  |
| [圣武士](Paladin.md "Paladin") |  |  |  |  | ✓ | ✓ |
| [游侠](Ranger.md "Ranger") | ✓ | ✓ |  |  |  |  |
| [游荡者](Rogue.md "Rogue") |  | ✓ |  | ✓ |  |  |
| [术士](Sorcerer.md "Sorcerer") |  |  | ✓ |  |  | ✓ |
| [邪术师](Warlock.md "Warlock") |  |  |  |  | ✓ | ✓ |
| [法师](Wizard.md "Wizard") |  |  |  | ✓ |  | ✓ |

## 业力骰子

游戏玩法选项中的业力骰子设置

当启用业力骰子选项<sup>[\[7\]](#cite_note-7)</sup>时（默认启用），游戏会减轻坏运气连续（例如，连续多次攻击未命中）。它适用于所有战斗人员，包括 NPC 和敌人，以及对话期间进行的属性检定。它不适用于对话外进行的属性检定，例如开锁时的巧手检定或发现隐藏物体的察觉技能检定。它不会惩罚幸运连续。<sup>[\[8\]](#cite_note-9)</sup><sup>[\[9\]](#cite_note-11)</sup> Larian 描述使用业力骰子类似于拥有一个“友好的 DM”。[[url 3]](#cite_note-12) 一些玩家报告说这可以让战斗感觉更快或更有效，但结果可能有所不同。

在内部，游戏跟踪任何给定掷骰的概率 p，如果掷骰失败，该金额会添加到“债务”中。该债务针对三个组分别跟踪：队伍成员及其控制下的单位（例如召唤物和[临时伙伴](Temporary_companion.md "Temporary companion")）、盟友 NPC 和敌人。还有一个针对对话检定的第四个债务。如果在任何给定掷骰之前债务为正，则有等于 p1−Debt 的机会自动通过它。在这种情况下，结果是随机选择的，每个可能成功的掷骰被选中的概率相等。如果攻击掷骰自动通过，并且唯一可能成功的掷骰是 20，则该攻击保证为[重击](#critical-hits)。在自动成功时，从债务总额中减去等于 2(1−p) 的金额。否则，掷骰按常规解析。请注意，为此目的，成功豁免敌方法术的[豁免检定](#saving-throws)被视为敌人的失败掷骰（反之亦然）。因此，业力骰子导致比通常更多的豁免检定失败。<sup>[\[10\]](#cite_note-karmic_dice_negative_impact-13)</sup>

启用业力骰子的次要效果是，伤害掷骰是针对[正态分布](https://en.wikipedia.org/wiki/normal_distribution)进行的，其均值等于 D+12，标准差等于 (D−1)(13−D120)（D 为伤害骰的面数），而不是[离散均匀分布](https://en.wikipedia.org/wiki/discrete_uniform_distribution)。这种效果是减少掷骰的方差并使其偏向均值。因此，减少伤害方差的特性，例如[巨武器战斗](Great_Weapon_Fighting.md "Great Weapon Fighting")和[凶蛮打手](Savage_Attacker.md "Savage Attacker")，在启用业力骰子时可能效果较差。<sup>[\[10\]](#cite_note-karmic_dice_negative_impact-13)</sup>

## 数学

可以应用各种数学来更深入地理解掷骰机制。

### 护甲等级数学

护甲等级越高（以越来越非线性的方式）就越有用。例如，从 19 AC 提高到 20 AC 的效果提升_大于_从 16 AC 提高到 17 AC。为了说明这一点：

- 如果防御者拥有 16 AC 和 10 HP，攻击者攻击掷骰 +5，每次攻击造成 2 点伤害，防御者平均将存活 10 回合，因为攻击有 50% 的机会命中。如果防御者的 AC 提高到 17（命中率降至 45%），他们平均将存活约 11.11 回合——提高了约 11.1%。
- 如果防御者起始为 19 AC（35% 被击中），他们平均将存活约 14.29 回合。但如果他们的 AC 提高到 20（30% 被击中），他们平均将能够存活约 16.67 回合（效果提高约 16.67%）。
- 从 24 到 25 的差异更大，效果提高_100%_（50 回合 vs 100 回合）。

### 伤害掷骰数学

由于掷骰的数学原理，例如 1d8 和 2d4 之间的差异不仅仅是 2d4 的最小值更高。使用 d8 时，每个结果的概率相同。获得 5 和 8 的机会相等。另一方面，2d4 掷骰在统计上更可能导致总值为 5，而不是总值为 8。这可以通过所有可能结果的表格更好地解释：

**4** | **5** | 6 | 7 | 8

注意 5 在总值可能性中出现的频率（16 种可能性中有 4 种）与 8 出现的频率（16 种可能性中有 1 种）相比。这意味着 2d4 掷骰有 25% 的机会造成 5 点伤害，但只有 6.25% 的机会造成 8 点伤害。同时，1d8 掷骰实际上有更高的机会造成最大伤害值 8，因为 8 种可能性中有 1 种（12.5%）结果为 8。然而，2d4 的平均掷骰伤害为 5，而 1d8 的平均掷骰伤害仅为 4.5。因此，2d4 在伤害输出上通常更一致，并且长期来看会产生更高的掷骰结果。

### 优势数学

#### 优势对成功率的影响

掷骰具有优势（或具有劣势）的好处取决于在 1d20 掷骰中需要达到的目标数字。优势带来的奖励在需要 1d20 掷骰掷出 9、10、11、12 或 13 时最大，可达 24-25%，而在需要掷出 19 时最小，仅为 9%。

5 | 80% | 96% | 64% 6 | 75% | 93.75% | 56.25% 7 | 70% | 91% | 49% 8 | 65% | 87.75% | 42.25% 9 | 60% | 84% | 36% 10 | 55% | 79.75% | 30.25%
11 | 50% | 75% | 25% 12 | 45% | 69.75% | 20.25% 13 | 40% | 64% | 16% 14 | 35% | 57.75% | 12.25% 15 | 30% | 51% | 9% 16 | 25% | 43.75% | 6.25%
17 | 20% | 36% | 4% 18 | 15% | 27.75% | 2.25% 19 | 10% | 19% | 1% 20 | 5% | 9.75% | 0.25%

#### 优势对掷骰平均值的影响

看待优势/劣势的更通用方法是计算其对掷骰平均值的影响。这使其比查看特定掷骰更具广泛适用性，并且更容易与其他可能适用于掷骰的奖励和惩罚进行比较。

为此，我们首先需要澄清下面使用的符号：Dn 表示 n 面骰，P(i) 是变量具有值 a 的概率，𝔼 表示掷骰的平均值或期望值，∑i=abxi 表示在索引 i 从 a 到 b 时一系列数字 x 的总和。

计算变量 x 的期望值 𝔼[x] 的公式等于 x 的每个可能值乘以 x 具有该值的概率的总和。

对于 n 面骰 Dn，这变为：

𝔼[Dn]=∑i=1n(i⋅P(i))

对于常规掷骰，概率分布是均匀的，这意味着对于任何 i，P(i)=1/n，并且使用 ∑i=1ni=12n(n+1)，我们得到

𝔼[Dn]=∑i=1n(i⋅P(i))=1n(n(n+1)2)=n+12

对于具有优势的掷骰，掷出数字 i 的概率等于第一个骰子掷出 i 的概率乘以第二个骰子掷出 i 或更小的概率，再乘以 2（因为两个骰子可互换），减去两个骰子都掷出 i 的概率（因为我们通过乘以 2 计算了两次该可能性）。这给出

Padv(i)=2P(i)∑j=1iP(j)−P(i)2=21n⋅in−1n2=2i−1n2

将其应用于骰子 Dn 的平均值公式，我们得到

𝔼[Dn with advantage]=∑i=1ni⋅2i−1n2=2n2⋅∑i=1ni2−1n2⋅∑i=1ni

这里我们可以使用平方和 ∑i=1ni2=16n(n+1)(2n+1)，这给出

𝔼[Dn with advantage]=2n2(n(n+1)(2n+1)6)−1n2(n(n+1)2)=2n3+1+13n−12−12n=2n3+12−16n

要知道优势给我们的掷骰带来多少奖励，我们计算

𝔼[Dn with advantage]−𝔼[Dn]=2n3+12−16n−n+12=16(n−1n)

当我们将此表达式应用于 d20 时，结果是拥有优势相当于平均奖励 +3.325。

由于对称性，拥有劣势而不是优势意味着我们可以简单地对掷骰值进行 {1,…,n}→{n,…,1} 的排列，所有计算将保持不变。因此，_优势的奖励大小_等于_劣势的惩罚大小_。

#### 优势对重击掷骰的影响

在进行属性检定、攻击掷骰或豁免检定时，1 或 20（几乎）总是被视为重击失败<sup>[\[2\]](#cite_note-lucky_half-2)</sup>或成功，无论应用任何潜在调整值后的结果如何。在没有优势或劣势的掷骰上，这实际上意味着有 1/20（或 5%）的机会发生重击成功或失败。

拥有优势或劣势对增加或减少重击成功和失败的机会有显著影响。例如，当掷骰具有优势时，获得重击失败的唯一方法是同时掷出_两个_ 1。此结果的几率是 1/20⋅1/20=1/400（或 0.25%）。相反，掷出重击成功要容易得多——在 400 种可能的掷骰结果中，有 39 种会得到 20（第一个骰子掷出 20，第二个骰子掷出 1、2、3、...、20，加上第二个骰子掷出 20，第一个骰子掷出 1、2、3、...、20，减去一个，这样两个 20 的结果不会被重复计算）。此结果的几率是 39/400（或 9.75%）。对于具有劣势的掷骰则相反：重击成功的几率为 0.25%，重击失败的几率为 9.75%。

实际上，掷骰具有优势意味着重击失败的可能性_降低 20 倍_，而重击成功的可能性几乎_翻倍_，而对于劣势则相反。

## 外部资源

- [掷多个骰子并选择最高值的意外逻辑](https://www.youtube.com/watch?v=X_DdGRjtwAo)（视频）by Matt Parker
- [D&D Next 中的优势和劣势：数学](http://onlinedungeonmaster.com/2012/05/24/advantage-and-disadvantage-in-dd-next-the-math/)（带文本和表格的博客）by The Online Dungeon Master (Michael Iachini)
- [D&D 5e：优势和劣势的概率](https://statmodeling.stat.columbia.edu/2014/07/12/dnd-5e-advantage-disadvantage-probability/)（带图表和表格的博客）by Bob Carpenter
- [D&D 中的优势有多好？](https://www.youtube.com/watch?v=R0gewfLILw0)（视频）by Joseph Newton
- [关于业力骰子你想知道的一切](https://redd.it/1ovj329) reddit 帖子 by [Jukervic](https://www.reddit.com/user/Jukervic/)

## 注释

| + | 第二次掷骰 |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 |  |  |
| **第一次掷骰** | 1 | 2 | 3 | 4 | 5 |
| 2 | 3 | 4 | 5 | 6 |  |
| 3 | 4 | 5 | 6 | 7 |  |
| 4 | 5 | 6 | 7 | 8 |  |

1. ↑ [2.0](#cite_ref-lucky_half_2-0) [2.1](#cite_ref-lucky_half_2-1) [2.2](#cite_ref-lucky_half_2-2) [半身人幸运](Halfling_Luck.md "Halfling Luck")允许几乎所有自然点数 1 的第一次实例重新掷骰。虽然可能再次掷出 1，但这很罕见，因此允许此种族专长抵消大多数重击失败。

1. [↑](#cite_ref-3) 这些掷骰在社区中通常被称为“技能检定”，尽管在游戏中并非如此称呼。

| 1d20 目标值 | 普通掷骰 | 具有优势的掷骰 | 具有劣势的掷骰 |
| --- | --- | --- | --- |
| 1 | 100% | 100% | 100% |
| 2 | 95% | 99.75% | 90.25% |
| 3 | 90% | 99% | 81% |
| 4 | 85% | 97.75% | 72.25% |
| 5 | 80% | 96% | 64% |
| 6 | 75% | 93.75% | 56.25% |
| 7 | 70% | 91% | 49% |
| 8 | 65% | 87.75% | 42.25% |
| 9 | 60% | 84% | 36% |
| 10 | 55% | 79.75% | 30.25% |
| 11 | 50% | 75% | 25% |
| 12 | 45% | 69.75% | 20.25% |
| 13 | 40% | 64% | 16% |
| 14 | 35% | 57.75% | 12.25% |
| 15 | 30% | 51% | 9% |
| 16 | 25% | 43.75% | 6.25% |
| 17 | 20% | 36% | 4% |
| 18 | 15% | 27.75% | 2.25% |
| 19 | 10% | 19% | 1% |
| 20 | 5% | 9.75% | 0.25% |

1. [↑](#cite_ref-5) [中甲大师](Medium_Armour_Master.md "Medium Armour Master")专长将上限从 +2 提高到 +3。

1. [↑](#cite_ref-6) 四件稀有中甲具有[特制材料](Exotic_Material.md "Exotic Material")被动，允许穿戴者将其完整的敏捷调整值加到 AC：[敏捷之铠](Armour_of_Agility.md "Armour of Agility")、[尖锐陷阱胸甲](Sharpened_Snare_Cuirass.md "Sharpened Snare Cuirass")、[多余的杰作鳞甲](Unwanted_Masterwork_Scalemail.md "Unwanted Masterwork Scalemail")和[蛇人鳞甲](Yuan-Ti_Scale_Mail.md "Yuan-Ti Scale Mail")。

1. [↑](#cite_ref-7) 先前称为“加载骰子”

1. [↑](#cite_ref-9) 在抢先体验热修复 10[[url 1]](#cite_note-8) 中，Larian 写道：“我们在补丁 4 中引入了加载骰子，以尝试平滑掷骰钟形曲线的极端情况……从现在开始，加载骰子将仅使随机数生成器偏向掷骰角色有利的方向。这意味着您不会因为连续幸运命中而被强制未命中。此更改也适用于 NPC 和敌人。”

1. [↑](#cite_ref-11) 一个备受讨论的敌人命中率远高于正常的情况与一个错误有关，Larian 称其在正式发布前已修复。[[url 2]](#cite_note-10)

1. ↑ [10.0](#cite_ref-karmic_dice_negative_impact_13-0) [10.1](#cite_ref-karmic_dice_negative_impact_13-1) 虽然游戏开发者从未声明这是有意的，但业力骰子的负面影响、其潜在滥用案例及其对长期概率的影响可以在[此](https://redd.it/1ovj329) Reddit 帖子中进一步探讨。

1. [↑](#cite_ref-8] Larian Studios 论坛：Jess (2021-04-15). [热修复 #10 现已上线！PC/Mac v4.1.104.3536 Stadia v4.1.103.0641](https://forums.larian.com/ubbthreads.php?Number=769744&ubb=showflat). 检索于 2025-11-26. [存档](https://web.archive.org/web/20250914070510/https://forums.larian.com/ubbthreads.php?ubb=showflat&Number=769744) 自原始链接，存档于 2025-09-14。

1. [↑](#cite_ref-10) PCGamesN：Will Nelson (2023-07-29). [博德之门3的作弊骰子不会给 NPC 400% 的额外伤害](https://www.pcgamesn.com/baldurs-gate-3/karmic-dice-fix). 检索于 2025-11-26. [存档](https://web.archive.org/web/20250913022015/https://www.pcgamesn.com/baldurs-gate-3/karmic-dice-fix) 自原始链接，存档于 2025-09-13。

1. [↑](#cite_ref-12) PC Gamer：Mollie Taylor (2023-08-11). [如果你陷入博德之门3业力骰子的争论中，Larian 说你应该把它想象成“一个友好的 DM”](https://www.pcgamer.com/if-youre-stuck-in-the-middle-of-baldurs-gate-3s-karmic-dice-debate-larian-says-you-should-think-of-it-like-a-friendly-dm/). 检索于 2025-11-26. [存档](https://web.archive.org/web/20250406095938/https://www.pcgamer.com/if-youre-stuck-in-the-middle-of-baldurs-gate-3s-karmic-dice-debate-larian-says-you-should-think-of-it-like-a-friendly-dm/) 自原始链接，存档于 2025-04-06。

---
*Source: [Dice rolls](https://bg3.wiki/wiki/Dice_rolls)*