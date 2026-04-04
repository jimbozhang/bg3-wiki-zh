# 守卫刻文：寒冷

**守卫刻文：寒冷** 是一个 [等级 3 防护学派法术](Spells.md "Spells")。此法术是等级 3 防护学派法术 [守卫刻文](Glyph_of_Warding.md "守卫刻文") 的变体。它允许施法者铭刻一个守卫，当触发时会爆炸并对敌人造成寒冷伤害。

## 描述

刻文爆炸，对附近的敌人造成 [寒冷](Cold.md "寒冷") 伤害。通过 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 的生物仍会受到一半伤害。

刻文将持续存在，直到被触发或进行 [长休](Long_Rest.md "长休")。

一次只能激活一个刻文。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3 级法术位](Spells.md#Spell_slots "法术")
伤害：5~40

5d8 [寒冷](Cold.md "寒冷")

详情
[敏](Dexterity.md "敏捷") [豁免](Saving_throws.md "豁免检定")
范围：9 米（30 英尺）
区域：4 米（13 英尺）半径

## 升环施法

[升环施法](Upcasting.md "升环施法")：以更高法术位施放此法术时，每比 3 级高一环，额外造成 1d8 [寒冷](Cold.md "寒冷") 伤害。

## 技术细节

UID

`Target_GlyphOfWarding_Cold`

`Projectile_GlyphOfWarding_Cold_Trap`

触发效果

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[IsTrap](IsTrap_(spell_flag).md)`

## 学习方式

此法术是以下法术的变体：
[守卫刻文](Glyph_of_Warding.md "守卫刻文")

## 备注

- 只有被视为敌人的单位才能触发刻文。对于玩家队伍，这通过生物下方的红色圆圈、高亮时的红色轮廓以及小地图上的红点来表示。中立、友好和盟友生物（分别高亮为黄色/绿色/蓝色）可以安全穿过刻文。
  - 这使得在对话后才被视为敌对的遭遇中，将刻文用作陷阱可能存在问题。
- 当刻文触发时，区域内的所有生物都会受到影响，无论其阵营如何。
- 当施法者被敌人包围时，有时值得将刻文直接扔在他们脚下。

## 错误

- 如果在潮湿的地表上施放，避免此法术创造的 [冰](Ice_(surface).md "冰（地表）") 地表造成的 [倒伏](Prone_(Condition).md "倒伏（状态）") 的 DC 基于创造潮湿地表的实体，而非施法者。
  - 如果德鲁伊施放 [造水术](Create_Water.md "造水术")，法师施放守卫刻文：寒冷，避免冰面倒伏的 DC 将是：8 + 德鲁伊智力调整值 + 德鲁伊熟练项 + 德鲁伊装备加值，而非 8 + 法师智力调整值 + 法师熟练项 + 法师装备加值。
  - 此公式仅在水首先与敌人接触时有效（例如，在 NPC 头顶施放造水术），如果施放/投掷到地面然后被此法术冻结，倒伏 DC 将默认为 12。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Glyph_of_Warding_Visuals.mp4>

## 外部链接

- [守卫刻文](https://forgottenrealms.fandom.com/wiki/Glyph_of_warding) 在 [被遗忘的国度 Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Glyph of Warding: Cold](https://bg3.wiki/wiki/Glyph_of_Warding:_Cold)*