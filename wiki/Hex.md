# 脆弱诅咒

**脆弱诅咒**是一个[法术](Spells.md "法术")。它允许施法者诅咒一个生物，并对其造成额外的黯蚀伤害。该诅咒还会使目标在你选择的属性检定上处于[劣势](Disadvantage.md "Disadvantage")。

## 描述

使你的攻击对目标造成额外的1d6⁠⁠[黯蚀](Necrotic.md "Necrotic")伤害，并使其在你选择的[属性值](Ability_Scores.md "属性值")上处于[劣势](Disadvantage.md "Disadvantage")。

如果目标在法术结束前死亡，你可以[再度施展脆弱诅咒](Reapply_Hex.md "Reapply Hex")到一个新生物上，而无需消耗[法术位](Spells.md#Spell_Slots "Spells")。

## 属性

消耗
[附赠动作](Actions.md#Resources "Actions") + [一级法术位](Spells.md#Spell_slots "Spells")
伤害：1~6

1d6⁠[黯蚀](Necrotic.md "Necrotic")（施法者每次攻击）

详情
射程：18米（60英尺）
[专注](Concentration.md "Concentration")

## 更高环阶施法

以此法术更高环阶施法不会获得额外收益。

## 技术细节

UID

`Target_Hex`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsLinkedSpellContainer](IsLinkedSpellContainer_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 变体

- [脆弱诅咒（力量）](Hex_(Strength).md "Hex (Strength)")
- [脆弱诅咒（敏捷）](Hex_(Dexterity).md "Hex (Dexterity)")
- [脆弱诅咒（体质）](Hex_(Constitution).md "Hex (Constitution)")
- [脆弱诅咒（智力）](Hex_(Intelligence).md "Hex (Intelligence)")
- [脆弱诅咒（感知）](Hex_(Wisdom).md "Hex (Wisdom)")
- [脆弱诅咒（魅力）](Hex_(Charisma).md "Hex (Charisma)")

## 状态：再度施展脆弱诅咒

**[再度施展脆弱诅咒](Reapply_Hex_(Condition).md "Reapply Hex (Condition)")**

- 可以施放脆弱诅咒而不消耗新的[法术位](Spell_Slot.md "Spell Slot")。

## 如何习得

职业：

- 职业等级1：[邪术师](Warlock.md "Warlock")
- 职业等级6：[逸闻学院](College_of_Lore.md "College_of_Lore")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）
- 职业等级10：[吟游诗人](Bard.md "Bard")（通过[魔法秘密](Magical_Secrets.md "Magical Secrets")）

由特性提供：

- [魔法学徒：邪术师](Magic_Initiate_colon__Warlock.md "Magic Initiate: Warlock")

## 注释

- “在你选择的属性上处于劣势”仅适用于选定的[_检定_](Dice_rolls.md#Ability_checks "Dice rolls")，而非使用该[属性](Abilities.md "Abilities")的_所有掷骰_：目标在[豁免检定](Saving_throws.md "Saving Throws")和[攻击掷骰](Attack_rolls.md "Attack Rolls")上仍正常掷骰。
- 如果目标在法术持续时间内死亡或倒地，获得[再度施展脆弱诅咒](Reapply_Hex.md "Reapply Hex")。在此状态下，施法者头顶会出现一个发光的破碎水晶。
- 脆弱诅咒的伤害可以多次施加，只要攻击由最初的邪术师施法者进行，且攻击掷骰成功。示例场景：
  - 邪术师用近战或远程武器攻击命中目标：额外1d6⁠⁠[黯蚀](Necrotic.md "Necrotic")。
  - 一级邪术师施放[魔能爆](Eldritch_Blast.md "Eldritch Blast")并命中目标：额外1d6⁠⁠[黯蚀](Necrotic.md "Necrotic")。
  - 五级邪术师施放[魔能爆](Eldritch_Blast.md "Eldritch Blast")并用_两道_射线命中目标：额外2d6⁠⁠[黯蚀](Necrotic.md "Necrotic")，因为命中两次。
  - 三级邪术师施放[灼热射线](Scorching_Ray.md "Scorching Ray")并用_所有三道_射线命中目标：额外3d6⁠⁠[黯蚀](Necrotic.md "Necrotic")，因为命中三次。
  - 五级邪术师施放[灼热射线](Scorching_Ray.md "Scorching Ray")并用_所有四道_射线命中目标：额外4d6⁠⁠[黯蚀](Necrotic.md "Necrotic")，因为命中四次。
- 脆弱诅咒仅在攻击掷骰成功命中目标时触发，而非由其他伤害来源触发。示例场景：
  - 邪术师施放[魔法飞弹](Magic_Missile.md "Magic Missile")（不需要攻击掷骰）：脆弱诅咒不造成额外伤害。
  - 邪术师施放[火球术](Fireball.md "火球术")（需要[豁免检定](Saving_throw.md "Saving Throw")，而非攻击掷骰）：脆弱诅咒不造成额外伤害。
- 与桌面版不同，此法术持续到施法者的专注被打破为止。
- 脆弱诅咒有两种咒语：**Te Exsecro**（拉丁语，意为“我诅咒你”）和**Maledictus**（拉丁语，意为“说坏话/虐待”）。

## 错误

- 如果一个生物被施加了脆弱诅咒，并对施法者发动重击，触发任何“命中/伤害”时伤害该被诅咒生物的能力，脆弱诅咒的伤害会与常规伤害一同翻倍。
  - 例如，一个地精邪术师对自己施放[艾嘉西斯之铠](Armour_of_Agathys.md "Armour_of_Agathys")，然后对莱埃泽尔施放脆弱诅咒。莱埃泽尔随后对地精邪术师发动重击，在此过程中受到5⁠⁠[寒冷](Cold.md "Cold")伤害（来自**艾嘉西斯之铠**）。这触发**脆弱诅咒**对莱埃泽尔造成额外1d6⁠⁠[黯蚀](Necrotic.md "Necrotic")，然后（错误地）因重击翻倍为2d6⁠⁠[黯蚀](Necrotic.md "Necrotic")。

## 外部链接

- ⁠[脆弱诅咒](https://forgottenrealms.fandom.com/wiki/Hex) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Hex](https://bg3.wiki/wiki/Hex)*