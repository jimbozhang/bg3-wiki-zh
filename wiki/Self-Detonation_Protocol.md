# 自爆程序

**自爆程序** 是 [钢铁卫士](Steel_Watcher_(creature).md)（包括 [钢铁卫士泰坦](Steel_Watcher_Titan.md "钢铁卫士泰坦")）使用的免费反应和动作。当它们的生命值过低时，此能力会启动自毁序列，最终导致 [爆炸](Self-Detonate.md "Self-Detonate")。

对于普通钢铁卫士，当生命值降至30%时，会自动作为反应触发。对于钢铁卫士泰坦，如果其生命值低于25%，则会在其回合使用此动作。

## 描述

作为最后的手段，启动倒计时序列，最终以 [爆炸](Self-Detonate.md "Self-Detonate") 结束。

## 属性

详情
范围：自身
充能：每场战斗

## 技术细节

UID

`Shout_SteelWatcher_Biped_SelfDestruct_Begin`

普通钢铁卫士版本

`Interrupt_SteelWatcher_Biped_SelfDestruct_Begin`

自动触发动作的反应

`Shout_SteelWatcher_Quadruped_SelfDestruct_Begin`

泰坦版本

法术标志

`[IsEnemySpell](https://bg3.wiki/w/index.php?title=IsEnemySpell_\(spell_flag\)&action=edit&redlink=1) "IsEnemySpell \(spell flag\) \(page does not exist\)")`

## 状态：即将引爆

**[即将引爆！](Detonation_Impending!_(Condition).md "即将引爆！ (状态)")**

持续时间：1 驱散

- 此钢铁卫士正准备 [爆炸](Self-Detonate.md "Self-Detonate")。

## 学习方式

由以下生物使用：[钢铁卫士 (生物)](Steel_Watcher_(creature).md) 和 [地狱火守望者](Hellfire_Watcher.md "地狱火守望者")

## 错误

- 尽管在战斗日志中显示为反应，但钢铁卫士即使执行了 [借机攻击](Opportunity_Attack.md "借机攻击") 或其反应被 impair（例如通过 [电爪](Shocking_Grasp_(Condition).md "电爪 (状态)")），仍可触发自爆程序。

---
*Source: [Self-Detonation Protocol](https://bg3.wiki/wiki/Self-Detonation_Protocol)*