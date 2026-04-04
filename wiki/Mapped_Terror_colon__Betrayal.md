# 恐怖映射：背叛

关于其他版本的恐怖映射，请参见 [恐怖映射（消歧义）](Mapped_Terror_(disambiguation)..md)

**恐怖映射：背叛** 是一个 [4级幻术法术](Spells.md "法术")。此法术会控制一个目标，然后以其背叛的必然恐惧来恐吓其盟友。队友无法学习此法术。

## 描述

利用目标的映射恐惧来 [恐吓](Frightened_(Condition).md "恐慌（状态）") 它并 [控制](Dominated_(Condition).md "受控（状态）") 其一名盟友。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")
详情
[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
范围效果：18米（60英尺）半径
充能：每回合

## 升环施法效应

以此法术升环施法不会获得额外收益。

## 技术细节

UID

`Target_LOW_HouseOfGrief_ExploitFear_Betrayal`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`

## 状态：恐慌

**[恐慌](Frightened_(Condition).md "恐慌（状态）")**

持续时间：2回合

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 16）

- 受影响的生物无法移动。恐慌的生物在 [属性检定](Ability_Check.md "属性检定") 和 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。

## 状态：受控

**[受控](Dominated_(Condition).md "受控（状态）")**

持续时间：2回合

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 16）

- 受影响的实体将跟随并协助施放此法术的施法者战斗。
- 每次受到伤害时，它可能通过成功的感知 [豁免检定](Saving_throw.md "豁免检定") 来打破施法者对它的控制。

## 如何学习

由以下生物使用：[维康妮亚·迪佛](Viconia_DeVir.md "维康妮亚·迪佛")

## 备注

- 由 [维康妮亚·迪佛](Viconia_DeVir.md "维康妮亚·迪佛") 在对一名在 [心脏映射](Mapping_of_the_Heart.md "心脏映射") 中声称恐惧“背叛”的角色使用 [惩治心形](Castigate_Heartform.md "惩治心形") 后施放。
- 此法术以一名 *未* 经历心脏映射的队友为目标。若豁免检定失败，他们将被 [控制](Dominated_(Condition).md "受控（状态）")。如果经历映射的角色在该队友的18米（60英尺）范围内，则他们进行相同的豁免检定，否则将变得 [恐慌](Frightened_(Condition).md "恐慌（状态）")。
- 此法术施加一个具有 `StackPriority` 为 2 的特殊受控版本。这意味着它会覆盖任何现有的受控状态。
- 对受控豁免检定成功的受控目标仍受益于对恐吓豁免检定具有优势或劣势的效果，例如 [反魅惑](Countercharm_(Condition).md "反魅惑（状态）")。

---
*Source: [Mapped Terror: Betrayal](https://bg3.wiki/wiki/Mapped_Terror:_Betrayal)*