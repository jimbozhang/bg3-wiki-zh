# 倒伏 (状态)

另见 [倒伏 (状态类型)](Prone_(Condition_Type).md)

**倒伏**

- 受影响的生物无法移动或进行 [动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作") 或 [反应](Actions.md#Reactions "反应"），并且在 [力量](Strength.md "力量") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 上具有 [劣势](Disadvantage.md "劣势")。
- 在距离生物 3 米（10 英尺）范围内进行的攻击对倒伏生物具有 [优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的 [移动速度](Movement_speed.md "移动速度") 才能站起。
  - 拥有 [运动员](Athlete.md "运动员") 专长的角色仅需花费 1.5 米（5 英尺）的移动速度即可站起。

[倒伏](Prone_(status_group).md), [昏迷](Unconscious_(status_group).md)

## 属性

[状态组](Status_groups.md "状态组"): [SG_Prone](SG_Prone.md "SG 倒伏"), [SG_Condition](SG_Condition.md "SG 状态"), [SG_Unconscious](SG_Unconscious.md "SG 昏迷")

[持续时间结束](Conditions.md#Duration "状态"): 回合开始时

[更多属性](Status_properties.md "状态属性"):

- [IgnoredByImmobilized](Status_properties/IgnoredByImmobilized.md "状态属性/IgnoredByImmobilized")
- [InitiateCombat](Status_properties/InitiateCombat.md "状态属性/InitiateCombat")
- [DisableOverhead](Status_properties/DisableOverhead.md "状态属性/DisableOverhead")

## 备注

- 如果生物在回合 *开始时* 变为倒伏状态，它会使用一半的可用移动速度站起。如果生物在回合 *期间* 被击倒，其回合将自动结束。
  - 执行 [协助](Help.md "协助") 动作可以移除倒伏状态，即使是在同一回合的早些时候获得的，这实际上可以“取消跳过”该角色的回合并允许其正常行动。专注状态仍会被打破。
- 击倒生物并使其移动速度降至 50% 以下不会自动跳过其下一回合，因为生物会使用其 *可用* 移动速度的 50% 来站起。
- 一些生物对倒伏状态免疫，包括没有实体的生物（例如 [暗影](Shadow.md "暗影") 和 [缚灵](Wraith.md "缚灵")）。
- [塔莎狂笑术](Tasha's_Hideous_Laughter.md "塔莎狂笑术") 会使目标遭受 [狂笑](Hideous_Laughter_(Condition).md)，其效果与倒伏相同，但技术上不被视为倒伏。因此，该法术的效果无法用 [协助](Help.md "协助") 移除。
- 变为倒伏会立即结束 [专注](Concentration.md "专注")。

## 倒伏来源

### 无限持续时间

以下倒伏来源会无限期地施加该状态。如果受影响的生物花费移动速度站起，仍可移除该状态。但是，如果生物无法移动（例如受到 [诱捕](Ensnared_(Condition).md "诱捕 (状态)")、[网缚](Enwebbed_(Condition).md "网缚 (状态)")、[恐慌](Frightened_(Condition).md "恐慌 (状态)")、[严重超重](Heavily_Encumbered_(Condition).md "严重超重 (状态)")、[跛足](Maimed_(Condition).md "跛足 (状态)") 和 [束缚](Restrained_(Condition).md "束缚 (状态)") 等状态影响），它将无限期保持倒伏状态。

- [清流鞭：击倒](Water_Whip_colon__Knock_Prone.md "清流鞭：击倒")
- [摔绊攻击（远程）](Trip_Attack_(Ranged).md "摔绊攻击（远程）")

### 两回合持续时间

两回合是倒伏效果的典型持续时间。由于倒伏的持续时间在受影响生物的回合开始时递减，因此 2 回合的持续时间实际上相当于 1 轮。具体行为如下：

- 在受影响生物的回合开始时，剩余持续时间递减至 1 回合。
- 如果受影响生物可以花费移动速度，它会这样做并站起，剩余的倒伏回合将被移除。
  - 如果无法花费移动速度，它将保持倒伏状态并跳过其回合。在这种情况下，在下一回合开始时，生物会花费一半的移动速度（如果可能）并站起，然后移除倒伏状态。
- 如果倒伏是由某些来源引起的，例如 [凶蛮跳跃](Brutal_Leap.md "凶蛮跳跃")、[原始践踏](Primal_Stampede.md "原始践踏")、[残响](Reverberation_(Condition).md "残响 (状态)") 或 [投掷](Throw.md "投掷")，则在状态结束前无法将持续时间 1 增加到 2，这通常意味着直到下一回合。对于其他一些来源，例如 [冰](Ice_(surface).md "冰 (地表)")，可以施加一个持续时间为 2 的独立倒伏状态。

以下来源的持续时间为 2 回合：

- [粘稠之鞭](Adhesive_Whip.md "粘稠之鞭")
- [摔翻打击](Backbreaker.md "摔翻打击")
- [啃咬（剑齿虎）](Bite_(Sabre-Toothed_Tiger).md "啃咬（剑齿虎）")
- [野猪冲撞](Boar_Charge.md "野猪冲撞")
- [凶蛮跳跃](Brutal_Leap.md "凶蛮跳跃")
- [冲锋（地底洛斯兽）](Charge_(Deep_Roth%C3%A9).md "冲锋（地底洛斯兽）")
- [冲锋（牛头人）](Charge_(Minotaur).md "冲锋（牛头人）")
- [粉碎跃击](Crushing_Flight.md "粉碎跃击")
- [死亡之跃](Deadly_Leap.md "死亡之跃")
- [俯冲突袭](Diving_Strike.md "俯冲突袭")
- [雷地拳](Grounded_Thunder_Strike.md "雷地拳")
- [斥力爆](Impulse_Blast.md "斥力爆")
- [铁意追击](Ironbound_Pursuit.md "铁意追击")
- [飞扑啃咬](Lunging_Bite.md "飞扑啃咬")
- [多重攻击（枭熊）](Multiattack_(Owlbear).md "多重攻击（枭熊）")
- [猛扑](Pounce.md "猛扑")
- [猛扑（分支龙）](Pounce_(Alioramus).md "猛扑（分支龙）")
- [猛扑（双脊龙）](Pounce_(Dilophosaurus).md "猛扑（双脊龙）")
- [猛扑（恐爪怪）](Pounce_(Hook_Horror).md "猛扑（恐爪怪）")
- [原始践踏](Primal_Stampede.md "原始践踏")
- [撼地](Quake.md "撼地")
- [无情猛扑](Relentless_Lunge.md "无情猛扑")
- [残响](Reverberation_(Condition).md "残响 (状态)")
- [罗兰的雷鸣波](Rolan's_Thunderwave.md "罗兰的雷鸣波")
- [急冲（野猪）](Rush_(Boar).md "急冲（野猪）")
- [热风伤痕](Scar_of_the_Sirocco.md "热风伤痕")
- [猛击（安苏）](Slam_(Ansur).md "猛击（安苏）")
- [猛击（复侍仇卫）](Slam_(Grym).md "猛击（复侍仇卫）")
- [猛击（食人魔）](Slam_(Ogre).md "猛击（食人魔）")
- [泥泞猛击](Soil-Clogged_Slam.md "泥泞猛击")
- [风暴新星](Stormheart_Nova.md "风暴新星")
- [强化导力](Strengthened_Force_Tunnel.md "强化导力")
- [推翻大个](Topple_the_Big_Folk.md "推翻大个")
- [劈颅](Trephination.md "劈颅")
- [爆破喇叭](Trumpet_of_Blasting.md "爆破喇叭")
- [挥发集群](Volatile_Cluster.md "挥发集群")

### 一回合持续时间

以下倒伏来源仅施加 1 回合。由于倒伏的持续时间在受影响生物的回合开始时递减，因此状态会结束，*即使* 该生物因某种原因缺乏站起所需的移动速度。由于生物通常在回合开始时恢复移动速度，这仅在该生物还受到移动限制状态影响时才相关。

- [黎明破晓](Break_of_Dawn.md "黎明破晓")
- [壁垒叱喝](Bulwark_Rebuke.md "壁垒叱喝")
- [掘穴（獾）](Burrow_(Badger).md "掘穴（獾）")
- [粉碎跃击（枭熊荒野形态）](Crushing_Flight_(Owlbear_Wild_Shape).md "粉碎跃击（枭熊荒野形态）")
- [湮灭波](Destructive_Wave.md "湮灭波")
- [湮灭波：黯蚀](Destructive_Wave_colon__Necrotic.md "湮灭波：黯蚀")
- [湮灭波：光耀](Destructive_Wave_colon__Radiant.md "湮灭波：光耀")
- [愤怒投掷](Enraged_Throw.md "愤怒投掷")
- [凝气刚拳](Fist_of_Unbroken_Air.md "凝气刚拳")
- [疾风连击：摔绊](Flurry_of_Blows_colon__Topple.md "疾风连击：摔绊")
- [强力投掷](Forceful_Throw.md "强力投掷")
- [盖尔（职业动作）](Gale_(class_action).md "盖尔（职业动作）")
- [油脂](Grease_(surface).md "油脂 (地表)")
- [分泌油脂](Greasy_Discharge.md "分泌油脂")
- [沾蜜利爪](Honeyed_Paws.md "沾蜜利爪")
- [冰](Ice_(surface).md "冰 (地表)")
- [即兴近战武器](Improvised_Melee_Weapon.md "即兴近战武器")
- [即兴近战武器（附赠动作）](Improvised_Melee_Weapon_(Bonus_Action).md "即兴近战武器（附赠动作）")
- [蜜蜂军团：强力击退](Legion_of_Bees_colon__Mighty_Knockback.md "蜜蜂军团：强力击退")
- [主手攻击（钢铁卫士）](Main_Hand_Attack_(Steel_Watcher).md "主手攻击（钢铁卫士）")
- [无情碾压](Merciless_Crush.md "无情碾压")
- [多重攻击（肉肉）](Multiattack_(Flesh).md "多重攻击（肉肉）")
- [多重攻击（钢铁卫士泰坦）](Multiattack_(Steel_Watcher_Titan).md "多重攻击（钢铁卫士泰坦）")
- \_(状态)[失衡](Off_Balance_(Gargantuan_Cleave)_(Condition).md "失衡（巨像切割者） (状态)")
- [推斥协议](Repelling_Protocol.md "推斥协议")
- [训斥](Reprimand.md "训斥")
- [污物](Sewage.md "污物")
- [阴影之噬](Shadowjaw_Bite.md "阴影之噬")
- [盾牌猛击](Shield_Blow.md "盾牌猛击")
- [猛击（酿酒师僵尸，硬核）](Slam_(Brewer_Zombie,_tactician).md "猛击（酿酒师僵尸，硬核）")
- [念力推击](Telekinetic_Thrust.md "念力推击")
- [锁喉击](Throat_Punch.md "锁喉击")
- [投掷](Throw.md "投掷")
- [雷鸣打击](Thunderous_Smite.md "雷鸣打击")
- [摔绊](Topple.md "摔绊")
- [摔绊攻击（近战）](Trip_Attack_(Melee).md "摔绊攻击（近战）")

---
*Source: [Prone (Condition)](https://bg3.wiki/wiki/Prone_(Condition)*