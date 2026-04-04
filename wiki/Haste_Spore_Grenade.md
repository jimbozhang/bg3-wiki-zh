# 加速孢子弹

加速孢子弹是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")）物品，可被[投掷](Throw.md "投掷")。

一种几乎充满潜在能量的炼金混合物。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：不常见
- 重量：0.3 千克 (0.6 磅)
- 价格：25 金币
- UID `ALCH_Solution_Grenade_SporesHaste` UUID `6008231b-9f5a-44f6-8050-14586b7626fd` Stats `ALCH_Solution_Grenade_SporesHaste` ### 效果

[动作](Actions.md#Resources "动作")

- 在振奋能量的云中爆炸
  - 范围：18 米 (60 英尺)
  - 创建区域：加速孢子

## 区域：加速孢子

**[加速孢子](Haste_Spores_(cloud).md "加速孢子 (云)")**

持续时间：3 驱散

范围效果：2 米 (7 英尺) 半径

生物获得 +2 [护甲等级](Armour_Class.md "护甲等级") 加成，[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定") 具有[优势](Advantage.md "优势")，其[移动速度](Movement_speed.md "移动速度") 翻倍，并且每驱散可以执行一次额外的[动作](Action.md "动作")。

类型：[云](Area.md#Cloud "区域")

### 状态：加速孢子

**[加速孢子](Haste_Spores_(Condition).md "加速孢子 (状态)")**

- 目标获得 +2 [护甲等级](Armour_Class.md "护甲等级") 和 [敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定") 的[优势](Advantage.md "优势")。
- 目标的[移动速度](Movement_speed.md "移动速度") 翻倍。
- 目标获得一次额外的[动作](Actions.md#Resources "动作")。

## 获取地点

- 通过[炼金术](Alchemy.md "炼金术")合成：结合[加速孢子升华物](Sublimate_of_Haste_Spores.md "加速孢子升华物")（从[加速孢子](Hastening_Spores.md "加速孢子")获取）和任意[精华](Alchemy.md#Extractions "炼金术")
- 由[斯波](Spaw.md "斯波")给予

## 备注

- 尽管投掷此手雷创建的[加速孢子](Haste_Spores_(cloud).md "加速孢子 (云)")区域持续 3 驱散，但穿过该区域创建的[加速孢子](Haste_Spores_(Condition).md "加速孢子 (状态)")状态仅持续 1 驱散\[[_verify_](bg3wiki_colon_Verification.md "bg3wiki:Verification")\]，除非在消散前离开并重新进入该区域以刷新状态。
  - 尽管功能上与[加速术](Haste.md "加速术")相似，但当此物品的[加速孢子](Haste_Spores_(Condition).md "加速孢子 (状态)")状态到期时，使用者不会陷入[力竭](Lethargic_(Condition).md "力竭 (状态)")。
  - 加速孢子弹的价格比加速药水高 5 金币。
- 要从斯波处获得此物品，队伍必须在第一次与他对话时同意帮助杀死灰矮人入侵者，选择“当然，我能处理附近的那些灰矮人。”，因为标志 `UND_MyconidCircle_SovereignOfferedSpores` 仅针对此对话行设置。询问斯波关于复活尸体（“你对那具尸体做了什么？”），返回上一个对话树（“我们谈谈别的吧。”），然后同意帮助（“我会清除腐烂。湖边的那些灰矮人会死。”）不会奖励手雷，因为这不会设置标志。

---
*Source: [Haste Spore Grenade](https://bg3.wiki/wiki/Haste_Spore_Grenade)*