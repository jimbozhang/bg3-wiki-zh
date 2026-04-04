# 大步奔行

**大步奔行**是一个[1级变化学派法术](Spells.md "Spells")。它允许施法者使一个生物在单回合内移动更远的距离。

## 描述

使一个生物的[移动速度](Movement_speed.md "移动速度")增加3米（10英尺）。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术位")
详情
近战：1.5米（5英尺）
[仪式](Spells.md#Ritual_spells "法术")

## 升环施法

[升环施法](Upcasting.md "升环施法")：每比1环高一环的法术位，可影响一个额外目标。

## 技术细节

UID

`Target_Longstrider`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IgnorePreviouslyPickedEntities](IgnorePreviouslyPickedEntities_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：大步奔行

**[大步奔行](Longstrider_(Condition).md "大步奔行 (状态)")**

持续时间：直至[长休](Long_Rest.md "长休")

- 使一个生物的[移动速度](Movement_speed.md "移动速度")增加3米（10英尺）。

## 学习方式

职业：

- 职业等级1：[吟游诗人](Bard.md "吟游诗人")、[德鲁伊](Druid.md "德鲁伊")和[法师](Wizard.md "法师")
- 职业等级2：[游侠](Ranger.md "游侠")
- 职业等级3：[诡术师](Arcane_Trickster.md "诡术师")和[奥法骑士](Eldritch_Knight.md "奥法骑士")

由特性授予：

- [魔法学徒：吟游诗人](Magic_Initiate_colon__Bard.md "魔法学徒：吟游诗人")
- [魔法学徒：德鲁伊](Magic_Initiate_colon__Druid.md "魔法学徒：德鲁伊")
- [魔法学徒：法师](Magic_Initiate_colon__Wizard.md "魔法学徒：法师")
- [仪式施法者：法术研习](Ritual_Caster_colon__Free_Spells.md "仪式施法者：法术研习")

由物品授予：

- [黑暗卫士的护胫](Blackguard's_Greaves.md "黑暗卫士的护胫")
- [坚毅之靴](Boots_of_Persistence.md "坚毅之靴")

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书中的卷轴。

## 备注

- 由于这是一个仪式法术，在战斗外施放是免费的，并且会持续作用于所有受术者（即使不在当前队伍中），直至死亡或[长休](Long_Rest.md "长休")。因此，如果队伍中有能施放此法术的人，建议让所有队伍成员始终保持此效果。
  - 如果由[德鲁伊](Druid.md "德鲁伊")或[法师](Wizard.md "法师")施放，此法术必须由施法者[预备](Prepared_spells.md "预备法术")；从施法者的预备法术列表中移除该法术会立即移除施法者施加给所有队伍成员的增益效果。
- 这是《博德之门3》中唯一一个具有升环施法增益的仪式法术；游戏允许在战斗外仪式施法时选择更高环的法术位，尽管这所做的只是在单次施法中将效果应用于多个目标。
- 大步奔行的施法咒语是 **Properō**（拉丁语命令“加速！”）、**Citium**（拉丁语“快速”）和 **Ocior**（“更快”）。

---
*Source: [Longstrider](https://bg3.wiki/wiki/Longstrider)*