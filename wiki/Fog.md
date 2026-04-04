# 雾

另请参阅：[云雾术](Fog_Cloud.md "Fog Cloud")

**雾**是一种[云](Cloud.md "Cloud")，会使其中的生物目盲并遮蔽视线，阻挡NPC的视线锥，并阻止需要视线的攻击和法术。

## 描述

使其中的生物重度遮蔽并目盲。

## 属性

类型：[云](Area.md#Cloud "Area")

## 状态：目盲

**[目盲](Blinded_(Condition).md "Blinded (Condition)")**

持续时间：停留在地表时

- 受影响的生物在[攻击掷骰](Attack_roll.md "Attack Roll")上具有[劣势](Disadvantage.md "Disadvantage")。
- 受影响的生物的攻击和法术范围减少至3米（10英尺）。
- 对受影响生物的攻击掷骰具有[优势](Advantage.md "Advantage")。

## 创建

此区域可由以下方式创建：

物品：

- [诡诈之雾披风](Cloak_of_Cunning_Brume.md "Cloak of Cunning Brume")
- [严厉之锤的薄雾护符](Hammergrim_Mist_Amulet.md "Hammergrim Mist Amulet")

法术和动作：

- [云雾术](Fog_Cloud.md "Fog Cloud")
- [狂野魔法：雾](Wild_Magic_colon__Fog.md "Wild Magic: Fog")

## 备注

**错误与技术说明**

- 有一个已知的关于 `IgnoreSurfaceCover` 内部增益的错误，该错误在**雾**中显现。具体来说，如果一个地表具有属性 `CanSeeThrough = false` 但 `CanShootThrough = true`（如[云雾术](Fog_Cloud.md "Fog Cloud")），_任何_ 活跃的 `IgnoreSurfaceCover` 增益都允许生物看穿它。相反，如果 `CanShootThrough = false`（如[黑暗术](Darkness.md "Darkness")），则生物必须具有特定的 `IgnoreSurfaceCover(SurfaceDarknessCloud)` 增益才能看穿它。结果是，授予看穿魔法黑暗能力的特性（例如[魔鬼视界](Devil's_Sight.md "Devil's Sight")）隐含地授予看穿雾的能力，但针对雾的防护对黑暗无效。

如果以上内容未能让您完全理解，请继续阅读：

**雾与视觉的技术影响**
在_博德之门3_中，**雾**（以及[云雾术](Fog_Cloud.md "Fog Cloud")法术）充当一种独特的战术屏障，因为它扰乱了游戏正常的战场逻辑。与实体墙壁不同，_雾_允许物理物体（如箭）通过，同时完全阻挡生物的视线。这为隐匿、瞄准和战斗提供了一套特定的互动方式：

1. 隐匿与视线锥

  - 雾的主要战术优势是其创造“盲点”的能力。因为雾阻挡所有视线，它会立即终止NPC的视线锥。这使得角色即使在完全光照的区域也能保持隐藏，只要他们站在雾云内部或后面。NPC无法发现穿过薄雾潜行的角色，使其成为扒窃或重新定位而不被发现的有用工具。

1. 抛射物动作 vs. 瞄准动作

  - 游戏引擎区分了“发射抛射物”和通过雾使用“瞄准动作”。_以生物或地面位置为目标_的动作需要“视线”，因此会被雾云阻挡。此限制不适用于抛射物动作，如远程武器攻击或抛射物类法术（[魔法飞弹](Magic_Missile.md "Magic Missile")）。抛射物动作通常可以通过瞄准时从施法者到目标的“轨迹线”来区分。
- _远程攻击_（如射箭）则受遮蔽规则而非完全掩护规则支配。虽然雾会创建一个[重度遮蔽](Heavily_Obscured_(Condition).md "Heavily Obscured (Condition)")区域——通常施加[劣势](Disadvantage.md "Disadvantage")——但这可以通过[高级黑暗视觉](Darkvision.md "Darkvision")完全抵消。具有高级黑暗视觉的生物将雾视为一个黑暗的房间；他们可以以正常的攻击掷骰向雾内的目标发射箭或投掷物体，即使他们仍然无法以允许对预定目标施放目标法术的方式“看到”目标。

1. 已知错误

  - 游戏引擎处理允许角色忽略地表覆盖的特性（如[魔鬼视界](Devil's_Sight.md "Devil's Sight")或[永察之戒](Eversight_Ring.md "Eversight Ring")）的方式存在一个错误。如上文代码所示，这源于引擎对地表阻挡_抛射物_能力与阻挡_视觉_能力的分类方式。
    - 如果一个地表阻挡视觉但允许抛射物通过（如_云雾术_），游戏的逻辑是“宽松的”。因此，拥有_任何_形式的“忽略地表”增益——即使是针对完全不同地表（如魔法黑暗）的增益——都会错误地允许角色看穿雾。
- 相反，因为_黑暗_同时阻挡视觉和抛射物，游戏引擎更严格；角色必须具有专门为黑暗编码的增益才能看穿它。具体来说，授予看穿_魔法黑暗_能力的特性（[魔鬼视界](Devil's_Sight.md "Devil's Sight")）也授予看穿_雾_的能力，而仅授予看穿**雾**能力的特性（[高级黑暗视觉](Darkvision.md "Darkvision")）仍然会被_[黑暗](Darkvision_Mechanics.md "Darkvision Mechanics")_阻挡。

1. 效果总结

- _对于隐匿：_ 雾是一个绝对屏障。它在雾的边缘终止NPC的视线锥，允许自动潜行成功而无需掷骰。
- _对于施法者：_ 角色通常无法向云内或云外施放需要“目标”的法术。
- _对于近战角色：_ [高级黑暗视觉](Darkvision.md "Darkvision")允许角色忽略雾的精度惩罚，允许进行正常的远程武器攻击。
- _对于专业装备和被动：_ 绕过魔法黑暗的特性（例如[生于黑暗](Born_into_Darkness.md "Born into Darkness")）充当一种“通用视觉”，允许拥有或使用此类特性的人看穿雾。

---
*Source: [Fog](https://bg3.wiki/wiki/Fog)*