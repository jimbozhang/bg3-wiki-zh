# 曲射

**曲射**是[奥术射手](Arcane_Archer.md "奥术射手")战士的被动特性/反应，允许战士将一次未命中的远程武器攻击重定向至另一个附近的敌人。

## 描述

当你使用任何魔法远程攻击未命中时，使用[附赠动作](Actions.md#Resources "动作")以相同攻击攻击下一个最近的目标。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作")
详情
远程武器[攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
目标：初始目标最近的敌人
充能：每回合

## 学习方式

职业：

- 职业等级7：[奥术射手](Arcane_Archer.md "奥术射手")

## 备注

- 尽管任何工具提示中均未说明，但曲射每回合只能使用一次，因为它需要并消耗一个隐藏资源。
- 无法选择重定向攻击的目标。它会选择离原始目标最近的敌人。
- 如果原始目标和重定向目标之间没有清晰路径，弹射物可能会与地形碰撞并浪费。
- 此特性适用于一组硬编码的特殊远程武器攻击<sup>[\[1\]](#cite_note-1)</sup>，包括奥术射击。完整列表如下：
  - 普通远程攻击，但不包括副手攻击
  - 所有奥术射击
  - 所有[箭](Arrows.md "箭")，但不包括[多靶箭](Arrow_of_Many_Targets.md "多靶箭")、[慰藉箭](Arrow_of_Salving.md "慰藉箭")和[置换箭](Arrow_of_Transposition.md "置换箭")。
  - 基础远程武器动作[腿筋射击](Hamstring_Shot.md "腿筋射击")、[穿刺射击](Piercing_Shot.md "穿刺射击")和[移动射击](Mobile_Shot.md "移动射击")
  - [剑舞学院](College_of_Swords.md "剑舞学院")的华舞[防御华舞（远程）](Defensive_Flourish_(Ranged).md "防御华舞（远程）")、[移动华舞（远程）](Mobile_Flourish_(Ranged).md "移动华舞（远程）")、[挥砍华舞（远程）](Slashing_Flourish_(Ranged).md "挥砍华舞（远程）")
  - 游侠的特殊攻击[灭族者（远程）](Horde_Breaker_(Ranged).md "灭族者（远程）")和[惧怖伏兵（远程）](Dread_Ambusher_(Ranged).md "惧怖伏兵（远程）")
- 法术[诱捕攻击（远程）](Ensnaring_Strike_(Ranged).md "诱捕攻击（远程）")（当施放于等级1、2或3时）和[印记斩](Branding_Smite.md "印记斩")（当施放于等级2或通过[扎瑞尔的提夫林](Tiefling.md#Zariel_tiefling "提夫林")的种族能力时）
- [偷袭（远程）](Sneak_Attack_(Ranged).md "偷袭（远程）")
  - 特殊武器动作[天界光箭](Bolt_of_Celestial_Light.md "天界光箭")和[照亮射击](Illuminating_Shot.md "照亮射击")
  - 不可访问的武器动作[裂颅碎击](Headcrack.md "裂颅碎击")和[约束](Pin_Down.md "约束")
- 任何其他未列出的攻击动作均不适用于曲射。这包括副手攻击、特殊武器动作如[致盲射击](Blinding_Shot.md "致盲射击")，以及任何战技大师的战斗策略（可通过[战技专家](Martial_Adept.md "战技专家")专长作为奥术射手获得）。
- 如果所有附近的敌人均为[失能](SG_Incapacitated.md "SG 失能")且未命中主要目标，则曲射不会触发。这是因为，`SG_Incapacitated` 被排除在 `HasEnemyWithinRange()` 函数检查之外。这不是错误，而是有意为之的检查。
  - 如果至少有一个附近的敌人未失能且未命中主要目标，则曲射会触发。

## 参考文献

1. [↑](#cite_ref-1) 这些由 `Mods/Shared/Scripts/thoth/helpers/CommonConditions.khn` 中的 `IsCurvingShot()` 函数定义。

---
*Source: [Curving Shot](https://bg3.wiki/wiki/Curving_Shot)*