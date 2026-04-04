# 生物体型

**[生物](Creatures.md "Creatures")的体型**表示其大小。

## 目录

- [1 概述](#overview)
- [2 体型类别](#size-categories)
- [3 修改体型](#modifying-size)
  - [3.1 形态改变](#altered-form)
  - [3.2 巨化与缩小](#enlarge-and-reduce)
- [4 错误](#bugs)
- [5 注释](#notes)

## 概述

生物体型大致传达了其他参数，如模型尺寸、物理占据的空间、重量以及与环境的互动能力，例如通过[崎岖的裂缝](Rocky_Crevice.md "Rocky Crevice")和[地洞](Burrow_Hole.md "Burrow Hole")。

通过选择生物并选择*检查*，或用光标瞄准它并按下相应的快捷键，可以检查生物的体型和重量。

生物的重量影响谁或什么可以[投掷](Throw.md "Throw")或[推击](Shove.md "Shove")它。

- 生物可以投掷重量不超过 0.2×力量² 公斤或 0.4×力量² 磅的物品和其他生物。
  - 例如，力量为 18 时，可以投掷重量不超过 0.2×18² 公斤 = 64.8 公斤（或 130 磅）的物体。
- 当生物的体型改变时，其重量也会根据需要调整以符合上述类别。

## 体型类别

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "Cat")、[岩石蛛](Crag_Spider.md "Crag Spider")、[青蛙](Frog.md "Frog")和[风元素](Air_Elemental.md "Air Elemental") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "Halfling")、[侏儒](Gnome.md "Gnome")、[地精](Goblin.md "Goblin")和[恐鸦](Dire_Raven.md "Dire Raven") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "Human")、[矮人](Dwarf.md "Dwarf")[[#cite_note-1](#cite_note-1) "note 1"]，以及大多数其他[可玩种族](Race.md "Race") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "Ogre (creature)")、[枭熊](Owlbear.md "Owlbear")、[安苏](Ansur.md "Ansur")[[#cite_note-2](#cite_note-2) "note 2"] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "Red Dragon") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "Nautiloid (Creature)") |

## 修改体型

### 形态改变

当生物的形态被改变时（下表中的示例），其继承的部分参数包括该形态的体型和重量，如上表所示。

| 状态 | 体型 | 来源 | 持续时间 |
| --- | --- | --- | --- |
| [伪装术](Disguise_Self_(Condition).md "Disguise Self (Condition)") | 相应[种族](Race.md "Race")的体型（侏儒和半身人为小型，其他为中型） | [变形生物面具](Mask_of_the_Shapeshifter.md "Mask_of_the Shapeshifter") ([变形](Shapeshift.md "Shapeshift")) | 持续时间：直至[长休](Long_Rest.md "Long rest") |
| [伪装术](Disguise_Self.md "Disguise Self") |  |  |  |
| [千面之脸](Mask_of_Many_Faces.md "Mask of Many Faces") |  |  |  |
| [伪装术](Seeming.md "Seeming") |  |  |  |
| [荒野形态：獾](Wild_Shape_colon__Badger_(Condition).md "Wild Shape: Badger (Condition)") | 中型 | [荒野形态](Wild_Shape.md "Wild Shape") | 持续时间：直至[长休](Long_Rest.md "Long rest") |
| [荒野形态：极地熊](Wild_Shape_colon__Polar_Bear_(Condition).md "Wild Shape: Polar Bear (Condition)") | 大型 |  |  |
| [荒野形态：猫](Wild_Shape_colon__Cat_(Condition).md "Wild Shape: Cat (Condition)") | 微型 |  |  |
| [荒野形态：巨蜘蛛](Wild_Shape_colon__Giant_Spider_(Condition).md "Wild Shape: Giant Spider (Condition)") | 中型 |  |  |
| [荒野形态：恐狼](Wild_Shape_colon__Dire_Wolf_(Condition).md "Wild Shape: Dire Wolf (Condition)") | 中型 |  |  |
| [荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven_(Condition).md "Wild Shape: Dire Raven (Condition)") | 小型 |  |  |
| [荒野形态：地底洛斯兽](Wild_Shape_colon__Deep_Rothé_(Condition).md "Wild Shape: Deep Rothé (Condition)") | 大型 |  |  |
| [荒野形态：黑豹](Wild_Shape_colon__Panther_(Condition).md "Wild Shape: Panther (Condition)") | 中型 |  |  |
| [荒野形态：枭熊](Wild_Shape_colon__Owlbear_(Condition).md "Wild Shape: Owlbear (Condition)") | 大型 |  |  |
| [荒野形态：剑齿虎](Wild_Shape_colon__Sabre-Toothed_Tiger_(Condition).md "Wild Shape: Sabre-Toothed Tiger (Condition)") | 中型 |  |  |
| [荒野形态：双脊龙](Wild_Shape_colon__Dilophosaurus_(Condition).md "Wild Shape: Dilophosaurus (Condition)") | 大型 |  |  |
| [荒野形态：风元素执政官](Wild_Shape_colon__Air_Myrmidon_(Condition).md "Wild Shape: Air Myrmidon (Condition)") | 小型 |  |  |
| [荒野形态：土元素执政官](Wild_Shape_colon__Earth_Myrmidon_(Condition).md "Wild Shape: Earth Myrmidon (Condition)") | 中型 |  |  |
| [荒野形态：火元素执政官](Wild_Shape_colon__Fire_Myrmidon_(Condition).md "Wild Shape: Fire Myrmidon (Condition)") | 小型 |  |  |
| [荒野形态：水元素执政官](Wild_Shape_colon__Water_Myrmidon_(Condition).md "Wild Shape: Water Myrmidon (Condition)") | 中型 |  |  |
| [气化形体](Gaseous_Form_(Condition).md "Gaseous Form (Condition)") | 微型 | [气化形体](Gaseous_Form.md "Gaseous Form") | 持续时间：直至[长休](Long_Rest.md "Long rest") |
| [云雾势](Mist_Stance.md "Mist Stance") |  |  |  |
| [御风而行](Wind_Walk.md "Wind Walk") |  |  |  |
| [狂野魔法：猫形态](Wild_Magic_colon__Cat_Form_(Condition).md "Wild Magic: Cat Form (Condition)") | 微型 | [狂野魔法：猫与狗](Wild_Magic_colon__Cats_and_Dogs.md "Wild Magic: Cats and Dogs") | 持续时间：2 回合 |
| [狂野魔法：狗形态](Wild_Magic_colon__Dog_Form_(Condition).md "Wild Magic: Dog Form (Condition)") | 小型 |  |  |
| [变形](Polymorphed_(Condition).md "Polymorphed (Condition)") | 中型 | [狂野魔法：变形术](Wild_Magic_colon__Polymorph.md "Wild Magic: Polymorph") | 持续时间：2 回合 |
| [变形术](Polymorph.md "Polymorph") | 持续时间：5 回合 |  |  |
| [蟾蜍模式](Toad_Mode_(Condition).md "Toad Mode (Condition)") | 微型 | [多利多利多利](Dolly_Dolly_Dolly.md "Dolly Dolly Dolly") | 持续时间：1 回合 |
| [大猪](Big_Pig_(Condition).md "Big Pig (Condition)") | 中型 |  |  |
| [牛语](Cattle_Prattle_(Condition).md "Cattle Prattle (Condition)") | 大型 |  |  |
| [移位兽形态](Displacer_Beast_Form_(Condition).md "Displacer Beast Form (Condition)") | 中型 | [移位兽形态](Displacer_Beast_Shape.md "Displacer Beast Shape") | 持续时间：直至[长休](Long_Rest.md "Long rest") |
| [杀戮者形态](Slayer_Form_(Condition).md "Slayer Form (Condition)") | 大型 | [杀戮者 (职业动作)](Slayer_(class_action).md "Slayer (Class Action)") | 持续时间：直至[长休](Long_Rest.md "Long rest") |

### 巨化与缩小

此外，可以对角色的体型进行额外修改，将其转移到相邻的类别，如下表所示。

- 生物无法改变为大于超巨型或小于微型的类别。
  - 其他参数（如物理模型）仍可改变大小。
- 巨化重量 = 原始重量 × 2.35，或新体型的最小重量，取较大者。
- 缩小重量 = 原始重量 / 2.35，或新体型的最大重量，取较小者。
- 具有*相同*堆叠 ID（见下文）的状态，如果添加了另一个来源，则会被替换/刷新；它们不会叠加。
| [堆叠 ID](Conditions#Stack_ID.md#Stack_ID "Conditions") | 状态 | 体型变化 | 来源 | 持续时间 |
| --- | --- | --- | --- | --- |
| SIZE | [缩小](Reduced_(Condition).md "Reduced (Condition)") | -1 | [收缩油](Oil_of_Diminution.md "Oil of Diminution") | 持续时间：2 回合 |
| [塞山](Sethan.md "Sethan") ([塞山：缩小](Sethan_colon__Reduce.md "Sethan: Reduce")) | 持续时间：5 回合 |  |  |  |
| [缩小](Reduce.md "Reduce") | 持续时间：10 回合 |  |  |  |
| [巨化](Enlarged_(Condition).md "Enlarged (Condition)") | +1 | [巨化](Enlarge.md "Enlarge") | 持续时间：10 回合 |  |
| [灰矮人](Duergar.md "Duergar")的[巨化](Enlarge.md "Enlarge") |  |  |  |  |
| [大男孩的磨牙玩具](Bigboy's_Chew_Toy.md "Bigboy's Chew Toy") ([大块头？](Whossa_Large_Fellow_q_.md "Whossa Large Fellow?")) |  |  |  |  |
| [巨人狂暴](Giant's_Rage_(Condition).md "Giant's Rage (Condition)") | [巨人野蛮人](Giant_Barbarian.md "Giant Barbarian")的[巨人狂暴](Giant's_Rage.md "Giant's Rage") |  |  |  |
| [巨人形态](Giant_Form_(Condition).md "Giant Form (Condition)") | [博德安的巨人杀手](Balduran's_Giantslayer.md "Balduran's Giantslayer") ([巨人形态](Giant_Form.md "Giant Form")) |  |  |  |
| ALCH_ELIXIR | [巨像灵药](Elixir_of_The_Colossus_(Condition).md "Elixir of The Colossus (Condition)") | +1 | [巨像灵药](Elixir_of_the_Colossus.md "Elixir of the Colossus") | 持续时间：直至[长休](Long_Rest.md "Long rest") |

  - 例如，一个[灰矮人](Duergar.md "Duergar")受到[巨化](Enlarged_(Condition).md "Enlarged (Condition)")效果时是大型，使用[大块头？](Whossa_Large_Fellow_q_.md "Whossa Large Fellow?")会先取消巨化，然后重新应用它。
- 对一个[缩小](Reduced_(Condition).md "Reduced (Condition)")的角色使用[巨化](Enlarge.md "Enlarge")会先取消后一个状态（无论初始来源如何），然后应用巨化，可能使其整体体型改变 2 个类别。
  - 尽管是一个独立的状态并有额外效果，[巨人形态](Giant_Form_(Condition).md "Giant Form (Condition)")占据与巨化和缩小相同的“槽位”。
- 具有*不同*堆叠 ID 的状态*可以*叠加，根据需要改变角色的体型。
  - 巨化的角色使用[巨像灵药](Elixir_of_the_Colossus.md "Elixir of the Colossus")会进一步增加体型。
  - 具有[巨像灵药](Elixir_of_The_Colossus_(Condition).md "Elixir of The Colossus (Condition)")的生物如果被缩小，会先返回原始体型，然后在任一效果结束或被替换时再次根据需要改变。
- 这些变化*在*考虑形态/形态改变*之后*应用。
  - 因此，中型猫、超巨型枭熊或小型绵羊都是可能的，以及其他组合。
- 在荣誉模式中，[巨像灵药](Elixir_of_The_Colossus_(Condition).md "Elixir of The Colossus (Condition)")与[缩小](Reduced_(Condition).md "Reduced (Condition)")、[巨化](Enlarged_(Condition).md "Enlarged (Condition)")和[巨人形态](Giant_Form_(Condition).md "Giant Form (Condition)")互斥，但仍可与[巨人狂暴](Giant's_Rage_(Condition).md "Giant's Rage (Condition)")叠加。

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "Cat")、[岩石蛛](Crag_Spider.md "Crag Spider")、[青蛙](Frog.md "Frog")和[风元素](Air_Elemental.md "Air Elemental") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "Halfling")、[侏儒](Gnome.md "Gnome")、[地精](Goblin.md "Goblin")和[恐鸦](Dire_Raven.md "Dire Raven") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "Human")、[矮人](Dwarf.md "Dwarf")[[#cite_note-1](#cite_note-1) "note 1"]，以及大多数其他[可玩种族](Race.md "Race") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "Ogre (creature)")、[枭熊](Owlbear.md "Owlbear")、[安苏](Ansur.md "Ansur")[[#cite_note-2](#cite_note-2) "note 2"] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "Red Dragon") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "Nautiloid (Creature)") |

## 错误

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "Cat")、[岩石蛛](Crag_Spider.md "Crag Spider")、[青蛙](Frog.md "Frog")和[风元素](Air_Elemental.md "Air Elemental") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "Halfling")、[侏儒](Gnome.md "Gnome")、[地精](Goblin.md "Goblin")和[恐鸦](Dire_Raven.md "Dire Raven") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "Human")、[矮人](Dwarf.md "Dwarf")[[#cite_note-1](#cite_note-1) "note 1"]，以及大多数其他[可玩种族](Race.md "Race") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "Ogre (creature)")、[枭熊](Owlbear.md "Owlbear")、[安苏](Ansur.md "Ansur")[[#cite_note-2](#cite_note-2) "note 2"] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "Red Dragon") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "Nautiloid (Creature)") |

- 任何 4 种巨化状态（[巨化](Enlarged_(Condition).md "Enlarged (Condition)")等）在生物最终变为巨型或超巨型时引起的重量增加（而非体型）是不稳定的；它可能会在执行动作或获得或失去状态时丢失或恢复。
- [变形](Polymorphed_(status_group) other than Starry Forms double all adjustments to size category (but not weight or visual size) from [缩小](Reduced_(Condition).md "Reduced (Condition)") and pre-existing enlarging conditions. For example, a reduced character [Disguised](Disguise_Self_(Condition).md "Disguise Self (Condition)") as an elf is Tiny, not Small, but still weighs 32 kg (64 lb).

## 注释

1. [↑](#cite_ref-1) 尽管身材较矮且[移动速度](Resources.md#Movement_speed "Movement speed")较慢，矮人确实是中型生物，并相应地与其他游戏机制互动。
2. [↑](#cite_ref-2) 安苏的体型在死亡时显示为巨型，活着时显示为大型。这是由于两个角色属性条目，一个 GameSize 为巨型，重量为 4000 公斤。死亡时，安苏的尸体被视为游戏对象（类似于可拾取的尸体），游戏引用 GameSize 条目，将安苏归类为巨型。活着时，安苏被视为变形角色，游戏引用 Weight 条目，由于其值将安苏归类为大型。因此，活着的安苏可以受到通常不会对巨型角色生效的法术和攻击的影响。

---
*Source: [Creature size](https://bg3.wiki/wiki/Creature_size)*