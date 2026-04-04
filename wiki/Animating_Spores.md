# 活化孢子

本文介绍的是格鲁特（Glut）使用的动作。关于孢子结社德鲁伊习得的类似动作，请参阅 [真菌感染](Fungal_Infestation.md "真菌感染")。

**活化孢子**是 [格鲁特](Glut.md "Glut") 和 [斯波](Spaw.md "Spaw") 可用的特殊职业动作，允许他们复活一具尸体并使其并肩作战。复活的生物保留其所有动作，但无法使用施法。

## 描述

向尸体释放孢子，将其活化为受你指挥的孢子仆从。

一次仅影响一个目标。
对构装生物、植物或异怪的尸体无效。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
射程：3米（10英尺）
目标：[怪兽](Monstrosity.md "怪兽")、[类人生物](Humanoid.md "Humanoid") 或 [野兽](Beast.md "Beast") 的尸体
充能：每回合

## 技术细节

UID

`Target_AnimatingSpores`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`

## 状态：孢子仆从

**[孢子仆从](Spore_Servant_(Condition).md "孢子仆从 (状态)")**

持续时间：直至 [长休](Long_Rest.md "长休")

- 蕈人王的活化孢子已接管这具已故生物的躯体，根据王的意志移动它。
- 复活的生物被归类为 [植物](Plant.md "植物")。
- 免疫所有 [恐慌](Frightened_(status_group).md) 状态、[目盲](Blinded_(status_group).md) 状态、[昏沉](Befuddled_(Condition).md "昏沉 (状态)")、[魅惑](Charmed_(Condition).md "魅惑 (状态)")、[疯狂](Crown_of_Madness_(Condition).md "疯狂 (状态)")、[交友术](Friends_(Condition).md "交友术 (状态)")、[狂笑](Hideous_Laughter_(Condition).md "狂笑 (状态)")、[人类定身术](Hold_Person_(Condition).md "人类定身术 (状态)")、[心智奴役](Mind_Mastery_(Condition).md "心智奴役 (状态)")、\_(状态)[有毒烟雾](Noxious_Fumes_(Bibberbang)_(Condition).md "有毒烟雾 (噼啪砰) (状态)")、[麻痹](Paralysed_(Condition).md "麻痹 (状态)")，以及 [沉睡](Sleeping_(Condition).md "沉睡 (状态)")。
- 生物对 ⁠[中毒](Poison.md "中毒") 伤害具有抗性。
- 生物无法施法或使用荒野形态。

## 如何习得

由生物使用：[格鲁特](Glut.md "Glut") 和 [斯波](Spaw.md "Spaw")

## 备注

- 目标生物以 65% 的生命值复活。
- 此动作一次只能复活一个生物。复活新生物会杀死已存在的生物。
- 一具尸体只能用此动作复活一次。
- 虽然 [格鲁特](Glut.md "Glut") 是临时伙伴，但此动作允许玩家角色通过复活一些强大的怪物来直接控制它们。最显著的例子是 [鲨蜥兽](Bulette.md "Bulette")，其他例子包括 [牛头人](Minotaur.md "Minotaur") 和 [恐爪怪](Hook_Horror.md "恐爪怪")。
  - 此外，可以将幽暗地域以外的尸体带给格鲁特进行复活。一个显著的例子是 [德罗尔·拉格兹林](Dror_Ragzlin.md "德罗尔·拉格兹林")，他甚至在 [荣誉](Honour.md "荣誉") 模式下保留其传奇动作。为此，尸体必须足够轻以便拾取，因此较重的怪物如 [枭熊](Owlbear.md "枭熊") 或 [相位蜘蛛女王](Phase_Spider_Matriarch.md "相位蜘蛛女王") 将不起作用。
  - 描述中未说明，但此动作不能用于 [邪魔](Fiend.md "邪魔")，（不包括 [弗林德](Flind.md "弗林德")，他也受仅对 [类人生物](Humanoids.md "类人生物") 生效的法术影响，例如 [人类定身术](Hold_Person.md "人类定身术")）。

---
*Source: [Animating Spores](https://bg3.wiki/wiki/Animating_Spores)*