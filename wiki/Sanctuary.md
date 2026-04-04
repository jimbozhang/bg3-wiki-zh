# 庇护术

**庇护术**是一个[法术](Spells.md "法术")。它允许施法者保护自己或盟友免受敌人攻击。

## 描述

在你攻击或伤害一个生物之前，你或盟友无法被选为目标。你仍然可能受到影响范围法术的伤害。

在受影响的实体攻击或伤害另一个生物之前，它无法被敌人的攻击选为目标。但是，它仍然可能受到影响更大区域的法术伤害。

## 属性

消耗
[附赠动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
详情
范围：18米（60英尺）

## 更高环阶施法

以更高环阶施放此法术不会获得额外收益。

## 技术细节

UID

`Target_Sanctuary`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：庇护术

**[庇护术](Sanctuary_(Condition).md "庇护术（状态）")**

持续时间：10回合

- 受影响的实体无法被敌人的攻击或法术选为目标。但是，它仍然可能受到影响更大区域的法术伤害。如果受影响的实体攻击或伤害另一个生物，状态将结束，并会获得[庇护格挡](Sanctuary_Blocked_(Condition).md "庇护格挡（状态）")，持续1回合。

## 如何习得

职业：

- 职业等级1：[牧师](Cleric.md "牧师")
- 职业等级3：[奉献之誓](Oath_of_Devotion.md "奉献之誓")（誓约法术）
- 职业等级6：[逸闻学院](College_of_Lore.md "逸闻学院")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

由特性授予：

- [魔法学徒：牧师](Magic_Initiate_colon__Cleric.md "魔法学徒：牧师")

## 备注

- 受庇护术影响的生物可以使用多种动作和效果，这些会提前结束法术：
  - 命中或造成伤害的武器攻击
- 自伤伤害\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
- [推击](Shove.md "推击")
  - [投掷](Throw.md "投掷") – 这适用于任何物体，包括治疗药水\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
  - 由受庇护术影响的生物创造的地表或由地表施加的状态造成的伤害 – 无论地表何时被创造
  - 由受庇护术影响的生物施加的状态造成的伤害 – 无论状态何时被施加
    - 这不包括状态不归因于受庇护术影响的生物的情况，例如[歌唱之剑：尖叫](Singing_Sword_colon__Shriek_(Condition).md "歌唱之剑：尖叫（状态）")\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
  - 针对敌人的[反应](Actions.md#Reactions "动作")，例如：\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
    - [法术反制](Counterspell.md "法术反制")
    - [借机攻击](Opportunity_Attack.md "借机攻击") – 仅当命中时
    - [语出惊人](Cutting_Words.md "语出惊人")
- 受庇护术影响的生物可以使用一些看似有害的动作和效果，这些不会结束法术：
  - 未命中的武器攻击
  - 由受控召唤物造成的伤害
  - [催眠凝视](Hypnotic_Gaze.md "催眠凝视")
- [雪雨暴](Sleet_Storm.md "雪雨暴") * [月华之光](Moonbeam.md "月华之光") 或 [移动月华之光](Move_Moonbeam.md "移动月华之光") – 无论是否造成伤害
  - [烈焰复仇](Flaming_Revenge.md "烈焰复仇") 或 [异能复仇](Psionic_Revenge.md "异能复仇")
  - [预兆骰子](Portent_Die.md "预兆骰子") 或 [扭曲幸运：属性检定减值](Bend_Luck_colon__Ability_Check_Penalty.md "扭曲幸运：属性检定减值")
  - [造风术](Gust_of_Wind.md "造风术") 或 [繁彩球](Chromatic_Orb.md "繁彩球") – 假设未造成伤害\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]
- 庇护术的咒语是 _Mactē Virtutē_ ，拉丁语意为“以伟大的美德”。

## 错误

- 受庇护术影响的生物仍然可以被[枯萎术](Blight.md "枯萎术")、[链状闪电](Chain_Lightning.md "链状闪电")和[荆棘之鞭](Thorn_Whip.md "荆棘之鞭")选为目标，因为这些法术缺少 `IsHarmful` 法术标志。出于同样的原因，大量[NPC](NPC.md "NPC")动作（例如[尖利岩石](Sharp_Rock.md "尖利岩石")）可以选中受庇护术影响的生物。

## 外部链接

- ⁠[庇护术](https://forgottenrealms.fandom.com/wiki/Sanctuary) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Sanctuary](https://bg3.wiki/wiki/Sanctuary)*