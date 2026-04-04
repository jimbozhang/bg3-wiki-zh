# 灼热金属

**灼热金属**是一个[2级变化学派法术](Spells.md "法术")。它允许施法者加热目标生物身上的金属武器或护甲，迫使其松手或承受伤害或遭受各种惩罚。

## 描述

使金属武器或护甲炽热发红，迫使穿戴者松手或在[攻击掷骰](Attack_roll.md "攻击掷骰")和[属性检定](Ability_Check.md "属性检定")上获得[劣势](Disadvantage.md "劣势")。

如果该生物只穿着金属护甲，它总是获得劣势。

如果该生物仍然接触金属，你可以在后续回合使用附赠动作造成额外的2d8⁠⁠[火焰](Fire.md "火焰")伤害，并迫使该生物松手或获得劣势。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [2级法术位](Spells.md#Spell_slots "法术")
伤害：2~16

2d8⁠[火焰](Fire.md "火焰")

详情
[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定")（豁免成功时：目标承受全额伤害，但攻击掷骰获得[劣势](Disadvantage.md "劣势")，而非被缴械）
射程：18米（60英尺）
[专注](Concentration.md "专注")

## 升环施法效果

[升环施法](Upcasting.md "升环施法")：以更高环位施放此法术时，每比2环高1环，额外造成1d8⁠⁠[火焰](Fire.md "火焰")伤害。

## 技术细节

UID

`Target_HeatMetal`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsHarmful](IsHarmful_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 赋予

- [重新施放灼热金属](Reapply_Heat_Metal.md "重新施放灼热金属")

## 状态：武器掉落

**[武器掉落！](Weapon_Dropped!_(Condition).md "武器掉落！ (状态)")**

[体质](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- 敌人使你将武器掉落在地，类似于[缴械](Disarmed_(Condition).md "缴械 (状态)")。

## 状态：灼热金属：劣势

**[灼热金属：劣势](Heat_Metal_colon__Disadvantage_(Condition).md "灼热金属：劣势 (状态)")**

持续时间：1回合

- 在施法者的下一回合开始前，[攻击掷骰](Attack_roll.md "攻击掷骰")和[属性检定](Ability_Check.md "属性检定")具有[劣势](Disadvantage.md "劣势")。

## 状态：灼热金属

**[灼热金属](Heat_Metal_(Condition).md "灼热金属 (状态)")**

持续时间：10回合

- 使目标生物身上的金属武器或护甲发热，无需豁免（优先武器）。
- 如果持有金属武器的生物未能通过其初始[豁免检定](Saving_throw.md "豁免检定")，则武器会掉落。
- 如果该生物接触发热的金属物品，其[攻击掷骰](Attack_roll.md "攻击掷骰")和[属性检定](Ability_Check.md "属性检定")将获得[劣势](Disadvantage.md "劣势")。
- 每后续回合，如果该生物仍接触金属，施法者可使用[重新施放灼热金属](Reapply_Heat_Metal.md "重新施放灼热金属")造成额外的2d8⁠⁠[火焰](Fire.md "火焰")伤害，迫使该生物再次通过豁免检定或掉落物品（如果是金属武器）。

## 学习方式

职业：

- 职业等级3：[吟游诗人](Bard.md "吟游诗人")和[德鲁伊](Druid.md "德鲁伊")

生物使用：[岩浆魔蝠](Magma_Mephit.md "岩浆魔蝠")

其他学习方式：

- 没有可供[法师](Wizard.md "法师")[抄录](Transcribing_scrolls.md "抄录卷轴")到其法术书的卷轴。

## 备注

- 由[灼热金属](Heat_Metal_(Condition).md "灼热金属 (状态)")状态提供的附赠动作施放，与主施放一样享受相同的升环伤害加成。
- 附赠动作重施放在施法者的下一回合前不可用。
- 拥有火焰抗性或免疫不会阻止武器缴械效果。
- [重新施放灼热金属](Reapply_Heat_Metal.md "重新施放灼热金属")是一个“赋予”法术，或可[重施放](Category_colon_Recastable_spells.md "类别：可重施放法术")的法术。_赋予法术_在施放原始法术后发放给施法者，只要[专注](Concentration.md "专注")未被打破，即可再次施放而无需消耗另一个法术位。此类赋予法术不直接与施法者的已知法术库（即游戏中的法术书图标）相关联。因此，如果在身兼多职时施放赋予法术，后续重施放（本例中为[重新施放灼热金属](Reapply_Heat_Metal.md "重新施放灼热金属")）使用最近获得的施法职业的施法调整值，而非初始施放灼热金属时使用的施法调整值。在这种情况下，可能导致法术豁免DC意外偏低。

## 错误

- 由于编码错误，为目标提供劣势的状态（在成功豁免后应用）会在目标被移除另一个无关状态时被移除。
  - 此特定错误仅影响此法术的2环版本。
- 由于编码错误，为目标提供劣势的状态在灼热金属法术提前结束时_不会_自动移除。
  - 此特定错误影响此法术的所有环位。
- 4环施放的灼热金属仅造成2d8⁠⁠[火焰](Fire.md "火焰")伤害，且其工具提示不显示重新施放灼热金属造成的伤害。
  - 此外，它缺少此法术其他环位中的几个功能器。
  - 4环施放的重新施放灼热金属正确造成4d8⁠⁠[火焰](Fire.md "火焰")伤害。
- 5环和6环施放的重新施放灼热金属错误地将其工具提示伤害显示为3环版本。

## 外部链接

- ⁠[灼热金属](https://forgottenrealms.fandom.com/wiki/Heat_metal) 在 [被遗忘的国度Wiki](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Heat Metal](https://bg3.wiki/wiki/Heat_Metal)*