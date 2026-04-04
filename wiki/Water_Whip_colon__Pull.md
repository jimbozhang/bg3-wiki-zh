# 清流鞭：牵引

**清流鞭：牵引**是一项职业动作，允许[四象宗](Way_of_the_Four_Elements.md "四象宗")武僧对目标造成伤害并将其拉向自己。

## 描述

使用水鞭将目标拉向你。

## 属性

消耗
[动作](Actions.md#Resources "动作") + 2 [气点](Ki_Point.md "气点")
伤害：3~30

3d10⁠[钝击](Bludgeoning.md "钝击")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[武器动作DC](Dice_rolls.md#Weapon_action_DC "掷骰")）
射程：9米（30英尺）
牵引距离：9米（30英尺）

## 高级效果

在9级时，若拥有[精通元素施法](Improved_Elemental_Casting.md "精通元素施法")，伤害将提升至4d10⁠[钝击](Bludgeoning.md "钝击")。

## 技术细节

UID

`Target_WaterWhip_Pull`

法术标志

`[DisableBlood](https://bg3.wiki/w/index.php?title=DisableBlood_\(spell_flag\)&action=edit&redlink=1) "DisableBlood \(spell_flag\) \(页面不存在\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 赠予

- [武艺：附赠徒手打击](Martial_Arts_colon__Bonus_Unarmed_Strike.md "武艺：附赠徒手打击")

## 学习方式

此法术是以下法术的变体：
[清流鞭](Water_Whip.md "清流鞭")

## 备注

- 与[火蛇利牙](Fangs_of_the_Fire_Snake.md "火蛇利牙")（使用徒手攻击掷骰）一样，这是四象宗中唯一两个不依赖感知，而是根据力量或敏捷进行调整的能力。
- 由于此技能使用武器动作DC，[战神的铁手套](Gauntlets_of_the_Warmaster.md "战神的铁手套")的[高强战技](Heightened_Manoeuvre.md "高强战技")将生效。相反，法术豁免DC的加成（如[不羁库席戈之帽](Hat_of_Uninhibited_Kushigo.md "不羁库席戈之帽")的[暴露弱点](Lay_Bare_Their_Weakness.md "暴露弱点")）_不会_生效。

## 错误

- 使用此法术将目标从边缘牵引下来时，由于缺少`[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)`标志，无法造成坠落伤害。
- 战斗日志会错误地显示DC计算为基础DC + 敏捷调整值 + 熟练项加值，但实际DC仍基于角色敏捷或力量调整值中较高的一项。

---
*Source: [Water Whip: Pull](https://bg3.wiki/wiki/Water_Whip:_Pull)*