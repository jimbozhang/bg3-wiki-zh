# 假死术

**假死术**是一个[法术](Spells.md "法术")。它允许施法者让盟友进入魔法保护性昏迷状态，假装死亡。

## 描述

让一名盟友进入保护性昏迷状态。他们变得对所有[伤害](Damage_types.md "伤害类型")具有[抗性](Resistant.md "抗性")，除了[心灵](Psychic.md "心灵")伤害。[疾病](Diseased_(status_group).md)和[中毒](Poisoned_(status_group)不再有任何效果.md)。

当被[协助](Help.md "协助")时移除。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [3级法术位](Spells.md#Spell_slots "法术")
详情
范围：1.5米（5英尺）

## 更高环阶施法

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_FeignDeath`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：假死中

**[假死中](Feigning_Death_(Condition).md "假死中（状态）")**

持续时间：10回合

- 已陷入足以模仿死亡的深度魔法昏迷
- 对所有伤害具有[抗性](Damage_types.md#Resistance "伤害类型")，除了[心灵](Psychic.md "心灵")伤害，且疾病和中毒不再有任何效果
- 当被[协助](Help.md "协助")时移除

## 如何习得

职业：

- 职业等级5：[吟游诗人](Bard.md "吟游诗人")、[牧师](Cleric.md "牧师")、[德鲁伊](Druid.md "德鲁伊")和[法师](Wizard.md "法师")

其他习得方式：

- 拥有[3级法术位](Spells.md#Spell_slots "法术")的[法师](Wizard.md "法师")可以将[假死术卷轴](Scroll_of_Feign_Death.md "假死术卷轴")[抄录](Transcribing_scrolls.md "抄录卷轴")到他们的法术书中。

## 备注

- 如果队伍犯罪并被守卫呼叫，可以对犯罪的队伍成员施放假死术以避免被审问。守卫通常会在法术结束前离开，然后队伍可以保留所有偷来的物品。
- 根据犯罪的严重程度，其他队伍成员也可能被审问，并需要进行魅力检定。鉴于这一点，建议对轻微犯罪（如[巧手](Sleight_of_Hand.md "巧手")）或更严重的犯罪（如果其他队伍成员不在附近）使用**假死术**。
- 尽管法术有其背景描述，但在战斗中，敌人可能不会将拥有此增益的角色视为死亡，并通常会继续攻击他们。因此，它不能用于重置或逃脱战斗。
- 在补丁7之前，对盟友NPC（鼠标悬停时显示为绿色轮廓）施放假死术不被视为敌对行为，也不会冒犯目标或附近的NPC。此外，从处于[假死中](Feigning_Death_(Condition).md "假死中（状态）")状态的NPC处[偷窃](Stealing.md "偷窃")不会触发敌意，前提是其他NPC没有目击犯罪，且目标NPC在醒来后没有注意到任何物品被偷。然而，扒窃尝试失败会终止当前的扒窃会话，直到下一个[回合](Turn-based_mode.md "回合制模式")才能恢复，但不会唤醒NPC。这在对[商人](Traders.md "商人")使用时特别有效。然而，随着补丁7的应用，只有盟友才能成为假死术的目标。
  - 从卷轴施放的假死术似乎没有应用此限制。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Feign-death-showcase.mp4>

## 外部链接

- ⁠[假死术](https://forgottenrealms.fandom.com/wiki/Feign_death) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Feign Death](https://bg3.wiki/wiki/Feign_Death)*