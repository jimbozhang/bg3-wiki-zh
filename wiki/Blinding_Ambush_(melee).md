# 伏击目盲 (近战)

此页面内容为 [荣誉模式](Honour_Mode.md "荣誉模式") 独占。

**伏击目盲**是 [尤格](Yurgir.md "尤格") 使用的 [传奇动作](Legendary_action.md "传奇动作")，当被 [警戒追猎](Watchful_Hunt.md "警戒追猎") 标记的目标攻击或施放法术时触发。这是一个近战攻击，造成光耀伤害并可能使被标记的目标目盲。尤格还拥有此攻击的 [远程版本](Blinding_Ambush_(ranged).md)。

## 描述

尝试在 [被追猎者](Hunted_(Condition).md "被追猎者 (状态)") 攻击或对你施放法术前使其 [目盲](Blinded_(Condition).md "目盲 (状态)")。

## 属性

伤害：5~50

5d10⁠[光耀](Radiant.md "光耀")

详情
近战武器 [攻击掷骰](Attack_roll.md "攻击掷骰") (未命中：目标仍承受一半伤害)
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免 DC](Dice_rolls.md#Spell_save_DC "骰子掷骰"))
范围：3 米 (10 英尺)
充能：每回合

## 技术细节

UID

`Target_SHA_Orthon_BlindingPursuit_Melee`

实际攻击

`Interrupt_SHA_Orthon_BlindingPursuit_Melee`

触发攻击的反应

法术标志

`[IsAttack](IsAttack_(spell_flag).md)`, `[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`

## 状态：目盲

**[目盲](Blinded_(Condition).md "目盲 (状态)")**

持续时间：2 回合

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免 DC](Dice_rolls.md#Spell_save_DC "骰子掷骰"))

- 受影响的生物在 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术范围减少至 3 米 (10 英尺)。
- 对受影响生物的攻击掷骰具有 [优势](Advantage.md "优势")。

## 如何习得

由生物使用：[尤格](Yurgir.md "尤格")

## 注释

- 与远程版本不同，近战版本对 [目盲](Blinded_(Condition).md "目盲 (状态)") 效果有豁免检定。

---
*Source: [Blinding Ambush (melee)](https://bg3.wiki/wiki/Blinding_Ambush_(melee)*