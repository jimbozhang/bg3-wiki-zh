# 受惊 (状态)

**受惊**

- 无法采取 [动作](Actions.md#Resources "动作") 或 [反应](Actions.md#Reactions "动作")。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `SURPRISED` [持续时间结束](Conditions.md#Duration "状态"): 回合结束

[更多属性](Status_properties.md "状态属性"):

- [OverheadOnTurn](Status_properties/OverheadOnTurn.md "状态属性/OverheadOnTurn")

## 受惊的来源

*维基数据库中未定义*

## 拥有受惊状态的生物

*维基数据库中未定义*

## 拥有相同堆叠ID的状态

| 状态 | 效果 |
| --- | --- |
| 受惊 | 无法采取 [动作](Actions#Resources.md#Resources "动作") 或 [反应](Actions#Reactions.md#Reactions "动作")。 |

受惊是一种特殊的 [状态](Conditions.md "状态"), 可在战斗的第一回合影响 [生物](List_of_creature_types.md "生物类型列表")。

## 概述

当战斗遭遇的一方未察觉另一方时，他们可能会 _受惊_。一个 _受惊_ 的生物在一回合内无法采取任何 [动作](Action.md "动作") 或 [反应](Reaction.md "反应")。拥有 [警觉](Alert.md "警觉") 专长、[野性直觉](Feral_Instinct.md "野性直觉") 特性或特定物品（如 [警觉灵药](Elixir_of_Vigilance.md "警觉灵药")）的角色不会 _受惊_。

某些战斗遭遇，尤其是在游戏内过场动画之后发生的遭遇，被设定为总是让队伍受惊。通常可以通过利用上述特性或状态（如 [隐形](Invisible_(Condition).md "隐形 (状态)")）或在触发遭遇前使用 [黑暗术](Darkness.md "黑暗术") 等法术隐藏在重度遮蔽区域来应对。

## 如何让敌人受惊

让敌人受惊的关键是视线：他们必须对让其受惊的角色有清晰的视线。如果没有，那么他们会开始搜索该角色，并且一旦找到他们并开始战斗，就不会 _受惊_。

这使得成功让一群敌人受惊变得具有挑战性和反直觉。以下预防措施可能有助于此过程：

1. 使用 [躲藏](Hide.md "躲藏") 让 _整个_ 队伍进入隐匿状态，包括宠物。
2. 解散队伍，包括宠物，然后选择一名队伍成员作为伏击者，并将其移动到触发受惊的位置。
| 状态 | 效果 |
| --- | --- |
| 受惊 | 无法采取 [动作](Actions#Resources.md#Resources "动作") 或 [反应](Actions#Reactions.md#Reactions "动作")。 |
3. 伏击者 _必须_ 从敌人的视线范围内发起战斗。如果这样做，敌人应该会受惊。然而，如果他们在视线范围之外，敌人会开始搜索队伍成员，并且一旦找到他们并开始战斗，就不会 _受惊_。
4. 战斗开始的方式很重要。以下是一些关键点（但测试尚未详尽）：
   1. 近战攻击总是有效。
   2. 在近战范围内进行的远程攻击总是有效。
   3. 法术攻击规则要么有错误，要么很复杂。法术攻击在近战范围内几乎总是有效，在非近战范围内则较少。以下示例展示了差异：
      1. [魔能爆](Eldritch_Blast.md "魔能爆")（攻击掷骰）在近战和非近战范围内都有效。
      2. [火球术](Fireball.md "火球术")（敏捷豁免）在近战范围内有效，但在非近战范围内无效。
      3. [恐惧](Fear.md "恐惧")（感知豁免）在近战和非近战范围内都有效。
      4. [魔法飞弹](Magic_Missile.md "魔法飞弹")（无攻击掷骰）在近战和非近战范围内都无效。
      5. [巫术箭](Witch_Bolt.md "巫术箭")（攻击掷骰）在近战范围内有效，但在非近战范围内无效。
5. 如果攻击类型（近战、远程、法术）有效，那么是否命中并不重要。
6. [手雷](Grenades.md "手雷") 无效，即使你直接击中敌人。
7. 对于 [伏击](Ambushing_(Condition).md "伏击 (状态)") 的敌人，每种攻击类型，甚至手雷，都有效，只要敌人尚未发现队伍。即使 [察觉技能](Perception.md "察觉技能") 检定失败并攻击敌人当前所在位置的空地，也是如此。
8. 一旦敌人受惊，其余队伍成员可以移动到位置加入战斗。一旦他们进入敌人的视野锥或攻击敌人，就会被拉入战斗。

如果角色的隐匿值足够高，敌人有时即使其盟友在远处被攻击和杀死，也无法注意到他们。这甚至可以与 [火球术](Fireball.md "火球术") 等范围效果法术一起使用，只要施法的队伍成员保持隐藏。敌人会四处奔跑，拼命搜索队伍成员但无法找到他们。这可以通过高 [敏捷](Dexterity.md "敏捷") 分数、[熟练项](Proficiency.md "熟练项") 和 [专精](Expertise.md "专精") 隐匿、[优势](Advantage.md "优势") 敏捷或隐匿检定，以及某些法术和能力（如 [行动无踪](Pass_Without_Trace.md "行动无踪")）来实现。

### 从隐形状态触发受惊

让敌人受惊最可靠的方法是变为隐形并攻击他们。这种隐形可以来自任何来源（例如 [隐形药水](Potion_of_Invisibility.md "隐形药水")、[隐形术](Invisibility_(spell).md "隐形术")、[高等隐形术](Greater_Invisibility.md "高等隐形术") 或 [魔索布莱城之影](Shadow_of_Menzoberranzan.md "魔索布莱城之影")）。[夸塞魔](Quasit.md "夸塞魔") 和 [小魔鬼](Imp.md "小魔鬼") 宠物也有效，[荒野形态：黑豹](Wild_Shape_colon__Panther.md "荒野形态：黑豹") 也有效。

## 受惊遭遇列表

### 第一幕

- 潜入 [蔓生废墟 卧室](Overgrown_Ruins.md#Refectory "蔓生废墟") 会让 [安东](Andorn.md "安东") 受惊。
- 接近 [纳迪拉](Nadira.md "纳迪拉") 会让试图伏击她的 [熊地精刺客](Bugbear_Assassin.md "熊地精刺客") 受惊。
- 与 [药剂师地窖](Apothecary's_Cellar.md "药剂师地窖") 内洞穴中的某些棺材互动会导致 [机敏的守卫者](Agile_Guardian.md "机敏的守卫者") 突然出现并让队伍受惊。
- 攻击 [复生之路](Risen_Road.md "复生之路") 沿线肿胀的 [鬣狗](Hyena.md "鬣狗") 会让它们受惊。
- 在 [幽暗地域](Underdark.md "幽暗地域")，接近 [石化战场](Underdark.md#Petrified_Battlefield "幽暗地域") 会与 [观察者眼魔](Spectator.md "观察者眼魔") 发起战斗，触发过场动画，让队伍成员受惊。
- 接近 [幽暗地域海滩](Underdark.md#Beach "幽暗地域海滩") 会触发与灰矮人的对话。如果立即攻击，海滩上的所有灰矮人都会受惊。如果 [格克·煤球](Gekh_Coal.md "格克·煤球") 被召唤并变得敌对，队伍成员反而会受惊。
- 在 [复仇之炉](Grymforge.md "复仇之炉")，攻击三个 [拟形怪](Mimic.md "拟形怪") 在伪装形态下互动时总是会让队伍成员受惊。从远程攻击它们会开始战斗而不会受惊。
- [岩浆魔蝠](Magma_Mephit.md "岩浆魔蝠") 如果接近最靠近 [精金熔炉](Adamantine_Forge_(location).md) 的秘银矿脉，会让队伍成员受惊。

### 第二幕

- 在 [幽影诅咒之地](Shadow-Cursed_Lands.md "幽影诅咒之地")，与 [枯萎术](Blight_(race).md) 的三次单独遭遇如果队伍成员靠得太近，可能会让他们受惊。
- 在 [月出之塔](Moonrise_Towers.md "月出之塔")，攻击 [拟形怪](Mimic.md "拟形怪") 在伪装形态下互动时总是会让队伍成员受惊。从远程攻击它们会开始战斗而不会受惊。
- 在 X: -43 Y: 7 的 [废弃战场](Ruined_Battlefield.md "废弃战场") 遇到的 [鬾魊](Meazel.md "鬾魊") 如果未通过 DC 18 察觉检定，会让队伍受惊。

### 第三幕

- 在 [终末马戏团](Circus_of_the_Last_Days.md "终末马戏团") 的 "[德里布斯](Dribbles.md "德里布斯")" 表演结束时，除非通过被动 [察觉技能](Perception.md "察觉技能") 检定注意到伏击，否则队伍成员会受惊，此时伏击者反而会受惊。
- 在 [丹瑟隆的飞斧](Danthelon's_Dancing_Axe.md "丹瑟隆的飞斧") 的 [恩萨尔的地下室](Entharl's_basement.md "恩萨尔的地下室") 中，为 [高阶竖琴手](The_High_Harper.md "高阶竖琴手") 任务，可以与一群伪装成竖琴手的 [变形怪](Doppelganger.md "变形怪") 对话。对话检定和选择的组合可能导致队伍成员或伏击者受惊。

---
*Source: [Surprised (Condition)](https://bg3.wiki/wiki/Surprised_(Condition)*