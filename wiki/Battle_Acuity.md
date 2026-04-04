# 战法师的敏锐

**战法师的敏锐**是一个被动特性，当你造成武器伤害时，会增强你的施法能力。

## 描述

每当你通过武器攻击造成伤害时，你将获得 [奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")，持续 2 驱散。

## 状态：奥术敏锐

**[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")**

持续时间：2 驱散

- 受影响实体在剩余的每驱散中，其 [法术](Spells.md "法术") [攻击掷骰](Attack_roll.md "攻击掷骰") 和 [法术豁免 DC](Saving_throw.md#The_Difficulty_Class_of_saving_throws "豁免检定") 获得 +1 奖励。
- 每当实体受到伤害时，持续时间减少 2。
- **奥术敏锐**的最大持续时间：10 驱散。

## 如何习得

由以下装备提供：

- [战法师的骄傲](Helmet_of_Arcane_Acuity.md "战法师的骄傲")

## 错误

- **战法师的敏锐**缺少 `OncePerAttack` 标志。因此，对于那些被视为武器攻击并包含多个 `DealDamage` 函数的法术（例如 [轰鸣剑](Booming_Blade.md "轰鸣剑") 和各种 [至圣斩](Smite.md "至圣斩") 法术），它可能在一次攻击中多次触发。

---
*Source: [Battle Acuity](https://bg3.wiki/wiki/Battle_Acuity)*