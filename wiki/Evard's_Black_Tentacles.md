# 艾伐黑触手

**艾伐黑触手**是一个[4级咒法学派法术](Spells.md "法术")。它在区域内召唤触手，使移动变得困难并伤害生物。

## 描述

触手从地面冒出，将区域转变为[劣势地形](Difficult_Terrain_(Condition).md "劣势地形 (状态)")，攻击并[窒息](Black_Tentacles_(Condition).md "黑色触须 (状态)")区域内的生物。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术")
伤害：3~18

3d6⁠[钝击](Bludgeoning.md "钝击")（可通过[力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定")来避免）

详情
[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")
范围：18米（60英尺）
区域效果：6米（20英尺）半径
创造区域：黑色触须
[专注](Concentration.md "专注")

## 高阶施法

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_BlackTentacles`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：黑色触须

**[黑色触须](Black_Tentacles.md "黑色触须")**

持续时间：10回合

区域效果：6米（20英尺）半径

扭动的黑色触手充满区域，将其转变为[劣势地形](Difficult_Terrain_(Condition).md "劣势地形 (状态)")，并对所有进入的生物造成3~18⁠⁠[钝击](Bludgeoning.md "钝击")伤害并[窒息](Black_Tentacles_(Condition).md "黑色触须 (状态)")它们。

类型：[地表](Area.md#Surface "区域")

### 状态：黑色触须

**[黑色触须](Black_Tentacles_(Condition).md "黑色触须 (状态)")**

[力量](Strength.md "力量") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 被黑暗触须束缚。受影响实体无法移动，每回合受到3d6⁠⁠[钝击](Bludgeoning.md "钝击")伤害。

- 对受影响实体的[攻击掷骰](Attack_roll.md "攻击掷骰")具有[优势](Advantage.md "优势")，而该实体的攻击掷骰和[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")具有[劣势](Disadvantage.md "劣势")

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形 (状态)")**

- [移动速度](Movement_speed.md "移动速度")减半

## 学习方式

职业：

- 职业等级7：[法师](Wizard.md "法师")和[旧日支配者](The_Great_Old_One.md "旧日支配者")

由物品提供：

- [怪须护符](Strange_Tendril_Amulet.md "怪须护符")（充能：[长休](Long_Rest.md "长休")）

其他学习方式：

- 拥有[4级法术位](Spells.md#Spell_slots "法术位")的[法师](Wizard.md "法师")可以[抄录](Transcribing_scrolls.md "抄录卷轴")[艾伐黑触手卷轴](Scroll_of_Evard's_Black_Tentacles.md "艾伐黑触手卷轴")到他们的法术书中。

## 备注

- [黑色触须](Black_Tentacles_(Condition).md "黑色触须 (状态)")状态有两种可能效果：它可以阻止角色移动，并造成伤害。
  - 束缚有豁免检定，束缚可能在以下情况发生：
  - 法术施放时
  - 角色回合开始时
  - 重新进入区域时。
- 伤害仅在角色豁免失败_且_在回合开始前已有该状态时，在回合开始时造成。
- 受影响的角色似乎会失去所有移动速度，但实际上该状态的持续时间仅在_位于其地表上时_应用；这意味着如果角色逃离地表（例如使用[迷踪步](Misty_Step.md "迷踪步")），移动速度会恢复。相比之下，[网缚](Enwebbed_(Condition).md "网缚 (状态)")的持续时间为1，因此逃离网缚地表不会恢复移动速度。
- 如果角色在同一轮中较早受到武器伤害（至少，法术和拳头似乎没有此效果），则在施放法术时不受影响。然而，如果在同一回合稍后，该角色在受影响的地表中移动，则需要进行豁免检定。

## 视觉效果

加载视频

本地文件

本地文件可能会收集个人数据。

继续 关闭

<https://bg3.wiki/wiki/File:Evard%27s_Black_Tentacles_Visuals.mp4>

## 外部链接

- ⁠[艾伐黑触手](https://forgottenrealms.fandom.com/wiki/Evard%27s_black_tentacles) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Evard's Black Tentacles](https://bg3.wiki/wiki/Evard's_Black_Tentacles)*