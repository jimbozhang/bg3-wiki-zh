# 法术标志

**法术标志**是能力的技术属性。尽管名称如此，它们并非特定于[法术](Spells.md "Spells")，而是用于博德之门3中的所有动作。其中一些属性会反映在游戏内的工具提示中，例如 `IsConcentration`，但其他如 `HasHighGroundRangeExtension` 则是隐藏的，不过了解它们仍然很有用。

`CannotRotate`
|
`CannotTargetCharacter`
|
`CannotTargetItems`
|
`CannotTargetTerrain`
|
`ChasmRecovery`
|
`CombatLogSetSingleLineRoll`
|
| 法术标志 | 含义 |
| --- | --- |
| AbortOnSecondarySpellRollFail | 此标志专用于可以投掷另一个目标的动作，如[投掷](Throw.md "Throw")或[心灵遥控](Telekinesis.md "Telekinesis")。它决定在投掷法术检定失败后动作是否继续，该检定通常是[对抗](Contests.md "Contests")的运动检定。大多数投掷类动作都有此标志，但有些没有，例如[愤怒投掷](Enraged_Throw.md "Enraged Throw")。没有此标志，生物即使赢得对抗技能检定也无法避免被投掷。 |
| AbortOnSpellRollFail |  |
| AddFallDamageOnLand | 对于推动或移动的动作，目标在适用时会遭受[坠落伤害](Falling_damage.md "Falling damage")。 |
| AllowMoveAndCast | 使用此动作不会中断排队的移动。这仅由[躲藏](Hide.md "躲藏")及相关动作使用，允许玩家在移动时隐藏。 |
| CallAlliesSpell |  |
| CanAreaDamageEvade | 造成区域伤害的动作，可受[反射闪避](Evasion.md "Evasion")影响。 |
| CanDualWield |  |
| CannotRotate |  |
| CannotTargetCharacter |  |
| CannotTargetItems |  |
| CannotTargetTerrain |  |
| ChasmRecovery |  |
| CombatLogSetSingleLineRoll |  |
| DisableBlood | 动作在造成伤害时不会产生血迹飞溅。这不会影响生成的[血](Blood_(surface).md "Blood (surface)")地表，只影响撞击时的粒子效果。 |
| DisplayDamageModifiers |  |
| DisplayInItemTooltip | 对于附加到消耗品物品的动作，在物品工具提示中显示此动作。 |
| DontAbortPerforming |  |
| HasHighGroundRangeExtension | 当以较低海拔的敌人为目标时，动作的射程会增加。详见[高地规则](High_ground_rules.md "High ground rules")。 |
| HasSomaticComponent |  |
| HasVerbalComponent | 动作需要言语成分，该成分可被[沉默](Silenced_(Condition).md "Silenced (Condition)")抑制。 |
| HideInItemTooltip |  |
| IgnoreAoO | 对于不会引发[借机攻击](Opportunity_Attack.md "Opportunity Attack")的移动动作。 |
| IgnorePreviouslyPickedEntities | 对于可以选择多个目标的动作，这意味着单个目标不能被多次选择。 |
| IgnoreSilence |  |
| IgnoreVisionBlock | 动作可以以被魔法[黑暗术](Darkness_(cloud).md "Darkness (cloud)")或类似效果遮蔽的生物或点为目标。 |
| ImmediateCast | 动作在使用时立即执行，而不是进入目标选择或确认界面。 |
| InventorySelection | 动作打开库存选择菜单。这专用于[投掷](Throw.md "Throw")、[心灵遥控](Telekinesis.md "Telekinesis")和类似动作。 |
| Invisible | 动作可以在不打破[隐形](Invisible_(Condition).md "Invisible (Condition)")或触发[高等隐形术](Greater_Invisibility_(Condition).md "Greater Invisibility (Condition)")的隐匿检定的情况下执行。另见隐匿。 |
| IsAttack |  |
| IsConcentration | 动作需要[专注](Concentration.md "Concentration")。 |
| IsDefaultWeaponAction |  |
| IsEnemySpell |  |
| IsHarmful |  |
| IsJump |  |
| IsLinkedSpellContainer |  |
| IsMelee |  |
| IsSpell | 动作是真正的[法术](Spell.md "Spell")，所有与法术交互的内容（例如[法术反制](Counterspell.md "Counterspell"))都将应用于此动作。 |
| IsSwarmAttack |  |
| IsTrap |  |
| NoAOEDamageOnLand |  |
| NoCameraMove |  |
| NoCooldownOnMiss | 此动作在未命中时不会进入冷却。 |
| None |  |
| PickupEntityAndMove | 这专用于[即兴近战武器](Improvised_Melee_Weapon.md "Improvised Melee Weapon")（以及狂战士变体）。它决定目标物体或生物是否可以被拾起和移动。 |
| RangeIgnoreBlindness | [失明术](Blinded_(Condition).md "Blinded (Condition)")不会减少此能力的射程。 |
| RangeIgnoreSourceBounds |  |
| RangeIgnoreTargetBounds |  |
| RangeIgnoreVerticalThreshold |  |
| Stealth | 动作可以在不打破[隐藏](Hiding_(Condition).md "Hiding (Condition)")的情况下执行。另见隐形。 |
| TargetClosestEqualGroundSurface |  |
| Temporary | 此动作是临时授予的，出现在热键栏右侧的特殊区域中。 |
| UnavailableInDialogs |  |
| UNUSED_D |  |
| Wildshape |  |

---
*Source: [Spell flags](https://bg3.wiki/wiki/Spell_flags)*