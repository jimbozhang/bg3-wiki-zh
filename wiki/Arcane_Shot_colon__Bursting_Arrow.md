# 奥术射击：爆裂箭

**奥术射击：爆裂箭**是[奥术射手](Arcane_Archer.md "奥术射手")可用的一种特殊奥术箭攻击，除了正常武器伤害外，还会在目标周围小范围内造成2d6⁠⁠[力场](Force.md "力场")伤害。

## 描述

使用塑能学派魔法使你的箭在命中时爆炸，对5米（17英尺）范围内的目标造成额外的2d6⁠⁠[力场](Force.md "力场")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")
伤害：2~12

正常武器伤害

\+ 2d6⁠[力场](Force.md "力场")

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")（未命中时：箭不会爆炸，奥术箭消耗将被返还）
射程：正常武器射程
范围效果：5米（17英尺）半径

## 技术细节

UID

`Projectile_ArcaneShot_BurstingArrow`

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsAttack](IsAttack_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 学习方式

职业：

- 职业等级 3：[奥术射手](Arcane_Archer.md "奥术射手")

## 备注

- 没有豁免检定来减少或避免爆炸伤害，因此此奥术箭选项不会受益于[智力](Intelligence.md "智力")。

## 错误

- 与大多数其他奥术射击选项不同，此动作会立即消耗[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")，而不是在命中时消耗。相反，此资源消耗会在未命中时返还，这几乎是等效的行为。这导致与[曲线射击](Curving_Shot.md "曲线射击")产生一些不寻常的行为。如果爆裂箭未命中初始目标，[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")消耗将被返还，然后攻击将被重定向到新目标。如果此目标被命中，爆裂箭将有效免费施放。如果重定向的命中也未命中，它将返还另一个奥术箭，总计获得+1[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")。

---
*Source: [Arcane Shot: Bursting Arrow](https://bg3.wiki/wiki/Arcane_Shot:_Bursting_Arrow)*