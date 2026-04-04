# 冻僵 (状态)

**冻僵**

- 受影响实体对 ⁠[寒冷](Cold.md "寒冷") 伤害 [易伤](Vulnerable.md "易伤")，并对 ⁠[火焰](Fire.md "火焰") 伤害 [抗性](Resistant.md "抗性")。
| 状态 | 效果 |
| --- | --- |
| 冻僵 | 受影响实体对 ⁠[寒冷](Cold.md "寒冷") 伤害 [易伤](Vulnerable.md "易伤")，并对 ⁠[火焰](Fire.md "火焰") 伤害 [抗性](Resistant.md "抗性")。对冻僵实体施加 [濡湿](Wet_(Condition).md "濡湿 (状态)") 将使其 [冰冻](Frozen_(Condition).md "冰冻 (状态)")，持续时间：1 驱散。 |

## 属性

[堆叠 ID](Stack_ID.md "堆叠 ID")：`CHILLED` [状态组](Status_groups.md "状态组")：[SG_Surface](SG_Surface.md "SG Surface")

[更多属性](Status_properties.md "状态属性")：

- [InitiateCombat](Status_properties/InitiateCombat.md "状态属性/InitiateCombat")
- [DisableCombatlog](Status_properties/DisableCombatlog.md "状态属性/DisableCombatlog")
- [DisableOverhead](Status_properties/DisableOverhead.md "状态属性/DisableOverhead")

## 状态：冰冻

**[冰冻](Frozen_(Condition).md "冰冻 (状态)")**

持续时间：1 驱散

- 受影响实体完全被冰包裹，且处于 . 如果受到钝击、雷鸣或力场伤害，冰会碎裂，结束该状态。
- 获得对 ⁠[钝击](Bludgeoning.md "钝击")、⁠[雷鸣](Thunder.md "雷鸣") 和 ⁠[力场](Force.md "力场") 伤害的 [易伤](Vulnerability.md "易伤")。
- 获得对 ⁠[火焰](Fire.md "火焰") 伤害的 [抗性](Resistance.md "抗性")。
- 免疫 [燃烧](Burning_(Condition).md "燃烧 (状态)") 和 [冷冻](Encrusted_with_Frost_(Condition).md "冷冻 (状态)")。

## 注释

- 状态施加的顺序很重要。对已经濡湿的目标施加冻僵不会使其冰冻。必须先冻僵再濡湿。然而，对已经濡湿且冻僵的目标施加濡湿会使其冰冻。
- [冰冻](Frozen_(Condition).md "冰冻 (状态)") 状态的持续时间在受影响生物的驱散开始时递减。由于持续时间仅为 1 驱散，这意味着效果将在冰冻生物的驱散开始时立即结束，甚至不会使其失效一个驱散。
- 当与 [冷冻](Encrusted_with_Frost_(Condition).md "冷冻 (状态)") 一起施加时，[冰冻](Frozen_(Condition).md "冰冻 (状态)") 将持续 2 驱散（因此实际上为 1 个完整轮次），因此不会出现此问题。

## 冻僵的来源

- [寒冰还击](Chilling_Counter.md "寒冰还击")
- [时代元素](Elements_of_an_Epoch.md "时代元素")
- [隐袭酷寒](Insidious_Cold.md "隐袭酷寒")
- [酷寒之拥](Cold_Embrace.md "酷寒之拥")
- [寒冰回流](Icy_Regurgitation.md "寒冰回流")
- [猛击 (水元素)](Slam_(Water_Elemental).md "猛击 (水元素)")
- [寒冬打击](Hiemal_Strike.md "寒冬打击")

## 拥有冻僵的生物

*维基数据库中未定义*

## 具有相同堆叠 ID 的状态

| 状态 | 效果 |
| --- | --- |
| 冻僵 | 受影响实体对 ⁠[寒冷](Cold.md "寒冷") 伤害 [易伤](Vulnerable.md "易伤")，并对 ⁠[火焰](Fire.md "火焰") 伤害 [抗性](Resistant.md "抗性")。对冻僵实体施加 [濡湿](Wet_(Condition).md "濡湿 (状态)") 将使其 [冰冻](Frozen_(Condition).md "冰冻 (状态)")，持续时间：1 驱散。 |

---
*Source: [Chilled (Condition)](https://bg3.wiki/wiki/Chilled_(Condition)*