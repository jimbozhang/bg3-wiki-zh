# 克雷斯卡的雷鸣轰隆 (状态)

**克雷斯卡的雷鸣轰隆**

- 受影响实体对[雷鸣](Thunder.md "雷鸣")伤害具有[抗性](Resistance.md "抗性")。
- 其雷鸣法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。
- 当其造成法术伤害时，它会使目标受到2回合的[残响](Reverberation_(Condition).md "残响 (状态)")。
- 当与克雷斯卡的雷鸣调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[粉碎音波](Shatter.md "粉碎音波")和[湮灭波](Destructive_Wave.md "湮灭波")。

## 属性

[堆叠ID](Stack_ID.md "堆叠ID"): `MAG_LEGENDARY_CHROMATIC_ATTUNEMENT_FIRE` [持续时间结束](Conditions.md#Duration "状态"): 回合开始时

[如果已应用](Conditions.md#Stack_type "状态"): 替换当前

## 状态：残响

**[残响](Reverberation_(Condition).md "残响 (状态)")**

持续时间: 2回合

- 受影响实体在剩余回合内，其[力量](Strength.md "力量")、[敏捷](Dexterity.md "敏捷")和[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")具有-1减值。
- 当实体具有5回合或以上的残响时，它会受到1d4[雷鸣](Thunder.md "雷鸣")[DRS](Damage_rider_as_source.md "伤害来源附加")伤害，并且必须通过[DC](Dice_rolls.md#Save_DCs "掷骰") 10的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，否则将[倒伏](Prone_(Condition).md "倒伏 (状态)")。之后状态将被移除。
- 对[雷鸣](Thunder.md "雷鸣")伤害[免疫](Damage_types.md#Immunity "伤害类型")的生物无法获得残响。

## 备注

- 游戏内工具提示说明此效果施加1回合残响，但实际施加2回合。
- 每次攻击只能施加一次残响。像[粉碎音波](Shatter.md "粉碎音波")这样击中多个目标的法术只会对单个目标应用此状态。

## 错误

- 附加伤害仅基于所用动作的`DamageType`标志添加。它*并不*实际检查该动作是否为法术。

## 克雷斯卡的雷鸣轰隆来源

- [震骨雷鸣](Bone-shaking_Thunder.md "震骨雷鸣")

## 拥有克雷斯卡的雷鸣轰隆的生物

*维基数据库中未定义*

## 具有相同堆叠ID的状态

| 状态 | 效果 |
| --- | --- |
| [克雷斯卡的强酸滴落](Adrip_with_Kereska's_Acid_(Condition).md "克雷斯卡的强酸滴落 (状态)") | 受影响实体对[强酸](Acid.md "强酸")伤害具有[抗性](Resistance.md "抗性")。其强酸法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它可能使目标受到3回合的[有毒烟雾](Noxious_Fumes_(Condition).md "有毒烟雾 (状态)")。当与克雷斯卡的强酸调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[马友夫强酸箭](Melf's_Acid_Arrow.md "马友夫强酸箭")和[哈达之饥渴](Hunger_of_Hadar.md "哈达之饥渴")。 |
| [克雷斯卡的冰之导管](Conduit_of_Kereska's_Ice_(Condition).md "克雷斯卡的冰之导管 (状态)") | 受影响实体对[寒冷](Cold.md "寒冷")伤害具有[抗性](Resistance.md "抗性")。其寒冷法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它会使目标受到2回合的[冷冻](Encrusted_with_Frost_(Condition).md "冷冻 (状态)")。当与克雷斯卡的冰调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[寒冰锥](Cone_of_Cold.md "寒冰锥")和以4环施放一次[冰风暴](Ice_Storm.md "冰风暴")。 |
| [克雷斯卡的闪电爆裂](Crackling_with_Kereska's_Lightning_(Condition).md "克雷斯卡的闪电爆裂 (状态)") | 受影响实体对[闪电](Lightning.md "闪电")伤害具有[抗性](Resistance.md "抗性")。其闪电法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它获得2点[闪电充能](Lightning_Charges_(Condition).md "闪电充能 (状态)")。当与克雷斯卡的闪电调谐时，它可以在一次[短休](Short_Rest.md "短休")内以6环施放一次[链状闪电](Chain_Lightning.md "链状闪电")和以3环施放一次[闪电束](Lightning_Bolt.md "闪电束")。 |
| [克雷斯卡的火焰擒握](Gripped_by_Kereska's_Flame_(Condition).md "克雷斯卡的火焰擒握 (状态)") | 受影响实体对[火焰](Fire.md "火焰")伤害具有[抗性](Resistance.md "抗性")。其火焰法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它获得2回合的[灼热](Heat_(Condition).md "灼热 (状态)")。当与克雷斯卡的火焰调谐时，它可以在一次[短休](Short_Rest.md "短休")内以3环施放一次[火球术](Fireball.md "火球术")和以5环施放一次[火墙术](Wall_of_Fire.md "火墙术")。 |
| 克雷斯卡的雷鸣轰隆 | 受影响实体对[雷鸣](Thunder.md "雷鸣")伤害具有[抗性](Resistance.md "抗性")。其雷鸣法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它会使目标受到2回合的[残响](Reverberation_(Condition).md "残响 (状态)")。当与克雷斯卡的雷鸣调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[粉碎音波](Shatter.md "粉碎音波")和[湮灭波](Destructive_Wave.md "湮灭波")。 |
| [克雷斯卡的毒之容器](Vessel_for_Kereska's_Poison_(Condition).md "克雷斯卡的毒之容器 (状态)") | 受影响实体对[中毒](Poison.md "中毒")伤害具有[抗性](Resistance.md "抗性")。其中毒法术造成的伤害等于其[熟练项加值](Proficiency_Bonus.md "熟练项加值")。当其造成法术伤害时，它会使目标受到2回合的[中毒](Poisoned_(Condition).md "中毒 (状态)")。当与克雷斯卡的毒调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[死云术](Cloudkill.md "死云术")和[疾病射线](Ray_of_Sickness.md "疾病射线")。 |
- 当与克雷斯卡的毒调谐时，它可以在一次[短休](Short_Rest.md "短休")内以5环施放一次[死云术](Cloudkill.md "死云术")和[疾病射线](Ray_of_Sickness.md "疾病射线")。

---
*Source: [Rumbling with Kereska's Thunder (Condition)](https://bg3.wiki/wiki/Rumbling_with_Kereska's_Thunder_(Condition)*