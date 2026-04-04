# 翼龙毒素

翼龙毒素是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。它可以涂抹在武器上，使其获得特殊效果，持续十回合；或者作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")，在区域内造成其效果。

瓶中的毒素变幻莫测，预示着迅捷而美味的死亡。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：稀有
- 重量：0.2 千克 (0.4 磅)
- 价格：65 金币
- UID `CONS_Poison_Wyvern` UUID `eca393b0-3f8e-4862-814b-9e236a0d4129` Stats `OBJ_WyvernPoison` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用翼龙毒素涂抹你的主动武器。

[动作](Actions.md#Resources "动作")

- [投掷](Throw.md "投掷")毒素
  - 范围：18 米 (60 英尺)
  - 创建区域：翼龙毒素

## 状态：涂抹了翼龙毒素

**[涂抹了翼龙毒素](Coated_in_Wyvern_Toxin_(Condition).md "涂抹了翼龙毒素 (状态)")**

持续时间：10 回合

- 目标在其下一回合结束时受到 1d8⁠⁠[中毒](Poison.md "中毒")伤害，除非他们通过一次 [DC](Dice_rolls.md#Save_DCs "掷骰") 15 的 [体质](Constitution.md "体质") [豁免检定](Saving_throw.md "豁免检定")。

## 区域：翼龙毒素

**[翼龙毒素](Wyvern_Poison_(surface).md "翼龙毒素 (地表)")**

持续时间：永久

范围效果：1 米 (3 英尺) 半径

施加中毒。

类型：[地表](Area.md#Surface "区域")

### 状态：翼龙毒素

**[翼龙毒素](Wyvern_Toxin_(Condition).md "翼龙毒素 (状态)")**

[体](Constitution.md "体质") [豁免检定](Saving_throws.md "豁免检定") ([DC](DC.md "DC") 15)

- 受影响实体在其下一回合结束时受到 1d8⁠⁠[中毒](Poison.md "中毒")伤害。

## 获取地点

- 由 [丽德雯姐妹](Anna_Lidwin.md "安娜·丽德雯") 在 [治疗中心](House_of_Healing.md "治疗中心") 出售
- 由 [内蒂](Nettie.md "内蒂") 在 [翠绿林地](Emerald_Grove.md "翠绿林地") 赠予玩家角色
- 在 [隐藏金库](Hidden_Vault.md "隐藏金库") 的一个木箱中，可通过闲庭图书馆进入，位于内蒂实验室旁边
- 通过 [炼金术](Alchemy.md "炼金术") 制造，将 [飞龙毒刺灰烬](Ashes_of_Wyvern_Stinger.md "飞龙毒刺灰烬")（从 [飞龙毒刺](Wyvern_Stinger.md "飞龙毒刺") 获取）与任意 [升华物](Alchemy.md#Extractions "炼金术") 结合。

## 备注

- 在 [抢先体验](Early_Access.md "抢先体验") 中，翼龙毒素被称为 [翼龙毒素](Wyvern_Poison.md "翼龙毒素")，并且效果更为强大。
- 制造此物品的成本远高于直接从商人处购买毒素。
- 当多个目标同时被使用涂抹了此毒素的武器的范围效果攻击击中时，一次只能有一个目标受到毒素影响。

## 错误

- 由于一行错误的代码，对 [中毒](Poisoned_(Condition).md "中毒 (状态)") 的 [豁免检定](Saving_throw.md "豁免检定") 上的 [优势](Advantage.md "优势")（例如来自 [矮人活力](Dwarven_Resilience.md "矮人活力")、[壮心体魄](Strongheart_Resilience.md "壮心体魄") 和 [防护毒素](Protection_from_Poison_(Condition).md "防护毒素 (状态)")）对抵抗此毒素影响的豁免检定没有效果。
- 当用涂抹了此毒素的武器伤害目标时，战斗日志中一个隐藏的技术被动描述会显示，如果目标通过体质豁免检定，则受到一半伤害。这并不正确；如果豁免成功，目标根本不会受到施加伤害的状态。

## 被动特性

翼龙毒素有 1 [生命值](Hit_Points.md "生命值")。

## 图库

- 道具设计：Cliff Laureys

---
*Source: [Wyvern Toxin](https://bg3.wiki/wiki/Wyvern_Toxin)*