# 屠夫的甜心

屠夫的甜心是一件非常稀有的[戒指](Rings.md "Rings")，它能让佩戴者在杀死一个生物后，下一次[攻击掷骰](Attack_roll.md "Attack Roll")必定[重击](Critical_Hit.md "Critical Hit")，每[长休](Long_Rest.md "Long Rest")一次。

尽管戒指经过高度抛光，但深色的血迹碎片仍附着在细小的刮痕和角落处。

## 属性

- [戒指](Rings.md "Rings")
- 稀有度：非常稀有
- 重量：0.05 千克 (0.1 磅)
- 价格：140 gp
- UID `MAG_Critical_CriticalExecution_Ring` UUID `2f2d4bf3-6a14-43f5-81fe-e14aa9871215` Stats `MAG_Critical_CriticalExecution_Ring` ### 特殊

佩戴此物品的角色获得：

[处刑者](Executioner.md "Executioner")
当你杀死一个生物时，你的下一次[攻击掷骰](Attack_roll.md "攻击掷骰")将是一次[重击](Critical_Hit.md "重击")。一旦消耗，此效果将在[长休](Long_Rest.md "长休")后刷新。

## 获取地点

- [莎尔铁手神殿](Gauntlet_of_Shar.md "Gauntlet_of_Shar") X: -833 Y: -729：在[同我试炼](Self-Same_Trial.md "同我试炼")中，击败出现在火盆旁的暗影复制品后，地面上。

## 备注

_关于处刑者：_

- 在一个生物被杀死后，处刑者的重击效果可以在[反应标签页](Reactions_tab.md "反应标签页")中设置为“询问”或完全禁用，以便将其留到以后使用。使用它不会消耗[反应资源](Resources.md#Reaction "资源")。
- 处刑者的自动重击可以应用于单次范围攻击（AOE）击中的每个目标，例如[旋风斩](Whirlwind_Attack.md "旋风斩")或[剃刀狂风](Razor_Gale.md "剃刀狂风")。

## 错误

_关于处刑者：_

- 尽管工具提示暗示相反，但处刑者仅适用于_[武器](Weapon.md "武器")_攻击掷骰。
- 当使用施加[豁免检定](Saving_throws.md "豁免检定")的武器特定能力时，例如[推撞攻击（近战）](Pushing_Attack_(Melee).md "推撞攻击（近战）")和[割裂](Lacerate.md "割裂")，**处刑者**会尝试将其“自然20”效果应用于敌人的豁免检定以及角色的攻击。这存在浪费[处刑者](Executioner_(Condition).md "处刑者（状态）")状态来帮助敌人的风险。
  - 如果处刑者反应设置为“自动”：游戏会强制角色的攻击掷骰为20（重击），但_也_强制目标的_豁免检定_为20。这使敌人有很高的概率抵抗次要效果（例如，他们受到伤害但不会被推开）。
  - 如果处刑者反应设置为“询问”：游戏会触发两个独立的提示：
    - _第一个提示_：询问是否将角色的攻击掷骰变为20。（建议：_是_）
    - _第二个提示_：询问是否将敌人的_豁免检定_变为20。（建议：_否_）
      - 如果角色接受第二个提示，[处刑者](Executioner_(Condition).md "处刑者（状态）")状态将被消耗，敌人将获得豁免检定的大额加值。
- 注意：虽然_豁免检定_在20时并不技术上“重击成功”，但高掷骰通常会导致敌人抵抗效果。
- **浪费冲锋**：由于脚本错误，[处刑者](Executioner_(Condition).md "处刑者（状态）")未能检查攻击角色是否已经正常掷出自然20。如果角色自己重击成功，反应仍可能触发（并被消耗），如果他们要么_接受_反应提示，要么将其设置为“自动”。

---
*Source: [Killer's Sweetheart](https://bg3.wiki/wiki/Killer's_Sweetheart)*