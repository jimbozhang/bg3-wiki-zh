# 守卫刻文：雷鸣

**守卫刻文：雷鸣** 是一个 [3级防护学派法术](Spells.md "Spells")。此法术是3级防护学派法术 [守卫刻文](Glyph_of_Warding.md "Glyph_of_Warding") 的变体。它允许施法者铭刻一个守卫，当触发时会爆炸并对敌人造成雷鸣伤害。

## 描述

守卫刻文爆炸，对附近的敌人造成 [雷鸣](Thunder.md "Thunder") 伤害。通过 [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") 的生物仍会受到一半伤害。

守卫刻文将持续存在，直到被触发，或直到一次 [长休](Long_Rest.md "Long Rest")。

一次只能激活一个守卫刻文。

## 属性

消耗
[动作](Actions.md#Resources "Actions") + [3级法术位](Spells.md#Spell_slots "Spells")
伤害：5~40

5d8 [雷鸣](Thunder.md "Thunder")

详情
[敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throws.md "Saving throws")
范围：9米（30英尺）
区域效果：4米（13英尺）半径

## 升环施法

[升环施法](Upcasting.md "Upcasting")：以更高环位施放此法术时，每比3环高一环，额外造成1d8 [雷鸣](Thunder.md "Thunder") 伤害。

## 技术细节

UID

`Target_GlyphOfWarding_Thunder`

`Projectile_GlyphOfWarding_Thunder_Trap`

触发效果

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[IsTrap](IsTrap_(spell_flag).md)`

## 如何习得

此法术是以下法术的变体：
[守卫刻文](Glyph_of_Warding.md "Glyph_of_Warding")

## 备注

- 只有被视为敌人的单位才能触发守卫刻文。对于玩家队伍，这通过生物下方的红色圆圈、高亮时的红色轮廓以及小地图上的红点来指示。中立、友好和盟友生物（分别以黄色/绿色/蓝色高亮）可以安全穿过守卫刻文。
  - 这使得将守卫刻文用作陷阱在某些遭遇中可能存在问题，因为这些遭遇中的生物只有在对话后才被视为敌对。
- 当守卫刻文被触发时，区域内的所有生物都会受到影响，无论其阵营如何。
- 当施法者被敌人包围时，有时值得直接在敌人脚下投下守卫刻文。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Glyph_of_Warding_Visuals.mp4>

## 外部链接

- ⁠[守卫刻文](https://forgottenrealms.fandom.com/wiki/Glyph_of_warding) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Glyph of Warding: Thunder](https://bg3.wiki/wiki/Glyph_of_Warding:_Thunder)*