# 减速术

**减速术**是一个[法术](Spells.md "法术")。它允许施法者降低移动速度、护甲等级和敏捷豁免检定，并限制动作。

## 描述

改变最多6个敌人周围的时间以使其减速。他们无法跑远，无法做太多事情，并且更容易被击中。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
[WIS](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
目标：6个生物
[专注](Concentration.md "专注")

## 升环施法

以更高环位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_Slow`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：减速

**[减速](Slowed_(Condition).md "减速 (状态)")**

持续时间：10回合

[WIS](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- [移动速度](Movement_speed.md "移动速度")减半
- [护甲等级](Armour_Class.md "护甲等级")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")降低2点
- 只能采取[动作](Action.md "动作")或[附赠动作](Bonus_action.md "附赠动作")，不能同时采取两者
- 无法进行[反应](Reaction.md "反应")
- 无法进行[额外攻击](Extra_Attack.md "额外攻击")或[精通额外攻击](Improved_Extra_Attack.md "精通额外攻击") _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_
- 施放的法术可能会延迟一回合 _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_

## 学习方式

职业：

- 职业等级5：[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[旧日支配者](The_Great_Old_One.md "旧日支配者")和[知识领域](Knowledge_Domain.md "知识领域")（领域法术）
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

其他学习方式：

- 5级及以上选择[异界恩赐](Eldritch_Invocation.md "异界恩赐")[精神泥沼](Mire_the_Mind.md "精神泥沼")的[邪术师](Warlock.md "邪术师")也会获得此法术。
- 拥有[3级法术位](Spells.md#Spell_slots "法术")的[法师](Wizard.md "法师")可以将[缓慢术卷轴](Scroll_of_Slow.md "缓慢术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 每个受影响的生物在其回合结束时重复进行[感知](Wisdom.md "感知")豁免检定，如果成功则结束效果。

## 错误

- 通常，减速术的目标必须是不同的，但当升环至4环时，_且仅限4环_，目标可以被多次选择。例如，两个敌人可以各自被选择三次，迫使他们进行三次独立的豁免检定以避免被减速。这是由于4环升环版本缺少`[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`标志。
- 通过卷轴施放时，减速术_需要_6个目标；由于敌人不能被选择两次，且盟友无法成为目标，此卷轴在第一轮之后可能难以使用。
- 参见[减速 (状态)#错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Slow_Visuals.mp4>

## 外部链接

- ⁠[减速术](https://forgottenrealms.fandom.com/wiki/Slow) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Slow](https://bg3.wiki/wiki/Slow)*