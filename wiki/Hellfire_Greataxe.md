# 地狱火巨斧

地狱火巨斧是一件非常稀有的+2 [巨斧](Greataxes.md "巨斧")，能造成额外的火焰伤害，每次成功命中都会使使用者获得[灼热](Heat_(Condition).md "灼热（状态）")状态，并赋予[地狱火撕裂](Hellflame_Cleave.md "地狱火撕裂")武器动作。

被此武器击中的任何东西，其预期寿命都如同玻璃锤子一般。

## 属性

伤害

1d12 + 2 (3~14) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[挥砍](Slashing.md "挥砍")

额外伤害

1d6 (1~6) ⁠[火焰](Fire.md "火焰")

详情
[巨斧](Greataxes.md "巨斧")
稀有度：非常稀有
惑控学派：**+ 2**
[双手](Two-Handed.md "双手")
近战：1.5 米 (5 英尺)
重量：3.15 千克 (6.3 磅)
价格：960 金币
UID `MAG_WATCHER_Human_Greataxe` UUID `dd0e9fa2-e012-454d-9f2d-53c0a0776015` Stats `MAG_WATCHER_Human_Greataxe` ### 特殊

**持有此物品者获得：**

[热力充沛](Thermodynamo.md "热力充沛")
每当你用此武器造成伤害时，你获得2回合的[灼热](Heat_(Condition).md "灼热（状态）")。

### 武器动作

_如果你拥有[熟练项](Proficiency.md "熟练项")，装备在**主手**以获得：_

[劈砍](Cleave.md "劈砍") ()
挥舞武器进行大范围弧线攻击，最多同时攻击3个敌人。每个敌人受到你武器通常造成伤害的一半。（充能：[短休](Short_rest.md "短休")。）

[割裂](Lacerate.md "割裂") ()
砍向目标的要害部位，使其[流血](Bleeding_(Condition).md "流血（状态）")。（充能：[短休](Short_rest.md "短休")。）

[准备](Prepare.md "准备") ()
消耗6米（20英尺）的[移动](Movement_speed.md "移动速度")，在本回合剩余时间内，每次成功的近战武器攻击都会造成额外的力量调整值⁠⁠[物理](Physical.md "物理")[DRS](Damage_rider_as_source.md "伤害来源")伤害（最低1点）。（充能：[短休](Short_rest.md "短休")。）

### 特殊武器动作

此武器还赋予以下动作：

[地狱火撕裂](Hellflame_Cleave.md "地狱火撕裂") ()
喷吐地狱烈焰并攻击你的敌人。（充能：[短休](Short_rest.md "短休")。）

## 获取地点

- [巫术杂物店地窖](Sorcerous_Vault.md "巫术杂物店地窖") X: 366 Y: 941：在“幻术”区域的镀金箱子中

## 备注

- 进入地窖后，找到指定的门，队伍必须穿过“银手”门，并在下一个区域摧毁标有“幻术”的门（尝试正常进入该门将无效）。穿过门后就是有箱子的房间。
- 这是游戏中极少数不可[可蘸取](Dippable.md "可蘸取")的武器之一，因为其特殊属性的功能与蘸取[火焰](Fire_(surface).md "火焰（地表）")大致相同。

_关于热力充沛：_

- 游戏中未列出，但热力充沛每轮攻击只能激活一次，即使使用[劈砍](Cleave.md "劈砍")或类似能力击中多个目标也是如此。

_关于地狱火撕裂：_

- 此武器动作不计入[额外攻击](Extra_Attack.md "额外攻击")，需要消耗完整的[动作](Actions.md#Resources "动作")来使用。
- 相反，它实际上被归类为戏法，这会导致一些意外的交互。
  - 它可以被[法术反制](Counterspell.md "法术反制")。
  - [术士](Sorcerer.md "术士")可以对其应用[超魔](Metamagic.md "超魔")。适用的选项包括[超魔：谨慎法术](Metamagic_colon__Careful_Spell.md "超魔：谨慎法术")、[超魔：延长法术](Metamagic_colon__Extended_Spell.md "超魔：延长法术")、[超魔：高强法术](Metamagic_colon__Heightened_Spell.md "超魔：高强法术")、[超魔：默发法术](Metamagic_colon__Subtle_Spell.md "超魔：默发法术")，以及最重要的[超魔：瞬发法术](Metamagic_colon__Quickened_Spell.md "超魔：瞬发法术")。
  - 它受益于法术和戏法特定的伤害加成，如[元素亲和：伤害](Elemental_Affinity_colon__Damage.md "元素亲和：伤害")和[元素强化项链](Necklace_of_Elemental_Augmentation.md "元素强化项链")。
  - 它会激活[奥法骑士](Eldritch_Knight.md "奥法骑士")的[战斗魔法](War_Magic.md "战斗魔法")。
  - 在[沉默](Silenced_(Condition).md "沉默（状态）")状态下仍可施放。
  - 在[狂暴](Rage.md "狂暴")状态下无法施放。
- 滚烫地狱火状态由武器动作本身和它创造的[地狱火](Hellfire.md "地狱火")地表共同施加。即使目标通过了攻击豁免，仍会受到地表造成的滚烫地狱火影响。

## 错误

- 此武器有一个隐藏状态 `MAG_FIRE_DIPPED_HELLFIRE`，本应使其1d6⁠⁠[火焰](Fire.md "火焰")伤害无视火焰抗性。此外，地狱火撕裂及其创造的地狱火地表也本应无视火焰抗性。目前这些效果均未无视火焰抗性。

_关于地狱火撕裂：_

- 尽管工具提示说地狱火无视抗性和免疫，但它并未做到。
- 由于此攻击不涉及攻击掷骰，它无法受益于某些额外伤害来源，这些来源会检查攻击掷骰类型，尽管工具提示中列出了额外伤害。这些包括：
- [奥术协同](Arcane_Synergy_(Condition).md "奥术协同（状态）")
  - [巨武器大师：全力一击](Great_Weapon_Master_colon__All_In.md "巨武器大师：全力一击")
  - [猎人印记](Hunter's_Mark.md "猎人印记")
- [准备](Prepare.md "准备")
- [怒火](Wrath_(Condition).md "怒火（状态）")

---
*Source: [Hellfire Greataxe](https://bg3.wiki/wiki/Hellfire_Greataxe)*