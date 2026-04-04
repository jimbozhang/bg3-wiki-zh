# 有错误的动作和反应列表

此列表旨在记录那些根据其工具提示无法按预期运作，或在其描述、功能或位置存在其他问题（或信息缺失）的动作和反应。此列表不太可能完整，因为很可能存在许多我们尚未知晓的动作和反应问题。

由于此列表涉及的问题很可能在补丁和热修复中被更改，因此在更新后条目很可能不再正确。

所有条目目前均正确，截至 **热修复 33**。

## 动作和反应

- 此反应无法在受[星界形态](Starry_Form.md "星界形态")影响时使用。

[ Accursed Spectre (reaction) ](Accursed_Spectre_(reaction).md "Accursed Spectre (reaction)")
|

- 描述中未说明，但此反应无法对[亡灵](Undead.md "亡灵")使用。
- 被[恃强凌弱](Cull_the_Weak.md "恃强凌弱")杀死的生物不会触发此反应。
- 此召唤生物的 `CharacterStats` 未正确设置 `DifficultyStatuses`，因此该生物会因[探索者难度](Difficulty.md#Explorer_mode "难度")修正器而损失 30% 生命值，如同其为敌对 NPC。
- 此反应无法在受[星界形态](Starry_Form.md "星界形态")影响时或[伪装术](Disguise_Self.md "伪装术")时使用。

[ 强酸吐息 ](Acid_Breath.md "强酸吐息")
|

- 工具提示错误地将效果区域描述为锥形，而实际上它是线形。

[ 奥术射击：放逐箭 ](Arcane_Shot_colon__Banishing_Arrow.md "奥术射击：放逐箭")
|

- 由于错误地使用了 `DamageBonus` 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。

[ 奥术射击：魅惑箭 ](Arcane_Shot_colon__Beguiling_Arrow.md "奥术射击：魅惑箭")
|

- 由于错误地使用了 `DamageBonus` 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。

[ 奥术射击：爆裂箭 ](Arcane_Shot_colon__Bursting_Arrow.md "奥术射击：爆裂箭")
|

- 与大多数其他奥术射击选项不同，此动作会立即消耗[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")，而非在命中时消耗。相反，此资源消耗会在未命中时返还，这几乎等同于原有效果。这导致与[曲射](Curving_Shot.md "曲射")产生一些不寻常的交互。如果爆裂箭未命中其初始目标，[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")消耗将被返还，然后攻击将被重定向到新目标。如果此目标被命中，爆裂箭将免费生效。如果重定向的命中也未命中，它将返还另一支奥术箭，总计获得 +1 支[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")。

[ 奥术射击：衰弱箭 ](Arcane_Shot_colon__Enfeebling_Arrow.md "奥术射击：衰弱箭")
|

- 由于错误地使用了 `DamageBonus` 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。

[ 奥术射击：抓取箭 ](Arcane_Shot_colon__Grasping_Arrow.md "奥术射击：抓取箭")
|

- - 由于错误地使用了 `DamageBonus` 函数，奥术射击在击中敌人时获得的额外伤害永远无法造成重击。

[ 奥术射击：穿透箭 ](Arcane_Shot_colon__Piercing_Arrow.md "奥术射击：穿透箭")
|

- 由于此攻击不涉及攻击掷骰，因此无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示中列出了额外伤害。这些包括：
- [奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）")
  - [箭术手套](Gloves_of_Archery.md "箭术手套")
  - [猎人印记](Hunter's_Mark.md "猎人印记")
  - [神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷")
  - [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓")

[ 奥术射击：寻的箭 ](Arcane_Shot_colon__Seeking_Arrow.md "奥术射击：寻的箭")
|

- 由于此攻击不涉及攻击掷骰，因此无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示中列出了额外伤害。这些包括：
- [奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）")
  - [箭术手套](Gloves_of_Archery.md "箭术手套")
  - [猎人印记](Hunter's_Mark.md "猎人印记")
  - [神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷")
  - [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓")

[ 奥术射击：暗影箭 ](Arcane_Shot_colon__Shadow_Arrow.md "奥术射击：暗影箭")
|

- 由于错误地使用了 `DamageBonus` 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。

[ 驼鹿面貌 ](Aspect_of_the_Elk.md "驼鹿面貌")
|

- 额外移动速度会在角色在其效果范围内开始回合或移动进入其范围时应用。此效果在同一回合内应用的次数没有限制，且额外移动速度在离开有效范围后不会被移除。角色在范围内非常轻微地多次进出（每次消耗少于 1.5 米 / 5 英尺的移动速度）可以逐渐获得理论上无上限的额外移动速度。

[ 谋杀灵光（动作） ](Aura_of_Murder_(action).md "谋杀灵光（动作）")
|

- 尽管有额外描述，但不存在任何限制导致无法被恐慌的生物免疫谋杀灵光。

[ 唤醒蠕行之爪 ](Awaken_Crawling_Claws.md "唤醒蠕行之爪")
|

- 游戏内描述称此动作会击晕 4 米 / 13 英尺内的敌人，但实际半径显著更大，为 12 米 / 40 英尺。

[ 摔翻打击 ](Backbreaker.md "摔翻打击")
|

- 此攻击只能以[大型](Large.md "大型")或更小体型的角色为目标，且缺少类似攻击（如[摔绊攻击（近战）](Trip_Attack_(Melee).md "摔绊攻击（近战）")）上找到的相关工具提示警告。

[ 诗人激励（职业动作） ](Bardic_Inspiration_(class_action).md "诗人激励（职业动作）")
|

- 当用于以 +1d10 加值修改攻击掷骰时，诗人激励状态不会从角色身上移除。
- 诗人激励可能以已受 +1d10 版本影响的角色为目标，浪费效果，因为它们不叠加。

[ 啮咬（蝙蝠） ](Bite_(Bat).md "啮咬（蝙蝠）")
|

- 工具提示称此攻击应施加两回合名为“虚弱感染”的状态，该状态与[感染](Infected_(Condition).md "感染（状态）")相同，但体质 -3。此攻击缺少将此类状态施加于目标的必要代码。

[ 刀锋之歌 ](Bladesong.md "刀锋之歌")
|

- 挥舞匕首、长剑等的要求仅适用于主手。虽然“刀锋之歌受阻”将显示在法师身上，但如果副手挥舞着不兼容的武器，刀锋之歌仍然可用。
  - 如果副手武器不兼容，你无法积累任何高潮充能，也无法使用高潮。

[ 强化魔法：一级法术位 ](Bolstering_Magic_colon__Level_1_Spell_Slot.md "强化魔法：一级法术位")
|

- 此能力无法为[德鲁伊](Druid.md "德鲁伊")恢复法术位，因为该职业被错误地未赋予技术被动 `UnlockedSpellSlotLevel1`。然而，此被动特性的缺失对德鲁伊的施法能力没有其他影响。这仅适用于一级法术位，因此[强化魔法：二级法术位](Bolstering_Magic_colon__Level_2_Spell_Slot.md "强化魔法：二级法术位")和[强化魔法：三级法术位](Bolstering_Magic_colon__Level_3_Spell_Slot.md "强化魔法：三级法术位")应能正常工作。

[ 天界光箭 ](Bolt_of_Celestial_Light.md "天界光箭")
|

- 此动作在任何时候都不使用卓越骰，与游戏内工具提示“未命中：不消耗卓越骰”相反。

[ 不可撼动之恩赐 ](Boon_of_the_Unstoppable.md "不可撼动之恩赐")
|

- 当巴尔邪教徒吟唱仪式以触发此动作时，它会施加一个有错误的状态，显示为不可撼动，但缺乏任何实际的伤害减免。因此，每回合的第一次伤害实例不会被减至 1。
- 同一回合内的后续伤害实例会被正确的不可撼动状态正确地减至 1。

[ 备战（近战） ](Brace_(Melee).md "备战（近战）")
|

- 当与其他重掷骰子的特性结合时，战斗日志可能显示错误的重掷次数。

[ 黎明破晓 ](Break_of_Dawn.md "黎明破晓")
|

- 工具提示错误地称“目标仍承受一半伤害”，而实际上它们既未被击退也未被击倒。

[ 公牛冲锋 ](Bull_Rush.md "公牛冲锋")
|

- 游戏内工具提示不准确。它复制自类似的[原始践踏](Primal_Stampede.md "原始践踏")能力。特别是，工具提示称公牛冲锋会造成伤害、击倒目标，并且仅在[狂暴](Rage.md "狂暴")时可用，但这些都不属实。

[ 壁垒叱喝 ](Bulwark_Rebuke.md "壁垒叱喝")
|

- 成功豁免时的伤害被错误地计算为 1d4[力场](Force.md "力场")，而不是 2d4/2[力场](Force.md "力场")。

[ 请求协助 ](Call_for_Help.md "请求协助")
|

- 尽管工具提示中显示，但此动作不会授予[动作如潮](Action_Surge_(Condition).md "动作如潮（状态）")。

[ 圣杯治疗 ](Chalice_Healing.md "圣杯治疗")
|

- 当通过星界形态获得此能力时，此法术未正确赋予，其施法调整值应为感知，但会使用最近获得的施法职业的施法调整值。

[ 引导神力：幽影斗篷 ](Channel_Divinity_colon__Cloak_of_Shadows.md "引导神力：幽影斗篷")
|

- 此能力错误地使用了[幽影斗篷](Cloak_of_Shadows.md "幽影斗篷")的描述。它实际上不需要使用者处于遮蔽状态，可以在他人视线范围内，甚至在明亮光线下使用。

[ 冲锋（地底洛斯兽） ](Charge_(Deep_Roth%C3%A9).md "冲锋（地底洛斯兽）")
|

- 此能力可以以死亡生物为目标，导致与[恃强凌弱](Cull_the_Weak.md "恃强凌弱")等其他命中效果产生意外交互。

[ 魅惑动植物 ](Charm_Animals_and_Plants.md "魅惑动植物")
|

- 此法术未按描述运作，而是类似于[魅惑人类](Charm_Person.md "魅惑人类")。因此，尽管缺乏相关工具提示警告，此动作会被成功豁免的生物视为敌对。如果施法者或盟友伤害目标，状态也会提前结束，在更高难度模式下，目标可能在法术结束时变得敌对。
- 游戏内工具提示错误地链接了默认的[魅惑](Charmed_(Condition).md "魅惑（状态）")状态，而非其实际施加的状态。

[ 灰烬猛击 ](Cinderous_Swipe.md "灰烬猛击")
|

- 野兽形态下获得的此能力版本仅造成 1d6[火焰](Fire.md "火焰")额外伤害，而非工具提示所说的 2d6[火焰](Fire.md "火焰")。

| 名称 | 错误 |
| --- | --- |
| [ 吸收元素 ](Absorb_Elements.md "吸收元素") | 此反应无法在受[星界形态](Starry_Form.md "星界形态")影响时使用。 |
| [  Accursed Spectre (反应)  ](Accursed_Spectre_(reaction).md "Accursed Spectre (反应)") | 描述中未说明，但此反应无法对[亡灵](Undead.md "亡灵")使用。被[恃强凌弱](Cull_the_Weak.md "恃强凌弱")杀死的生物不会触发此反应。此召唤生物的 CharacterStats 未正确设置 DifficultyStatuses，因此该生物会因[探索者难度](Difficulty#Explorer_mode.md#Explorer_mode "难度")修正器而损失 30% 生命值，如同其为敌对 NPC。此反应无法在受[星界形态](Starry_Form.md "星界形态")影响时或[伪装术](Disguise_Self.md "伪装术")时使用。 |
| [ 强酸吐息 ](Acid_Breath.md "强酸吐息") | 工具提示错误地将效果区域描述为锥形，而实际上它是线形。 |
| [ 奥术射击：放逐箭 ](Arcane_Shot_colon__Banishing_Arrow.md "奥术射击：放逐箭") | 由于错误地使用了 DamageBonus 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。 |
| [ 奥术射击：魅惑箭 ](Arcane_Shot_colon__Beguiling_Arrow.md "奥术射击：魅惑箭") | 由于错误地使用了 DamageBonus 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。 |
| [ 奥术射击：爆裂箭 ](Arcane_Shot_colon__Bursting_Arrow.md "奥术射击：爆裂箭") | 与大多数其他奥术射击选项不同，此动作会立即消耗[奥术箭](Arcane_Archer#Arcane_Arrow.md#Arcane_Arrow "奥术射手")，而非在命中时消耗。相反，此资源消耗会在未命中时返还，这几乎等同于原有效果。这导致与[曲射](Curving_Shot.md "曲射")产生一些不寻常的交互。如果爆裂箭未命中其初始目标，[奥术箭](Arcane_Archer#Arcane_Arrow.md#Arcane_Arrow "奥术射手")消耗将被返还，然后攻击将被重定向到新目标。如果此目标被命中，爆裂箭将免费生效。如果重定向的命中也未命中，它将返还另一支奥术箭，总计获得 +1 支[奥术箭](Arcane_Archer#Arcane_Arrow.md#Arcane_Arrow "奥术射手")。 |
| [ 奥术射击：衰弱箭 ](Arcane_Shot_colon__Enfeebling_Arrow.md "奥术射击：衰弱箭") | 由于错误地使用了 DamageBonus 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。 |
| [ 奥术射击：抓取箭 ](Arcane_Shot_colon__Grasping_Arrow.md "奥术射击：抓取箭") | 由于错误地使用了 DamageBonus 函数，奥术射击在击中敌人时获得的额外伤害永远无法造成重击。 |
| [ 奥术射击：穿透箭 ](Arcane_Shot_colon__Piercing_Arrow.md "奥术射击：穿透箭") | 由于此攻击不涉及攻击掷骰，因此无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示中列出了额外伤害。这些包括：[奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）") [箭术手套](Gloves_of_Archery.md "箭术手套") [猎人印记](Hunter's_Mark.md "猎人印记") [神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷") [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓") |
| [ 奥术射击：寻的箭 ](Arcane_Shot_colon__Seeking_Arrow.md "奥术射击：寻的箭") | 由于此攻击不涉及攻击掷骰，因此无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示中列出了额外伤害。这些包括：[奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）") [箭术手套](Gloves_of_Archery.md "箭术手套") [猎人印记](Hunter's_Mark.md "猎人印记") [神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷") [泰坦弦弓](Titanstring_Bow.md "泰坦弦弓") |
| [ 奥术射击：暗影箭 ](Arcane_Shot_colon__Shadow_Arrow.md "奥术射击：暗影箭") | 由于错误地使用了 DamageBonus 函数，奥术射击在击中敌人时造成的额外伤害永远无法造成重击。 |
| [ 驼鹿面貌 ](Aspect_of_the_Elk.md "驼鹿面貌") | 额外移动速度会在角色在其效果范围内开始回合或移动进入其范围时应用。此效果在同一回合内应用的次数没有限制，且额外移动速度在离开有效范围后不会被移除。角色在范围内非常轻微地多次进出（每次消耗少于 1.5 米 / 5 英尺的移动速度）可以逐渐获得理论上无上限的额外移动速度。 |
| [ 谋杀灵光（动作） ](Aura_of_Murder_(action).md "谋杀灵光（动作）") | 尽管有额外描述，但不存在任何限制导致无法被恐慌的生物免疫谋杀灵光。 |
| [ 唤醒蠕行之爪 ](Awaken_Crawling_Claws.md "唤醒蠕行之爪") | 游戏内描述称此动作会击晕 4 米 / 13 英尺内的敌人，但实际半径显著更大，为 12 米 / 40 英尺。 |
| [ 摔翻打击 ](Backbreaker.md "摔翻打击") | 此攻击只能以[大型](Large.md "大型")或更小体型的角色为目标，且缺少类似攻击（如[摔绊攻击（近战）](Trip_Attack_(Melee).md "摔绊攻击（近战）")）上找到的相关工具提示警告。 |
| [ 诗人激励（职业动作） ](Bardic_Inspiration_(class_action).md "诗人激励（职业动作）") | 当用于以 +1d10 加值修改攻击掷骰时，诗人激励状态不会从角色身上移除。诗人激励可能以已受 +1d10 版本影响的角色为目标，浪费效果，因为它们不叠加。 |
| [ 啮咬（蝙蝠） ](Bite_(Bat).md "啮咬（蝙蝠）") | 工具提示称此攻击应施加两回合名为“虚弱感染”的状态，该状态与[感染](Infected_(Condition).md "感染（状态）")相同，但体质 -3。此攻击缺少将此类状态施加于目标的必要代码。 |
| [ 刀锋之歌 ](Bladesong.md "刀锋之歌") | 挥舞匕首、长剑等的要求仅适用于主手。虽然“刀锋之歌受阻”将显示在法师身上，但如果副手挥舞着不兼容的武器，刀锋之歌仍然可用。如果副手武器不兼容，你无法积累任何高潮充能，也无法使用高潮。 |
| [ 强化魔法：一级法术位 ](Bolstering_Magic_colon__Level_1_Spell_Slot.md "强化魔法：一级法术位") | 此能力无法为[德鲁伊](Druid.md "德鲁伊")恢复法术位，因为该职业被错误地未赋予技术被动 UnlockedSpellSlotLevel1。然而，此被动特性的缺失对德鲁伊的施法能力没有其他影响。这仅适用于一级法术位，因此[强化魔法：二级法术位](Bolstering_Magic_colon__Level_2_Spell_Slot.md "强化魔法：二级法术位")和[强化魔法：三级法术位](Bolstering_Magic_colon__Level_3_Spell_Slot.md "强化魔法：三级法术位")应能正常工作。 |
| [ 天界光箭 ](Bolt_of_Celestial_Light.md "天界光箭") | 此动作在任何时候都不使用卓越骰，与游戏内工具提示“未命中：不消耗卓越骰”相反。 |
| [ 不可撼动之恩赐 ](Boon_of_the_Unstoppable.md "不可撼动之恩赐") | 当巴尔邪教徒吟唱仪式以触发此动作时，它会施加一个有错误的状态，显示为不可撼动，但缺乏任何实际的伤害减免。因此，每回合的第一次伤害实例不会被减至 1。同一回合内的后续伤害实例会被正确的不可撼动状态正确地减至 1。 |
| [ 备战（近战） ](Brace_(Melee).md "备战（近战）") | 当与其他重掷骰子的特性结合时，战斗日志可能显示错误的重掷次数。 |
| [ 黎明破晓 ](Break_of_Dawn.md "黎明破晓") | 工具提示错误地称“目标仍承受一半伤害”，而实际上它们既未被击退也未被击倒。 |
| [ 公牛冲锋 ](Bull_Rush.md "公牛冲锋") | 游戏内工具提示不准确。它复制自类似的[原始践踏](Primal_Stampede.md "原始践踏")能力。特别是，工具提示称公牛冲锋会造成伤害、击倒目标，并且仅在[狂暴](Rage.md "狂暴")时可用，但这些都不属实。 |
| [ 壁垒叱喝 ](Bulwark_Rebuke.md "壁垒叱喝") | 成功豁免时的伤害被错误地计算为 1d4[力场](Force.md "力场")，而不是 2d4/2[力场](Force.md "力场")。 |
| [ 请求协助 ](Call_for_Help.md "请求协助") | 尽管工具提示中显示，但此动作不会授予[动作如潮](Action_Surge_(Condition).md "动作如潮（状态）")。 |
| [ 圣杯治疗 ](Chalice_Healing.md "圣杯治疗") | 当通过星界形态获得此能力时，此法术未正确赋予，其施法调整值应为感知，但会使用最近获得的施法职业的施法调整值。 |
| [ 引导神力：幽影斗篷 ](Channel_Divinity_colon__Cloak_of_Shadows.md "引导神力：幽影斗篷") | 此能力错误地使用了[幽影斗篷](Cloak_of_Shadows.md "幽影斗篷")的描述。它实际上不需要使用者处于遮蔽状态，可以在他人视线范围内，甚至在明亮光线下使用。 |
| [ 冲锋（地底洛斯兽） ](Charge_(Deep_Roth%C3%A9).md "冲锋（地底洛斯兽）") | 此能力可以以死亡生物为目标，导致与[恃强凌弱](Cull_the_Weak.md "恃强凌弱")等其他命中效果产生意外交互。 |
| [ 魅惑动植物 ](Charm_Animals_and_Plants.md "魅惑动植物") | 此法术未按描述运作，而是类似于[魅惑人类](Charm_Person.md "魅惑人类")。因此，尽管缺乏相关工具提示警告，此动作会被成功豁免的生物视为敌对。如果施法者或盟友伤害目标，状态也会提前结束，在更高难度模式下，目标可能在法术结束时变得敌对。游戏内工具提示错误地链接了默认的[魅惑](Charmed_(Condition).md "魅惑（状态）")状态，而非其实际施加的状态。 |
| [ 灰烬猛击 ](Cinderous_Swipe.md "灰烬猛击") | 野兽形态下获得的此能力版本仅造成 1d6[火焰](Fire.md "火焰")额外伤害，而非工具提示所说的 2d6[火焰](Fire.md "火焰")。 |
| [ 利爪（鹰身女妖） ](Claws_(Harpy).md "利爪（鹰身女妖）") | 由于[诱惑之歌](Luring_Song.md "诱惑之歌")的编码方式，鹰身女妖无法对任何在诱惑之歌施加时处于其半径内的目标使用此攻击，无论目标是否成功豁免效果，只要歌声持续。她们只能对这类目标使用[多重攻击（鹰身女妖）](Multiattack_(Harpy).md "多重攻击（鹰身女妖）")。 |
| [ 北风之握 ](Clench_of_the_North_Wind.md "北风之握") | 与其他四象宗动作不同，此动作仍保留了其父法术[人类定身术](Hold_Person.md "人类定身术")的 HasVerbalComponent SpellFlag，因此无法在[沉默](Silenced_(Condition).md "沉默（状态）")时使用。 |
| [ 碰撞鞋跟 ](Click_Heels.md "碰撞鞋跟") | 由于脚本错误，此效果的[劣势](Disadvantage.md "劣势")组件实际上应用于施法者执行的[反应](Actions#Reactions.md#Reactions "动作")攻击，而非针对施法者的反应攻击。 |
| [ 幽影斗篷 ](Cloak_of_Shadows.md "幽影斗篷") | 由于 RemoveConditions 字段编码不当，当从[轻度遮蔽](Lightly_Obscured_(Condition).md "轻度遮蔽（状态）")区域过渡到[重度遮蔽](Heavily_Obscured_(Condition).md "重度遮蔽（状态）")区域时，幽影斗篷会丢失，反之亦然。 |
| [ 水母云：攻击 ](Cloud_of_Jellyfish_colon__Attack.md "水母云：攻击") | 一个隐藏的技术状态（负责对击中目标施加视觉效果）会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 水母云：强力电刺 ](Cloud_of_Jellyfish_colon__Mighty_Shocking_Sting.md "水母云：强力电刺") | 此动作实际上无法解除目标武装，因为它施加的是[解除武装](Disarmed_(Condition).md "解除武装（状态）")，而非[武器掉落！](Weapon_Dropped!_(Condition).md "武器掉落！（状态）")，前者用于作为施加解除武装条件（如后者）的法术的工具提示描述标记。一个隐藏的技术状态（负责对目标施加视觉效果）会在目标成功豁免此反应时触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 水母云：电刺 ](Cloud_of_Jellyfish_colon__Shocking_Sting.md "水母云：电刺") | 一个隐藏的技术状态（负责对目标施加视觉效果）会在目标成功豁免此反应时触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 震荡爆炸 ](Concussive_Burst.md "震荡爆炸") | 游戏内工具提示称此攻击涉及体质豁免检定，但实际上使用的是攻击掷骰。 |
| [ 震荡猛击（灵体武器） ](Concussive_Smash_(Spiritual_Weapon).md "震荡猛击（灵体武器）") | 游戏内工具提示不正确 - 所有造成伤害均为[力场](Force.md "力场")伤害。与其他灵体武器攻击不同，此攻击造成的伤害是非魔法的。 |
| [ 困惑射线 ](Confusion_Ray.md "困惑射线") | 此能力的工具提示称其施加[昏沉](Befuddled_(Confusion_Ray)_(Condition).md "昏沉（困惑射线）（状态）") 3 回合。 |
| [ 腐蚀唾液 ](Corrosive_Spit.md "腐蚀唾液") | 此动作缺少[IsHarmful](IsHarmful_(spell_flag).md "IsHarmful（法术标志）")[法术标志](Spell_flags.md "法术标志")，因此能够以受[庇护术](Sanctuary_(Condition).md "庇护术（状态）")影响的生物为目标。 |
| [ 创造术法点 ](Create_Sorcery_Points.md "创造术法点") | 此特性可用于通过允许你获得无限次[自由施法](Freecast.md "自由施法")使用的错误（详见其页面）来获得几乎无限的术法点。 |
| [ 粉碎跃击（枭熊野兽形态） ](Crushing_Flight_(Owlbear_Wild_Shape).md "粉碎跃击（枭熊野兽形态）") | 目标在豁免时不会承受一半伤害（应为 (2d8 + 额外伤害)/2[钝击](Bludgeoning.md "钝击")），而是承受 (1d8 + 额外伤害)/2[钝击](Bludgeoning.md "钝击")，更接近四分之一伤害。此伤害始终为魔法伤害，无论攻击者是否拥有[原初打击](Primal_Strike.md "原初打击")。 |
| [ 语出惊人 ](Cutting_Words.md "语出惊人") | 视觉效果和反应法术始终指向攻击来源，无论攻击是否涉及攻击掷骰或豁免检定。因此，当语出惊人用于降低敌人对非敌对生物施放法术的豁免掷骰时，视觉效果和反应法术仍会指向施法者。反应法术被标记为有害法术，如果施法者是中立生物，它可能对吟游诗人及其队伍变得敌对。尽管标记了 HasVerbalComponent，语出惊人仍可在沉默时使用。语出惊人显示在战斗日志中时缺少吟游诗人骰子的威力。语出惊人检查攻击来源的吟游诗人等级，而不是使用语出惊人的吟游诗人（观察者）。因此，除非攻击者也是吟游诗人，否则语出惊人可触发的最大掷骰值差异为 6，而不是 5 级或以上吟游诗人的预期 8 或 10。 |
| [ 黎明爆裂打击 ](Dawnburst_Strike.md "黎明爆裂打击") | 游戏内描述注明了不正确的[DC](Dice_rolls#Save_DCs.md#Save_DCs "掷骰") 13 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")。它需要一个武器动作豁免检定，并带有 +2 DC 加值。尽管游戏内描述称只有光中的敌人必须豁免以避免失明，但失明会影响区域内的所有生物，包括盟友。由于编码错误，失明不影响攻击的原始目标。 |
| [ 眩目吐息 ](Dazzling_Breath.md "眩目吐息") | 当通过星界形态获得此能力时，此法术未正确赋予，其施法调整值应为感知，但会使用最近获得的施法职业的施法调整值。 |
| [ 防御式决斗 ](Defensive_Duellist.md "防御式决斗") | 与类似反应（[盾牌大师：格挡](Shield_Master_colon__Block.md "盾牌大师：格挡")）不同，反应选项卡中的防御式决斗图标在反应因装备不兼容武器而不可用时不会“变灰”。 |
| [ 拨挡飞弹 ](Deflect_Missiles.md "拨挡飞弹") | 伤害无需减至 0 即可重定向攻击。对于发射多个弹射物的远程攻击，如[多重攻击（远程）](Multiattack_(Ranged).md "多重攻击（远程）")或双持[手弩](Hand_Crossbows.md "手弩")，只有最后一次攻击可以被拨挡以减少其伤害。没有任何弹射物可以用[拨挡飞弹：重定向](Deflect_Missiles_colon__Redirect.md "拨挡飞弹：重定向")扔回。 |
| [ 毁灭狂怒 ](Destructive_Wrath.md "毁灭狂怒") | 毁灭狂怒会在施放[守卫刻文](Glyph_of_Warding.md "守卫刻文")的闪电或雷鸣变体时触发，但刻文爆炸的伤害不受影响。当施放一些不造成伤害的法术时，反应也会触发。'"`UNIQ--ref-00009930-QINU`"' 毁灭狂怒在用于以下法术时会被浪费：[毁灭飞矢](Bolts_of_Doom.md "毁灭飞矢") [震骨雷鸣](Bone-shaking_Thunder.md "震骨雷鸣") [召唤元素生物：风元素](Conjure_Elemental_colon__Air_Elemental.md "召唤元素生物：风元素") [召唤元素生物：风元素执政官](Conjure_Elemental_colon__Air_Myrmidon.md "召唤元素生物：风元素执政官") [召唤元素生物：土元素](Conjure_Elemental_colon__Earth_Elemental.md "召唤元素生物：土元素") [召唤元素生物：土元素执政官](Conjure_Elemental_colon__Earth_Myrmidon.md "召唤元素生物：土元素执政官") [召唤初级元素生物：泥魔蝠](Conjure_Minor_Elemental_colon__Mud_Mephits.md "召唤初级元素生物：泥魔蝠") [异界誓盟：灯神](Planar_Ally_colon__Djinni.md "异界誓盟：灯神") |
| [ 引爆 ](Detonate.md "引爆") | 工具提示称此攻击造成 100[火焰](Fire.md "火焰")。这应用于生物和生长的闸门时是不正确的。使用[活化孢子](Animating_Spores.md "活化孢子")复活为孢子仆从的工兵仅造成 2d6[力场](Force.md "力场")和 2d6[火焰](Fire.md "火焰")，并带有豁免检定以否定火焰伤害（相当于烟粉表面点燃）。 |
| [ 卑劣技巧：手腕轻弹 ](Dirty_Trick_colon__Flick_o'_the_Wrist.md "卑劣技巧：手腕轻弹") | 此动作不会触发许多武器上找到的命中武器函数，如[轻语匕首](Sussur_Dagger.md "轻语匕首")。 |
| [ 卑劣技巧：扬沙 ](Dirty_Trick_colon__Sand_Toss.md "卑劣技巧：扬沙") | 当与当前激活的远程武器一起使用时，[攻击掷骰](Attack_roll.md "攻击掷骰")使用[力量](Strength.md "力量")调整值。由于此动作为近战武器攻击掷骰，它会受到[巨武器大师：全力一击](Great_Weapon_Master_colon__All_In.md "巨武器大师：全力一击")的 -5 惩罚，但当挥舞[双手](Two-Handed.md "双手")和[两用](Versatile.md "两用")（无盾牌）武器时，其伤害不会增加 10。 |
| [ 缴械打击 ](Disarming_Strike.md "缴械打击") | 此动作的工具提示称“未命中：不消耗卓越骰”。这是一个简单的显示错误；此动作不需要[卓越骰](Battle_Master#Level_3.md#Level_3 "战斗大师")，在成功命中时也不会消耗任何卓越骰。 |
| [ 神圣干预：光耀复苏 ](Divine_Intervention_colon__Opulent_Revival.md "神圣干预：光耀复苏") | 此能力不会恢复补丁 8 中添加的任何新职业资源。生命值根据施法者的最大生命值恢复给角色，而非受影响的角色。 |
| [ 至圣斩 ](Divine_Smite.md "至圣斩") | 此动作的[一级法术位](Spells#Spell_slots.md#Spell_slots "法术")版本在荣誉模式下会因代码覆盖而改变攻击动画。此动作的[四级法术位](Spells#Spell_slots.md#Spell_slots "法术")、[五级法术位](Spells#Spell_slots.md#Spell_slots "法术")和[六级法术位](Spells#Spell_slots.md#Spell_slots "法术")版本在荣誉模式下用作攻击时不会丢失 DRS，而等效的[反应](Divine_Smite_(reaction).md "至圣斩（反应）")版本会丢失。 |
| [ 神圣打击：寒冷（近战） ](Divine_Strike_colon__Cold_(Melee).md "神圣打击：寒冷（近战）") | 此攻击未正确标记寒冷 DamageType 标志，这意味着它不会触发某些检查寒冷伤害的效果。 |
| [ 神圣打击：寒冷（远程） ](Divine_Strike_colon__Cold_(Ranged).md "神圣打击：寒冷（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击会消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。 |
| [ 神圣打击：火焰（近战） ](Divine_Strike_colon__Fire_(Melee).md "神圣打击：火焰（近战）") | 此攻击未正确标记火焰 DamageType 标志，这意味着它不会触发某些检查火焰伤害的效果。 |
| [ 神圣打击：火焰（远程） ](Divine_Strike_colon__Fire_(Ranged).md "神圣打击：火焰（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击会消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。 |
| [ 神圣打击：闪电（近战） ](Divine_Strike_colon__Lightning_(Melee).md "神圣打击：闪电（近战）") | 此攻击未正确标记闪电 DamageType 标志，这意味着它不会触发某些检查闪电伤害的效果。 |
| [ 神圣打击：闪电（远程） ](Divine_Strike_colon__Lightning_(Ranged).md "神圣打击：闪电（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击会消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。 |
| [ 神圣打击：黯蚀（近战） ](Divine_Strike_colon__Necrotic_(Melee).md "神圣打击：黯蚀（近战）") | 此攻击错误地标记了穿刺 DamageType 标志，而非黯蚀，这意味着它不会触发某些检查黯蚀伤害的效果，如[邪恶真菌](Malefic_Funghi.md "邪恶真菌")。一个隐藏的技术状态（负责对击中目标施加视觉效果）会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 神圣打击：黯蚀（远程） ](Divine_Strike_colon__Necrotic_(Ranged).md "神圣打击：黯蚀（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用[双持客](Dual_Wielder.md "双持客")切换时，此攻击消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。此攻击错误地标记了穿刺 DamageType 标志，而非黯蚀，这意味着它不会触发某些检查黯蚀伤害的效果，如[邪恶真菌](Malefic_Funghi.md "邪恶真菌")。一个隐藏的技术状态（负责对击中目标施加视觉效果）会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 神圣打击：毒素（近战） ](Divine_Strike_colon__Poison_(Melee).md "神圣打击：毒素（近战）") | 此攻击未正确标记毒素 DamageType 标志，这意味着它不会触发某些检查毒素伤害的效果。 |
| [ 神圣打击：光耀（近战） ](Divine_Strike_colon__Radiant_(Melee).md "神圣打击：光耀（近战）") | 此攻击未正确标记光耀 DamageType 标志，这意味着它不会触发某些检查光耀伤害的效果。 |
| [ 神圣打击：光耀（远程） ](Divine_Strike_colon__Radiant_(Ranged).md "神圣打击：光耀（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击会消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。 |
| [ 神圣打击：雷鸣（近战） ](Divine_Strike_colon__Thunder_(Melee).md "神圣打击：雷鸣（近战）") | 此攻击未正确标记雷鸣 DamageType 标志，这意味着它不会触发某些检查雷鸣伤害的效果，最显著的是[毁灭狂怒](Destructive_Wrath.md "毁灭狂怒")。 |
| [ 神圣打击：雷鸣（远程） ](Divine_Strike_colon__Thunder_(Ranged).md "神圣打击：雷鸣（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击会消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。 |
| [ 神圣打击：武器（近战） ](Divine_Strike_colon__Weapon_(Melee).md "神圣打击：武器（近战）") | 此攻击用作[动作](Actions#Resources.md#Resources "动作")时造成非魔法伤害，但用作攻击后[反应](Actions#Reactions.md#Reactions "动作")时造成魔法伤害。由于编码错误，当在[荣誉模式](Difficulty#Honour_mode.md#Honour_mode "难度")下用作攻击后反应时，此攻击造成非魔法伤害。 |
| [ 神圣打击：武器（远程） ](Divine_Strike_colon__Weapon_(Ranged).md "神圣打击：武器（远程）") | 当挥舞两把[手弩](Hand_Crossbows.md "手弩")并启用双持切换时，此攻击消耗一个[动作](Actions#Resources.md#Resources "动作")和一个[附赠动作](Actions#Resources.md#Resources "动作")，但不会执行副手攻击。此攻击用作动作时造成非魔法伤害，但用作攻击后反应时造成魔法伤害。 |
| [ 俯冲突袭 ](Diving_Strike.md "俯冲突袭") | 如果此攻击未命中且触发[鲁莽攻击](Reckless_Attack.md "鲁莽攻击")作为响应，攻击掷骰实际上不会重掷，因此它将始终未命中。然而，如果鲁莽攻击已激活，攻击掷骰会如预期般以[优势](Advantage.md "优势")进行。 |
| [ 醉拳技巧 ](Drunken_Technique.md "醉拳技巧") | 此攻击不会触发[诡诈之雾披风](Cloak_of_Cunning_Brume.md "诡诈之雾披风")，尽管它提供了[撤离](Disengage.md "撤离")的益处。 |
| [ 黑暗之刃 ](Edge_of_Darkness.md "黑暗之刃") | 此动作的游戏内工具提示不准确，且缺少其为范围攻击的关键信息。工具提示声称存在相关的[体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")，但事实并非如此。 |
| [ 结束狂暴 ](End_Rage.md "结束狂暴") | 此动作缺少 Self() 限制，可以用于移除其他角色的狂暴效果，尽管需要非常近的距离。 |
| [ 狂怒 ](Enrage.md "激怒") | 由于编码错误，如果枭熊形态丢失，枭熊之怒可能不会从德鲁伊身上移除。 |
| [ 熵光结界 ](Entropic_Ward.md "熵光结界") | 此反应无法在受[星界形态](Starry_Form.md "星界形态")影响时或[伪装术](Disguise_Self.md "伪装术")时使用。 |
| [ 灵巧步法 ](Evasive_Footwork.md "灵巧步法") | [灵巧步法](Evasive_Footwork_(Condition).md "灵巧步法（状态）")的 1 回合持续时间具有欺骗性。持续时间在战斗大师回合结束时计算，因此在同一回合立即结束。因此，除了借机攻击或反击外，灵巧步法在敌人进行任何攻击之前就会结束。此动作缺少 Self() 限制，可以为其他角色提供其效果，尽管需要非常近的距离。 |
| [ 暴露啃咬 ](Exposing_Bite.md "暴露啃咬") | 此状态在 3 米（10 英尺）内对受影响生物进行任何攻击掷骰后移除，但重击仅在 2 米（7 英尺）内进行时才适用。这意味着当使用[额外范围](Extra_Reach.md "额外范围")武器从最大范围攻击受影响生物时，效果会被浪费。 |
| [ 火蛇利牙 ](Fangs_of_the_Fire_Snake.md "火蛇利牙") | 尽管描述如此，远程武器攻击的伤害也会在持续时间内增加。 |
| [ 恐惧射线 ](Fear_Ray.md "恐惧射线") | 此能力的工具提示称其施加[恐慌](Frightened_(Condition).md "恐慌（状态）") 3 回合。 |
| [ 妖精仪态：魅惑 ](Fey_Presence_colon__Beguiling.md "妖精仪态：魅惑") | 此法术不受提供对[魅惑](Charmed_(Condition).md "魅惑（状态）")豁免[优势](Advantage.md "优势")或[劣势](Disadvantage.md "劣势")的效果影响。相反，它受提供对[恐慌](Frightened_(Condition).md "恐慌（状态）")豁免优势或劣势的效果影响（例如，[不诚者之盾](Shield_of_the_Undevout.md "不诚者之盾")）。 |
| [ 邪魔爆焰 ](Fiendish_Flameblast.md "邪魔爆焰") | 法术描述称其应施加[邪魔火焰](Infernal_Burning_(Condition).md "邪魔火焰（状态）")，但它施加的是[燃烧（奥顿）](Burning_(Orthonic)_(Condition).md "燃烧（奥顿）（状态）")。 |
| [ 极端孤注一掷 ](Fierce_Perilous_Stakes.md "极端孤注一掷") | 此法术可对同一目标多次施放，以一次施加多个[极端孤注一掷](Fierce_Perilous_Stakes_(Condition).md "极端孤注一掷（状态）")实例，甚至可以与[孤注一掷](Perilous_Stakes_(Condition).md "孤注一掷（状态）")叠加。每次施加的重击阈值降低、额外伤害和治疗效果都会相互叠加。伤害易伤不会叠加。 |
| [ 火酒爆炸 ](Firewine_Explosion.md "火酒爆炸") | 豁免时，目标承受 (4d6)/2[火焰](Fire.md "火焰")伤害，而不是 (2d6)/2[火焰](Fire.md "火焰")伤害，这实际上是全额伤害。 |
| [ 四雷拳 ](Fist_of_Four_Thunders.md "四雷拳") | 此法术缺少[武艺：附赠徒手打击](Martial_Arts_colon__Bonus_Unarmed_Strike.md "武艺：附赠徒手打击")的触发器，因此不会授予其效果。 |
| [ 蛾群乱舞：攻击 ](Flurry_of_Moths_colon__Attack.md "蛾群乱舞：攻击") | 一个隐藏的技术状态（负责对击中目标施加视觉效果）会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 蛾群乱舞：致盲虫群 ](Flurry_of_Moths_colon__Blinding_Swarm.md "蛾群乱舞：致盲虫群") | 一个隐藏的技术状态（负责对目标施加视觉效果）会在目标成功豁免此反应时触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 蛾群乱舞：强力致盲虫群 ](Flurry_of_Moths_colon__Mighty_Blinding_Swarm.md "蛾群乱舞：强力致盲虫群") | 一个隐藏的技术状态（负责对目标施加视觉效果）会在目标成功豁免此反应时触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果。 |
| [ 飞行（灵吸怪能力） ](Fly_(Illithid_Power).md "飞行（灵吸怪能力）") | 虽然它应该替换跳跃动作的键绑定，但此交互不可靠且似乎有错误。它通常最初有效，但在加载保存的游戏等情况下会重置为跳跃。 |
| [ 狂怒攻击 ](Frenzied_Strike.md "狂怒攻击") | 野蛮人达到 9 级后，此攻击不再施加发狂昏迷。 |
| [ 狂乱 ](Frenzy.md "狂怒") | 野蛮人达到 9 级后，此版本的狂暴可在已受狂暴影响时使用。 |
| [ 真菌感染 ](Fungal_Infestation.md "真菌感染") | 真菌感染可以在[第二幕](Act_Two.md "第二幕")结束时使用 boss 战前的恢复站来恢复充能，并且能够复活[噬脑怪](Intellect_Devourer.md "噬脑怪")，即使其尸体已被使用，从而制造无限僵尸。 |
| [ 飓风（职业动作） ](Gale_(class_action).md "飓风（职业动作）") | 工具提示错误地称此动作需要力量豁免。正确的敏捷豁免列在上方。 |
| [ 巨像切割者 ](Gargantuan_Cleave.md "巨像切割者") | 工具提示显示此动作施加全额武器伤害，而实际上它造成一半武器伤害。 |
| [ 挑衅攻击（近战） ](Goading_Attack_(Melee).md "挑衅攻击（近战）") | 目标在所有攻击上具有[劣势](Disadvantage.md "劣势")，即使是对挑衅攻击者。 |
| [ 挑衅攻击（远程） ](Goading_Attack_(Ranged).md "挑衅攻击（远程）") | 目标在所有攻击上具有[劣势](Disadvantage.md "劣势")，即使是对挑衅攻击者。 |
| [ 震峰拳 ](Gong_of_the_Summit.md "震峰拳") | 与其他四象宗动作不同，此动作仍保留了其父法术[粉碎音波](Shatter.md "粉碎音波")的 HasVerbalComponent SpellFlag，因此无法在[沉默](Silenced_(Condition).md "沉默（状态）")时使用。 |
| [ 全垒打 ](Grand_Slam.md "全垒打") | 由于此攻击不涉及攻击掷骰，因此无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示中列出了额外伤害。这些包括：[奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）") [巨武器大师：全力一击](Great_Weapon_Master_colon__All_In.md "巨武器大师：全力一击") [猎人印记](Hunter's_Mark.md "猎人印记") [愤怒](Wrath_(Condition).md "愤怒（状态）")尽管工具提示有警告，[大型](Large.md "大型")及更大体型的目标仍会被击退。 |
| [ 巨斧挥砍 ](Greataxe_Slash.md "巨斧挥砍") | 游戏内工具提示不正确 - 所有造成伤害均为[力场](Force.md "力场")伤害。 |

---
*Source: [List of bugged actions and reactions](https://bg3.wiki/wiki/List_of_bugged_actions_and_reactions)*