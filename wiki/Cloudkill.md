# 死云术

**死云术** 是一个 [法术](Spells.md "法术")。它召唤一团可移动的云，对笼罩其中的一切造成伤害并使其隐蔽。

## 描述

制造一团巨大的云，每回合对其中目标造成 5d8⁠⁠[中毒](Poison.md "Poison") 伤害。你可以每回合重新定位这团云。

这团云会**重度隐蔽**其中的一切。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [5环法术位](Spells.md#Spell_slots "Spells")
伤害：5~40

5d8⁠[中毒](Poison.md "Poison")（需通过 [体质](Constitution.md "Constitution") [豁免检定](Saving_throw.md "Saving Throw") 以减半伤害）

详情
射程：18 米（60 英尺）
创造区域：死云术
[专注](Concentration.md "Concentration")

## 升环施法

[升环施法](Upcasting.md "Upcasting")：以更高环位施放此法术时，每比5环高1环，额外造成 1d8⁠⁠[中毒](Poison.md "Poison") 伤害。

## 技术细节

UID

`Target_Cloudkill`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 区域：死云术

**[死云术](Cloudkill_(cloud).md "死云术 (云)")**

持续时间：10 驱散

范围效果：6 米（20 英尺）半径

停留在云中的生物会受到重度中毒伤害。这团云也会重度隐蔽其中的内容。

类型：[云](Area.md#Cloud "区域")

### 状态：死云术

**[死云术](Cloudkill_(Condition).md "死云术 (状态)")**

- 当受影响实体停留在云中时，每回合受到 5d8⁠⁠[中毒](Poison.md "Poison") 伤害。

## 如何习得

职业：

- 职业等级 9：[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[孢子结社](Circle_of_the_Spores.md "孢子结社")（结社法术）、[大地结社](Circle_of_the_Land.md "大地结社")（沼泽和幽暗地域），以及[死亡领域](Death_Domain.md "死亡领域")（领域法术）

由物品授予：

- [玛科赫什基](Markoheshkir.md "玛科赫什基")（充能：[短休](Short_rest.md "短休")）

其他习得方式：

- 拥有 [5环法术位](Spells.md#Spell_slots "Spells") 的 [法师](Wizard.md "法师") 可以将 [死云术卷轴](Scroll_of_Cloudkill.md "死云术卷轴") [抄录](Transcribing_scrolls.md "抄录卷轴") 到他们的法术书中。

## 备注

- 处于 [英雄盛宴](Heroes'_Feast.md "英雄盛宴") 效果下的角色对此法术的伤害免疫。
- [死云术](Cloudkill_(Condition).md "死云术 (状态)") 被视为一种“授予”状态，类似于“授予”法术。*授予*法术在使用原始法术后发放给施法者，并且只要[专注](Concentration.md "专注")未被打破，就可以[重施](Category_colon_Recastable_spells.md "类别：可重施法术")而无需消耗另一个法术位。此（10驱散）状态与施法者的已知法术列表（即游戏中的法术书图标）没有直接关联。因此，如果在身兼多职时使用了授予法术（或在此情况下是授予状态），后续的再次使用（在此情况下是[死云术](Cloudkill_(Condition).md "死云术 (状态)")) 将使用最近获得的施法职业的施法调整值，而不是最初施放死云术时使用的施法调整值。就本状态而言，这可能导致法术豁免DC意外地偏低。
- 当重施时，死云术的射程仅为 9 米（30 英尺）。

## 错误

- 如果升环至6环，死云术会创造一团隐形的云，因为地表缺少附着的粒子效果。
  - NPC不会自动离开这团云，因为其地表ID未包含在角色的`PathInfluence`中。
- 这团云从最后一次重施开始持续10驱散，而不是从初始施法开始。这通常会导致施法者不再有能力重施死云术，但专注效果和云团却持续的时间比预期更长。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Clouldkill_Visuals.mp4>

## 外部链接

- ⁠[死云术](https://forgottenrealms.fandom.com/wiki/Cloudkill) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Cloudkill](https://bg3.wiki/wiki/Cloudkill)*