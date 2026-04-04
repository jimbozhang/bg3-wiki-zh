# 毒过砒霜

**毒过砒霜** 是一个 [法术](Spells.md "法术")。它是 [克雷斯卡的恩惠](Kereska's_Favour.md "Kereska's Favour") 的一个变体，允许施法者将自己灌注中毒之力，并解锁与之相关的抗性和法术。它由 [玛科赫什基](Markoheshkir.md "Markoheshkir") 提供。

## 描述

拥抱克雷斯卡的毒力，获得对 ⁠[中毒](Poison.md "Poison") 伤害的 [抗性](Resistance.md "Resistance")。你的中毒法术造成额外的 ⁠[中毒](Poison.md "Poison") 伤害，伤害值等于你的 [熟练项加值](Proficiency_Bonus.md "Proficiency bonus")。

当你造成法术伤害时，对目标施加 2 驱散 _\[[参见注释](#notes)\]_ 的 [中毒](Poisoned_(Condition).md "中毒（状态）") 状态。当你与克雷斯卡的毒力共鸣时，你可以在每个 [短休](Short_rest.md "短休") 中施放一次 [死云术](Cloudkill.md "Cloudkill") 和一次 [疾病射线](Ray_of_Sickness.md "Ray of Sickness")。

[死云术](Cloudkill.md "Cloudkill") ()
以 5 环法术施放（充能：[短休](Short_rest.md "短休")。）

[疾病射线](Ray_of_Sickness.md "Ray_of_Sickness") ()
以 5 环法术施放（充能：[短休](Short_rest.md "短休")。）

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
距离：自身
充能：[短休](Short_rest.md "短休")

## 升环施法

以更高环位施放此法术不会获得额外收益。

## 技术细节

UID

`Shout_MAG_TheChromatic_PoisonAttunement`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：克雷斯卡毒力的容器

**[克雷斯卡毒力的容器](Vessel_for_Kereska's_Poison_(Condition).md "克雷斯卡毒力的容器（状态）")**

持续时间：直至 [长休](Long_Rest.md "长休")

- 受影响实体对 ⁠[中毒](Poison.md "Poison") 伤害具有 [抗性](Resistance.md "Resistance")。
- 其中毒法术造成的伤害等于其 [熟练项加值](Proficiency_Bonus.md "Proficiency bonus")。
- 当其造成法术伤害时，对目标施加 2 驱散的 [中毒](Poisoned_(Condition).md "中毒（状态）") 状态。
- 当与克雷斯卡的毒力共鸣时，它可以在每个短休中以 5 环施放一次 [死云术](Cloudkill.md "Cloudkill") 和一次 [疾病射线](Ray_of_Sickness.md "Ray of Sickness")。

## 如何习得

由物品提供：

- [玛科赫什基](Markoheshkir.md "Markoheshkir")

此法术是以下法术的变体：
[克雷斯卡的恩惠](Kereska's_Favour.md "Kereska's Favour")

## 注释

- 游戏内工具提示说此效果施加 1 驱散的中毒，但实际上它施加 2 驱散。
- 应用中毒状态每攻击只能发生一次。像 [死云术](Cloudkill.md "Cloudkill") 这样击中多个目标的法术只会对单个目标施加状态。
- 此法术提供的 [疾病射线](Ray_of_Sickness.md "Ray_of Sickness") 版本与 5 环升环施法版本的伤害相匹配（6d8⁠⁠[中毒](Poison.md "Poison")），但它只计为 1 环法术。

---
*Source: [Deadlier than Arsenic](https://bg3.wiki/wiki/Deadlier_than_Arsenic)*