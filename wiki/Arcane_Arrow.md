# 奥术射击

奥术射击是一组从3级开始可供[奥术射手](Arcane_Archer.md "奥术射手")副职使用的类别动作。它们是利用[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")为远程攻击添加额外效果的强大攻击。它们在[短休](Short_rest.md "短休")时恢复，并且数量众多，允许它们比许多其他法术和类别能力更频繁地使用。

## 目录

- [1 保存DC](#保存DC)
- [2 奥术箭](#奥术箭)
- [3 奥术射击列表](#奥术射击列表)
- [4 错误](#错误)

### 保存DC

- 如果奥术射击需要保存DC，DC将等于8 + 你的熟练项调整值 + 你的智力调整值

## 奥术箭

[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")在[短休](Short_rest.md "短休")或[长休](Long_Rest.md "长休")时恢复至最大值。随着奥术射手等级的提升，可用的[奥术箭](Arcane_Archer.md#Arcane_Arrow "奥术射手")数量和已知的奥术射击数量都会增加。

## 奥术射击列表

| 等级 |  | 已知奥术射击 |
| --- | --- | --- |
| 3 | 4 | 3 |
| 7 | 7 | 4 |
| 10 | 10 | 5 |

## 错误

- 穿刺箭和追踪箭与其他奥术射击不同，由于缺少攻击掷骰，它们与[伤害附加](Damage_mechanics.md "伤害机制")的交互方式不同。因此，来自[泰坦弦弓](Titanstring_Bow.md "泰坦弦弓")和[神射手：孤注一掷](Sharpshooter_colon__All_In.md "神射手：孤注一掷")的额外伤害不会被应用，尽管工具提示显示会应用。然而，其他类似于[蘸取](Dip.md "蘸取")或[闪电充能](Lightning_Charges_(Condition).md "闪电充能（状态）")的伤害附加确实会将额外伤害应用于这些箭。
- 由于错误地使用了`DamageBonus`函数，奥术射击在击中敌人时提供的额外伤害在[重击](Critical_Hit.md "重击")时不会翻倍。

---
*Source: [Arcane Shots](https://bg3.wiki/wiki/Arcane_Shots)*