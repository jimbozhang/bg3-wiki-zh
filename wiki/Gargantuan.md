# 生物体型

**[生物](Creatures.md "生物")** 的**体型**表示其大小。

## 目录

- [1 概述](#overview)
- [2 体型类别](#size-categories)
- [3 修改体型](#modifying-size)
  - [3.1 形态改变](#altered-form)
  - [3.2 巨化与缩小](#enlarge-and-reduce)
- [4 错误](#bugs)
- [5 注释](#notes)

## 概述

生物体型大致传达了其他参数，如模型尺寸、物理占据空间、重量以及与环境互动的能力，例如通过[崎岖的裂缝](Rocky_Crevice.md "崎岖的裂缝")和[地洞](Burrow_Hole.md "地洞")。

生物的体型和重量可以通过选择它并选择*检查*，或用光标瞄准它并按下相应的热键来查看。

生物的重量影响谁或什么可以[投掷](Throw.md "投掷")或[推击](Shove.md "推击")它。

- 生物可以投掷重量不超过 0.2×力量² 公斤或 0.2×力量² 磅的物品和其他生物。
  - 例如，力量为 18 时，可以投掷重量不超过 0.2×18² 公斤 = 64.8 公斤（或 130 磅）的物体。
- 当生物的体型改变时，其重量也会根据需要调整以符合上述类别。

## 体型类别

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "猫")、[岩石蛛](Crag_Spider.md "岩石蛛")、[青蛙](Frog.md "青蛙")和[风元素](Air_Elemental.md "风元素") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "半身人")、[侏儒](Gnome.md "侏儒")、[地精](Goblin.md "地精")和[恐鸦](Dire_Raven.md "恐鸦") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "人类")、[矮人](Dwarf.md "矮人")[[#cite_note-1](#cite_note-1 "注释 1")]，以及大多数其他[可玩种族](Race.md "种族") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "食人魔（生物）")、[枭熊](Owlbear.md "枭熊")、[安苏](Ansur.md "安苏")[[#cite_note-2](#cite_note-2 "注释 2")] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "红龙") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "鹦鹉螺（生物）") |

## 修改体型

### 形态改变

当生物的形态被改变时（下表中的示例），它们继承的部分参数包括该形态的体型和重量，如上表所示。

| 状态 | 体型 | 来源 | 持续时间 |
| --- | --- | --- | --- |
| [伪装术](Disguise_Self_(Condition).md "伪装术（状态）") | 相应[种族](Race.md "种族")的体型（侏儒和半身人为小型，其他为中型） | [变形生物面具](Mask_of_the_Shapeshifter.md "变形生物面具")（[变形](Shapeshift.md "变形")） | 持续时间：直至[长休](Long_Rest.md "长休") |
| [伪装术](Disguise_Self.md "伪装术") |  |  |  |
| [千面之脸](Mask_of_Many_Faces.md "千面之脸") |  |  |  |
| [伪装术](Seeming.md "伪装术") |  |  |  |
| [荒野形态：獾](Wild_Shape_colon__Badger_(Condition).md "荒野形态：獾（状态）") | 中型 | [荒野形态](Wild_Shape.md "荒野形态") | 持续时间：直至[长休](Long_Rest.md "长休") |
| [荒野形态：极地熊](Wild_Shape_colon__Polar_Bear_(Condition).md "荒野形态：极地熊（状态）") | 大型 |  |  |
| [荒野形态：猫](Wild_Shape_colon__Cat_(Condition).md "荒野形态：猫（状态）") | 微型 |  |  |
| [荒野形态：巨蜘蛛](Wild_Shape_colon__Giant_Spider_(Condition).md "荒野形态：巨蜘蛛（状态）") | 中型 |  |  |
| [荒野形态：恐狼](Wild_Shape_colon__Dire_Wolf_(Condition).md "荒野形态：恐狼（状态）") | 中型 |  |  |
| [荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven_(Condition).md "荒野形态：恐鸦（状态）") | 小型 |  |  |
| [荒野形态：地底洛斯兽](Wild_Shape_colon__Deep_Rothé_(Condition).md "荒野形态：地底洛斯兽（状态）") | 大型 |  |  |
| [荒野形态：黑豹](Wild_Shape_colon__Panther_(Condition).md "荒野形态：黑豹（状态）") | 中型 |  |  |
| [荒野形态：枭熊](Wild_Shape_colon__Owlbear_(Condition).md "荒野形态：枭熊（状态）") | 大型 |  |  |
| [荒野形态：剑齿虎](Wild_Shape_colon__Sabre-Toothed_Tiger_(Condition).md "荒野形态：剑齿虎（状态）") | 中型 |  |  |
| [荒野形态：双脊龙](Wild_Shape_colon__Dilophosaurus_(Condition).md "荒野形态：双脊龙（状态）") | 大型 |  |  |
| [荒野形态：风元素执政官](Wild_Shape_colon__Air_Myrmidon_(Condition).md "荒野形态：风元素执政官（状态）") | 小型 |  |  |
| [荒野形态：土元素执政官](Wild_Shape_colon__Earth_Myrmidon_(Condition).md "荒野形态：土元素执政官（状态）") | 中型 |  |  |
| [荒野形态：火元素执政官](Wild_Shape_colon__Fire_Myrmidon_(Condition).md "荒野形态：火元素执政官（状态）") | 小型 |  |  |
| [荒野形态：水元素执政官](Wild_Shape_colon__Water_Myrmidon_(Condition).md "荒野形态：水元素执政官（状态）") | 中型 |  |  |
| [气化形体](Gaseous_Form_(Condition).md "气化形体（状态）") | 微型 | [气化形体](Gaseous_Form.md "气化形体") | 持续时间：直至[长休](Long_Rest.md "长休") |
| [云雾势](Mist_Stance.md "云雾势") |  |  |  |
| [御风而行](Wind_Walk.md "御风而行") |  |  |  |
| [狂野魔法：猫形态](Wild_Magic_colon__Cat_Form_(Condition).md "狂野魔法：猫形态（状态）") | 微型 | [狂野魔法：猫狗](Wild_Magic_colon__Cats_and_Dogs.md "狂野魔法：猫狗") | 持续时间：2 驱散 |
| [狂野魔法：狗形态](Wild_Magic_colon__Dog_Form_(Condition).md "狂野魔法：狗形态（状态）") | 小型 |  |  |
| [变形](Polymorphed_(Condition).md "变形（状态）") | 中型 | [狂野魔法：变形术](Wild_Magic_colon__Polymorph.md "狂野魔法：变形术") | 持续时间：2 驱散 |
| [变形术](Polymorph.md "变形术") | 持续时间：5 驱散 |  |  |
| [蟾蜍模式](Toad_Mode_(Condition).md "蟾蜍模式（状态）") | 微型 | [多利多利多利](Dolly_Dolly_Dolly.md "多利多利多利") | 持续时间：1 驱散 |
| [大猪](Big_Pig_(Condition).md "大猪（状态）") | 中型 |  |  |
| [牛语](Cattle_Prattle_(Condition).md "牛语（状态）") | 大型 |  |  |
| [移位兽形态](Displacer_Beast_Form_(Condition).md "移位兽形态（状态）") | 中型 | [移位兽形态](Displacer_Beast_Shape.md "移位兽形态") | 持续时间：直至[长休](Long_Rest.md "长休") |
| [杀戮者形态](Slayer_Form_(Condition).md "杀戮者形态（状态）") | 大型 | [杀戮者（职业动作）](Slayer_(class_action).md "杀戮者（职业动作）") | 持续时间：直至[长休](Long_Rest.md "长休") |

### 巨化与缩小

此外，可以对角色的体型进行额外修改，将其转移到相邻的类别，如下表所示。

- 生物无法改变为大于超巨型或小于微型的类别。
  - 其他参数（如物理模型）仍可改变大小。
- 巨化重量 = 原始重量 × 2.35，或新体型的最小重量，取较大者。
- 缩小重量 = 原始重量 / 2.35，或新体型的最大重量，取较小者。
- 具有*相同*堆叠 ID（见下文）的状态，如果添加了另一个来源，则会被替换/刷新；它们不会堆叠。
| [堆叠 ID](Conditions#Stack_ID.md#Stack_ID "状态") | 状态 | 体型变化 | 来源 | 持续时间 |
| --- | --- | --- | --- | --- |
| SIZE | [缩小](Reduced_(Condition).md "缩小（状态）") | -1 | [收缩油](Oil_of_Diminution.md "收缩油") | 持续时间：2 驱散 |
| [塞山](Sethan.md "塞山")（[塞山：缩小](Sethan_colon__Reduce.md "塞山：缩小")） | 持续时间：5 驱散 |  |  |  |
| [缩小](Reduce.md "缩小") | 持续时间：10 驱散 |  |  |  |
| [巨化](Enlarged_(Condition).md "巨化（状态）") | +1 | [巨化](Enlarge.md "巨化") | 持续时间：10 驱散 |  |
| [灰矮人](Duergar.md "灰矮人")的[巨化](Enlarge.md "巨化") |  |  |  |  |
| [大男孩的磨牙玩具](Bigboy's_Chew_Toy.md "大男孩的磨牙玩具")（[谁是大块头？](Whossa_Large_Fellow_q_.md "谁是大块头？")） |  |  |  |  |
| [巨人狂暴](Giant's_Rage_(Condition).md "巨人狂暴（状态）") | [巨人野蛮人](Giant_Barbarian.md "巨人野蛮人")的[巨人狂暴](Giant's_Rage.md "巨人狂暴") |  |  |  |
| [巨人形态](Giant_Form_(Condition).md "巨人形态（状态）") | [博德安的巨人杀手](Balduran's_Giantslayer.md "博德安的巨人杀手")（[巨人形态](Giant_Form.md "巨人形态")） |  |  |  |
| ALCH_ELIXIR | [巨像灵药](Elixir_of_The_Colossus_(Condition).md "巨像灵药（状态）") | +1 | [巨像灵药](Elixir_of_the_Colossus.md "巨像灵药") | 持续时间：直至[长休](Long_Rest.md "长休") |

  - 例如，一个[灰矮人](Duergar.md "灰矮人")受到[巨化](Enlarged_(Condition).md "巨化（状态）")影响时体型为大型，使用[谁是大块头？](Whossa_Large_Fellow_q_.md "谁是大块头？")会先取消巨化，然后重新应用。
- 对处于[缩小](Reduced_(Condition).md "缩小（状态）")状态的角色使用[巨化](Enlarge.md "巨化")会先取消后一状态（无论初始来源如何），然后应用巨化，可能使其整体体型改变 2 个类别。
  - 尽管是一个独立的状态并有额外效果，[巨人形态](Giant_Form_(Condition).md "巨人形态（状态）")占用与巨化和缩小相同的“槽位”。
- 具有*不同*堆叠 ID 的状态*可以*堆叠，根据需要改变角色的体型。
  - 处于巨化状态的角色使用[巨像灵药](Elixir_of_the_Colossus.md "巨像灵药")会进一步增加体型。
  - 具有[巨像灵药](Elixir_of_The_Colossus_(Condition).md "巨像灵药（状态）")的生物如果随后被缩小，会先返回原始体型，然后在任一效果结束或被替换时再次根据需要改变。
- 这些变化*在*考虑形态/形态改变*之后*应用。
  - 因此，中型猫、超巨型枭熊或小型绵羊都是可能的，以及其他组合。
- 在荣誉模式中，[巨像灵药](Elixir_of_The_Colossus_(Condition).md "巨像灵药（状态）")与[缩小](Reduced_(Condition).md "缩小（状态）")、[巨化](Enlarged_(Condition).md "巨化（状态）")和[巨人形态](Giant_Form_(Condition).md "巨人形态（状态）")互斥，但仍可与[巨人狂暴](Giant's_Rage_(Condition).md "巨人狂暴（状态）")堆叠。

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "猫")、[岩石蛛](Crag_Spider.md "岩石蛛")、[青蛙](Frog.md "青蛙")和[风元素](Air_Elemental.md "风元素") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "半身人")、[侏儒](Gnome.md "侏儒")、[地精](Goblin.md "地精")和[恐鸦](Dire_Raven.md "恐鸦") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "人类")、[矮人](Dwarf.md "矮人")[[#cite_note-1](#cite_note-1 "注释 1")]，以及大多数其他[可玩种族](Race.md "种族") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "食人魔（生物）")、[枭熊](Owlbear.md "枭熊")、[安苏](Ansur.md "安苏")[[#cite_note-2](#cite_note-2 "注释 2")] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "红龙") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "鹦鹉螺（生物）") |

## 错误

| 体型 | 最小重量 | 最大重量 | 示例生物 |  |  |
| --- | --- | --- | --- | --- | --- |
| 公斤 | 磅 | 公斤 | 磅 |  |  |
| 微型 | 0 | 0 | 6 | 12 | [猫](Cat.md "猫")、[岩石蛛](Crag_Spider.md "岩石蛛")、[青蛙](Frog.md "青蛙")和[风元素](Air_Elemental.md "风元素") |
| 小型 | 11 | 22 | 40 | 80 | [半身人](Halfling.md "半身人")、[侏儒](Gnome.md "侏儒")、[地精](Goblin.md "地精")和[恐鸦](Dire_Raven.md "恐鸦") |
| 中型 | 45 | 90 | 200 | 400 | [人类](Human.md "人类")、[矮人](Dwarf.md "矮人")[[#cite_note-1](#cite_note-1 "注释 1")]，以及大多数其他[可玩种族](Race.md "种族") |
| 大型 | 205 | 410 | 5,000 | 10,000 | [食人魔](Ogre_(creature).md "食人魔（生物）")、[枭熊](Owlbear.md "枭熊")、[安苏](Ansur.md "安苏")[[#cite_note-2](#cite_note-2 "注释 2")] |
| 巨型 | 5,005 | 10,010 | 50,000 | 100,000 | [红龙](Red_Dragon.md "红龙") |
| 超巨型 | 50,005 | 100,010 | 500,000 | 1,000,000 | [鹦鹉螺](Nautiloid_(Creature).md "鹦鹉螺（生物）") |

- 任何 4 种巨化状态（[巨化](Enlarged_(Condition).md "巨化（状态）")等）在生物最终成为巨型或超巨型时引起的重量增加（而非体型）不稳定；它可能会在执行动作或获得或失去状态时丢失或恢复。
- [变形](Polymorphed_(status_group) other than Starry Forms 双倍所有对体型类别（而非重量或视觉大小）的调整，来自[缩小](Reduced_(Condition).md "缩小（状态）")和预先存在的巨化状态。例如，一个被缩小的角色[伪装](Disguise_Self_(Condition).md "伪装术（状态）")成精灵是微型，而非小型，但重量仍为 32 公斤（64 磅）。

## 注释

1. [↑](#cite_ref-1) 尽管身材较矮且[移动速度](Resources.md#Movement_speed "移动速度")降低，但矮人确实是中型生物，相应地与其他游戏机制互动。
1. [↑](#cite_ref-2) 安苏的体型在死亡时显示为巨型，存活时显示为大型。这是由于两个角色属性条目，GameSize 为巨型，重量为 4000 公斤。死亡时，安苏的尸体被视为游戏对象（类似于可拾取的尸体），游戏引用 GameSize 条目，将安苏归类为巨型。存活时，安苏被视为变形角色，游戏引用 Weight 条目，由于其值将安苏归类为大型。因此，存活时安苏会受到通常对巨型角色无效的法术和攻击的影响。

---
*Source: [Creature size](https://bg3.wiki/wiki/Creature_size)*