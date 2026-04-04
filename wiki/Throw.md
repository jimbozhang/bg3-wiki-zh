# 投掷

**投掷**是一种常见的[动作](Action.md "动作")，允许使用者投掷特定的[武器](Weapon.md "武器")、[消耗品](Consumables.md "消耗品")、环境物品，甚至其他生物。

## 描述

投掷世界或你物品栏中的角色或物品。

你的[力量](Strength.md "力量")影响你能投掷的重量。越重的物品造成越多伤害。

具有[投掷攻击](Thrown.md "投掷攻击")属性的武器的伤害与其近战伤害相同。

## 属性

消耗：
[动作](Actions.md#Resources "动作")
伤害：
正常武器伤害
详情：
[攻击掷骰](Attack_roll.md "攻击掷骰")
范围：3-18米（10-60英尺）

范围取决于物品的重量，见下文。从地面拾取物品的范围是范围：1米（3英尺）半径

- 伤害：
  - 对于具有[投掷攻击](Thrown.md "投掷攻击")属性的武器，伤害和伤害类型与武器的近战伤害相同。
  - 对于其他物品和生物，伤害由被投掷物品的重量<sup>[\[1\]](#cite_note-creature_weight-1)</sup>决定：
    - 轻型物品，重量低于：10千克（20磅）：
  1⁠⁠[钝击](Bludgeoning.md "钝击")伤害
    - 中型物品，重量：10千克（20磅） - 50千克 / 100磅：
  1d4⁠⁠[钝击](Bludgeoning.md "钝击")伤害
    - 重型物品，重量超过：50千克（100磅）：
  2d4⁠⁠[钝击](Bludgeoning.md "钝击")伤害
- 如果被投掷的物品或生物超过目标重量的一半，目标会被击退2米（7英尺）。<sup>[\[1\]](#cite_note-creature_weight-1)</sup>
- 如果被投掷的物品或生物比目标更重，目标会变为[倒伏](Prone_(Condition).md "倒伏 (状态)")（*无*豁免检定）。<sup>[\[1\]](#cite_note-creature_weight-1)</sup>
- 被投掷的生物总是以[倒伏](Prone_(Condition).md "倒伏 (状态)")状态落地（*无*豁免检定）。
- 投掷生物需要成功的[运动](Athletics.md "运动")检定，使用与[推击生物](Shove.md#Roll "推击")相同的DC，但在隐藏时检定不具有优势。

## 范围

投掷攻击的范围取决于物品的重量（千克）和投掷者的力量属性，根据以下公式：<sup>[\[2\]](#cite_note-2)</sup>

round(3+15⋅15⋅Strength2−Weight2⋅Weight)

如果公式的输出低于3米，则调整为3米；如果高于18米，则调整为18米。

## 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏 (状态)")**

持续时间：1回合

- 受影响的生物无法移动或采取[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作")，并且在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 对倒伏生物的攻击在3米（10英尺）范围内进行时具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色站起仅需花费1.5米（5英尺）的移动速度。

## 备注

- 投掷是一个明确定义的动作，在游戏代码中具有详尽的交互列表。投掷是其自己的动作类型，与武器攻击分开，即使与[投掷攻击](Thrown.md "投掷攻击")武器一起使用也是如此。[武器动作](Weapon_actions.md "武器动作")明确定义为与武器攻击配合使用，因此不能与投掷一起使用。另一个主要后果是投掷武器不会触发大多数“命中”被动，除非下面提到的那些。此外，投掷武器不会应用任何固有的额外伤害（例如，[闪亮的碎颅锤](Shining_Staver-of-Skulls.md "闪亮的碎颅锤")的1d4⁠⁠[光耀](Radiant.md "光耀")伤害）或来自[涂层](Coatings.md "涂层")或[蘸取](Dip.md "蘸取")的任何伤害。
  - 以下交互被明确编码为与投掷配合工作：
    - [飞索鞋](Slinging_Shoes.md "飞索鞋")在被投掷时造成额外的2d4⁠⁠[心灵](Psychic.md "心灵")伤害。
    - [尼鲁纳](Nyrulna.md "尼鲁纳")在被投掷时在⁠6米（20英尺）爆炸范围内造成3d4⁠⁠[雷鸣](Thunder.md "雷鸣")伤害。
    - [闪电混语](Lightning_Jabber.md "闪电混语")在被投掷时造成额外的1d4⁠⁠[闪电](Lightning.md "闪电")伤害。
- [布布](Boo.md "布布")在被[明斯克](Minsc.md "明斯克")投掷时，可以使目标进行DC 15的[敏捷](Dexterity.md "敏捷")豁免检定，若失败则[目盲](Blinded_(Condition).md "目盲 (状态)")。
    - [矮人投手](Dwarven_Thrower.md "矮人投手")在被[矮人](Dwarf.md "矮人")投掷时造成额外的1d8⁠⁠[钝击](Bludgeoning.md "钝击")伤害，如果目标是大型、巨型或超巨型，则造成2d8⁠⁠[钝击](Bludgeoning.md "钝击")伤害。
    - 被[猎人印记](Hunter's_Mark.md "猎人印记")标记的生物在被投掷武器击中时会受到额外的1d6⁠⁠[武器](Weapon.md "武器")伤害。
    - [元素劈砍](Elemental_Cleaver.md "元素劈砍")的所有变体都会灌注武器，使其在被投掷时造成额外的1d6所选元素类型的伤害。
  - [投掷之戒](Ring_of_Flinging.md "投掷之戒")和[不羁库席戈的手套](Gloves_of_Uninhibited_Kushigo.md "不羁库席戈的手套")为所有投掷攻击提供额外的1d4⁠⁠[武器](Weapon.md "武器")伤害。
  - 任何*不*检查近战或武器攻击掷骰的武器伤害增益*都*会应用于投掷武器攻击。例子包括[狂暴](Rage.md "狂暴")、[腐蚀指环](Caustic_Band.md "腐蚀指环")、[黯狱手套](Helldusk_Gloves.md "黯狱手套")、[十字军披风](Crusader's_Mantle.md "十字军披风")等。
- 生物可以投掷重量高达0.2⋅STR2千克的物品和其他生物。<sup>[\[3\]](#cite_note-3)</sup> 例如，力量属性为18时，投掷的重量限制为64.8千克（129.6磅）。
  - 需要力量至少20才能举起一个中型类人生物（75千克（150磅））。
- 投掷会触发[额外攻击](Extra_Attack.md "额外攻击")，并且可以在触发额外攻击后无需[动作](Actions.md#Resources "动作")使用。
- [狂战士](Berserker.md "狂战士")野蛮人拥有改进的投掷能力[愤怒投掷](Enraged_Throw.md "愤怒投掷")。
- [酒馆殴斗者](Tavern_Brawler.md "酒馆殴斗者")专长显著提高投掷伤害。
- 被投掷的物品和生物如果从足够高的高度投掷，会受到[坠落伤害](Falling_damage.md "坠落伤害")（并可能造成碾压伤害）。
- [誓缚武器](Bound_Weapon_(Condition).md "誓缚武器 (状态)")在被投掷时会返回给使用者，但如果它们本身没有投掷属性，则*不会*获得投掷属性。
- 从角色物品栏中投掷[归巢武器](Homing_Weapon.md "归巢武器")或誓缚武器会导致它们装备到主手，而无需消耗动作。

## 错误

- 如果一个生物在高地上被投掷武器杀死，但并非死于投掷攻击本身，而是死于武器坠落的碾压伤害，则其死亡可能不会授予经验值；在这种情况下，游戏会将被杀死的目标视为被中立实体杀死，而非攻击者。

## 脚注

1. ↑ [1.0](#cite_ref-creature_weight_1-0) [1.1](#cite_ref-creature_weight_1-1) [1.2](#cite_ref-creature_weight_1-2) 活体生物的重量不受其装备或物品栏内物品的影响；它与其[体型](Creature_size.md "生物体型")相关，可以通过点击“检查 -> 详细信息”并在“重量：”下查看。
1. [↑](#cite_ref-2) 参数由`Public/Shared/Stats/Generated/Data/Data.txt`中定义的`ThrowDistanceMin`、`ThrowDistanceMax`、`ThrowWeightMultiplier`和`ThrowStrengthCapMultiplier`确定。
1. [↑](#cite_ref-3) 源自`Scripts/thoth/helpers/CommonConditions.khn`中`CanImprovisedWeaponWeight()`的定义。

---
*Source: [Throw](https://bg3.wiki/wiki/Throw)*