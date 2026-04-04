# 战斗法师之力手套

本文已被标记为过时，可能需要更新。笔记与错误之间存在差异。需要测试和验证。用户报告使用[破影利刃](Shadow_Blade.md "破影利刃")无法获得奥术敏锐。当文章更新后请移除此通知。

战斗法师之力手套是一双稀有[手套](Handwear.md "手部装备")。当穿戴者用使用武器的法术或戏法命中目标时，可获得[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")。

当手套指尖相触时，蓝色光带会闪烁收缩——这是连接它们的奥术极性的证明。

## 属性

- [手套](Gloves.md "手套")
- 稀有度：稀有
- 重量：0.5 千克（1 磅）
- 价格：290 gp
- UID `MAG_Gish_Acute_Gloves` UUID `15381544-e616-46e6-a881-0af793971863` 统计 `MAG_Gish_Acute_Gloves` 文件 `ARM_Gloves_Metal_I` ### 特殊

该物品穿戴者获得：

- [力量](Strength.md "力量") [豁免检定](Saving_throw.md "豁免检定") +1

[战斗法师之力](Battlemage's_Power.md "战斗法师之力")
当您用使用武器的法术或戏法命中目标时，您获得[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")。

## 状态：奥术敏锐

**[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐（状态）")**

- 受影响实体在剩余回合内，其[法术](Spells.md "法术")[攻击掷骰](Attack_roll.md "攻击掷骰")和[法术豁免DC](Saving_throw.md#The_Difficulty_Class_of_saving_throws "豁免检定")获得+1加值。
- 每次实体受到伤害时，持续时间减少2。
- **奥术敏锐**最大持续时间：10回合。

## 获取地点

- [雷斯文征税所](Reithwin_Tollhouse.md "雷斯文征税所") X: -84 Y: -88：在二楼带两扇锁门的房间内，一个上锁的华丽箱子中

## 备注

- 可使用DC 10[巧手](Sleight_of_Hand.md "巧手")[检定](Ability_Check.md "属性检定")来打开包含这些手套的箱子。
- 这些手套的功能在补丁8中被重新设计。

_关于战斗法师之力：_

- 可触发此效果的法术包括：
  - 任何[至圣斩](Smite.md "至圣斩")法术（以及[至圣斩](Divine_Smite.md "至圣斩")）。施放至圣斩法术然后用神圣至圣斩反应会触发战斗法师之力两次。
  - [轰鸣剑](Booming_Blade.md "轰鸣剑")
- [诱捕打击（近战）](Ensnaring_Strike_(Melee).md "诱捕打击（近战）")和[诱捕攻击（远程）](Ensnaring_Strike_(Ranged).md "诱捕攻击（远程）")
  - [荆雹术](Hail_of_Thorns.md "荆雹术")
  - 当主手装备[火焰刀](Flame_Blade.md "火焰刀")或[破影利刃](Shadow_Blade.md "破影利刃")时造成的任何伤害。伤害可来自任何来源，如武器攻击、法术伤害（包括[魔法飞弹](Magic_Missile.md "魔法飞弹")的每个飞镖），甚至来自状态效果的伤害，如[燃烧](Burning_(Condition).md "燃烧（状态）")。如果召唤武器在副手，即使使用召唤武器攻击，战斗法师之力也不会触发。

## 错误

_关于战斗法师之力：_

- 建议读者注意，**战斗法师之力**似乎是游戏中最复杂且最不直观的行为之一，使得难以区分什么是真正的错误。
  - 当主手装备火焰刀时造成的任何伤害都会触发战斗法师之力。伤害可来自任何来源，如武器攻击、法术伤害（包括[魔法飞弹](Magic_Missile.md "魔法飞弹")的每个飞镖），甚至来自状态效果的伤害，如[燃烧](Burning_(Condition).md "燃烧（状态）")。如果召唤武器在副手，即使使用召唤武器攻击，战斗法师之力也不会触发。此效果过去在主手装备破影利刃时也有效，但在补丁8后的热修复中被移除。
  - 战斗法师之力与[梅菲斯特提夫林](Mephistopheles_Tiefling.md "梅菲斯特提夫林")版本的火焰刀不兼容，因为此版本应用了不同的状态，未在`ArcaneAcuityGlovesCondition() .khn`脚本中列出。
  - 投掷[治疗药水](Potions.md#Healing_Potions "药水")和[手雷](Grenades.md "手雷")会触发战斗法师之力，即使未命中任何目标。
  - 反应至圣斩仅在触发攻击提供敏锐时才提供敏锐。如果源攻击触发了战斗法师之力，反应至圣斩会再次触发它们，总共+4敏锐。
  - 以下所有效果都提供敏锐：
    - 持续性的范围法术效果，如[死云术](Cloudkill.md "死云术")和[火墙术](Wall_of_Fire.md "火墙术")
    - 游戏中每个造成归因于穿戴者伤害的状态都会触发战斗法师之力。例如，[燃烧](Burning_(Condition).md "燃烧（状态）")和[电击](Electrocuted_(Condition).md "电击（状态）")。
    - 穿戴者造成的坠落伤害
    - 一些杂项效果，如[圣枪头盔](Holy_Lance_Helm.md "圣枪头盔")
  - 报偿效果，如[艾嘉西斯之铠](Armour_of_Agathys.md "艾嘉西斯之铠")和[灼热复仇盾牌](Shield_of_Scorching_Reprisal.md "灼热复仇盾牌")不会触发战斗法师之力。
  - 战斗法师之力本应具有`OncePerAttack`限制，意味着它们应仅在每次伤害事件中提供一次敏锐。然而，OncePerAttack限制会在玩家角色执行任何针对游戏内实体的效果时重置，无论该实体是敌人、盟友还是穿戴者本人。
    - 这包括常规攻击以及自我目标能力，如[疾走](Dash.md "疾走")和[狂暴](Rage.md "狂暴")。
    - 这还包括游戏认为是“攻击”的效果（由于底层代码），例如：使用表演动作（包括战斗中）、与[感知护符](Sentient_Amulet.md "感知护符")对话（包括战斗中）、用属性检定版本的[扭曲幸运](Bend_Luck.md "扭曲幸运")瞄准某人，以及引发借机攻击（尽管如果穿戴者因此受到伤害，他们会失去2敏锐）。
  - 爆炸也会重置手套的每次攻击限制。这包括来自[当锤棒喝](Hamarhraft.md "当锤棒喝")和[发光护甲](Luminous_Armour.md "发光护甲")的范围“爆炸”，以及如[炼金火焰](Alchemist's_Fire.md "炼金火焰")和[粘性球茎](Caustic_Bulb.md "粘性球茎")等手雷。

## 图库

- [染色](Dye.md "染色")变体

---
*Source: [Gloves of Battlemage's Power](https://bg3.wiki/wiki/Gloves_of_Battlemage's_Power)*