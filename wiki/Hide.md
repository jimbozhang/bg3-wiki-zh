# 躲藏

**躲藏**是一种常见的[动作](Action.md "动作")，允许使用者隐藏其位置。

## 描述

尝试隐藏自己。

躲藏取决于你的[隐匿](Stealth.md "隐匿")技能以及你是否处于[遮蔽](Obscured.md "遮蔽")状态。攻击或施放法术会暴露你的位置。

## 属性

消耗
[动作](Actions.md#Resources "动作")
详情
范围：自身

## 技术细节

UID

`Shout_Hide`

法术标志

`[AllowMoveAndCast](https://bg3.wiki/w/index.php?title=AllowMoveAndCast_\(spell_flag\)&action=edit&redlink=1) "AllowMoveAndCast \(spell flag\) \(page does not exist\)")`, `[CombatLogSetSingleLineRoll](https://bg3.wiki/w/index.php?title=CombatLogSetSingleLineRoll_\(spell_flag\)&action=edit&redlink=1) "CombatLogSetSingleLineRoll \(spell flag\) \(page does not exist\)")`, `[ImmediateCast](https://bg3.wiki/w/index.php?title=ImmediateCast_\(spell_flag\)&action=edit&redlink=1) "ImmediateCast \(spell flag\) \(page does not exist\)")`, `[Invisible](Invisible_(spell_flag).md)`, `[Stealth](Stealth_(spell_flag).md)`, `[UnavailableInDialogs](https://bg3.wiki/w/index.php?title=UnavailableInDialogs_\(spell_flag\)&action=edit&redlink=1) "UnavailableInDialogs \(spell flag\) \(page does not exist\)")`

## 状态：隐藏

**[隐藏](Hiding_(Condition).md "隐藏 (状态)")**

- 受影响实体对敌人隐形，直到其穿过敌人的视野锥。
- 该实体在所有[攻击掷骰](Attack_roll.md "攻击掷骰")上具有[优势](Advantage.md "优势")。

## 备注

- 如果玩家角色处于非盟友生物的视线内，并且处于近战范围内或被视为处于[开阔区域](Clear_Area_(Condition).md "开阔区域 (状态)")（参见[遮蔽](Obscurity.md "遮蔽")和[高级黑暗视觉](Darkvision.md "高级黑暗视觉")），则该角色会被立即发现。
- 如果他们在非盟友生物的视线内，同时被视为[轻度遮蔽](Lightly_Obscured_(Condition).md "轻度遮蔽 (状态)")（考虑高级黑暗视觉）且不在近战范围内，则玩家角色会进行一次[隐匿](Stealth.md "隐匿")检定，与另一生物的[被动察觉检定](Passive_checks.md "被动检定")对抗。这在战斗日志中显示为“隐藏检定”，其[难度等级](Difficulty_Class.md "难度等级")由另一生物的被动察觉分数决定。每回合（或在回合制模式外每6秒）以及对每个视线内有隐藏玩家角色的非盟友生物都会重复此检定。
- 没有高级黑暗视觉的生物的视线不会延伸到[重度遮蔽](Heavily_Obscured_(Condition).md "重度遮蔽 (状态)")区域，因此他们无法检测到藏在该区域的角色。
- 攻击会自动结束隐藏，这意味着无法从敌人视线内进行未被发现的[隐匿攻击](Stealth_attack.md "隐匿攻击")，即使在攻击前成功隐藏在遮蔽中。然而，从隐藏状态发动攻击仍然有益，因为它赋予[攻击掷骰](Attack_roll.md "攻击掷骰")[优势](Advantage.md "优势")。
- 视线（即“视野锥”）在玩家角色当前处于隐藏状态时会以红色覆盖层显示。可以使用[初级幻影](Minor_Illusion.md "初级幻影")或[猫叫声](Meow.md "猫叫声")等干扰手段来操纵视线，这些手段会迫使生物转向特定方向和/或走向另一个位置。这可以为[巧手](Sleight_of_Hand.md "巧手")尝试或隐匿攻击创造机会。
- 在[云雾术](Fog_Cloud.md "云雾术")或[黑暗术](Darkness.md "黑暗术")内隐藏是自动成功的，因为敌人的视野锥无法进入内部，除非他们拥有通过魔法黑暗视物的被动能力，如[魔鬼视界](Devil's_Sight.md "魔鬼视界")或[生于黑暗](Born_into_Darkness.md "生于黑暗")。这也弥补了[目盲](Blinded_(Condition).md "目盲 (状态)")减益效果，因为如果隐藏在云雾内，敌人无法从外部瞄准玩家角色。
- 在抢先体验补丁9中，躲藏是一个附赠动作，但在游戏正式版中改为[动作](Action.md "动作")。然而，[暗影宗](Way_of_Shadow.md "暗影宗")武僧副职、[阴影追猎者](Gloom_Stalker.md "阴影追猎者")游侠副职和[游荡者](Rogue.md "游荡者")职业仍能通过职业特性以[附赠动作](Bonus_action.md "附赠动作")进行躲藏。

## 另见

- [灵巧动作：躲藏](Cunning_Action_colon__Hide.md "灵巧动作：躲藏")
- [惧怖伏兵：躲藏](Dread_Ambusher_colon__Hide.md "惧怖伏兵：躲藏")
- [暗影技艺：躲藏](Shadow_Arts_colon__Hide.md "暗影技艺：躲藏")

---
*Source: [Hide](https://bg3.wiki/wiki/Hide)*