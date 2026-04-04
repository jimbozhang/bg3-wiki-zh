# 沉默术

关于等效的 [暗影宗](Way_of_Shadow.md "暗影宗") 武僧动作，请参见 [暗影技艺：沉默](Shadow_Arts_colon__Silence.md "暗影技艺：沉默").

**沉默术** 是一个 [等级 2 幻术学派法术](Spells.md "Spells"). 它允许施法者在射程范围内召唤一个绝对寂静的球体区域。处于该球体内的生物免疫 ⁠[雷鸣](Thunder.md "雷鸣") 伤害，并且无法施放言语类法术。

## 描述

创造一个隔音球体。所有内部生物均处于 [沉默](Silenced_(Condition).md "沉默 (状态)") 状态，并且 [免疫](Damage_types.md#Immunity "伤害类型") ⁠[雷鸣](Thunder.md "雷鸣") 伤害。

使用此法术可能导致目标变为敌对。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [二级法术位](Spells.md#Spell_slots "法术")
详情
射程：18 米（60 英尺）
创造区域：沉默
[仪式](Spells.md#Ritual_spells "法术")
[专注](Concentration.md "专注")

## 升环施法效应

以此法术的更高等级施放不会获得额外收益。

## 技术细节

UID

`Target_Silence`

法术标志

`[CannotTargetItems](https://bg3.wiki/w/index.php?title=CannotTargetItems_\(spell_flag\)&action=edit&redlink=1) "CannotTargetItems \(spell_flag\) \(page does not exist\)")`, `[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsConcentration](IsConcentration_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 区域：沉默

**[沉默](Silence_(area).md "沉默 (区域)")**

持续时间：100 驱散
范围：6 米（20 英尺）半径
处于光环内的生物将处于 [沉默](Silenced_(Condition).md "沉默 (状态)") 状态。
类型：[召唤](Area.md#Summoned "区域")

### 状态：沉默

**[沉默](Silenced_(Condition).md "沉默 (状态)")**

- 生物无法说话或施放带有言语成分的法术，并且免疫 ⁠[雷鸣](Thunder.md "雷鸣") 伤害。

## 学习方式

职业：

- 职业等级 3：[吟游诗人](Bard.md "吟游诗人")、[牧师](Cleric.md "牧师") 和 [大地结社](Circle_of_the_Land.md "大地结社")（沙漠）
- 职业等级 5：[游侠](Ranger.md "游侠") 和 [奉献之誓](Oath_of_Devotion.md "奉献之誓")（誓言法术）

其他学习方式：

- 选择 [异界恩赐](Eldritch_Invocation.md "异界恩赐") [远古奥秘之书](Book_of_Ancient_Secrets.md "远古奥秘之书") 的 [邪术师](Warlock.md "邪术师") 在 7 级以上时也会获得此法术。以此方式获得时，该法术可每 [长休](Long_Rest.md "长休") 施放一次，且不消耗 [法术位](Spells.md#Spell_Slots "法术")。

## 备注

- 沉默术不影响 [法术反制](Counterspell.md "法术反制")。
- 沉默术阻止与受影响角色/实体发起对话。
- 在包含中立 NPC 的区域施放此法术可能引发战斗。
- 沉默术有两种咒语：**Silencio**（拉丁语，意为“沉默”）和 **Te Astringo Lingua**（拉丁语，意为“我束缚你的舌头”）。

## 外部链接

- ⁠[沉默术](https://forgottenrealms.fandom.com/wiki/Silence) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Silence](https://bg3.wiki/wiki/Silence)*