# 精准报复

精准报复是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")）物品，可以[投掷](Throw.md "投掷")并在命中时[爆炸](Explosives.md "爆炸")。

拥有原版的所有声响与爆炸，但多了一份额外惊喜。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：稀有
- 重量：0.3 千克 (0.6 磅)
- 价格：120 gp
- UID `GRN_UNI_BrilliantRetort` UUID `11f7c9b6-6210-44f2-ae59-2f61f6ad7563` Stats `UNI_BrilliantRetort` ### 效果

[动作](Actions.md#Resources "动作") - [投掷](Throw.md "投掷")一枚在命中时爆炸的炸弹

- 范围：18 米 (60 英尺)
- 范围效果：4 米 (13 英尺) 半径
- 3d4 + 9 (12~21) ⁠[力场](Force.md "力场")

伤害

- 施加[沉默](Silenced_(Condition).md "沉默 (状态)")，持续 2 驱散
- [DC](Dice_rolls.md#Save_DCs "掷骰") 12 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")可使所有伤害减半，并移除沉默

## 状态：沉默

**[沉默](Silenced_(Condition).md "沉默 (状态)")**

持续时间：2 驱散

- 生物无法说话或施放带有语言成分的法术，并免疫⁠[雷鸣](Thunder.md "雷鸣")伤害。

## 获取地点

- 完成⁠[解救乌尔布伦](Rescue_Wulbren.md "解救乌尔布伦")后，由[巴克斯·鲁特](Barcus_Wroot.md "巴克斯·鲁特")奖励

## 备注

- 此物品为唯一物品，无法购买或通过[炼金术](Alchemy.md "炼金术")制作。

## Bug

- 精准报复触发与[烟粉炸弹](Smokepowder_Bomb.md "烟粉炸弹")相同的脚本，导致投掷或摧毁时造成第二次伤害，总计

6d4 + 18 (24~42) ⁠[力场](Force.md "力场")

伤害。当手雷对象被具有多重伤害来源的攻击摧毁时，此相同脚本也可能触发多次伤害。更多详情请参见[烟粉炸弹#bug](Smokepowder_Bomb.md#bugs "烟粉炸弹")。

---
*Source: [Brilliant Retort](https://bg3.wiki/wiki/Brilliant_Retort)*