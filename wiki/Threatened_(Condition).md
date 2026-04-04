# 受威胁 (状态)

**受威胁**

- 敌人靠近。对远程[攻击掷骰](Attack_roll.md "攻击掷骰")具有[劣势](Disadvantage.md "劣势")。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `FLANKED` [更多属性](Status_properties.md "状态属性"):

- [禁用头顶显示](Status_properties/DisableOverhead.md "状态属性/禁用头顶显示")
- [禁用战斗日志](Status_properties/DisableCombatlog.md "状态属性/禁用战斗日志")
- [忽略休息](Status_properties/IgnoreResting.md "状态属性/忽略休息")

## 备注

- 此状态适用于战斗中处于敌对生物近战范围内的任何生物。生物的近战范围可能受其近战武器的[额外范围](Extra_Reach.md "额外范围")影响。
- 此状态本身对攻击威胁者没有影响；劣势仅适用于对其他生物的远程攻击。如果多个敌人处于威胁范围内，则受威胁生物对所有敌人都将具有劣势。
- 然而，在距离目标3米（10英尺）内进行远程攻击时，还有一个单独的劣势来源（“目标太近”），这意味着大多数生物在对威胁生物进行远程攻击时都会具有劣势。
  - 这可以通过[强弩专家：近距平射](Crossbow_Expert_colon__Point-Blank.md "强弩专家：近距平射")移除，使得在近距离对敌人使用[弩](Crossbow.md "弩")攻击时不会产生劣势。但是，如果被多个生物威胁，则此效果无效。
  - 由于“目标太近”效果的实现方式，目标可能处于范围3米（10英尺）的光环内（例如\_(状态)[谋杀灵光](Aura_of_Murder_(Bhaalist_Armour)_(Condition).md "谋杀灵光 (巴尔信徒护甲) (状态)")），但距离不够近，不会对远程攻击施加劣势。这是因为该效果测量的是攻击者*中心*到目标的距离，而光环则考虑生物命中框的*体型*。

## 错误

- 当攻击非常大的目标时，例如[受控红龙](Dominated_Red_Dragon.md "受控红龙"), 其多个部分可能同时威胁攻击者，仿佛被多个敌人包围，导致所有远程攻击都具有劣势。这使得[强弩专家：近距平射](Crossbow_Expert_colon__Point-Blank.md "强弩专家：近距平射")对此类目标无效。

## 具有相同堆叠ID的状态

- 敌人靠近。对远程[攻击掷骰](Attack_roll.md "攻击掷骰")具有[劣势](Disadvantage.md "劣势")。

---
*Source: [Threatened (Condition)](https://bg3.wiki/wiki/Threatened_(Condition)*