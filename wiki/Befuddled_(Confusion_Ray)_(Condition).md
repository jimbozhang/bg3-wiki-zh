# 昏沉 (困惑射线) (状态)

**昏沉**

- 受影响实体无法控制其动作，并且会漫无目的地四处游荡。

## 属性

[状态组](Status_groups.md "状态组")：[SG_震慑](SG_Stunned.md "SG Stunned")，[SG_状态](SG_Condition.md "SG Condition")

[持续时间结束](Conditions.md#Duration "状态")：回合结束

[更多属性](Status_properties.md "状态属性")：

- [战斗开始](Status_properties/InitiateCombat.md "状态属性/战斗开始")
- [回合头顶显示](Status_properties/OverheadOnTurn.md "状态属性/回合头顶显示")

## 错误

- 此状态使用 [安抚](Pacified_(Condition).md "安抚 (状态)") (`PACIFYING_SPORES`) 而非 [昏沉](Befuddled_(Condition).md "昏沉 (状态)") (`TIMMASK_SPORES`) 作为父级。因此，受影响角色会被震慑，而非表现得像被困惑一样。

## 昏沉来源

- [困惑射线](Confusion_Ray.md "困惑射线")

## 拥有昏沉状态的生物

*维基数据库中未定义*

---
*Source: [Befuddled (Confusion Ray) (Condition)](https://bg3.wiki/wiki/Befuddled_(Confusion_Ray)*