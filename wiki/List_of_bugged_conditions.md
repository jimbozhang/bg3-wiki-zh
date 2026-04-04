# 有错误的状态列表

此列表旨在记录那些根据其工具提示未能按预期运行，或者在其描述、功能或位置中存在其他问题或缺失信息的状态。此列表不太可能全面，因为很可能存在许多我们尚未意识到的状态问题。

由于此列表涉及的问题很可能在补丁和热修复中被更改，因此在更新后条目很可能不再正确。

所有条目目前均正确，截至 **热修复 33**。

## 状态

- 移动速度未减半。相反，移动消耗乘以 1.5。
- 当对角色执行任何未导致未命中的动作时，此状态会被移除，而不是在角色受到伤害时移除。

**[克雷斯卡的酸液滴落](Adrip_with_Kereska's_Acid_(Condition).md "克雷斯卡的酸液滴落 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[野性活力](Animalistic_Vitality_(Condition).md "野性活力 (状态)")**
|

- 该能力的游戏中描述不准确。实际治疗量为每回合 1d8⁠⁠[治疗](Healing.md "治疗")。
  - 治疗在战斗外也生效，甚至在回合制模式外也生效。在实时模式下，治疗每 6 秒应用一次。

**[奥术充能](Arcane_Charge_(Condition).md "奥术充能 (状态)")**
|

- 游戏中的工具提示根据效果的编码方式有些模糊，内容如下：_“当受威胁时，受影响实体的法术伤害有 +2 加值。”_ 然而，拥有奥术充能状态会对*任何* [受威胁](Threatened_(Condition).md "受威胁 (状态)") 的生物造成额外法术伤害；使用者不需要被威胁。

**[恶毒打击](Baneful_Strike_(Condition).md "恶毒打击 (状态)")**
|

- **恶毒打击**在持续时间内对*所有*豁免检定施加 1d4 惩罚，而不仅仅是攻击者的下一个法术。

**\_(状态)[昏沉](Befuddled_(Confusion_Ray)_(Condition).md "昏沉 (困惑射线) (状态)")**
|

- 此状态使用 [镇定](Pacified_(Condition).md "镇定 (状态)") (`PACIFYING_SPORES`) 而非 [昏沉](Befuddled_(Condition).md "昏沉 (状态)") (`TIMMASK_SPORES`) 作为父状态。因此，受影响的角色会被震慑，而不是表现得像被困惑一样。

**[魅惑](Beguiled_(Condition).md "魅惑 (状态)")**
|

- 此魅惑变体缺少正确的 [魅惑状态组](Charmed_(status_group).md), 因此不会被典型方式移除或阻止。

**[巴尔的恩赐](Bhaal's_Boon_(Condition).md "巴尔的恩赐 (状态)")**
|

- 此状态的层数在比预期更多的情况下被移除，这使得几乎不可能积累层数。
  - 当屠戮者身上的任何类型状态被移除时，层数都会减少。许多特性涉及频繁应用和移除隐藏的技术状态。特别是，每次使用 [额外攻击](Extra_Attack.md "额外攻击") 进行攻击都会涉及应用和移除跟踪额外攻击的隐藏技术状态。因此，仅仅攻击就会导致层数减少，通常在获得第一层后立即发生。

**[剑舞疗愈充能](Bladesong_Healing_Charge_(Condition).md "剑舞疗愈充能 (状态)")**
|

- 当使用装备的 [火焰刀](Flame_Blade.md "火焰刀") 攻击时，不会获得充能，除非它是由 [梅菲斯特提夫林](Mephistopheles_Tiefling.md "梅菲斯特提夫林") 召唤的。

**[轰鸣剑](Booming_Blade_(Condition).md "轰鸣剑 (状态)")**
|

- ⁠[雷鸣](Thunder.md "雷鸣") 伤害随*受影响生物*的伤害加值增加，而不是随最初施加轰鸣剑的角色的伤害加值增加。

**[火焰之息药水](Bottled_Breath_(Condition).md "火焰之息药水 (状态)")**
|

- 尽管工具提示说明如此，饮用此药水实际上允许你每长休无限次施放 [造风术](Gust_of_Wind.md "造风术")。

**[绑定武器](Bound_Weapon_(Condition).md "绑定武器 (状态)")**
|

- 此状态缺少 `Attributed(InventoryBound)` 代码，而该代码在 [魔契武器誓缚](Bind_Pact_Weapon.md "魔契武器誓缚") 和 [缚誓诅咒武器](Bind_Hexed_Weapon.md "缚誓诅咒武器") 上存在。虽然这样做（显然）是为了允许绑定武器被 [投掷攻击](Thrown.md "投掷攻击")，但它也有副作用，允许 [奥法骑士](Eldritch_Knight.md "奥法骑士") 将其绑定武器交给任何其他角色使用，并产生相同效果。因此，其他人可以装备绑定武器并像自己绑定了一样使用它，即使他们不是奥法骑士。例如，可以使用奥法骑士 [雇佣兵](Hireling.md "雇佣兵") 对武器施放 [武器绑定](Weapon_Bond.md "武器绑定")，将其交给另一个角色，然后将雇佣兵从活跃队伍中移除和/或解散。这样，任何队伍成员都可以使用绑定武器——直到下一次 [长休](Long_Rest.md "长休")。

**\_(状态)[魅惑](Charmed_(Charm_Animals_and_Plants)_(Condition).md "魅惑 (魅惑动植物) (状态)")**
|

- 描述完全错误。受影响的生物不会对魅惑者或其盟友变得友好；只有来自魅惑者或其盟友的伤害才会打破此状态。此状态的效果与 [魅惑](Charmed_(Condition).md "魅惑 (状态)") 相同，后者被用作父状态。
- [魅惑](Charmed_(Condition).md "魅惑 (状态)")（以及此状态）的效果是：无法攻击施法者。施法者在对话中进行 [魅力](Charisma.md "魅力") [属性检定](Ability_Check.md "属性检定") 时具有 [优势](Advantage.md "优势")。

**[碰撞鞋跟](Click_Heels_(Condition).md "碰撞鞋跟 (状态)")**
|

- 此状态实际上对受影响生物的 [反应](Actions.md#Reactions "动作") 攻击施加 [劣势](Disadvantage.md "劣势")，而不是对以它们为目标的反应攻击施加劣势。

**[强令对决](Compelled_to_Duel_(Condition).md "强令对决 (状态)")**
|

- 此状态使用 [强令对决](Compelled_Duel_(Condition).md "强令对决 (状态)") 作为父状态，但未更改对施法者以外的任何人施加劣势的检定。因此，攻击者将对*所有*目标（包括此效果的施法者）具有劣势。

**[克雷斯卡的冰霜导能](Conduit_of_Kereska's_Ice_(Condition).md "克雷斯卡的冰霜导能 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[克雷斯卡的闪电爆裂](Crackling_with_Kereska's_Lightning_(Condition).md "克雷斯卡的闪电爆裂 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[水晶皮肤](Crystal_Skin_(Condition).md "水晶皮肤 (状态)")**
|

- 此状态仅提供对 ⁠[火焰](Fire.md "火焰")、⁠[寒冷](Cold.md "寒冷") 和 ⁠[闪电](Lightning.md "闪电") 的抗性，而不是所有元素伤害类型。

**[诅咒：恐惧](Cursed_colon__Dread_(Condition).md "诅咒：恐惧 (状态)")**
|

- 由于编码错误，如果生物在豁免失败时跳过了上一回合，则不会跳过其当前回合。

**[卑劣优势](Dirty_Advantage_(Condition).md "卑劣优势 (状态)")**
|

- 当执行任何未导致未命中的动作时，此状态会被移除，而不仅仅是攻击。

**[伪装术](Disguise_Self_(Condition).md "伪装术 (状态)")**
|

- 伪装术会禁用需要 [至上真神的印记](Brand_of_the_Absolute.md "至上真神的印记") 才能触发的效果，例如 [威能手套](Gloves_of_Power.md "威能手套")。
- 截至补丁 5，热修复 17，通过使用 [变形生物面具](Mask_of_the_Shapeshifter.md "变形生物面具")，取下面具，然后在不移除伪装的情况下长休，可以给施法者种族装备加成超过预期时间。醒来后，伪装消失，但装备上的种族加成仍然影响角色。这只适用于种族装备加成，不适用于种族对话选项。
- 如果玩家角色在 [第一幕](Act_One.md "第一幕") 开始时的海滩上第一次与 [影心](Shadowheart.md "影心") 对话时伪装成 [吉斯洋基人](Githyanki.md "吉斯洋基人")，则会获得额外 30 经验值。
- 如果 [伙伴](Companions.md "伙伴") 在 [营地](Campsite.md "营地") 时处于伪装状态，当选择另一个伙伴或玩家角色时，他们将停留在上次放置的位置，而不是自动返回帐篷，直到他们再次移动或进行 [长休](Resting.md#Long_rest "长休")。这在寻求对有限半径施加 [状态](Conditions.md "状态") 或 [法术](Spells.md "法术")（例如 [支援术](Aid.md "支援术")）时非常有用。
- 伪装时，无法与 [雇佣兵](Hirelings.md "雇佣兵") 对话。

**[树精的祝福](Dryad's_Blessing_(Condition).md "树精的祝福 (状态)")**
|

- 由于脚本错误，此状态不会添加到角色身上。

**[自由行动药水](Elixir_of_Guileful_Movement_(Condition).md "自由行动药水 (状态)")**
|

**[冷冻](Encrusted_with_Frost_(Condition).md "冷冻 (状态)")**
|

- 游戏中的描述不完全正确：在 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定") 的 [DC](Dice_rolls.md#Save_DCs "掷骰") 12 上失败会导致实体变为 [冰冻](Frozen_(Condition).md "冰冻 (状态)")，而成功则使其受到 1d4⁠⁠[寒冷](Cold.md "寒冷") 伤害。与描述所述相反，此伤害不会减半。

**[正义之敌](Enemy_of_Justice_(Condition).md "正义之敌 (状态)")**
|

- 可能永久存在于触发它的角色身上，即使在没有剩余“目击者”守卫的幕中。

**[暴露啃咬](Exposing_Bite_(Condition).md "暴露啃咬 (状态)")**
|

- 此状态在 3 米（10 英尺）内对受影响生物进行任何攻击掷骰后移除，但重击仅在 2 米（7 英尺）内进行时才适用。这意味着当使用 [额外范围](Extra_Reach.md "额外范围") 武器从最大范围攻击受影响生物时，效果将被浪费。

**[极端孤注一掷](Fierce_Perilous_Stakes_(Condition).md "极端孤注一掷 (状态)")**
|

- 可以对同一目标多次施放此效果，以同时应用多个状态实例。每次应用的重击阈值降低、额外伤害和治疗效果都会相互叠加。伤害易伤不会以这种方式叠加。

**[导力](Force_Conduit_(Condition).md "导力 (状态)")**
|

- 应用力场伤害的隐藏技术状态也会对敌方目标触发 [奥术共振](Arcane_Echomalefaction.md "奥术共振") 和 [寒意外溢](Coldbrim_Chill.md "寒意外溢")。

**[开放伤口](Gaping_Wounds_(Condition).md "开放伤口 (状态)")**
|

- 2⁠⁠[穿刺](Piercing.md "穿刺") 伤害不会触发需要穿刺伤害的效果，例如 [预言：小小一刺](Prophecy_colon__A_Little_Prick_(Condition).md "预言：小小一刺 (状态)")，因为对敌人造成的穿刺伤害来自施加在*敌人*身上的被动效果，而不是来自攻击者，而攻击者是触发此类效果所必需的。
- 荣誉模式将此状态的效果更改为简单的 +2 伤害掷骰，以确保它不会触发 [伤害附加](Damage_rider.md "伤害附加")。这导致它采用攻击的原始伤害类型，而不是总是造成 +2 穿刺伤害。
  - 此附加伤害也缺少对攻击掷骰的检查，因此会添加到*任何*伤害来源。

**[嘲弄](Goaded_(Condition).md "嘲弄 (状态)")**
|

- 尽管说明被嘲弄的敌人会攻击施法者，但敌人的 AI 完全没有改变，如果敌人离开攻击范围，可能不会优先攻击嘲弄的生物。
- 此状态的工具提示说明它有感知豁免，但不存在这样的回合内豁免检定。
- 受此状态影响的角色在*所有*攻击掷骰上具有劣势，即使是对状态来源的攻击也是如此。

**[蛛网墓穴](Gossamer_Tomb_(Condition).md "蛛网墓穴 (状态)")**
|

- 由于拼写错误，此状态实际造成 10d8⁠⁠[中毒](Poison.md "中毒") 伤害，而不是 8d10⁠⁠[中毒](Poison.md "中毒") 伤害。

**[攫取精华](Grasp_Essence_(Condition).md "攫取精华 (状态)")**
|

- 由于编码错误，如果持有者受到伤害且没有任何临时生命值，攫取精华将从持有者身上移除。

**[克雷斯卡的火焰擒握](Gripped_by_Kereska's_Flame_(Condition).md "克雷斯卡的火焰擒握 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[加速](Hastened_(Condition).md "加速 (状态)")**
|

- 游戏中的描述说它使移动速度加倍，但实际上它增加了 9 米 / 30 英尺。

**[灼热](Heat_(Condition).md "灼热 (状态)")**
|

- 根据灼热状态的来源，某些伤害附加（例如 [闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")、来自 [无情光芒之戒](Callous_Glow_Ring.md "无情光芒之戒") 的光耀伤害和 [灵能过载](Psionic_Overload.md "灵能过载")）会增加角色每回合受到的伤害。

**[霍慈的烈酒：口臭](Hoots'_Hooch_colon__Bad_Breath_(Condition).md "霍慈的烈酒：口臭 (状态)")**
|

- **霍慈的烈酒：口臭**存在错误。敌人不会获得恶心效果。相反，当拥有霍慈的烈酒：口臭的角色受到近战攻击时，该角色会进行一次体质豁免以对抗“%%% Empty”。

**[精通诗人激励](Improved_Bardic_Inspiration_(Condition).md "精通诗人激励 (状态)")**
|

- 由于编码错误，此状态还授予诗人激励资源和 d6 诗人激励的反应。使用其中一个反应会消耗诗人激励充能，但不会移除精通诗人激励状态，使非吟游诗人角色在状态结束前拥有一个空的、不可补充的诗人激励充能槽。

**[地狱狂怒](Infernal_Fury_(Condition).md "地狱狂怒 (状态)")**
|

- 卡菈克在使用 [徒手打击](Unarmed_Strike.md "徒手打击") 时，当 [地狱狂怒](Infernal_Fury_(Condition).md) 增益激活时，会造成*两*次额外的 1d4⁠⁠[火焰](Fire.md "火焰") 伤害（总计 2d4）。无论她的职业、狂暴状态和当前生命值如何，她都会造成此额外伤害。
- 卡菈克在进行武器攻击时，如果处于狂暴状态*或*生命值低于 25%，则会造成一次额外的 1d4⁠⁠[火焰](Fire.md "火焰") 伤害。
  - 这会与自身叠加，意味着当她处于 [狂暴](Rage_(Condition).md "狂暴 (状态)") 且生命值低于 25% 时进行武器攻击，将造成*两*次额外的 1d4⁠⁠[火焰](Fire.md "火焰") 伤害（总计 2d4）。

**[地狱震慑](Infernal_Stun_(Condition).md "地狱震慑 (状态)")**
|

- 工具提示说明它需要敏捷豁免，但实际上它需要感知豁免。

**[直觉魅惑：未受影响](Instinctive_Charm_colon__Unaffected_(Condition).md "直觉魅惑：未受影响 (状态)")**
|

- 由于缺少 `StatusPropertyFlag`，此状态在长休时不会被移除，并且会无限期保留。

**[闪电释能](Lightning_Blast_(Condition).md "闪电释能 (状态)")**
|

- 应用闪电伤害的隐藏技术状态也会对敌方目标触发 [奥术共振](Arcane_Echomalefaction.md "奥术共振") 和 [寒意外溢](Coldbrim_Chill.md "寒意外溢")。

**[闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")**
|

- 应用闪电伤害的隐藏技术状态也会对敌方目标触发 [奥术共振](Arcane_Echomalefaction.md "奥术共振") 和 [寒意外溢](Coldbrim_Chill.md "寒意外溢")。

**[爱之守护](Love_Protects_(Condition).md "爱之守护 (状态)")**
|

- 由于脚本错误，此状态不会应用于角色。

**[魔法感知](Magic_Awareness_(Condition).md "魔法感知 (状态)")**
|

- 游戏中的描述不准确。它说：“野蛮人和 3 米（10 英尺）内的所有生物在对抗法术的豁免检定中添加其熟练项加值。”实际上，加值是 1d4，并且它适用于*所有*豁免检定，而不仅仅是对抗法术。

**[魔法感知灵光](Magic_Awareness_Aura_(Condition).md "魔法感知灵光 (状态)")**
|

- 游戏中的描述不准确。它说：“在对抗法术的豁免检定中添加其熟练项加值。”实际上，加值是 1d4，并且它适用于*所有*豁免检定，而不仅仅是对抗法术。

**[致残](Maimed_(Condition).md "致残 (状态)")**
|

- 此状态缺少正确的 [状态组](Status_groups.md "状态组")，例如 [SG_Restrained](SG_Restrained.md "SG 束缚")，因此可以应用于拥有 [行动自如](Freedom_of_Movement_(Condition).md "行动自如 (状态)") 的生物。

**[亢奋](Momentum_(Condition).md "亢奋 (状态)")**
|

- 由于 `StatusHasStatusGroup()` 检查编码错误，除了 [减速](Slowed_(Condition).md "减速 (状态)") 之外的任何状态都无法提前移除亢奋。

**[月母之拥](Moonmother's_Embrace_(Condition).md "月母之拥 (状态)")**
|

- 尽管工具提示说明它授予 100⁠⁠[治疗](Healing.md "治疗")，但它实际上授予 100 [临时生命值](Temporary_Hit_Points.md "临时生命值")。

**[黯蚀灵光](Necrotic_Aura_(Condition).md "黯蚀灵光 (状态)")**
|

- 如果盖尔从 [倒地](Downed_(Condition).md "倒地 (状态)") 状态（不是 [死亡](Dead_(Condition).md "死亡 (状态)")）被 [回生术](Revivify.md "回生术")、[回生术卷轴](Scroll_of_Revivify.md "回生术卷轴") 或 [完全复生术卷轴](Scroll_of_True_Resurrection.md "完全复生术卷轴") 复活，他会在战斗中下一回合开始时（或在战斗外 6 秒后）获得黯蚀灵光，尽管他因可能编码错误的 [脚本](https://bg3.norbyte.dev/search?id=GLO_Origin_Gale_Death) 而活着。

**[有毒烟雾](Noxious_Fumes_(Condition).md "有毒烟雾 (状态)")**
|

- 对附近生物造成的 ⁠[中毒](Poison.md "中毒") 伤害随*受影响生物*的伤害加值增加，而不是随最初施加有毒烟雾的角色的伤害加值增加。

**[偏执梦境](Paranoid_Dreams_(Condition).md "偏执梦境 (状态)")**
|

- 如果 [观察者眼魔](Spectator.md "观察者眼魔") 成为 [道恩](Dhourn.md "道恩") 施放的 [魔法护甲](Mage_Armour.md "魔法护甲") 的目标，偏执梦境会增加。

**[孤注一掷](Perilous_Stakes_(Condition).md "孤注一掷 (状态)")**
|

- 可以在同一角色上叠加多次，提供多次治疗而没有任何额外负面效果。

**[魅影之力](Phantasmal_Force_(Condition).md "魅影之力 (状态)")**
|

- 工具提示错误地说明目标进行 [感知](Wisdom.md "感知") [豁免检定](Saving_throw.md "豁免检定")。

**[拘束](Pinched_(Condition).md "拘束 (状态)")**
|

- 此状态的描述错误地说明每回合造成 2⁠⁠[穿刺](Piercing.md "穿刺") 伤害，但实际正确造成 1d4⁠⁠[穿刺](Piercing.md "穿刺") 伤害。

**[预言：布施](Prophecy_colon__Delivering_Alms_(Condition).md "预言：布施 (状态)")**
|

- 此预言无法完成，因为它引用了游戏中不存在的被动技能。

**[预言：博学](Prophecy_colon__Well-Read_(Condition).md "预言：博学 (状态)")**
|

- 此预言只能在通过库存从卷轴学习法术时完成。在“学习更多法术”窗口中学到的法术无效。

**[防护善恶](Protection_from_Evil_and_Good_(Condition).md "防护善恶 (状态)")**
|

- 描述错误地说明它授予对 [魅惑](Charmed_(status_group).md) 状态的免疫，但这不是真的。
- 描述还错误地说明对恐慌和附身的免疫仅针对列出的生物类型；实际上，它针对任何来源，而不仅仅是列出的生物类型。

**[灵能探测：警报激活](Qua'nith_colon__Alert_Active_(Condition).md "灵能探测：警报激活 (状态)")**
|

- 此状态在角色对实体执行的下一个动作/能力时被移除，无论该动作/能力是否有攻击掷骰。

**\_(状态)[狂暴](Rage_(Boar)_(Condition).md "狂暴 (野猪) (状态)")**
|

- 尽管此特定状态的工具提示说明如果野蛮人自上一回合以来未攻击敌人或受到伤害，狂暴会提前结束，但它不会。

**[撕裂血肉](Rended_Flesh_(Condition).md "撕裂血肉 (状态)")**
|

- 工具提示错误地声称它会阻挡临时生命值，但它实际上不会阻挡游戏中使用的任何特定临时生命值来源。

**[残响](Reverberation_(Condition).md "残响 (状态)")**
|

- 尽管有描述，但不存在阻止雷鸣免疫生物接收残响的机制。
- 在实时模式下，应用 5 层或更多层时描述的效果都不会发生，但持续时间仍限制为 5 回合。
- 如果 [倒地](Prone_(Condition).md "倒地 (状态)") 的豁免检定触发任何需要确认的反应，则倒地不会被应用，并且无论结果如何或是否选择了任何反应，豁免检定都不会记录在战斗日志中。如果豁免检定由多个残响来源引起，则可能会出现多个连续的确认提示，而不是一个，并且缺少命名相关实体的文本行。

**[克雷斯卡的雷鸣轰隆](Rumbling_with_Kereska's_Thunder_(Condition).md "克雷斯卡的雷鸣轰隆 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[裂地](Ruptured_(Condition).md "裂地 (状态)")**
|

- 某些伤害附加（例如 [闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")、来自 [无情光芒之戒](Callous_Glow_Ring.md "无情光芒之戒") 的光耀伤害和 [灵能过载](Psionic_Overload.md "灵能过载")）会增加角色移动时受到的自我伤害。

**\_(状态)[暗影灌注](Shadow_Infusion_(Accursed_Spectre)_(Condition).md "暗影灌注 (诅咒幽鬼) (状态)")**
|

- 此状态的描述错误地说明它提供 [紧随其后](Right_Behind_You.md "紧随其后") 反应。它没有，而是提供 [裂影](Splinter_Shadow.md "裂影") 反应。

**[莎尔信徒惩戒](Sharran_Retribution_(Condition).md "莎尔信徒惩戒 (状态)")**
|

- 1d4⁠⁠[黯蚀](Necrotic.md "黯蚀") 伤害仅在施法者装备 [暗夜法官半身甲（非常稀有）](Dark_Justiciar_Half-Plate_(Very_Rare).md "暗夜法官半身甲（非常稀有）") 时应用，如果施法者装备 [暗夜法官半身甲（稀有）](Dark_Justiciar_Half-Plate_(Rare).md "暗夜法官半身甲（稀有）")，则仅应用伤害减免。

**[抗性外壳](Shell_of_Resistance_(Condition).md "抗性外壳 (状态)")**
|

- 戈塔什在非硬核难度下也对火焰免疫，尽管工具提示如此。

**[歌唱之剑：尖叫](Singing_Sword_colon__Shriek_(Condition).md "歌唱之剑：尖叫 (状态)")**
|

- 游戏中的工具提示指定尖叫对精神 [豁免检定](Saving_throw.md "豁免检定") 施加惩罚，但它实际上对所有豁免检定*和*攻击掷骰都施加惩罚。

**[歌唱之剑：尖叫](Singing_Sword_colon__Shrieking_(Condition).md "歌唱之剑：尖叫 (状态)")**
|

- 游戏中的工具提示指定尖叫对精神 [豁免检定](Saving_throw.md "豁免检定") 施加惩罚，但它实际上对所有豁免检定*和*攻击掷骰都施加惩罚。
- 1d4⁠⁠[雷鸣](Thunder.md "雷鸣") 伤害不会触发需要雷鸣伤害的物品或效果，例如 [风暴之子力量帽](Hat_of_Storm_Scion's_Power.md "风暴之子力量帽")、[天崩手套](Gloves_of_Belligerent_Skies.md "天崩手套") 或 [预言：雷鸣掌声](Prophecy_colon__Thunderous_Applause_(Condition).md "预言：雷鸣掌声 (状态)")，无论触发伤害的角色是否拥有该物品/效果，或者是激活 [生离死别：尖叫](Phalar_Aluve_colon__Shriek.md "生离死别：尖叫") 的角色。这是因为对敌人造成的雷鸣伤害来自施加在*敌人*身上的被动效果，而不是来自攻击者，而攻击者是触发任何此类物品或效果所必需的。
- 此效果在*荣誉*难度下被更改，并按预期运行。

**[歌唱之剑：吟唱](Singing_Sword_colon__Singing_(Condition).md "歌唱之剑：吟唱 (状态)")**
|

- 工具提示指定“精神” [攻击掷骰](Attack_roll.md "攻击掷骰") 和 [豁免检定](Saving_throw.md "豁免检定")，但加值实际上适用于所有攻击掷骰和豁免检定。

**[歌唱之剑：歌曲增益](Singing_Sword_colon__Song_(Condition).md "歌唱之剑：歌曲增益 (状态)")**
|

- 工具提示指定“精神” [攻击掷骰](Attack_roll.md "攻击掷骰") 和 [豁免检定](Saving_throw.md "豁免检定")，但加值实际上适用于所有攻击掷骰和豁免检定，而不仅仅是精神的。

**[减速](Slowed_(Condition).md "减速 (状态)")**
|

- [缓慢术：施法](Slow_colon__Casting.md "缓慢术：施法") 无法运行，被减速生物施放的法术永远不会被延迟。
- [缓慢术：动作](Slow_colon__Actions.md "缓慢术：动作") 不会阻止生物进行多次攻击，除非它们在自己的回合攻击之间以某种方式被减速。

**[灵魂烙印](Soul_Branding_(Condition).md "灵魂烙印 (状态)")**
|

- 游戏中的工具提示说明效果提供 1.5 米（5 英尺）的移动速度加值，但实际上是 5 米（17 英尺）。
- 当应用于具有 [投掷攻击](Thrown.md "投掷攻击") 属性的武器时，效果在通过 [投掷](Throw.md "投掷") 攻击击中敌人时不会丢失，并且会持续整个持续时间。伤害仍然会添加。

**[疾风迅捷](Swift_as_Wind_(Condition).md "疾风迅捷 (状态)")**
|

- 此状态仅在进行命中敌人的武器攻击时移除，而不是在下一次攻击掷骰时移除。

**[共生实体](Symbiotic_Entity_(Condition).md "共生实体 (状态)")**
|

- 尽管工具提示说此能力仅影响近战武器攻击，但它也影响远程武器攻击。

**\_(状态)[临时生命值](Temporary_Hit_Points_(Ever_Vigilant)_(Condition).md "临时生命值 (保持戒备) (状态)")**
|

- 与其他临时生命值不同，**保持戒备**授予的临时生命值在战斗结束时消失。此功能未在描述中说明。

**[受威胁](Threatened_(Condition).md "受威胁 (状态)")**
|

- 当攻击非常大的目标时，例如 [受控红龙](Dominated_Red_Dragon.md "受控红龙")，其多个部分可能同时威胁攻击者，就像被多个敌人包围一样，导致所有远程攻击具有劣势。这使得 [强弩专家：近距平射](Crossbow_Expert_colon__Point-Blank.md "强弩专家：近距平射") 对此类目标无效。

**[混沌之潮](Tides_of_Chaos_(Condition).md "混沌之潮 (状态)")**
|

- 当通过 [混沌之潮](Tides_of_Chaos_(passive_feature).md "混沌之潮 (被动特性)") 应用时，此状态在长休时*不*会被移除，尽管工具提示如此。当通过混沌之潮反应应用时，此状态在长休时会被正确移除。

**[点泥成金](Transmuted_To_Steel_(Condition).md "点泥成金 (状态)")**
|

- 与工具提示所述相反，点泥成金不会降低移动速度。激活 [点泥成金](Muck_to_Metal.md "点泥成金") 能力确实会消耗移动速度，但仅在激活时消耗；在激活后的后续回合中，会保留完整的移动速度。

**[防护不死生物灵光](Undead_Ward_Aura_(Condition).md "防护不死生物灵光 (状态)")**
|

- 尽管工具提示中未说明，但**防护不死生物**适用于具有 [邪魔](Fiend.md "邪魔") 分类的召唤物，例如 [铲子](Shovel_(familiar).md "铲子 (魔宠)")、[坎比翁（异界誓盟）](Cambion_(Planar_Ally).md "坎比翁（异界誓盟）") 和 [魔宠：小魔鬼](Conjured_Imp.md "魔宠：小魔鬼")。

**[克雷斯卡的毒素容器](Vessel_for_Kereska's_Poison_(Condition).md "克雷斯卡的毒素容器 (状态)")**
|

- 附加伤害仅基于所用动作的 `DamageType` 标志添加。它*不*实际检查该动作是否为法术。

**[水层防护](Water_Layer_Protection_(Condition).md "水层防护 (状态)")**
|

- 描述错误地使用了与 [潮湿](Wet_(Condition).md "潮湿 (状态)") 相同的描述，尽管这两种状态具有不同的效果。

**[愤怒之灵](Wrathful_Spirits_(Condition).md "愤怒之灵 (状态)")**
|

- 由于编码错误，此状态不会提供对 ⁠[力场](Force.md "力场") 伤害的易伤。

---
*Source: [List of bugged conditions](https://bg3.wiki/wiki/List_of_bugged_conditions)*