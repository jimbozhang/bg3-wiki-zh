# 蛛网爆弹

**蛛网爆弹**是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")），可以[投掷](Throw.md "投掷")。

这团蛛网脉动着期待的魔法，渴望在瞬间展开。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 千克（0.6 磅）
- 价格：16 金币
- UID `ALCH_Solution_Grenade_Web` UUID `a4d98266-948b-4467-96cd-6a316f37ceda` Stats `ALCH_Solution_Grenade_Web` ### 效果

[动作](Actions.md#Resources "动作")

- 投掷后爆炸成一团纠缠的乱麻，使范围内的生物[网缚](Enweb.md "网缚")
  - 范围：18 米（60 英尺）
  - 创建区域：蛛网

## 区域：蛛网

**[蛛网](Web_(surface).md "蛛网（地表）")**

持续时间：10 驱散

范围效果：3 米（10 英尺）半径

[劣势地形](Difficult_Terrain.md "劣势地形") - [移动速度](Movement_speed.md "移动速度")减半。可使生物[网缚](Enweb.md "网缚")。防止[坠落伤害](Falling_damage.md "坠落伤害")。可燃。

类型：[地表](Area.md#Surface "地表")

### 状态：网缚

**[网缚](Enwebbed_(Condition).md "网缚（状态）")**

[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throws.md "豁免检定")（[DC](DC.md "DC") 12）

- 无法移动。
- 对该生物的[攻击掷骰](Attack_roll.md "攻击掷骰")具有[优势](Advantage.md "优势")，而该生物的攻击掷骰和[敏捷](Dexterity.md "敏捷") [豁免检定](Saving_throw.md "豁免检定")掷骰具有[劣势](Disadvantage.md "劣势")。

### 状态：劣势地形：蛛网

**[劣势地形：蛛网](Difficult_Terrain_colon__Web_(Condition).md "劣势地形：蛛网（状态）")**

- [移动速度](Movement_speed.md "移动速度")减半。

## 获取地点

- 可通过[炼金术](Alchemy.md "炼金术")制作，将[蛛丝悬液](Suspension_of_Spider_Silk.md "蛛丝悬液")（从[丝腺](Silk_Gland.md "丝腺")获取）与任意[酸解物](Alchemy.md#Extractions "炼金术")组合

## Bug

- 炼金术制作所需的成分名称与提取物名称不同。

---
*Source: [Web Grenade](https://bg3.wiki/wiki/Web_Grenade)*