# 魅影之力

**魅影之力**是一个[法术](Spells.md "法术")。它允许施法者用目标生物最后攻击它的幻象充斥其心智，每回合造成1d6⁠⁠[心灵](Psychic.md "心灵")伤害，并根据对目标造成的最后伤害类型改变伤害类型。

## 描述

每回合对一个生物造成伤害。在其回合开始时，它受到⁠[心灵](Psychic.md "心灵")伤害。每次它受到伤害后，魅影之力的伤害类型会变为与该伤害类型相同。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
详情
[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
[专注](Concentration.md "专注")

## 升环施法效应

以此法术的更高环阶施法不会获得额外收益。

## 技术细节

UID

`Target_PhantasmalForce`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：魅影之力

**[魅影之力](Phantasmal_Force_(Condition).md "魅影之力（状态）")**

持续时间：10回合

[智力](Intelligence.md "智力") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

被最后攻击它的事物的回响所困扰。

- 每回合受到1d6⁠⁠[心灵](Psychic.md "心灵")伤害。
- 当目标受到来自其他来源的伤害时，魅影之力会变为该伤害类型。
- 每回合结束时，目标进行一次[智力](Intelligence.md "智力")[豁免检定](Saving_throw.md "豁免检定")。成功时，状态结束。

## 学习方式

职业：

- 职业等级3：[吟游诗人](Bard.md "吟游诗人")、[术士](Sorcerer.md "术士")、[法师](Wizard.md "法师")、[旧日支配者](The_Great_Old_One.md "旧日支配者")和[至高妖精](The_Archfey.md "至高妖精")
- 职业等级7：[诡术师](Arcane_Trickster.md "诡术师")
- 职业等级8：[奥法骑士](Eldritch_Knight.md "奥法骑士")

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书中的卷轴。

## 备注

- 单个魅影之力伤害状态都共享相同的`StackID`，这意味着一个角色上一次只能激活一个。由于被动技能的编写方式，这会导致优先级效果，状态遵循以下优先级顺序（较早的状态优先于较晚的状态）：
  - 挥砍 > 穿刺 > 钝击 > 强酸 > 雷鸣 > 黯蚀 > 火焰 > 闪电 > 寒冷 > 心灵 > 中毒 > 光耀 > 力场
    - 例如，如果一个角色对受魅影之力影响的目标施放[冰刃术](Ice_Knife.md "冰刃术")（造成穿刺和寒冷伤害），敌人将保留魅影之力：穿刺。

## 外部链接

- ⁠[魅影之力](https://forgottenrealms.fandom.com/wiki/Phantasmal_force) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Phantasmal Force](https://bg3.wiki/wiki/Phantasmal_Force)*