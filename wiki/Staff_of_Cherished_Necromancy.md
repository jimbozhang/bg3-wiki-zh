# 死灵珍爱法杖

死灵珍爱法杖是一把非常稀有的 +2 [长棍](Quarterstaves.md "长棍")，它能极大增强[死灵学派](Necromancy.md "死灵学派")法术，并且可以利用已死生物的[精华](Essence.md "精华")来施放死灵学派法术，而无需消耗[法术位](Spell_Slot.md "法术位")。

与他们的父亲蒂博不同，切丽丝·霍洛威并不害怕僵尸。切丽丝害怕鲨鱼、甘草、壁纸、耐瑟瑞尔遗物、帽子（大型）、户外、室内、帽子（小型）和牛奶桶。僵尸不过是场血腥的野餐。

## 属性

单手伤害

1d6 + 2 (3~8) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[钝击](Bludgeoning.md "钝击")

双手伤害

1d8 + 2 (3~10) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[钝击](Bludgeoning.md "钝击")

额外伤害

1d4 (1~4) ⁠[黯蚀](Necrotic.md "黯蚀")

详情
[长棍](Quarterstaves.md "长棍")
稀有度：非常稀有
附魔：**+ 2**
[两用](Versatile.md "两用")
[可蘸取](Dippable.md "可蘸取")
近战：1.5 米 (5 英尺)
重量：1.8 千克 (3.6 磅)
价格：480 金币
UID `MAG_GreaterNecromancy_Staff` UUID `ecb02247-a407-445e-8046-856133d198bf` Stats `MAG_GreaterNecromancy_Staff` ### 特殊

**持有此物品者获得：**

[高强死灵法术](Heightened_Necromancy.md "高强死灵法术")
生物对你[死灵学派](Necromancy.md "死灵学派")的[豁免检定](Saving_throw.md "豁免检定")具有[劣势](Disadvantage.md "劣势")。

[获取生命精华](Life_Essence_Harvest.md "获取生命精华")
当使用者用法术杀死一个敌对生物时，他们会贪婪地吸收其能量，并获得[生命精华](Life_Essence_(Condition).md "生命精华（状态）")，直到下一次长休。

### 武器动作

_如果你拥有[熟练项](Proficiency.md "熟练项")，装备在**主手**以获得：_

[摔绊](Topple.md "摔绊")
挥击一个生物以使其[倒伏](Prone_(Condition).md "倒伏（状态）")。（充能：[短休](Short_rest.md "短休")。）

## 获取地点

- [菲尔格雷弗宅邸](Philgrave's_Mansion.md "菲尔格雷弗宅邸") X: 14 Y: -160：由[秘术师卡里翁](Mystic_Carrion.md "秘术师卡里翁")携带

## 备注

_关于高强死灵法术：_

- 任何具有豁免检定的死灵学派法术都受益于高强死灵法术。这些法术包括：
  - [爆裂肌腱](Bursting_Sinew.md "爆裂肌腱")
  - [丧钟](Toll_the_Dead.md "丧钟")
  - [疾病射线](Ray_of_Sickness.md "疾病射线")
- [失明术](Blindness.md "失明术")
  - [麻痹射线](Paralyzing_Ray.md "麻痹射线")
  - [恐惧射线](Ray_of_Fear.md "恐惧射线")
  - [致伤射线](Wounding_Ray.md "致伤射线")
  - [降咒](Bestow_Curse.md "降咒")
  - [召唤黑暗](Beckoning_Darkness.md "召唤黑暗")
- [枯萎术](Blight.md "枯萎术")
- [废黜](Dethrone.md "废黜")
  - [死亡法阵](Circle_of_Death.md "死亡法阵")
- [摄心目光](Eyebite.md "摄心目光")
- [重伤术](Harm.md "重伤术")

_关于获取生命精华：_

- 获取生命精华没有冷却时间，并且可以无限触发。
- 用[生命精华](Life_Essence_(Condition).md "生命精华（状态）")赋予的法术杀死生物不会提供新的[生命精华](Life_Essence_(Condition).md "生命精华（状态）")充能。
- 来自[精魂守卫](Spirit_Guardians.md "精魂守卫")等来源的间接法术伤害在杀死敌对生物时不会提供[生命精华](Life_Essence_(Condition).md "生命精华（状态）")充能。
- 根据 `GreaterNecromancySpellFilter() .khn` 脚本，此效果旨在仅当法术等级小于或等于使用者拥有的生命精华回合数时，才允许施放额外的死灵学派法术。然而，此限制目前无法正常工作，任何等级的死灵学派法术都可以使用此效果施放。尽管工具提示均未明确提及此功能，但生命精华在其工具提示中显示了使用者拥有的回合数。

## 错误

_关于获取生命精华：_

- 如果角色在施放死灵学派的戏法时此被动效果处于激活状态，则该效果会被消耗，尽管该戏法在角色的施法栏中并未高亮显示。

---
*Source: [Staff of Cherished Necromancy](https://bg3.wiki/wiki/Staff_of_Cherished_Necromancy)*