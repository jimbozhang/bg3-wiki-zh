# 睡眠术卷轴

**睡眠术卷轴**是一种单次使用的卷轴，允许使用者以一个动作施放 [睡眠](Sleep.md "睡眠")。

## 属性

- [卷轴](Scrolls.md "卷轴")
- 单次使用
- 稀有度：普通
- 重量：0.02 千克 (0.04 磅)
- 价格：40 金币
- UID `LOOT_SCROLL_Sleep` UUID `2ce88bf0-fe06-46bd-b71e-18bc6dc8eb9d` Stats `OBJ_Scroll_Sleep` ### 效果

[动作](Actions.md#Resources "动作")

- 对生命值总和不超过 **24 生命值** 的目标施加 [沉睡](Sleeping_(Condition).md "沉睡 (状态)")。_\[[参见：错误](#bugs)\]_
  - 范围：18 米 (60 英尺)

## 状态：沉睡

**[沉睡](Sleeping_(Condition).md "沉睡 (状态)")**

持续时间：2 驱散

- 沉睡的生物无法移动或行动。
- 此外，该生物自动在 [力量](Strength.md "力量") 和 [敏捷](Dexterity.md "敏捷") 的 [豁免检定](Saving_throw.md "豁免检定") 中失败。
- 对其进行的 [攻击掷骰](Attack_roll.md "攻击掷骰") 具有 [优势](Advantage.md "优势")，并且如果攻击者在生物 1.5 米 (5 英尺) 范围内，任何命中该生物的攻击都是 [重击](Critical_Hit.md "重击")。
- 通过受到伤害、变为 [濡湿](Wet_(Condition).md "濡湿 (状态)")、接受 [协助](Help.md "协助") 或被 [推击](Shove.md "推击") 来移除。

## 获取地点

- 由商人出售，在容器中找到，并由敌人携带

## 错误

- 当通过卷轴使用键盘和鼠标界面施放时，睡眠术 _要求_ 目标生命值总和为 24；由于敌人不能被选择两次，且盟友不可被选为目标，此卷轴可能难以使用。

---
*Source: [Scroll of Sleep](https://bg3.wiki/wiki/Scroll_of_Sleep)*