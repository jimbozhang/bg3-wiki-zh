# 灵魂捕捉手套

灵魂捕捉手套是一双传奇级的[手套](Handwear.md "Handwear")。它们为徒手攻击提供额外的力场伤害，+2[体质](Constitution.md "Constitution")，并在徒手攻击后治疗穿戴者。

这双手套曾由奥托纳尔·巴斯金佩戴，他是一位职业冥想者，后来成为赤拳冠军，通过两种方法获得了开悟。第二种方法是获得大量战斗技巧。高级宇宙和谐就是鼻子。有时你必须把它打断几次才能得到最好的东西。

## 属性

- [手套](Gloves.md "Gloves")
- 稀有度：传奇
- 重量：0.5 千克（1 磅）
- 价格：960 金币
- UID `MAG_PHB_OfSoulCatching_Gloves` UUID `c1342b19-c898-451c-b2e8-6eb6666fe1c2` Stats `MAG_PHB_OfSoulCatching_Gloves` File `ARM_Cloth_Magic_A_Gloves` ### 特殊

此物品的穿戴者获得：

- [体质](Constitution.md "Constitution") +2，最高至 20。

[灵魂之拳](Soul_Fist.md "Soul Fist")
你的徒手攻击造成额外 1d10⁠⁠[力场](Force.md "Force")伤害。

[灵魂捕捉](Soul_Catching.md "Soul Catching")
每回合一次，在徒手命中时，你恢复 10⁠⁠[治疗](Healing.md "治疗")。或者，你可以放弃治疗，在你的下一回合结束前获得攻击掷骰或豁免检定的 +5 奖励。_\[[参见：错误](Soul_Catching.md#Bugs "Soul Catching")\]_

## 获取地点

- [希望之邸](House_of_Hope.md "House_of_Hope") X: -6477 Y: 2884：由[希望](Hope.md "Hope")在完成她的任务[解救希望](Save_Hope.md "Save Hope")后给予。

## 错误

_关于灵魂捕捉：_

- **灵魂捕捉**存在多处错误：
  - 它说明需要“徒手命中”，而[精华掌握](Grasp_Essence_(Condition).md "Grasp Essence (Condition)")状态说明“用徒手攻击命中一个生物”。实际上，任何造成伤害的徒手攻击都会触发效果，即使是对世界物品。
  - 它说明穿戴者恢复 10⁠⁠[治疗](Healing.md "治疗")，但实际上它提供了一个能力，使用时才会提供治疗。
  - 它说明穿戴者可以在攻击掷骰_和_豁免检定上获得优势，直到下一回合_结束_，而精华掌握状态说明穿戴者可以在攻击掷骰_或_豁免检定上获得优势，直到下一回合结束_之前_。
    - 实际上并未获得优势，而是获得了一个中断，为穿戴者提供选择：要么为单次攻击掷骰添加 +5 奖励，要么为单次豁免检定添加 +5 奖励，此时精华掌握状态被移除。
  - 由于编码错误，如果穿戴者受到伤害且没有任何临时生命值，精华掌握状态会被移除。

## 图库

- [染色](Dye.md "Dye")变体

---
*Source: [Gloves of Soul Catching](https://bg3.wiki/wiki/Gloves_of_Soul_Catching)*