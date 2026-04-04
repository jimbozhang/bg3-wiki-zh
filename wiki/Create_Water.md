# 造水术

**造水术**是一个[1级变化学派法术](Spells.md "Spells")。该法术是[造水/枯水术](Create_or_Destroy_Water.md "造水/枯水术")的一个变体，允许施法者召唤一片从稀薄空气中降下的雨水，并形成一片水地表。法术施放时处于该区域内的生物将变为[濡湿](Wet_(Condition).md "濡湿 (状态)")。

## 描述

召唤降雨。它会熄灭暴露的火焰，并形成一片[水](Water_(surface).md "水 (地表)")地表。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [1级法术位](Spells.md#Spell_slots "法术")
详情
范围：9米（30英尺）
范围效果：4米（13英尺）半径
创造区域：水

## 升环施法

[升环施法](Upcasting.md "升环施法")：当以2级或更高法术位施放该法术时，你可创造水的区域会比1级法术位时每高1环增加2米（7英尺）。

## 技术细节

UID

`Target_CreateWater`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`, `[RangeIgnoreVerticalThreshold](https://bg3.wiki/w/index.php?title=RangeIgnoreVerticalThreshold_\(spell_flag\)&action=edit&redlink=1) "RangeIgnoreVerticalThreshold \(spell flag\) \(page does not exist\)")`

## 状态：濡湿

**[濡湿](Wet_(Condition).md "濡湿 (状态)")**

持续时间：3回合

- [免疫](Immune.md "免疫")于[燃烧](Burning_(Condition).md "燃烧 (状态)")和[狂野魔法：燃烧](Wild_Magic_colon__Burning_(Condition).md "狂野魔法：燃烧 (状态)")。
- [抗性](Resistant.md "抗性")于[火焰](Fire.md "火焰")伤害。
- [易伤](Vulnerable.md "易伤")于[闪电](Lightning.md "闪电")和[寒冷](Cold.md "寒冷")伤害。

## 区域：水

**[水](Water_(surface).md "水 (地表)")**

范围效果：4米（13英尺）半径

熄灭未受保护的火焰。可被电击或冻结。

类型：[地表](Area.md#Surface "区域")

## 如何习得

该法术是以下法术的变体：
[造水/枯水术](Create_or_Destroy_Water.md "造水/枯水术")

## 备注

- 任何处于隐形状态的角色若被该法术范围覆盖，将被显形，且无需进行豁免检定。
- 造水术的咒语是 _Pluo_（“雨”）和 _Aqua pura_（“纯水”）。
- 处于战斗外的隐藏角色可以对战斗内的角色施放此法术，而无需使用动作。虽然施法会使你显形并可能迫使你进入战斗，但创造此水的角色在战斗的第一回合仍将拥有一个动作可使用，如同他们未曾施放法术一样。

## 外部链接

- ⁠[造水术](https://forgottenrealms.fandom.com/wiki/Create_water) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上

---
*Source: [Create Water](https://bg3.wiki/wiki/Create_Water)*