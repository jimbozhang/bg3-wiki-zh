# 谨慎的医师

**谨慎的医师**是一项被动特性，允许使用者在治疗后自动脱离敌人。

## 描述

当穿戴者治疗一个生物时，它会自动[撤离](Disengage.md "撤离")，并且不会触发[借机攻击](Opportunity_Attack.md "借机攻击")。

## 状态：撤离

**[撤离](Disengage_(Condition).md "撤离 (状态)")**

持续时间：1 驱散

- 可以移动而不引发[借机攻击](Attack_of_Opportunity.md "借机攻击")。

## 如何习得

由以下装备提供：

- [光滑的链甲衫](Slippery_Chain_Shirt.md "光滑的链甲衫")

## 备注

- 穿戴者是在治疗他人（包括自己）后[撤离](Disengage.md "撤离")的一方。
- 尽管给予穿戴者[撤离状态](Disengage_(Condition).md "撤离 (状态)")，但它不会在[诡诈之雾披风](Cloak_of_Cunning_Brume.md "诡诈之雾披风")上触发[诡诈之雾](Cunning_Brume.md "诡诈之雾")，因为其被动是在使用能力时（`OnCast`）触发的，而不是在状态应用时（`OnStatusApplied`）触发的。

---
*Source: [Cautious Healer](https://bg3.wiki/wiki/Cautious_Healer)*