# 状态

**状态**是角色状态的变化，包括有益和有害的。它们可以由某些[法术](Spells.md "法术")、职业特性、地表和其他环境危害等施加。许多状态是暂时的，有些也可以通过正确的法术或药水移除。

## 目录

- [1 堆叠ID](#stack-id)
- [2 堆叠类型](#stack-type)
- [3 持续时间](#duration)
  - [3.1 节拍类型](#tick-type)
- [4 状态属性](#status-properties)
- [5 状态类型](#condition-types)
- [6 状态列表](#list-of-conditions)

## 堆叠ID

所有状态都有一个在游戏中不可见的堆叠ID。具有相同堆叠ID的两个状态不能同时应用。例如，不可能同时拥有[加速](Hastened_(Condition).md "加速（状态）")、[天界加速](Celestial_Haste_(Condition).md "天界加速（状态）")和[加速孢子](Haste_Spores_(Condition).md "加速孢子（状态）")，因为它们都具有堆叠ID `HASTE`。当再次应用相同状态或应用具有相同堆叠ID的状态时会发生什么，由要应用的状态的[堆叠类型](Stack_type.md "堆叠类型")和[堆叠优先级](Stack_priority.md "堆叠优先级")的组合决定。

## 堆叠类型

堆叠类型决定了当应用一个状态时，如果相同状态或具有相同堆叠ID的状态已经存在，会发生什么。这告诉您如果尝试应用多个具有相同堆叠ID的状态，最终会得到哪个状态，并告诉您哪些状态可以叠加在一起以增加持续时间。

有四种不同的堆叠类型：

堆叠
新状态被单独应用，允许同一状态的多个实例。
忽略
不应用新状态，现有状态保持原样，保留其当前持续时间。通常用于状态的装备变体，例如，如果您拥有[树肤术](Barkskin_(Condition).md) 直到长休，并装备了[树肤护甲](Barkskin_Armour.md "树肤护甲")，来自护甲的状态将不会替换您直到长休的状态。
覆盖
现有状态被新状态替换。例如，如果您通过饮用[加速药水](Potion_of_Speed.md "加速药水")获得[加速](Hastened_(Condition).md)，并饮用另一瓶，您将替换当前的状态，立即使您[力竭](Lethargic_(Condition).md "力竭（状态）")。
叠加
新状态的持续时间添加到已存在状态的持续时间上。例如，如果一个生物剩余1回合的[光耀法球](Radiating_Orb_(Condition).md)，并再次获得2回合，它将剩余3回合。

## 持续时间

状态的持续时间由施加状态的来源决定。有些状态没有持续时间。这可能是基于其他条件激活的状态，例如被动特性或站在某物附近。状态[轻度遮蔽](Lightly_Obscured_(Condition).md "轻度遮蔽（状态）")是一个没有持续时间的状态，相反，如果您在光线不足的地方[隐藏](Hiding_(Condition).md "隐藏（状态）")，它会自动应用，并且当不再隐藏时自动移除。还有一些状态不会随时间失去持续时间。这可能是由于其他原因失去持续时间的状态，例如[奥术守御](Arcane_Ward_(Condition).md "奥术守御（状态）")，当您被击中时失去持续时间。如果您处于对话或过场动画中，状态也不会失去持续时间。但是，这仅适用于参与对话/过场动画的角色，而不仅仅是旁听的角色。

### 节拍类型

节拍类型决定了状态何时减少其剩余持续时间并应用其效果。大多数情况下，是在受影响生物回合的开始或结束时。当您处于[回合制模式](Turn-based_mode.md "回合制模式")或战斗模式之外时，一回合是6秒。节拍类型在游戏中不显示，但对于短持续时间效果可能特别重要。

另请参阅：[状态属性/TickingWithSource](Status_properties/TickingWithSource.md "状态属性/TickingWithSource")

不同的节拍类型有：

开始回合
状态在生物回合开始时失去持续时间，这是默认行为。具有此节拍类型的状态将持续时间比其声明的持续时间少一回合。例如，1回合持续时间的[冰冻](Frozen_(Condition).md "冰冻（状态）")效果（来自[冻僵](Chilled_(Condition).md "冻僵（状态）")）将在冰冻生物回合开始时立即结束，而不会使其失效一回合。2回合的[冰冻](Frozen_(Condition).md "冰冻（状态）")效果（来自[冷冻](Encrusted_with_Frost_(Condition).md "冷冻（状态）")）由于相同原因实际上只持续1回合。
结束回合
状态在生物回合结束时失去持续时间。[剑刃防护](Blade_Ward_(Condition).md "剑刃防护（状态）")就是这样一个例子。如果一个生物对自己施加一个持续1回合的状态，它将在结束回合时立即失去该状态，例如使用[动作如潮](Action_Surge.md "动作如潮")。
开始轮次
状态在_轮次_开始时失去持续时间。轮次开始发生在先攻顺序中的第一个生物开始其回合之前。
结束轮次
状态在_轮次_结束时失去持续时间。轮次结束发生在先攻顺序中的最后一个生物结束其回合之后。

## 状态属性

有些状态具有特殊属性，使它们以不同方式表现，例如发起战斗或不随时间失去持续时间。

以下是所有状态属性的列表：

[表演](Status_properties/Performing.md "状态属性/表演")
|
[发起战斗](Status_properties/InitiateCombat.md "状态属性/发起战斗")
|
| 名称 | 描述 |
| --- | --- |
| [无](Status_properties/None.md "状态属性/无") |  |
| [表演](Status_properties/Performing.md "状态属性/表演") |  |
| [发起战斗](Status_properties/InitiateCombat.md "状态属性/发起战斗") |  |
| [带入战斗](Status_properties/BringIntoCombat.md "状态属性/带入战斗") | 当应用带有此标签的状态时：队伍被迫进入战斗。 |
| [强制头顶显示](Status_properties/ForceOverhead.md "状态属性/强制头顶显示") | 应用和移除状态时，将在生物模型上方显示该状态。 |
| [引导中](Status_properties/IsChanneled.md "状态属性/引导中") |  |
| [无敌](Status_properties/IsInvulnerable.md "状态属性/无敌") | 应用此状态的生物无法承受伤害。 |
| [排除肖像渲染](Status_properties/ExcludeFromPortraitRendering.md "状态属性/排除肖像渲染") |  |
| [失去控制](Status_properties/LoseControl.md "状态属性/失去控制") | 禁止玩家控制角色，跳过这些角色的用户界面 |
| [强制中立交互](Status_properties/ForceNeutralInteractions.md "状态属性/强制中立交互") |  |
| [仅和平模式](Status_properties/PeaceOnly.md "状态属性/仅和平模式") | 只能在战斗外使用。 |
| [允许离开战斗](Status_properties/AllowLeaveCombat.md "状态属性/允许离开战斗") | 无强制回合制战斗：意味着敌人仍然敌对但不会主动攻击队伍 |
| [禁用免疫头顶显示](Status_properties/DisableImmunityOverhead.md "状态属性/禁用免疫头顶显示") |  |
| [禁用交互](Status_properties/DisableInteractions.md "状态属性/禁用交互") |  |
| [切换](Status_properties/Toggle.md "状态属性/切换") |  |
| [忽略休息](Status_properties/IgnoreResting.md "状态属性/忽略休息") | 此状态在[长休](Long_Rest.md "长休")后不会被移除。 |
| [被定身忽略](Status_properties/IgnoredByImmobilized.md "状态属性/被定身忽略") |  |
| [目盲](Status_properties/Blind.md "状态属性/目盲") |  |
| [效果乘以持续时间](Status_properties/MultiplyEffectsByDuration.md "状态属性/效果乘以持续时间") | 此状态的效果乘以剩余回合数。 |
| [随来源节拍](Status_properties/TickingWithSource.md "状态属性/随来源节拍") | 持续时间在状态来源的回合减少。 |
| [禁用头顶显示](Status_properties/DisableOverhead.md "状态属性/禁用头顶显示") | 应用和移除状态时，不在生物模型上方显示该状态。 |
| [禁用战斗日志](Status_properties/DisableCombatlog.md "状态属性/禁用战斗日志") | 应用或移除状态时，不在战斗日志中显示该状态。 |
| [禁用肖像指示器](Status_properties/DisablePortraitIndicator.md "状态属性/禁用肖像指示器") | 此状态被隐藏，不在生物上显示。 |
| [在所有者上执行函数](Status_properties/ExecuteFunctorsOnOwner.md "状态属性/在所有者上执行函数") |  |
| [无敌可见](Status_properties/IsInvulnerableVisible.md "状态属性/无敌可见") |  |
| [应用于死亡](Status_properties/ApplyToDead.md "状态属性/应用于死亡") | 此状态在对象/生物死亡后及复生后仍然存在。 |
| [给予经验](Status_properties/GiveExp.md "状态属性/给予经验") | 用于在解决（潜在）战斗情况时给予队伍经验点的标志 |
| [燃烧](Status_properties/Burning.md "状态属性/燃烧") |  |
| [不可延长](Status_properties/NonExtendable.md "状态属性/不可延长") |  |
| [冻结持续时间](Status_properties/FreezeDuration.md "状态属性/冻结持续时间") | 此状态不会随时间失去持续时间。 |
| [在主动检定中不可用](Status_properties/UnavailableInActiveRoll.md "状态属性/在主动检定中不可用") |  |
| [回合开始头顶显示](Status_properties/OverheadOnTurn.md "状态属性/回合开始头顶显示") | 将在生物回合开始时在其模型上方显示该状态。 |
| [取出乐器](Status_properties/UnsheathInstrument.md "状态属性/取出乐器") |  |
| [指示黑暗](Status_properties/IndicateDarkness.md "状态属性/指示黑暗") |  |
| [友方失去控制](Status_properties/LoseControlFriendly.md "状态属性/友方失去控制") |  |
| [禁用能力消息](Status_properties/DisableCapabilitiesMessage.md "状态属性/禁用能力消息") |  |
| [允许离开禁止加入战斗](Status_properties/AllowLeaveDisallowJoinCombat.md "状态属性/允许离开禁止加入战斗") |  |
[指示黑暗](Status_properties/IndicateDarkness.md "状态属性/指示黑暗")
|
[友方失去控制](Status_properties/LoseControlFriendly.md "状态属性/友方失去控制")
|
[禁用能力消息](Status_properties/DisableCapabilitiesMessage.md "状态属性/禁用能力消息")
|
[允许离开禁止加入战斗](Status_properties/AllowLeaveDisallowJoinCombat.md "状态属性/允许离开禁止加入战斗")
|

## 状态类型

有些状态具有“类型”，表明如何移除、预防该状态，或它如何对其他动作做出反应。

以下是移除或预防某些状态的一些方法。有关每种状态类型的完整治疗和预防列表，请参阅其文章。

[治疗](Heal.md "治疗")
[恢复](Lesser_Restoration.md "恢复")
[康复药水](Remedial_Potion.md "康复药水")
[(更多)](Blinded_(Condition_Type).md#Removal).md#Removal> "目盲（状态类型）")
|

[莎尔的黄昏短矛](Shar's_Spear_of_Evening.md "莎尔的黄昏短矛")
[钢铁卫士头盔](Steelwatcher_Helmet.md "钢铁卫士头盔")
[(更多)](Blinded_(Condition_Type).md#Immunity).md#Immunity> "目盲（状态类型）")
| [魅惑](Charmed_(status_group).md) | [魅惑](Charmed_(Condition).md "魅惑（状态）") |

[反制善恶：解除惑控](Dispel_Evil_And_Good_colon__Break_Enchantment.md "反制善恶：解除惑控")
[心如止水](Stillness_of_Mind.md "心如止水")
[(更多)](Charmed_(Condition_Type).md#Removal).md#Removal> "魅惑（状态类型）")
|

[诱导防御](Beguiling_Defences.md "诱导防御")
[安定心神](Calm_Emotions.md "安定心神")
[妖精血统](Fey_Ancestry.md "妖精血统") <sup>[\[2\]](#cite_note-adv-2)</sup>
[(更多)](Charmed_(Condition_Type).md#Immunity).md#Immunity> "魅惑（状态类型）")
| 名称 | 描述 |
| --- | --- |
| [无](Status_properties/None.md "状态属性/无") |  |
| [表演](Status_properties/Performing.md "状态属性/表演") |  |
| [发起战斗](Status_properties/InitiateCombat.md "状态属性/发起战斗") |  |
| [带入战斗](Status_properties/BringIntoCombat.md "状态属性/带入战斗") | 当应用带有此标签的状态时：队伍被迫进入战斗。 |
| [强制头顶显示](Status_properties/ForceOverhead.md "状态属性/强制头顶显示") | 应用和移除状态时，将在生物模型上方显示该状态。 |
| [引导中](Status_properties/IsChanneled.md "状态属性/引导中") |  |
| [无敌](Status_properties/IsInvulnerable.md "状态属性/无敌") | 应用此状态的生物无法承受伤害。 |
| [排除肖像渲染](Status_properties/ExcludeFromPortraitRendering.md "状态属性/排除肖像渲染") |  |
| [失去控制](Status_properties/LoseControl.md "状态属性/失去控制") | 禁止玩家控制角色，跳过这些角色的用户界面 |
| [强制中立交互](Status_properties/ForceNeutralInteractions.md "状态属性/强制中立交互") |  |
| [仅和平模式](Status_properties/PeaceOnly.md "状态属性/仅和平模式") | 只能在战斗外使用。 |
| [允许离开战斗](Status_properties/AllowLeaveCombat.md "状态属性/允许离开战斗") | 无强制回合制战斗：意味着敌人仍然敌对但不会主动攻击队伍 |
| [禁用免疫头顶显示](Status_properties/DisableImmunityOverhead.md "状态属性/禁用免疫头顶显示") |  |
| [禁用交互](Status_properties/DisableInteractions.md "状态属性/禁用交互") |  |
| [切换](Status_properties/Toggle.md "状态属性/切换") |  |
| [忽略休息](Status_properties/IgnoreResting.md "状态属性/忽略休息") | 此状态在[长休](Long_Rest.md "长休")后不会被移除。 |
| [被定身忽略](Status_properties/IgnoredByImmobilized.md "状态属性/被定身忽略") |  |
| [目盲](Status_properties/Blind.md "状态属性/目盲") |  |
| [效果乘以持续时间](Status_properties/MultiplyEffectsByDuration.md "状态属性/效果乘以持续时间") | 此状态的效果乘以剩余回合数。 |
| [随来源节拍](Status_properties/TickingWithSource.md "状态属性/随来源节拍") | 持续时间在状态来源的回合减少。 |
| [禁用头顶显示](Status_properties/DisableOverhead.md "状态属性/禁用头顶显示") | 应用和移除状态时，不在生物模型上方显示该状态。 |
| [禁用战斗日志](Status_properties/DisableCombatlog.md "状态属性/禁用战斗日志") | 应用或移除状态时，不在战斗日志中显示该状态。 |
| [禁用肖像指示器](Status_properties/DisablePortraitIndicator.md "状态属性/禁用肖像指示器") | 此状态被隐藏，不在生物上显示。 |
| [在所有者上执行函数](Status_properties/ExecuteFunctorsOnOwner.md "状态属性/在所有者上执行函数") |  |
| [无敌可见](Status_properties/IsInvulnerableVisible.md "状态属性/无敌可见") |  |
| [应用于死亡](Status_properties/ApplyToDead.md "状态属性/应用于死亡") | 此状态在对象/生物死亡后及复生后仍然存在。 |
| [给予经验](Status_properties/GiveExp.md "状态属性/给予经验") | 用于在解决（潜在）战斗情况时给予队伍经验点的标志 |
| [燃烧](Status_properties/Burning.md "状态属性/燃烧") |  |
| [不可延长](Status_properties/NonExtendable.md "状态属性/不可延长") |  |
| [冻结持续时间](Status_properties/FreezeDuration.md "状态属性/冻结持续时间") | 此状态不会随时间失去持续时间。 |
| [在主动检定中不可用](Status_properties/UnavailableInActiveRoll.md "状态属性/在主动检定中不可用") |  |
| [回合开始头顶显示](Status_properties/OverheadOnTurn.md "状态属性/回合开始头顶显示") | 将在生物回合开始时在其模型上方显示该状态。 |
| [取出乐器](Status_properties/UnsheathInstrument.md "状态属性/取出乐器") |  |
| [指示黑暗](Status_properties/IndicateDarkness.md "状态属性/指示黑暗") |  |
| [友方失去控制](Status_properties/LoseControlFriendly.md "状态属性/友方失去控制") |  |
| [禁用能力消息](Status_properties/DisableCapabilitiesMessage.md "状态属性/禁用能力消息") |  |
| [允许离开禁止加入战斗](Status_properties/AllowLeaveDisallowJoinCombat.md "状态属性/允许离开禁止加入战斗") |  |

[高等复原术](Greater_Restoration.md "高等复原术")
[移除诅咒](Remove_Curse.md "移除诅咒")
[(更多)](Cursed_(Condition_Type).md#Removal).md#Removal> "被诅咒（状态类型）")
|

[(更多)](Cursed_(Condition_Type).md#Immunity).md#Immunity> "被诅咒（状态类型）")
| [患病](Diseased_(status_group).md) | _(无)_ |

[治疗](Heal.md "治疗")
[圣疗](Lay_on_Hands.md "圣疗")
[恢复](Lesser_Restoration.md "恢复")
[(更多)](Diseased_(Condition_Type).md#Removal).md#Removal> "患病（状态类型）")
|

[神佑](Divine_Health.md "神佑")
[百病不侵](Purity_of_Body.md "百病不侵")
[(更多)](Diseased_(Condition_Type).md#Immunity).md#Immunity> "患病（状态类型）")
| [恐慌](Frightened_(status_group).md) | [恐慌](Frightened_(Condition).md "恐慌（状态）") |

[反制善恶](Dispel_Evil_And_Good.md "反制善恶")
[心如止水](Stillness_of_Mind.md "心如止水")
[(更多)](Frightened_(Condition_Type).md#Removal).md#Removal> "恐慌（状态类型）")
|

[勇气灵光](Aura_of_Courage.md "勇气灵光")
[安定心神](Calm_Emotions.md "安定心神")
[英雄气概](Heroism.md "英雄气概")
[自然防护](Nature's_Ward.md "自然防护") <sup>[\[3\]](#cite_note-elemental-fey-3)</sup>
[(更多)](Frightened_(Condition_Type).md#Immunity).md#Immunity> "恐慌（状态类型）")
| [失能](Incapacitated_(status_group).md) | [失能](Incapacitated_(Condition).md "失能（状态）") |

[(更多)](Incapacitated_(Condition_Type).md#Removal).md#Removal> "失能（状态类型）")
|

[(更多)](Incapacitated_(Condition_Type).md#Immunity).md#Immunity> "失能（状态类型）")
| [麻痹](https://bg3.wiki/w/index.php?title=Paralysed_(status_group)&action=edit&redlink=1) "麻痹（状态组）（页面不存在）") | [麻痹](Paralysed_(Condition).md "麻痹（状态）") |

[慰藉箭](Arrow_of_Salving.md "慰藉箭")
[恢复](Lesser_Restoration.md "恢复")
[(更多)](https://bg3.wiki/w/index.php?title=Paralysed_(Condition_Type)&action=edit&redlink=1) "麻痹（状态类型）（页面不存在）")
|

[自由行动药水](Elixir_of_Guileful_Movement.md "自由行动药水")
[自由动作戒指](Ring_of_Free_Action.md "自由动作戒指")
[行动自如](Freedom_of_Movement.md "行动自如")
[(更多)](https://bg3.wiki/w/index.php?title=Paralysed_(Condition_Type)&action=edit&redlink=1) "麻痹（状态类型）（页面不存在）")
| [石化](Petrified_(status_group).md) | [石化](Petrified_(Condition).md "石化（状态）") |

[石化蜥蜴油](Basilisk_Oil.md "石化蜥蜴油")
[高等复原术](Greater_Restoration.md "高等复原术")
[(更多)](Petrified_(Condition_Type).md#Removal).md#Removal> "石化（状态类型）")
|
| [中毒](Poisoned_(status_group).md) | [中毒](Poisoned_(Condition).md "中毒（状态）") |

[抗毒剂](Antidote.md "抗毒剂")
[圣疗](Lay_on_Hands.md "圣疗")
[恢复](Lesser_Restoration.md "恢复")
[(更多)](Poisoned_(Condition_Type).md#Removal).md#Removal> "中毒（状态类型）")
|

[毒素抗性灵药](Elixir_of_Poison_Resistance.md "毒素抗性灵药")
[防护毒素](Protection_from_Poison.md "防护毒素")<sup>[\[2\]](#cite_note-adv-2)</sup>
[百病不侵](Purity_of_Body.md "百病不侵")
[(更多)](Poisoned_(Condition_Type).md#Immunity).md#Immunity> "中毒（状态类型）")
| [变形](Polymorphed_(status_group).md) | [变形](Polymorphed_(Condition).md "变形（状态）") |

失去所有[生命值](Hit_Points.md "生命值")\[[_验证_](bg3wiki_colon_Verification.md "bg3wiki:验证")\]
[(更多)](Polymorphed_(Condition_Type).md#Removal).md#Removal> "变形（状态类型）")
|

[不变形态](Immutable_Form.md "不变形态")
[(更多)](Polymorphed_(Condition_Type).md#Immunity).md#Immunity> "变形（状态类型）")
| [倒伏](Prone_(status_group).md) | [倒伏](Prone_(Condition).md "倒伏（状态）") |

[协助](Help.md "协助")
[(更多)](Prone_(Condition_Type).md#Removal).md#Removal> "倒伏（状态类型）")
|

[(更多)](Prone_(Condition_Type).md#Immunity).md#Immunity> "倒伏（状态类型）")
| [束缚](Restrained_(status_group).md) | [束缚](Restrained_(Condition).md "束缚（状态）") |

[协助](Help.md "协助")
[(更多)](Restrained_(Condition_Type).md#Removal).md#Removal> "束缚（状态类型）")
|

[自由行动药水](Elixir_of_Guileful_Movement.md "自由行动药水")
[自由动作戒指](Ring_of_Free_Action.md "自由动作戒指")
[行动自如](Freedom_of_Movement.md "行动自如")
[(更多)](Restrained_(Condition_Type).md#Immunity).md#Immunity> "束缚（状态类型）")
| [沉睡](Sleeping_(status_group).md) | [沉睡](Sleeping_(Condition).md "沉睡（状态）") |

[推击](Shove.md "推击")
[倒伏](Prone_(Condition).md "倒伏（状态）")
[濡湿](Wet_(Condition).md "濡湿（状态）")
[(更多)](Sleeping_(Condition_Type).md#Removal).md#Removal> "沉睡（状态类型）")
|
| [震慑](Stunned_(status_group).md) | [震慑](Stunned_(Condition).md "震慑（状态）") |

[行动自如](Freedom_of_Movement.md "行动自如")
[高等复原术](Greater_Restoration.md "高等复原术")
[(更多)](Stunned_(Condition_Type).md#Removal).md#Removal> "震慑（状态类型）")
|
| [昏迷](Unconscious_(status_group).md) | _(无)_ |

[(更多)](Unconscious_(Condition_Type).md#Removal).md#Removal> "昏迷（状态类型）")
|

[(更多)](Unconscious_(Condition_Type).md#Immunity).md#Immunity> "昏迷（状态类型）")

1. [↑](#cite_ref-representative_1-0) 许多状态类型都有一个作为最基本形式的特定状态。
1. ↑ [2.0](#cite_ref-adv_2-0) [2.1](#cite_ref-adv_2-1) 在[豁免检定](Saving_throw.md "豁免检定")上给予[优势](Advantage.md "优势")
1. [↑](#cite_ref-elemental-fey_3-0) 仅限元素生物和妖精。

## 状态列表

游戏中的所有状态列表分为以下页面，以限制每个页面的大小：

- [状态/列表 (1-500)](Conditions/List_(1-500).md)
- [状态/列表 (501-1000)](Conditions/List_(501-1000).md)
- [状态/列表 (1001-1500)](Conditions/List_(1001-1500).md)

---
*Source: [Conditions](https://bg3.wiki/wiki/Conditions)*