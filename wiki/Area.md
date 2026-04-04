# 区域

**区域**描述的是对进入其中的生物具有特殊效果的空间。它们可以由[物品](Items.md "物品")、[法术](Spells.md "法术")或生物动作生成。区域具有描述其特性的属性。

## 目录

- [1 区域类型](#区域类型)
  - [1.1 地表](#地表)
  - [1.2 云](#云)
  - [1.3 召唤](#召唤)
- [2 区域交互](#区域交互)

## 区域类型

存在不同类型的区域，它们具有不同的属性和交互方式。

### 地表

主条目：[地表](Surfaces.md "地表")

一种作为平坦层存在于地板上的区域。地表的效果可以通过使用[飞行术](Fly_(class_action).md "飞行术（职业动作）")或[魔法飓风：飞行](Tempestuous_Magic_colon__Flight.md "魔法飓风：飞行")等飞越其上方来避免。地表包括[强酸](Acid_(surface).md "强酸（地表）")地表或[冰](Ice_(surface).md "冰（地表）")地表，也可以包括[蛛网术](Web.md "蛛网术")等法术。这些区域可以在游戏中检查，并显示为地表。

地表示例包括：

- [强酸](Acid_(surface).md "强酸（地表）")
- [火焰](Fire_(surface).md "火焰（地表）")
- [油脂](Grease_(surface).md "油脂（地表）")

### 云

主条目：[云](Clouds.md "云")

一种作为云存在于地板上方的区域。它们可以通过[造风术](Gust_of_Wind.md "造风术")吹散。这些区域可以在游戏中检查，并显示为云。

云示例包括：

- [死云术](Cloudkill_(cloud).md "死云术（云）")
- [雾](Fog.md "雾")

### 召唤

在战斗日志中显示为被召唤的区域。召唤区域通常通过向进入其中的生物施加状态来工作。召唤区域可以放置在彼此之上，但不能与相同的区域堆叠，因为一个生物一次只能拥有一个施加的状态实例。这些区域无法在游戏中检查，但可能在其源法术上找到一个代表它们的状态，该状态与进入时施加的状态不同。

召唤区域示例包括：

- [哈达之饥渴](Hunger_of_Hadar_(area).md "哈达之饥渴（区域）").

## 区域交互

游戏中存在多种可以改变区域的交互类型。这些交互以 `SurfaceChange()` 函数的形式出现。并非所有交互都适用于所有地表，请参阅区域页面上的“交互”以查看其交互对象和方式。

这些值来自 `ValueLists.txt`：

| 值 | 描述 | 示例 | 来源 |
| --- | --- | --- | --- |
| None |  |  |  |
| Clear |  |  |  |
| Condense |  |  |  |
| CreateWater | 熄灭火焰 | 可以移除火焰 | [造水术](Create_Water.md "造水术") |
| Daylight |  |  | [昼明术](Daylight.md "昼明术") |
| Deelectrify |  |  |  |
| DestroyWater | 摧毁水 | 移除水 | [枯水术](Destroy_Water.md "枯水术") |
| Douse | 熄灭火焰 | 可以移除火焰 | [冷冻射线](Ray_of_Frost.md "冷冻射线") |
| Electrify | 使地表带电 | 可以将水变成带电的水 | [电爪](Shocking_Grasp.md "电爪") |
| Freeze | 冻结区域 | 可以将水变成冰 | [冷冻射线](Ray_of_Frost.md "冷冻射线") |
| Ignite | 爆炸区域或将其点燃 | 可以引爆烟粉并将多个地表变成火焰 | [火球术](Fireball.md "火球术"), [火焰箭](Fire_Bolt.md "火焰箭") |
| Melt | 融化地表 | 可以将冰变成水 | [火球术](Fireball.md "火球术"), [火焰箭](Fire_Bolt.md "火焰箭") |
| TurnHellfire |  |  | [排放地狱火](Hellfire_Exhaust.md "排放地狱火"), [地狱火飞弹](Hellfire_Missiles.md "地狱火飞弹"), [爆燃火花](Igniting_Spark.md "爆燃火花"), [恶魔锁链](Diabolic_Chains.md "恶魔锁链"), [肆虐地狱](Ravaging_Inferno.md "肆虐地狱") |
| UnturnHellfire |  |  |  |
| Vaporize | 蒸发地表 |  |  |
|  |  |  |  |

---
*Source: [Areas](https://bg3.wiki/wiki/Areas)*