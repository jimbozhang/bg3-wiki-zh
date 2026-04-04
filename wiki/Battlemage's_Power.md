# 战斗法师之力

**战斗法师之力**是一个被动特性，当使用者通过武器攻击法术对敌人造成伤害时，会增强其施法能力。

## 描述

当你用使用武器的法术或戏法击中目标时，你获得[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")。

### 详情

充能：每次攻击

## 状态：奥术敏锐

**[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")**

持续时间：2 回合

- 受影响实体在每个剩余回合中，其[法术](Spells.md "法术")[攻击掷骰](Attack_roll.md "攻击掷骰")和[法术豁免DC](Saving_throw.md#The_Difficulty_Class_of_saving_throws "豁免检定")获得 +1 加值。
- 实体每次受到伤害时，持续时间减少 2。
- **奥术敏锐**的最大持续时间：10 回合。

## 如何习得

由装备提供：

- [战斗法师之力手套](Gloves_of_Battlemage's_Power.md "战斗法师之力手套")

## 备注

- 可以触发此效果的法术包括：
  - 任何[至圣斩](Smite.md "至圣斩")法术（以及[至圣斩](Divine_Smite.md "至圣斩")）。施放至圣斩法术然后以至圣斩反应将触发战斗法师之力两次。
  - [轰鸣剑](Booming_Blade.md "轰鸣剑")
- [诱捕打击（近战）](Ensnaring_Strike_(Melee).md "诱捕打击（近战）")和[诱捕攻击（远程）](Ensnaring_Strike_(Ranged).md "诱捕攻击（远程）")
  - [荆雹术](Hail_of_Thorns.md "荆雹术")
  - 当主手装备[火焰刀](Flame_Blade.md "火焰刀")或[破影利刃](Shadow_Blade.md "破影利刃")时造成的任何伤害。伤害可以来自任何来源，例如武器攻击、法术伤害（包括[魔法飞弹](Magic_Missile.md "魔法飞弹")的每个飞镖），甚至来自状态效果的伤害，如[燃烧](Burning_(Condition).md "燃烧（状态）")。如果召唤武器在副手，即使使用召唤武器攻击，战斗法师之力也不会触发。

## 错误

- 读者请注意，**战斗法师之力**似乎是游戏中最复杂且最不直观的行为之一，使得难以区分哪些实际上是错误。
  - 当主手装备火焰刀时造成的任何伤害都会触发战斗法师之力。伤害可以来自任何来源，例如武器攻击、法术伤害（包括[魔法飞弹](Magic_Missile.md "魔法飞弹")的每个飞镖），甚至来自状态效果的伤害，如[燃烧](Burning_(Condition).md "燃烧（状态）")。如果召唤武器在副手，即使使用召唤武器攻击，战斗法师之力也不会触发。此效果过去在主手装备破影利刃时也有效，但在补丁 8 后的热修复中被移除。
  - 战斗法师之力不适用于[梅菲斯特提夫林](Mephistopheles_Tiefling.md "梅菲斯特提夫林")版本的火焰刀，因为此版本应用了不同的状态，未在 `ArcaneAcuityGlovesCondition() .khn` 脚本中列出。
  - 投掷[治疗药水](Potions.md#Healing_Potions "药水")和[手雷](Grenades.md "手雷")会触发战斗法师之力，即使未击中任何目标。
  - 反应至圣斩仅在触发攻击提供敏锐时才提供敏锐。如果源攻击触发了战斗法师之力，反应至圣斩会第二次触发它们，总共提供 +4 敏锐。
  - 以下所有都会提供敏锐：
    - 持续的区域法术效果，如[死云术](Cloudkill.md "死云术")和[火墙术](Wall_of_Fire.md "火墙术")
    - 游戏中造成归因于穿戴者伤害的每个状态都会触发战斗法师之力。例如，[燃烧](Burning_(Condition).md "燃烧（状态）")和[电击](Electrocuted_(Condition).md "电击（状态）")。
    - 穿戴者造成的坠落伤害
    - 一些杂项效果，如[圣枪头盔](Holy_Lance_Helm.md "圣枪头盔")
  - 报偿效果，如[艾嘉西斯之铠](Armour_of_Agathys.md "艾嘉西斯之铠")和[灼热复仇盾牌](Shield_of_Scorching_Reprisal.md "灼热复仇盾牌")不会触发战斗法师之力。
  - 战斗法师之力本应具有 `OncePerAttack` 限制，意味着每个伤害事件只应提供一次敏锐。然而，每当玩家角色执行任何针对游戏内实体的效果时，OncePerAttack 限制都会重置，无论该实体是敌人、盟友还是穿戴者本人。
    - 这包括常规攻击以及自我目标能力，如[疾走](Dash.md "疾走")和[狂暴](Rage.md "狂暴")。
    - 这还包括游戏认为是“攻击”的效果（由于底层代码），例如：使用表演动作（包括在战斗中）、与[感知护符](Sentient_Amulet.md "感知护符")交谈（包括在战斗中）、以属性检定版本的[扭曲幸运](Bend_Luck.md "扭曲幸运")瞄准某人，以及引发借机攻击（尽管如果穿戴者因此受到伤害，他们会失去 2 敏锐）。
  - 爆炸也会重置手套的每次攻击限制。这包括来自[当锤棒喝](Hamarhraft.md "当锤棒喝")和[发光护甲](Luminous_Armour.md "发光护甲")的区域“爆炸”，以及[炼金火焰](Alchemist's_Fire.md "炼金火焰")和[粘性球茎](Caustic_Bulb.md "粘性球茎")等手雷。

## 参考

来自 `Mods/Shared/Scripts/thoth/helpers/CommonConditions.khn` 中 `ArcaneAcuityGlovesCondition()` 的定义：

显示代码

function ArcaneAcuityGlovesCondition()
return IsSmiteSpells()
| SpellId('Target_BoomingBlade_ClassSpell') | IsSpellChildOrVariantFromContext('Target_BoomingBlade_ClassSpell') | SpellId('Target_BoomingBlade') | IsSpellChildOrVariantFromContext('Target_BoomingBlade') | SpellId('Target_EnsnaringStrike') | SpellId('Projectile_EnsnaringStrike') | IsSpellChildOrVariantFromContext('Target_EnsnaringStrike') | IsSpellChildOrVariantFromContext('Projectile_EnsnaringStrike') | SpellId('Projectile_HailOfThorns') | IsSpellChildOrVariantFromContext('Projectile_HailOfThorns') | HasStatus('FLAME_BLADE',GetActiveWeapon()) | HasStatus('FLAME_BLADE_4',GetActiveWeapon()) | HasStatus('FLAME_BLADE_6',GetActiveWeapon()) | HasStatus('SHADOW_BLADE',GetActiveWeapon()) | (IsSpell() & IsWeaponAttack()) |
end

---
*Source: [Battlemage's Power](https://bg3.wiki/wiki/Battlemage's_Power)*