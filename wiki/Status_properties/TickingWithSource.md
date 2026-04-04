# 状态属性/TickingWithSource

另请参阅 [状态属性](../Status_properties.md "状态属性")。

**TickingWithSource** 是一个 [状态属性](../Status_property.md "状态 property")。具有此属性的效果将在状态来源的回合“生效”（即应用其效果并将剩余持续时间减少 1 回合）。通常，这会在受影响生物的回合发生。例如，受 [精魂守卫](../Spirit_Guardians_(Condition).md "精魂守卫 (状态)")（具有 TickingWithSource 属性）影响的目标会在施法者的回合受到伤害，而受 [燃烧](../Burning_(Condition).md "燃烧 (状态)")（不具有该属性）影响的目标会在其自己的回合受到伤害。

此属性对于一些持续时间为 1 回合的效果（如 [冻僵](../Bone_Chilled_(Condition).md "冻僵 (状态)") 或 [冷冻射线](../Ray_of_Frost_(Condition).md "冷冻射线 (状态)")）也尤为重要。如果没有此属性，这些效果会在目标回合开始时生效完毕，立即结束，甚至无法应用减益效果一个回合。

## 具有 TickingWithSource 的状态列表

| --- | --- |
| [恐惧](../Frightened_(Condition).md "恐惧 (状态)") | 受影响的生物无法移动。恐慌生物在 [属性检定](../Ability_Check.md "属性检定") 和 [攻击掷骰](../Attack_roll.md "攻击掷骰") 上也具有 [劣势](../Disadvantage.md "劣势")。 |
| [绝对护佑](../Aegis_of_the_Absolute_(Condition).md "绝对护佑 (状态)") | 主脑在下一回合开始前，对上一轮受到的所有伤害类型 [免疫](../Immune.md "免疫")。 |
| [野性活力](../Animalistic_Vitality_(Condition).md "野性活力 (状态)") | 受影响实体在生命值低于 60 时，每回合恢复 2d8⁠⁠[生命值](../Healing.md "治疗")。它还会获得额外 3.5 米（12 英尺）的移动速度。_\[[参见：错误](../Animalistic_Vitality_(Condition).md#Bugs).md#Bugs> "野性活力 (状态)")\]_ |
| [巴尔教徒仪式目标](../Bhaalist_Ritual_Target_(Condition).md "巴尔教徒仪式目标 (状态)") | 作为进入神殿挑战的一部分，受影响实体已成为一名吟唱邪教徒“远距杀手”的目标，该邪教徒在其亵渎仪式结束后可以施放 [巴尔的律令死亡仪式](../Bhaal's_Power_Word_Kill_Ritual.md "巴尔的律令死亡仪式")。离开远距杀手 55 米（183 英尺）的吟唱范围可使你免受该效果影响。击杀远距杀手可停止仪式并赢得冲突。 |
| [冻僵](../Bone_Chilled_(Condition).md "冻僵 (状态)") | 无法恢复 [生命值](../Hit_Points.md "生命值")。无法 [协助](../Help.md "协助") [倒地](../Downed_(Condition).md "倒地 (状态)") 的角色。如果是不死生物，在 [攻击掷骰](../Attack_roll.md "攻击掷骰") 上具有 [劣势](../Disadvantage.md "劣势")。 |
| [易碎](../Brittle_(Condition).md "易碎 (状态)") | 受影响实体在燃烧时被迅速冷却，使其对 [雷鸣](../Thunder.md "雷鸣") 和 [钝击](../Bludgeoning.md "钝击") 伤害 [易伤](../Vulnerable.md "易伤")。在其回合开始时受到 2d6⁠⁠[寒冷](../Cold.md "寒冷") 伤害。 |
| [暴政之链](../Chain_of_Tyranny_(Condition).md "暴政之链 (状态)") | 受影响实体的移动速度减半。当锁链断裂时，它会受到 8d8⁠⁠[力场](../Force.md "力场") 伤害。 |
| [绞缠](../Constricted_(Condition).md "绞缠 (状态)") | 受影响实体无法移动。对其的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [优势](../Advantage.md "优势")，而其攻击掷骰和 [敏捷](../Dexterity.md "敏捷") [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。该实体每回合受到 2d6+2⁠⁠[穿刺](../Piercing.md "穿刺") 和 1d4⁠⁠[黯蚀](../Necrotic.md "黯蚀") 伤害。可通过 [协助](../Help.md "协助") 移除。 |
| [恐鸦之诅咒](../Curse_of_the_Dire_Raven_(Condition).md "恐鸦之诅咒 (状态)") | 被恐鸦的羽毛标记。对受影响实体的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [优势](../Advantage.md "优势")。 |
| [诅咒：额外伤害](../Cursed_colon__Additional_Damage_(Condition).md "诅咒：额外伤害 (状态)") | 从咒法者的攻击或法术中受到额外 1d8⁠⁠[黯蚀](../Necrotic.md "黯蚀") 伤害。 |
| [诅咒：攻击劣势](../Cursed_colon__Attack_Disadvantage_(Condition).md "诅咒：攻击劣势 (状态)") | 对诅咒来源的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：魅力](../Cursed_colon__Charisma_(Condition).md "诅咒：魅力 (状态)") | 使用 [魅力](../Charisma.md "魅力") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：体质](../Cursed_colon__Constitution_(Condition).md "诅咒：体质 (状态)") | 使用 [体质](../Constitution.md "体质") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：敏捷](../Cursed_colon__Dexterity_(Condition).md "诅咒：敏捷 (状态)") | 使用 [敏捷](../Dexterity.md "敏捷") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：智力](../Cursed_colon__Intelligence_(Condition).md "诅咒：智力 (状态)") | 使用 [智力](../Intelligence.md "智力") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：力量](../Cursed_colon__Strength_(Condition).md "诅咒：力量 (状态)") | 使用 [力量](../Strength.md "力量") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [诅咒：感知](../Cursed_colon__Wisdom_(Condition).md "诅咒：感知 (状态)") | 使用 [感知](../Wisdom.md "感知") 的 [属性检定](../Ability_Check.md "属性检定") 和 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [死亡指令](../Deadly_Orders_(Condition).md "死亡指令 (状态)") | 受影响实体被命令攻击特定敌人。它更有可能以该敌人为目标，并且对该敌人的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [优势](../Advantage.md "优势")。 |
| [吞噬智力](../Devoured_Intellect_(Condition).md "吞噬智力 (状态)") | [智力](../Intelligence.md "智力") 每回合减少 1。 |
| [分心](../Distracted_(Condition).md "分心 (状态)") | 没有任何注意力放在周围环境上。分心者的盟友对下一个对该生物的攻击掷骰具有 [优势](../Advantage.md "优势")。 |
| [爆裂浮姆](../Exploding_Flumph_(Condition).md "爆裂浮姆 (状态)") | 此灵体将在回合结束时爆炸。2 米（7 英尺）内的每个生物必须通过敏捷 [豁免检定](../Saving_throw.md "豁免检定")，否则受到 1d6⁠⁠[力场](../Force.md "力场") 伤害。 |
| [爆炸在即！](../Explosion_Imminent!_(Condition).md "爆炸在即！ (状态)") | 冰封法球将爆炸，施放 [欧提路克冰封法球](../Otiluke's_Freezing_Sphere_(Launch).md "欧提路克冰封法球 (启动)")。 |
| [暴露啃咬](../Exposing_Bite_(Condition).md "暴露啃咬 (状态)") | 生物分心。下一次从 2 米（7 英尺）内对该生物的攻击必定是重击。 |
| [恐慌](../Frightened_(Condition).md "恐慌 (状态)") | 受影响的生物无法移动。恐慌生物在 [属性检定](../Ability_Check.md "属性检定") 和 [攻击掷骰](../Attack_roll.md "攻击掷骰") 上也具有 [劣势](../Disadvantage.md "劣势")。 |
| [被擒抱](../Grappled_(Condition).md "被擒抱 (状态)") | 受影响实体 [失能](../Incapacitated_(status_group).md) 且在擒抱期间无法被伤害。通过 [协助](../Help.md "协助") 来释放它！ |
| [被擒抱（触手）](../Grappled_(Tentacle)_(Condition).md "被擒抱（触手） (状态)") | 在每回合开始时，目标进行 [力量](../Strength.md "力量") [豁免检定](../Saving_throw.md "豁免检定") 以尝试挣脱。豁免失败时，受到 2d6⁠⁠[心灵](../Psychic.md "心灵") 伤害。 |
| [曳光弹](../Guiding_Bolt_(Condition).md "曳光弹 (状态)") | 下一次对该生物的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [优势](../Advantage.md "优势")。 |
| [灼热金属](../Heat_Metal_(Condition).md "灼热金属 (状态)") | 加热生物身上的金属武器或护甲，无需豁免（自动优先武器）。如果持有者初始 [豁免检定](../Saving_throw.md "豁免检定") 失败，金属武器会掉落。如果生物接触加热的金属物品，其 [攻击掷骰](../Attack_roll.md "攻击掷骰") 和 [属性检定](../Ability_Check.md "属性检定") 具有 [劣势](../Disadvantage.md "劣势")。在后续回合，如果生物仍接触金属，咒法者可使用 [重新施加热金属](../Reapply_Heat_Metal.md "重新施加热金属") 造成额外 2d8⁠⁠[火焰](../Fire.md "火焰") 伤害，迫使生物再次通过豁免检定或掉落物品（如果是金属武器）。 |
| [灼热金属：劣势](../Heat_Metal_colon__Disadvantage_(Condition).md "灼热金属：劣势 (状态)") | 在施法者下一回合开始前，[攻击掷骰](../Attack_roll.md "攻击掷骰") 和 [属性检定](../Ability_Check.md "属性检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [灭族者（目标）](../Horde_Breaker_(Target)_(Condition).md "灭族者（目标） (状态)") | 生物对后续攻击开放。 |
| [催眠凝视](../Hypnotic_Gaze_(Condition).md "催眠凝视 (状态)") | 无法移动或执行动作、附赠动作或反应。咒法者在对话中的 [属性检定](../Ability_Check.md "属性检定") 具有 [优势](../Advantage.md "优势")。受到伤害时移除。持续时间可通过 [维持催眠凝视](../Maintain_Hypnotic_Gaze.md "维持催眠凝视") 延长。 |
| [被催眠](../Hypnotised_(Condition).md "被催眠 (状态)") | 无法 [移动](../Movement_speed.md "移动速度") 或执行 [动作](../Action.md "动作")、[附赠动作](../Bonus_action.md "附赠动作") 或 [反应](../Reaction.md "反应")。受到伤害、被 [推击](../Shove.md "推击") 或被 [协助](../Help.md "协助") 时移除。 |
| [诱惑](../Lured_(Condition).md "诱惑 (状态)") | 受影响实体被鸟妖的诱捕旋律吸引，并使用其回合向鸟妖靠近，可能引发其他鸟妖的借机攻击。受影响实体必须在回合开始时通过 DC 13 [感知](../Wisdom.md "感知") [豁免检定](../Saving_throw.md "豁免检定")，否则保持被诱惑状态。受到伤害或被 [推击](../Shove.md "推击") 会移除该状态。 |
| [移动华舞的目标](../Mobile_Flourish_Target_(Condition).md "移动华舞的目标 (状态)") | 被吟游诗人的流畅攻击瞄准。吟游诗人可以传送到该生物旁边。 |
| [偏执梦境](../Paranoid_Dreams_(Condition).md "偏执梦境 (状态)") | 当此观察者眼魔被击中时，它会在恐惧中做梦。5 次偏执梦境后，它将花费一个传奇动作施放 [眼魔噩梦](../Ocular_Nightmare.md "眼魔噩梦")。如果观察者眼魔使用其一道眼射线，它会失去一次偏执梦境。 |
| [首要目标](../Prime_Target_(Condition).md "首要目标 (状态)") | 你已激起 [复仇侍卫](../Grym.md "复仇侍卫") 的怒火。复仇侍卫会尝试攻击此生物（如果可能）。 |
| [冷冻射线](../Ray_of_Frost_(Condition).md "冷冻射线 (状态)") | [移动速度](../Movement_speed.md "移动速度") 减少 3 米（10 英尺）。 |
| [再生](../Regeneration_(Condition).md "再生 (状态)") | [菘蓝树人](../Wood_Woad.md "菘蓝树人") 如果穿过藤蔓地表，会恢复 10⁠⁠[生命值](../Healing.md "治疗")，除非它最近受到了 ⁠[火焰](../Fire.md "火焰") 伤害。 |
| [活力血祭](../Revitalising_Gore_(Condition).md "活力血祭 (状态)") | 受影响实体浸透在敌人的血液中。每回合恢复 2d6⁠⁠[生命值](../Healing.md "治疗")。在 10 级时，治疗量增加到每回合 4d6⁠⁠[生命值](../Healing.md "治疗")。 |
| [败血症](../Septic_(Condition).md "败血症 (状态)") | 受影响实体的 [体质](../Constitution.md "体质") 减少 1，并且体质 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [碎甲](../Shredded_Armour_(Condition).md "碎甲 (状态)") | [护甲等级](../Armour_Class.md "护甲等级") 已减少 2。通过治疗移除。 |
| [灵魂麻木](../Soulnumbed_(Condition).md "灵魂麻木 (状态)") | 无法执行 [附赠动作](../Actions.md#Resources "动作") 或 [反应](../Actions.md#Reactions "动作")。 |
| [精魂守卫](../Spirit_Guardians_(Condition).md "精魂守卫 (状态)") | 灵体攻击受影响实体，每回合对其造成伤害并使其 [移动速度](../Movement_speed.md "移动速度") 减半。受到的伤害为 3d8⁠⁠[光耀](../Radiant.md "光耀") 或 3d8⁠⁠[黯蚀](../Necrotic.md "黯蚀") 加上每 [升环](../Upcast.md "升环") 等级 1d8。如果通过 [感知](../Wisdom.md "感知") [豁免检定](../Saving_throw.md "豁免检定")，伤害减半。 |
| [魔能惰性折磨](../Stricken_with_Eldritch_Inertia_(Condition).md "魔能惰性折磨 (状态)") | 受影响实体对状态来源施放的法术的下一次 [豁免检定](../Saving_throw.md "豁免检定") 具有 [劣势](../Disadvantage.md "劣势")。 |
| [外科医生之选](../Surgeon's_Chosen_(Condition).md "外科医生之选 (状态)") | 携带外科医生要求完成手术的工具。护士获得 +4 [护甲等级](../Armour_Class.md "护甲等级") 加值。 |
| [克敌机先](../True_Strike_(Condition).md "克敌机先 (状态)") | 咒法者对该生物的 [攻击掷骰](../Attack_roll.md "攻击掷骰") 具有 [优势](../Advantage.md "优势")。 |
| [难守秘密](../Untenable_Secret_(Condition).md "难守秘密 (状态)") | 被一个怪物般的秘密所折磨。受影响实体必须对盟友施放 [分享难守秘密](../Share_Untenable_Secret.md "分享难守秘密")，否则会遭受衰弱的 ⁠[心灵](../Psychic.md "心灵") 伤害。 |
| [吸血鬼再生](../Vampire_Regeneration_(Condition).md "吸血鬼再生 (状态)") | 吸血鬼在其回合开始时恢复 20 [生命值](../Hit_Points.md "生命值")，除非它处于阳光下，或受到了光耀伤害或圣水伤害。 |
| [巫术箭](../Witch_Bolt_(Condition).md "巫术箭 (状态)") | 咒法者每回合可使用一个 [动作](../Action.md "动作") 来激活连接至该生物的电弧，自动造成 1d12⁠⁠[闪电](../Lightning.md "闪电") 伤害。 |

---
*Source: [Status properties/TickingWithSource](https://bg3.wiki/wiki/Status_properties/TickingWithSource)*