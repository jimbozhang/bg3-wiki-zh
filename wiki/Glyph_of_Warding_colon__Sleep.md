# 守卫刻文：沉睡

**守卫刻文：沉睡** 是一个 [法术](Spells.md "法术")。此法术是3级防护学派法术 [守卫刻文](Glyph_of_Warding.md "守卫刻文") 的一个变体。它允许施法者铭刻一个守卫，当被触发时，可使敌人进入 [沉睡](Sleeping_(Condition).md "沉睡（状态）") 状态。

## 描述

当敌人踩中时，刻文会散发出舒缓的魔法，使范围内的所有人进入 [沉睡](Sleeping_(Condition).md "沉睡（状态）") 状态。任何处于效果区域内（且不免疫魔法沉睡）的生物，若 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 失败，将被陷入沉睡。

刻文将持续存在，直到被触发，或直到一次 [长休](Long_Rest.md "长休")。

同一时间只能激活一个刻文。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术位")
详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")
范围：9米（30英尺）
效果区域：4米（13英尺）半径

## 高等级施法

以更高等级施放此法术不会获得额外收益。

## 技术细节

UID

`Target_GlyphOfWarding_Sleep`

`Projectile_GlyphOfWarding_Sleep_Trap`

触发效果

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell flag\) \(page does not exist\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[IsTrap](IsTrap_(spell_flag).md)`

## 状态：沉睡

**[沉睡](Sleeping_(Condition).md "沉睡（状态）")**

持续时间：2回合

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 沉睡的生物无法移动或行动。
- 此外，该生物自动在 [力量](Strength.md "力量") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 上失败。
- 对其进行的 [攻击掷骰](Attack_roll.md "攻击掷骰") 具有 [优势](Advantage.md "优势")，且如果攻击者在该生物1.5米（5英尺）范围内，任何命中该生物的攻击均为 [重击](Critical_Hit.md "重击")。
- 通过承受伤害、变为 [濡湿](Wet_(Condition).md "濡湿（状态）")、接受 [协助](Help.md "协助") 或被 [推击](Shove.md "推击") 可移除此状态。

## 如何学习

此法术是以下法术的变体：
[守卫刻文](Glyph_of_Warding.md "守卫刻文")

## 注释

- 只有被视为敌人的单位才能触发刻文。对于玩家队伍而言，这通过生物下方的红色圆圈、高亮时的红色轮廓以及小地图上的红点来指示。中立、友好和盟友生物（分别以黄色/绿色/蓝色高亮）可以安全穿过刻文。
  - 这使得在对话后才被视为敌对的遭遇中，将刻文用作陷阱可能存在问题。
- 当刻文被触发时，范围内的每个生物都会受到影响，无论其阵营如何。
- 当施法者被敌人包围时，有时值得将刻文直接扔在他们脚下。这对于大多数范围效果法术都是如此，但对于沉睡变体尤其如此：
  - 共享先攻系统意味着，如果盟友因自己的刻文而陷入沉睡，其他盟友可以立即推击/协助将其唤醒。
  - 魔法沉睡免疫相当常见，无论是来自 [卓越专注灵药](Elixir_of_Peerless_Focus.md "卓越专注灵药") 还是来自 [妖精血统](Fey_Ancestry.md "妖精血统")。
    - 作为 [半精灵](Half-Elf.md "半精灵") [牧师](Cleric.md "牧师")，[影心](Shadowheart.md "影心") 从5级开始就可以自然地运用此战术。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Glyph_of_Warding_Visuals.mp4>

## 外部链接

- ⁠[守卫刻文](https://forgottenrealms.fandom.com/wiki/Glyph_of_warding) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Glyph of Warding: Sleep](https://bg3.wiki/wiki/Glyph_of_Warding:_Sleep)*