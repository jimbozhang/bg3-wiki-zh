# 剑刃屏障

**剑刃屏障**是一个[6级塑能学派法术](Spells.md "法术")。它允许施法者召唤一堵切割之刃的墙壁。

## 描述

召唤一堵锋利的刀刃之墙，将区域变成[劣势地形](Difficult_Terrain.md "劣势地形")，并对任何愚蠢到靠近的人造成伤害。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [6级法术位](Spells.md#Spell_slots "法术位")
伤害：6~60

6d10⁠[挥砍](Slashing.md "挥砍")

详情
[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
创造区域：剑刃屏障
[专注](Concentration.md "专注")

## 更高环阶

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Wall_BladeBarrier`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：剑刃屏障

**[剑刃屏障](Blade_Barrier_(area).md "剑刃屏障 (区域)")**

持续时间：60驱散

范围效果：36米（120英尺）线型

类型：[召唤](Area.md#Summoned "区域")

### 状态：剑刃屏障

**[剑刃屏障](Blade_Barrier_(Condition).md "剑刃屏障 (状态)")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 靠近屏障的生物会被切开、劈开、切割和雕刻，就像血染砧板上的肉一样。
- 受影响的实体每驱散受到6d10⁠⁠[挥砍](Slashing.md "挥砍")伤害。

## 如何习得

职业：

- 职业等级11：[牧师](Cleric.md "牧师")

## 错误

- 此法术豁免检定的DC无法正常运作：
  - 施放并进入墙壁时造成伤害的初始法术豁免DC固定为15。
  - 在墙壁内开始驱散的DC固定为3。
  - 在墙壁附近开始驱散的DC固定为10。

## 外部链接

- ⁠[剑刃屏障](https://forgottenrealms.fandom.com/wiki/Blade_barrier) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Blade Barrier](https://bg3.wiki/wiki/Blade_Barrier)*