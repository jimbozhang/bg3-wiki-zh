# 超魔：成双法术

**超魔：成双法术** 是 [术士](Sorcerer.md "术士") 使用的可切换被动特性。此能力允许术士对特定 [法术](Spell.md "法术") 的两个目标生效。

## 描述

仅以单个生物为目标的法术可以额外以一个生物为目标。

每使用一个 [法术位](Sorcerer.md#Spell_Slots "术士") 等级消耗 1 [术法点](Sorcery_Point.md "术法点")。[戏法](Spells.md#Cantrips "法术") 也消耗 1 [术法点](Sorcery_Point.md "术法点")。

对于不发射投射物的法术，目标需要足够靠近。

### 详情

可切换

## 如何习得

职业：

- 职业等级 2：[术士](Sorcerer.md "术士")

生物使用：

- [米佐拉](Mizora.md "米佐拉")

## 备注

- 当成双施放法术时，必须选择两个独立的目标。同一个生物不能被同一个成双法术两次以目标。
- 能够以多个生物为目标的法术不能使用 **成双法术**，即使这些法术仅用于以一个生物为目标。这包括 [魔法飞弹](Magic_Missile.md "魔法飞弹") 和 [魔能爆](Eldritch_Blast.md "魔能爆")（5 级后）等法术。
- 以施法者自身为目标的法术不能成双，即使它仅影响施法者。
- 影响区域的法术不能成双。这包括像 [冰刃术](Ice_Knife.md "冰刃术") 这样的单目标但带有额外区域效果的法术。唯一的例外是 [荆雹术](Hail_of_Thorns.md "荆雹术") 和 [闪电箭](Lightning_Arrow.md "闪电箭")。
- 召唤法术不能成双。
- 自补丁 6 起，[链状闪电](Chain_Lightning.md "链状闪电") 不能成双。但是，此限制不适用于由 [玛科赫什基](Markoheshkir.md "玛科赫什基") 赋予的链状闪电版本。

## 错误

- 由于缺乏对投射物法术的 `TargetRadius` 检查，**成双法术** 与某些法术的 _远程_ 版本兼容，但与 _近战_ 版本不兼容。例如 [钉刺](Ensnaring_Strike.md "钉刺")。

---
*Source: [Metamagic: Twinned Spell](https://bg3.wiki/wiki/Metamagic:_Twinned_Spell)*