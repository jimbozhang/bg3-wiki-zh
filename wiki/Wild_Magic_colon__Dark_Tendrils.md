# 狂野魔法：暗影触须

**狂野魔法：暗影触须**是[狂野魔法野蛮人](Wild_Magic_Barbarian.md "狂野魔法野蛮人")的自由动作，当由[狂暴：狂野魔法](Rage_colon__Wild_Magic.md "狂暴：狂野魔法")掷骰触发时随机使用。每驱散，它会对附近所有生物造成[黯蚀](Necrotic.md "黯蚀")伤害并治疗野蛮人。

## 描述

暗影触须从你身上向外鞭打。你周围9米（30英尺）内的每个生物必须通过[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，否则受到1d12[黯蚀](Necrotic.md "黯蚀")伤害。此外，你获得1d12[临时生命值](Temporary_Hit_Points.md "临时生命值")。

只能拥有来自一个来源的临时生命值。

## 属性

详情
[体质](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）
范围：自身
范围效果：9米（30英尺）半径

## 技术细节

UID

`Shout_WildMagicBarbarian_ShadowyTendrils`

## 状态：狂野魔法：暗影触须

**[狂野魔法：暗影触须](Wild_Magic_colon__Dark_Tendrils_(Condition).md "狂野魔法：暗影触须（状态）")**

持续时间：10驱散

[体质](Constitution.md "体质") [豁免](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）

- 你周围9米（30英尺）内的每个生物必须通过[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，否则受到1d12[黯蚀](Necrotic.md "黯蚀")伤害。此外，你获得1d12[临时生命值](Temporary_Hit_Points.md "临时生命值")。
- DC基于你的[魅力](Charisma.md "魅力")调整值

## 如何习得

职业：

- 职业等级3：[狂野魔法野蛮人](Wild_Magic_Barbarian.md "狂野魔法野蛮人")

## 错误

- 尽管有工具提示警告，但授予临时生命值的状态未使用“TEMPORARY_HP”`StackId`，因此可能与其他临时生命值来源同时在角色上激活。在这种情况下，角色将从最高来源获得临时生命值，而任何较低来源将用于补充来自最高来源的任何丢失的临时生命值。

---
*Source: [Wild Magic: Dark Tendrils](https://bg3.wiki/wiki/Wild_Magic:_Dark_Tendrils)*