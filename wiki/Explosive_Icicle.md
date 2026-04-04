# 三棱冰柱

**三棱冰柱**是[水元素执政官](Water_Myrmidon.md "水元素执政官")的动作。元素执政官使用此能力发射三枚爆炸性冰弹，冻结周围地面。

## 描述

投掷三把由闪亮冰晶锻造的三叉戟，穿透目标并在命中时创造冰面。

## 属性

消耗
[动作](Actions.md#Resources "动作")
伤害：9~72

3d8⁠[寒冷](Cold.md "寒冷")

\+ 3d8⁠[寒冷](Cold.md "寒冷")

\+ 3d8⁠[寒冷](Cold.md "寒冷")

详情
远程法术 [攻击掷骰](Attack_roll.md "攻击掷骰")
射程：18米（60英尺）
范围：2米（7英尺）半径
创造区域：冰

## 技术细节

UID

`Projectile_ExplosiveIcicle_Myrmidon_Water`

NPC和召唤元素执政官使用的版本

`Projectile_ExplosiveIcicle_Wildshape_Myrmidon_Water`

荒野形态中使用的版本，造成魔法伤害

法术标志

`[IsMelee](IsMelee_(spell_flag).md)`, `[Wildshape](https://bg3.wiki/w/index.php?title=Wildshape_\(spell_flag\)&action=edit&redlink=1) "Wildshape \(spell_flag\) \(页面不存在\)")`

## 区域：冰

**[冰](Ice_(surface).md "冰（地表）")**

持续时间：2回合
范围：2米（7英尺）半径
劣势地形 - [移动速度](Movement_speed.md "移动速度")减半，生物可能倒伏。

类型：[地表](Area.md#Surface "区域")

### 状态：倒伏

**[倒伏](Prone_(Condition).md "倒伏（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[法术豁免DC](Dice_rolls.md#Spell_save_DC "掷骰")）

- 受影响的生物无法移动或进行[动作](Actions.md#Resources "动作")、[附赠动作](Actions.md#Resources "动作")或[反应](Actions.md#Reactions "动作"），并在[力量](Strength.md "力量")和[敏捷](Dexterity.md "敏捷")[豁免检定](Saving_throw.md "豁免检定")上具有[劣势](Disadvantage.md "劣势")。
- 在距离生物3米（10英尺）内进行的攻击对倒伏生物具有[优势](Advantage.md "优势")。
- 倒伏生物必须花费其一半的[移动速度](Movement_speed.md "移动速度")才能站起。
  - 拥有[运动员](Athlete.md "运动员")专长的角色仅需花费1.5米（5英尺）的移动速度即可站起。

### 状态：劣势地形

**[劣势地形](Difficult_Terrain_(Condition).md "劣势地形（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半

## 如何习得

由以下生物使用：[水元素执政官](Water_Myrmidon.md "水元素执政官")

## 备注

- 三枚投射物可以独立瞄准。
- 每个投射物在爆炸范围内击中每个目标时，都会进行一次单独的攻击掷骰。
- 盟友可能受到爆炸的附带伤害，但不会对元素执政官本身造成伤害。
- 此能力使用远程法术攻击掷骰。通过[召唤元素生物：水元素执政官](Conjure_Elemental_colon__Water_Myrmidon.md "召唤元素生物：水元素执政官")召唤的元素执政官的施法关键属性是[智力](Intelligence.md "智力")，但其智力属性仅为8。因此，当由召唤的元素执政官使用此能力时，其准确性将远低于由德鲁伊使用[荒野形态：水元素执政官](Wild_Shape_colon__Water_Myrmidon.md "荒野形态：水元素执政官")时。

---
*Source: [Explosive Icicle](https://bg3.wiki/wiki/Explosive_Icicle)*