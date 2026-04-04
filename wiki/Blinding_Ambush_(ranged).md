# 盲目伏击（远程）

此页面内容为 [荣誉模式](Honour_Mode.md "荣誉模式") 独占。

**盲目伏击**是 [尤格](Yurgir.md "尤格") 使用的 [传奇动作](Legendary_action.md "传奇动作")，当被 [警戒狩猎](Watchful_Hunt.md "警戒狩猎") 标记的目标攻击或施放法术时触发。这是一个远程攻击，造成光耀伤害并可能使被标记的目标 [目盲](Blinded_(Condition).md "目盲（状态）")。尤格还拥有此攻击的 [近战变体](Blinding_Ambush_(melee).md)。

## 描述

尝试在被 [狩猎](Hunted_(Condition).md "狩猎（状态）") 的生物攻击或对你施放法术之前使其 [目盲](Blinded_(Condition).md "目盲（状态）")。

## 属性

伤害：5~50

5d10⁠[光耀](Radiant.md "光耀")

详情
远程武器 [攻击掷骰](Attack_roll.md "攻击掷骰")（未命中：目标仍承受一半伤害）
射程：18 米（60 英尺）
充能：每回合

## 技术细节

UID

`Projectile_SHA_Orthon_BlindingPursuit_Ranged`

实际攻击

`Interrupt_SHA_Orthon_BlindingPursuit_Ranged`

触发攻击的反应

法术标志

`[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：目盲

**[目盲](Blinded_(Condition).md "目盲（状态）")**

持续时间：2 回合

- 受影响的生物在 [攻击掷骰](Attack_roll.md "攻击掷骰") 上具有 [劣势](Disadvantage.md "劣势")。
- 受影响的生物的攻击和法术射程减少至 3 米（10 英尺）。
- 对受影响生物的攻击掷骰具有 [优势](Advantage.md "优势")。

## 学习方式

使用者：[尤格](Yurgir.md "尤格")

## 备注

- 与近战版本不同，远程版本的 [目盲](Blinded_(Condition).md "目盲（状态）") 效果无需豁免。

---
*Source: [Blinding Ambush (ranged)](https://bg3.wiki/wiki/Blinding_Ambush_(ranged)*