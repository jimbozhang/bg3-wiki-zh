# 坠落伤害

**坠落伤害**是生物在从足够高的地方坠落时，以[钝击](Bludgeoning.md "钝击")伤害形式对其[生命值](Hit_Points.md "Hit_Points")造成的[伤害](Damage.md "Damage")。坠落伤害最常见于从高处[跳跃](Jump.md "Jump")、被[推击](Shove.md "Shove")或[投掷](Throw.md "Throw")出去，或被具有击退效果的法术和能力推下时发生[[注1]](#cite_note-1)。坠落伤害随坠落高度增加而增加，如果坠落高度足够高，还可能使生物陷入[倒伏](Prone.md "Prone")状态。

## 目录

- [1 坠落伤害计算](#坠落伤害计算)
  - [1.1 倒伏](#倒伏)
  - [1.2 示例](#示例)
- [2 坠落伤害抗性与免疫](#坠落伤害抗性与免疫)
  - [2.1 抗性来源](#抗性来源)
  - [2.2 免疫来源](#免疫来源)
- [3 碾压伤害](#碾压伤害)
- [4 成就](#成就)
- [5 脚注与参考文献](#脚注与参考文献)

## 坠落伤害计算

_博德之门3_ 并未使用标准的D&D 5e规则集来计算坠落伤害（在该规则集中，生物每坠落10英尺会受到1d6点伤害）<sup>[\[1\]](#cite_note-2)</sup>。相反，它使用了自己的公式，使伤害保持一致，并随坠落高度增加而更离散地增加。游戏中使用的计算似乎涉及大量四舍五入，因此实际受到的伤害可能并不总是与计算结果完全一致。

坠落造成的伤害量随坠落高度线性增加，造成生物最大生命值（包括[临时生命值](Temporary_Hit_Points.md "Temporary_Hit_Points")）的一定百分比：

- 坠落高度低于4米（13英尺）时，不造成伤害。
- 坠落高度超过4米（13英尺）时，伤害起始为生物最大生命值的2%，之后每额外坠落0.2米，伤害增加1%。根据大量实验得出的精确公式似乎为：

坠落伤害 = (最大生命值 + 临时生命值) × (高度 - 4) / 17 + 1 （适用于高度 ≥ 4米）

- 在没有任何伤害抗性调整的情况下，从满生命值状态坠落接近21米（70英尺）将是致命的。坠入深渊或游戏可玩区域外总是致命的。
- 使用[移位](Displace_(Condition).md "移位（状态）")的生物，会使因其实用动作而承受坠落伤害的任何生物额外受到1d8点[心灵](Psychic.md "心灵")伤害。
- 如果坠落是由一个生物投掷或推击另一个生物引起，而非跳跃所致，那么某些影响伤害的物品或状态也会添加到坠落伤害中，例如[闪电充能](Lightning_Charges.md "Lightning_Charges")或[无情光芒之戒](Callous_Glow_Ring.md "Callous_Glow_Ring")[[注2]](#cite_note-3)。即使承受坠落伤害的生物拥有该物品或状态，这些伤害加成也会生效。

显示坠落伤害的工具提示示例。

当从足以造成伤害的高度跳跃时，工具提示会显示生物跳到目标位置时将承受的伤害。如果伤害足以杀死生物，则会显示“死亡”文本。该工具提示会准确显示因坠落伤害抗性而减少的伤害，但对于具有钝击伤害抗性的生物，仍会错误地显示全额伤害。移位或其他效果造成的任何额外伤害，以及来自[重甲大师](Heavy_Armour_Master.md "Heavy_Armour_Master")等特性的固定伤害减免，都不会包含在此工具提示中。该工具提示总是会提示生物可能因坠落而倒伏，即使坠落高度不足。

### 倒伏

坠落也可能在生物落地时使其陷入[倒伏](Prone.md "Prone")状态。如果坠落造成的伤害超过其最大生命值的25%<sup>[\[2\]](#cite_note-4)</sup>，则坠落总是会使生物倒伏，这意味着对于没有坠落伤害抗性的角色，约8米/27英尺的坠落高度，或对于具有坠落伤害抗性的生物，约12.3米/40英尺的坠落高度。具有钝击伤害抗性但不具有特定坠落伤害抗性的生物，在8米/27英尺的坠落中仍会倒伏，尽管其承受的伤害仅为其最大生命值的12.5%。同样，固定伤害减免不影响此阈值。

### 示例

一个生物从5.4米/17.7英尺的高度坠落，且没有坠落伤害抗性，预计会受到相当于其最大生命值2%的伤害，加上伤害开始后每额外0.2米/0.6英尺高度增加1%的伤害，在此情况下，5.4米/17.7英尺的坠落将造成约2% + 7% = 9%最大生命值的伤害。由于坠落高度低于8米/27英尺，该生物不会倒伏。如果坠落是由推击或投掷引起，且任一生物佩戴了[无情光芒之戒](Callous_Glow_Ring.md "Callous_Glow_Ring")，则坠落的生物还会额外受到2点光耀伤害。

## 坠落伤害抗性与免疫

有多种来源可提供对坠落伤害的[抗性](Resistance.md "Resistance")和[免疫](Immunity.md "Immunity")，有些来自法术和消耗品的临时效果，有些来自特定职业或被动特性的永久效果。

任何提供钝击伤害抗性的来源都会使生物获得坠落伤害抗性，而[魔法板甲](Magical_Plate.md "Magical_Plate")等被动特性也会减少伤害。此外，还有专门提供坠落伤害抗性或免疫的来源。如果生物同时具有钝击伤害抗性和坠落伤害抗性，这些效果会叠加，使其承受的坠落伤害减少75%。坠落伤害抗性不会列在生物角色表的抗性部分，只能在其显著特性列表中查看。

### 抗性来源

- [梁上君子](Second-Story_Work.md "梁上君子")：游荡者在3级选择[盗贼](Thief.md "盗贼")副职时获得的职业特性[[注3]](#cite_note-5)。
- [轻身坠](Slow_Fall.md "轻身坠")：武僧在4级获得的反应。
- [野兽形态：黑猩猩](Aspect_of_the_Beast_colon__Chimpanzee.md "野兽形态：黑猩猩")：野蛮人在6级或10级选择[荒蛮之心](Wildheart.md "荒蛮之心")副职时可获得的职业特性。
- [猫之轻灵](Cat's_Grace.md "猫之轻灵")：[强化属性](Enhance_Ability.md "强化属性")的变体，吟游诗人、牧师、德鲁伊和术士在3级可使用，或来自[优雅布衣](The_Graceful_Cloth.md "优雅布衣")。
- [猫之轻落](Feline_Fall.md "猫之轻落")：[猫](Cat.md "猫")独有的被动特性。
- [荒野形态：猫](Wild_Shape_colon__Cat_(Condition).md "荒野形态：猫（状态）")：猫的荒野形态。

显示抗性减少坠落伤害的示例。

### 免疫来源

- [羽落术](Feather_Fall_(Condition).md "羽落术（状态）")：由[羽落术](Feather_Fall.md "羽落术")、[羽落术药水](Potion_of_Feather_Fall.md "羽落术药水")、[羽落术卷轴](Scroll_of_Feather_Fall.md "羽落术卷轴")和[乌鸦徽记](Corvid_Token.md "乌鸦徽记")赋予的状态。
- [蛛网术](Web.md "蛛网术")：落在该法术创造的[蛛网](Web_(surface).md "蛛网（地表）")地表上，可消除任何高度的所有坠落伤害。
- [风之纱](Veil_of_the_Wind.md "风之纱")：由[尼鲁纳](Nyrulna.md "Nyrulna")赋予的被动特性。
- [星界重力](Astral_Gravity_(Condition).md "星界重力（状态）")：在[星界](Astral_Plane.md "星界")和[堕影冥界](Shadowfell.md "堕影冥界")赋予的状态。
- [超尘脱俗](Unearthly.md "超尘脱俗")：[促狭鬼](Poltergeist.md "促狭鬼")独有的被动特性。
- [荒野形态：恐鸦](Wild_Shape_colon__Dire_Raven_(Condition).md "荒野形态：恐鸦（状态）")：恐鸦的荒野形态。
- [荒野形态：巨蜘蛛](Wild_Shape_colon__Giant_Spider_(Condition).md "荒野形态：巨蜘蛛（状态）")：巨蜘蛛的荒野形态。

## 碾压伤害

如果坠落实体重量至少为0.5千克（1磅）且从至少4米（13英尺）的高度坠落，则被坠落实体击中的实体（物体或生物）将根据以下公式受到碾压伤害，其中重量以克为单位<sup>[\[4\]](#cite_note-7)</sup>，坠落高度以米为单位，round()表示四舍五入到最接近的整数：

碾压伤害 = round((重量 × 0.000005 + 1) × 坠落高度 - 1)

## 成就

推下去
用坠落伤害杀死一个生物。

## 脚注与参考文献

1. [↑](#cite_ref-1) 能造成坠落伤害的能力具有 `[AddFallDamageOnLand](AddFallDamageOnLand_(spell_flag).md)` 法术标志。
2. [↑](#cite_ref-3) 此额外伤害仅来自使用DamageBonus()但不要求来源为徒手、武器或法术攻击才能触发的被动或状态。[[_验证_](bg3wiki_colon_Verification.md "bg3wiki:验证")]
3. [↑](#cite_ref-5) 梁上君子似乎错误地将坠落伤害减少了75%而非50%，但这并不会使你在不倒伏的情况下可坠落的距离超过普通抗性。
4. [↑](#cite_ref-2) <https://www.dndbeyond.com/sources/basic-rules/adventuring#Falling>
5. [↑](#cite_ref-4) 此值由 `Public/Shared/Stats/Generated/Data/Data.txt` 中定义的 `FallDamagePronePercent` 确定。
6. [↑](#cite_ref-6) 这由 `Public/Shared/Stats/Generated/Data/Data.txt` 中定义的 `FallImpactMinWeight` 和 `FallDamageMinimumDistance` 确定。
7. [↑](#cite_ref-7) 此参数由 `Public/Shared/Stats/Generated/Data/Data.txt` 中定义的 `FallImpactConstant` 确定。

---
*Source: [Falling damage](https://bg3.wiki/wiki/Falling_damage)*