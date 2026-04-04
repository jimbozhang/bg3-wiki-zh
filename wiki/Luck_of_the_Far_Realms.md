# 远域幸运

**远域幸运**是一个被动特性/反应和[灵吸怪威能](Illithid_power.md "灵吸怪威能")。它允许角色每[长休](Long_Rest.md "长休")一次，将一次成功的[攻击掷骰](Attack_roll.md "攻击掷骰")变为[重击](Critical_Hit.md "重击")。

## 描述

每[长休](Long_Rest.md "长休")一次，你可以将一次对敌人的成功[攻击掷骰](Attack_roll.md "攻击掷骰")变为[重击](Critical_Hit.md "重击")。

### 详情

消耗：
[反应](Actions.md#Reactions "动作")
充能：[长休](Long_Rest.md "长休")

## 如何习得

生物使用：

- [完整的灵吸怪](Full-illithid.md "完整的灵吸怪")

其他习得方式：

- 在获得以下条件后，使用[夺心魔寄生虫标本](Mind_Flayer_Parasite_Specimen.md "夺心魔寄生虫标本")从[灵吸怪威能](Illithid_powers.md "灵吸怪威能")技能树中解锁：
  - [有利开局](Favourable_Beginnings.md "有利开局")

## 备注

- 与能为单次攻击增加大量伤害骰的能力（如[偷袭](Sneak_Attack.md "偷袭")或[至圣斩](Divine_Smite.md "至圣斩")）配合良好。

## 错误

- 由于该被动反应的编码方式<sup>[\[1\]](#cite_note-1)</sup>，它会在并非自然20点掷骰但因[重击阈值降低](Critical_Hit.md#Reducing_critical_threshold "重击")而已是重击的攻击上触发。
- 消耗[深邃沉眠药水](Potion_of_Angelic_Slumber.md "深邃沉眠药水")或受[神圣干预：光耀复苏](Divine_Intervention_colon__Opulent_Revival.md "神圣干预：光耀复苏")影响时，远域幸运不会重置。
- 受[星界形态](Starry_Form.md "星界形态")影响时，无法使用此反应。

1. [↑](#cite_ref-1) 源自 `Mods/Shared/Scripts/thoth/helpers/CommonConditionsDev.khn` 中 `LuckOfTheFarRealmCheck()` 的定义：显示代码

function LuckOfTheFarRealmCheck()
local notCrit = context.InterruptedRoll.NaturalRoll < 20 and context.InterruptedRoll.NaturalRoll > 1
local isHit = context.InterruptedRoll.Total >= context.InterruptedRoll.Difficulty

return ConditionResult(notCrit and isHit)
end

---
*Source: [Luck of the Far Realms](https://bg3.wiki/wiki/Luck_of_the_Far_Realms)*