# 荆棘丛生

**荆棘丛生**是一个[法术](Spells.md "法术")。它允许施法者将一片土地转变为危险的尖刺地形。穿过该区域的生物其移动速度减半，并受到穿刺伤害。

## 描述

将一片地面塑造成坚硬的尖刺。在尖刺上行走的生物每移动1.5米（5英尺）会受到2d4⁠⁠[穿刺](Piercing.md "Piercing")伤害。

尖刺是[劣势地形](Difficult_Terrain.md "Difficult Terrain")，使生物的[移动速度](Movement_speed.md "Movement Speed")减半。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [2级法术位](Spells.md#Spell_slots "Spells")
伤害：2~8

2d4⁠[穿刺](Piercing.md "Piercing")（每移动1.5米（5英尺））

详情
射程：18米（60英尺）
创造区域：尖刺
[专注](Concentration.md "Concentration")

## 更高环阶施法

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_SpikeGrowth`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：尖刺

**[尖刺](Spikes.md "Spikes")**

持续时间：100驱散

范围效果：6米（20英尺）半径

每当有生物在尖刺上移动时，造成2d4⁠⁠[穿刺](Piercing.md "Piercing")伤害。

类型：[地表](Area.md#Surface "Area")

### 状态：荆棘丛生

**[荆棘丛生](Spike_Growth_(Condition).md "Spike Growth (Condition)")**

- 在尖刺上每移动1.5米（5英尺），受到2d4⁠⁠[穿刺](Piercing.md "Piercing")伤害。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "Difficult Terrain (Condition)")**

- [移动速度](Movement_speed.md "Movement Speed")减半

## 如何习得

职业：

- 职业等级3：[德鲁伊](Druid.md "Druid")、[自然领域](Nature_Domain.md "Nature Domain")（领域法术）和[大地结社](Circle_of_the_Land.md "Circle of the Land")（极地或山岳）
- 职业等级5：[游侠](Ranger.md "Ranger")
- 职业等级6：[逸闻学院](College_of_Lore.md "College of Lore")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）
- 职业等级10：[吟游诗人](Bard.md "Bard")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）

## 备注

- 此法术需要[专注](Concentration.md "Concentration")；施放其他[专注法术](Concentration.md#Concentration_Spells "Concentration")，如[猎人印记](Hunter's_Mark.md "Hunter's Mark")，将移除该地表。
- 此法术的伤害可被[陆地行者：植物](Land's_Stride_colon__Plants.md "Land's Stride: Plants")免疫。大地结社德鲁伊、荒蛮之心野蛮人和游侠在分别于6级和8级获得此隐藏特性后，能够完全不受阻碍地穿越荆棘丛生。
  - 其他形式的[劣势地形](Difficult_Terrain.md "Difficult Terrain")免疫，如[行动自如](Freedom_of_Movement.md "Freedom of Movement")，虽然允许完全移动，但在穿越此法术区域时无法防止伤害。

## 错误

- 此法术的4级版本错误地使用了3级法术位。

## 外部链接

- ⁠[荆棘丛生](https://forgottenrealms.fandom.com/wiki/Spike_growth) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Spike Growth](https://bg3.wiki/wiki/Spike_Growth)*