# 罗兰的火球术术

关于原始法术，请参阅 [火球术术](Fireball.md "火球术术")。

**罗兰的火球术术**是一个[4级塑能学派法术](Spells.md "法术")。这是[火球术术](Fireball.md "火球术术")的一个特殊版本，仅由[罗兰](Rolan.md "罗兰")在[洛若坎](Lorroakan.md "洛若坎")被击败且罗兰成为[拉玛吉斯高塔](Ramazith's_Tower.md "拉玛吉斯高塔")的主人时使用。它允许他在射程内选择一个点释放一次大型爆炸，并使敌人掉落装备的武器。

## 描述

从你的手指射出一道明亮的火焰，在接触时爆炸，烧焦附近的一切，并[灼热](Heat_Metal_(Condition).md "灼热金属 (状态)")火焰中金属武器和护甲。

如果生物只穿着金属护甲，它总是获得劣势。

如果生物仍然接触着金属，你可以在后续回合使用附赠动作造成另一次伤害，并迫使生物松手或获得劣势。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")
伤害：7~42

7d6⁠[火焰](Fire.md "火焰")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：目标仍承受一半伤害。）
射程：18米（60英尺）
范围：4米（13英尺）半径

## 更高法术位

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Projectile_LOW_Rolan_Fireball`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[HasHighGroundRangeExtension](HasHighGroundRangeExtension_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：灼热金属

**[灼热金属](Heat_Metal_(Condition).md "灼热金属 (状态)")**

持续时间：10回合

- 使生物身上的金属武器或护甲过热，无需豁免（自动优先武器）。
- 如果持有金属武器的生物初始[豁免检定](Saving_throw.md "豁免检定")失败，则掉落武器。
- 如果生物接触着过热的金属物品，他们在[攻击掷骰](Attack_roll.md "攻击掷骰")和[属性检定](Ability_Check.md "属性检定")上获得[劣势](Disadvantage.md "劣势")。
- 每个后续回合，如果生物仍然接触着金属，施法者可以使用[重新施加热金属](Reapply_Heat_Metal.md "重新施加热金属")造成另一次2d8⁠⁠[火焰](Fire.md "火焰")伤害，迫使生物再次通过豁免检定或掉落物品（如果是金属武器）。

## 状态：灼热金属：劣势

**[灼热金属：劣势](Heat_Metal_colon__Disadvantage_(Condition).md "灼热金属：劣势 (状态)")**

持续时间：10回合

- 在施法者的下一个回合开始前，在[攻击掷骰](Attack_roll.md "攻击掷骰")和[属性检定](Ability_Check.md "属性检定")上具有[劣势](Disadvantage.md "劣势")。

## 如何习得

由以下生物使用：[罗兰](Rolan.md "罗兰")

## 备注

- 与[灼热金属](Heat_Metal.md "灼热金属")法术不同，罗兰的火球术术不会使受害者获得[武器掉落！](Weapon_Dropped!_(Condition).md "武器掉落！ (状态)")状态并掉落武器。

---
*Source: [Rolan's Fireball](https://bg3.wiki/wiki/Rolan's_Fireball)*