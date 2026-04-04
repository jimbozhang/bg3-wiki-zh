# 地狱火撕裂

**地狱火撕裂**是一个[戏法](Spells.md "法术")。它是[地狱火巨斧](Hellfire_Greataxe.md "地狱火巨斧")赋予的独特攻击，能够劈开一片区域，并用致命的地狱火覆盖它。

## 描述

喷吐地狱烈火并打击你的敌人。

地狱火无视[抗性](Resistance.md "抗性")和[免疫](Damage_types.md#Immunity "伤害类型")于[火焰](Fire.md "火焰")伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：2~12

普通武器伤害

+ 2d6[火焰](Fire.md "火焰")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")) (若豁免成功：目标仍承受一半伤害。)
范围：3米（10英尺）锥形
创造区域：地狱火
充能：[短休](Short_rest.md "短休")

## 技术细节

UID

`Zone_MAG_Automaton_Human_Steelwatcher_HellfireCleave`

法术标志

`[CanAreaDamageEvade](CanAreaDamageEvade_(spell_flag).md)`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[IsDefaultWeaponAction](https://bg3.wiki/w/index.php?title=IsDefaultWeaponAction_\(spell_flag\)&action=edit&redlink=1) "IsDefaultWeaponAction \(spell flag\) \(page does not exist\)")`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：翻腾地狱火

**[翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火 (状态)")**

持续时间：1回合

- 来自阿弗纳斯核心的火焰吞噬此实体，每回合造成6d6[火焰](Fire.md "火焰")伤害。

## 区域：地狱火

**[地狱火](Hellfire.md "地狱火")**

持续时间：2回合
范围：3米（10英尺）锥形

每回合造成6d6火焰伤害，无视[抗性](Resistant.md "抗性")和[免疫](Immune.md "免疫")。

类型：[地表](Area.md#Surface "区域")

### 状态：翻腾地狱火

**[翻腾地狱火](Roiling_Hellfire_(Condition).md "翻腾地狱火 (状态)")**

- 来自阿弗纳斯核心的火焰吞噬此实体，每回合造成6d6[火焰](Fire.md "火焰")伤害。

## 如何习得

由物品赋予：

- [地狱火巨斧](Hellfire_Greataxe.md "地狱火巨斧")

## 备注

- 此武器动作不计入[额外攻击](Extra_Attack.md "额外攻击")的攻击次数，且需要消耗完整的[动作](Actions.md#Resources "动作")来使用。
- 相反，它实际上被归类为戏法，这会导致一些意外的交互。
- 它可以被[法术反制](Counterspell.md "法术反制")。
  - [术士](Sorcerer.md "术士")可以对其应用[超魔](Metamagic.md "超魔")。适用的选项包括[超魔：谨慎法术](Metamagic_colon__Careful_Spell.md "超魔：谨慎法术")、[超魔：延长法术](Metamagic_colon__Extended_Spell.md "超魔：延长法术")、[超魔：高强法术](Metamagic_colon__Heightened_Spell.md "超魔：高强法术")、[超魔：默发法术](Metamagic_colon__Subtle_Spell.md "超魔：默发法术")，以及可能最重要的[超魔：瞬发法术](Metamagic_colon__Quickened_Spell.md "超魔：瞬发法术")。
  - 它受益于法术和戏法特定的伤害加成，如[元素亲和：伤害](Elemental_Affinity_colon__Damage.md "元素亲和：伤害")和[元素强化项链](Necklace_of_Elemental_Augmentation.md "元素强化项链")。
  - 它会激活[奥法骑士](Eldritch_Knight.md "奥法骑士")的[战斗魔法](War_Magic.md "战斗魔法")。
  - 在[沉默](Silenced_(Condition).md "沉默 (状态)")状态下仍可施放。
  - 在[狂暴](Rage.md "狂暴")状态下无法施放。
  - 翻腾地狱火状态由武器动作本身和它创造的[地狱火](Hellfire.md "地狱火")区域施加。即使目标豁免了攻击，它仍会因区域效果而承受翻腾地狱火。

## 错误

- 尽管工具提示说地狱火无视抗性和免疫，但它实际上并不无视。
- 由于此攻击不涉及攻击掷骰，它无法受益于某些检查攻击掷骰类型的额外伤害来源，尽管工具提示上列出了额外伤害。这些包括：
- [奥术协同](Arcane_Synergy_(Condition).md "奥术协同 (状态)")
- [巨武器大师：全力一击](Great_Weapon_Master_colon__All_In.md "巨武器大师：全力一击")
  - [猎人印记](Hunter's_Mark.md "猎人印记")
  - [准备](Prepare.md "准备")
- [怒火](Wrath_(Condition).md "怒火 (状态)")

## 视觉效果

<https://bg3.wiki/wiki/File:Hellflame_Cleave_Action.mp4>

---
*Source: [Hellflame Cleave](https://bg3.wiki/wiki/Hellflame_Cleave)*