# 缓慢术卷轴

缓慢术卷轴是一种单次使用的卷轴，允许使用者以动作施放 [减速](Slow.md "减速")。

## 属性

- [卷轴](Scrolls.md "卷轴")
- 单次使用
- 稀有度：稀有
- 重量：0.02 千克 (0.04 磅)
- 价格：100 金币
- UID `LOOT_SCROLL_Slow` UUID `4c990ca3-01f6-4536-b8f3-c26cd9a0ca8b` Stats `OBJ_Scroll_Slow` ### 效果

[动作](Actions.md#Resources "动作")

- 使最多 6 个目标陷入 [减速](Slowed_(Condition).md "减速 (状态)")。_\[[参见：错误](#bugs)\]_
  - 范围：18 米 (60 英尺)
  - [专注](Concentration.md "专注")

## 状态：减速

**[减速](Slowed_(Condition).md "减速 (状态)")**

持续时间：10 驱散

[感知](Wisdom.md "感知") [豁免检定](Saving_throws.md "豁免检定") ([法术豁免 DC](Dice_rolls.md#Spell_save_DC "掷骰"))

- [移动速度](Movement_speed.md "移动速度") 减半
- [护甲等级](Armour_Class.md "护甲等级") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 降低 2
- 只能采取一个 [动作](Action.md "动作") 或一个 [附赠动作](Bonus_action.md "附赠动作")，不能同时进行两者
- 无法进行 [反应](Reaction.md "反应")
- 无法进行 [额外攻击](Extra_Attack.md "额外攻击") 或 [精通额外攻击](Improved_Extra_Attack.md "精通额外攻击") _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_
- 施放的法术可能会延迟一驱散 _\[[参见：错误](Slowed_(Condition).md#Bugs).md#Bugs> "减速 (状态)")\]_

## 获取地点

- 由商人出售、在容器中找到、或由敌人携带

## 错误

- 当通过键盘和鼠标界面使用卷轴施放时，减速 _需要_ 6 个目标；由于敌人不能被重复选择且盟友无法被选为目标，此卷轴可能难以使用。

---
*Source: [Scroll of Slow](https://bg3.wiki/wiki/Scroll_of_Slow)*