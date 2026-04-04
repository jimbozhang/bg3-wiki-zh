# 西索博得的特制穿肠散

西索博得的特制穿肠散是一种[消耗品](Consumables.md "消耗品")（[涂层](Coatings.md "涂层")）。可涂抹于武器上，使其获得特殊效果，持续十个回合。

这是一种由[西索博得·索姆](Thisobald_Thorm.md "西索博得·索姆")的实验性思维，从死尸玫瑰的凝结物中设计出的真正可憎的毒药。

## 属性

- [涂层](Coatings.md "涂层")
- 单次使用
- 稀有度：非常稀有
- 重量：0.2 千克 (0.4 磅)
- 价格：65 金币
- UID `UNI_Poison_Brewer` UUID `6db9ed3d-2d72-43ad-a2b8-02365728f29f` Stats `UNI_Poison_Brewer` ### 效果

[附赠动作](Actions.md#Resources "动作")

- 用西索博得的特制穿肠散涂抹你的主动武器。

## 状态：涂抹了特制穿肠散

**[涂抹了特制穿肠散](Coated_in_Brewed-up_Bellyglummer_(Condition).md "涂抹了特制穿肠散 (状态)")**

持续时间：10 回合

- 武器涂抹了特制穿肠散。目标必须通过[DC](Dice_rolls.md#Save_DCs "掷骰") 17 的[体质](Constitution.md "体质")[豁免检定](Saving_throw.md "豁免检定")，否则将[中毒](Brewed-Up_Bellyglummer_(Condition).md "特制穿肠散 (状态)")。

## 状态：特制穿肠散

**[特制穿肠散](Brewed-Up_Bellyglummer_(Condition).md "特制穿肠散 (状态)")**

持续时间：直到通过[豁免检定](Saving_throw.md "豁免检定")

[体质](Constitution.md "体质")[豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 17）

- 在[攻击掷骰](Attack_roll.md "攻击掷骰")和[检定](Checks.md "检定")上具有[劣势](Disadvantage.md "劣势")
- 受影响实体在其下一回合结束时受到 1d6⁠⁠[中毒](Poison.md "中毒")伤害。

## 获取地点

- 通过[炼金术](Alchemy.md "炼金术")制造，将[死尸玫瑰之盐](Salts_of_Corpse_Rose.md "死尸玫瑰之盐")（从[死尸玫瑰](Corpse_Rose.md "死尸玫瑰")获取）与任意[悬液](Alchemy.md#Extractions "炼金术")结合。

## 备注

- 此物品*无法*作为[手雷](Grenades.md "手雷")[投掷](Throw.md "投掷")以在区域内造成其效果。

- 与毒素不同，此毒药的伤害每回合只能应用一次。

- 首次制造此物品会获得以下[激励点](Inspiration.md "激励点")：

  - ⁠[业余笔记](Criminal.md#Notes_of_an_Amateur "罪犯")（适用于具有[罪犯](Criminal.md "罪犯")背景的角色）

  - ⁠[特殊冰冻砒霜...酿造？](Guild_Artisan.md#Special_Iced_Arsenic..._Brew? "公会工匠")（适用于具有[公会工匠](Guild_Artisan.md "公会工匠")背景的角色）

## 错误

- 与其他毒药不同，此物品在豁免成功时不会给予**免疫**状态，因此可以在同一回合内多次尝试对同一目标涂抹此毒药。这是由于编码错误，尝试应用不存在的状态 `UNI_POISON_IMMUNE` 而非正确的状态 `UNI_POISON_BREWER_IMMUNE`（该状态会提供**免疫：穿肠散**）。
- 负责将毒药状态应用于被击中目标的隐藏技术状态，会触发[喧嚣风暴之靴](Boots_of_Stormy_Clamour.md "喧嚣风暴之靴")、[寒意之帽](Coldbrim_Hat.md "寒意之帽")和[奥术协同王冠](Diadem_of_Arcane_Synergy.md "奥术协同王冠")的被动效果，即使目标豁免成功且毒药状态未被应用。

---
*Source: [Thisobald's Brewed-Up Bellyglummer](https://bg3.wiki/wiki/Thisobald's_Brewed-Up_Bellyglummer)*