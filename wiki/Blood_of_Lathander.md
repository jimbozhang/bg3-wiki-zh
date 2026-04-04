# 洛山达之血

洛山达之血是一件传奇的 **+3** [硬头锤](Maces.md "硬头锤")，通过 ⁠[寻找洛山达之血](Find_the_Blood_of_Lathander.md "寻找洛山达之血") 任务获得。它会持续散发光芒，用光芒使附近的[邪魔](Fiends.md "邪魔")和[不死生物](Undead.md "不死生物")目盲，能够防止死亡并治疗持有者，并允许持有者施放[阳炎射线](Sunbeam.md "阳炎射线")。

## 属性

伤害

1d6 + 3 (4~9) + [力量调整值](Damage_Roll.md#Modifiers "伤害掷骰") ⁠[钝击](Bludgeoning.md "钝击")

详情
[硬头锤](Maces.md "硬头锤")
稀有度：传奇
附魔：**+3**
单手
[可蘸取](Dippable.md "可蘸取")
近战：1.5 米 (5 英尺)
重量：1.8 千克 (3.6 磅)
价格：640 金币
UID `S_CRE_BloodOfLathander` 状态 `CRE_BloodOfLathander` *UID `UNI_CRE_HUM_Sun_Mace_BloodOfLathander` UUID `96a35552-0c05-4df0-9974-2a8f142e4be6` 状态 `CRE_BloodOfLathander`* UID `WPN_HUM_Sun_Mace_Lathander_Blood_A_Glow` UUID `7b961f08-46c1-46b1-99bc-c59283831a0b` 状态 `CRE_BloodOfLathander` ### 特殊

**持有此物品获得：**

[阳炎射线](Sunbeam.md "阳炎射线")
作为 6 级法术施放（充能：[长休](Long_Rest.md "长休")。）

[洛山达的祝福](Lathander's_Blessing.md "洛山达的祝福")
每[长休](Long_Rest.md "长休")一次，当你的生命值降至 0 时，你恢复 2d6⁠⁠[治疗](Healing.md "治疗")。9 米 / 30 英尺内的盟友也恢复 1d6⁠⁠[治疗](Healing.md "治疗")。

[洛山达的光芒](Lathander's_Light.md "洛山达的光芒")
在 6 米 / 20 英尺半径范围内散发神圣光芒。在战斗中，站在光芒中的[邪魔](Fiends.md "邪魔")和[不死生物](Undead.md "不死生物")如果未能通过 DC 14 体质豁免，则会[目盲](Blinded_(Condition).md "目盲（状态）")。

### 武器动作

_如果你有[熟练项](Proficiency.md "熟练项")，装备在**主手**以获得：_

[震荡猛击](Concussive_Smash.md "震荡猛击")
全力击中敌人以造成伤害并可能使其[眩晕](Dazed_(Condition).md "眩晕（状态）")。（充能：[短休](Short_rest.md "短休")。）

## 获取地点

- [伊雷珂养育间](Cr%C3%A8che_Y'llek.md "伊雷珂养育间") X: 1068 Y: -779：在[隐蔽房间](Secret_Chamber.md "隐蔽房间")的上锁祭坛上

## 备注

- 此物品授予的[阳炎射线](Sunbeam.md "阳炎射线")版本*不*允许在后续回合中重新施放。
- 在游戏文件中，此物品有多个变体，名称不同但功能相同：
- UUID: `96a35552-0c05-4df0-9974-2a8f142e4be6`（洛山达之血）。此版本的物品有一条引文，与游戏内版本不同，可能本意用于可使用版本：*这把发光硬头锤的柄上镶嵌着一大块琥珀，据说其中蕴含着四滴神血，这些血在洛山达的形象与密斯特拉疯狂的选民之间的战斗中坠落凡间。*
- UUID: `7b961f08-46c1-46b1-99bc-c59283831a0b`（黎明之握硬头锤）。这是当前可用的变体。

_关于洛山达的祝福：_

- 如果持有者不在活跃队伍中，洛山达的祝福不会激活。例如，留在[营地](Campsite.md "营地")的伙伴通过[守护之链](Warding_Bond.md "守护之链")受到伤害导致生命值降至零，不会触发此效果。
- 洛山达的祝福无法防止被推击、投掷或以其他方式强行移位至深渊。

_关于洛山达的光芒：_

- 与[光亮术](Light_(Condition).md "光亮术（状态）")不同，洛山达的光芒状态即使在装备远程武器时也有效。
- 洛山达的光芒发出的光具有以下特性：
  - 它不适用于盟友，意味着你不会使自己召唤的不死生物目盲。
- 它会驱散[幽影诅咒](Shadow_Curse_(Condition).md "幽影诅咒（状态）")，无需装备[火把](Torch.md "火把")。
  - 它使需要目标被照亮的效果生效，例如应用[无情光芒之戒](Callous_Glow_Ring.md "无情光芒之戒")的伤害。
- 它*是*阳光，用于触发[日照敏感](Sunlight_Hypersensitivity_(Condition).md "日照敏感（状态）")，但*不是*用于[日照敏感](Sunlight_Sensitivity.md "日照敏感")。
  - 它适用于中立生物（包括中立的[不死生物](Undead.md "不死生物")），可能使它们变为敌对。

## 错误

_关于洛山达的祝福：_

- 洛山达的祝福不会治疗持有者的盟友，而只会治疗附近的活跃队伍成员。
  - 由于治疗的编码方式，触发洛山达的祝福的攻击者被视为治疗来源。因此，当持有者装备[轻声承诺](The_Whispering_Promise.md "轻声承诺")时，治疗不会触发[祝福慈悲](Blessed_Mercy.md "祝福慈悲")等治疗效果。
- 由于 `TargetConditions` 字段设置不正确，额外的 1d6⁠⁠[治疗](Healing.md "治疗")会影响持有者，除了 2d6⁠⁠[治疗](Healing.md "治疗")之外。
- 由于治疗应用方式的时间限制，持有者可能并不总是获得战斗日志中所述的所有治疗；他们通常只获得 1⁠⁠[治疗](Healing.md "治疗")（来自稳定）或 1d6⁠⁠[治疗](Healing.md "治疗")，而不是所述的 1d6+2d6⁠⁠[治疗](Healing.md "治疗")。持有者也可能获得治疗，但仍保持死亡状态，显示其可掠夺的尸体并有剩余生命值。
- 由于缺少技术条件 (`MAG_LATHANDERS_TRACKER`)，导致洛山达之血通过“本地物品”在游戏中生成，此被动的“每长休一次”冷却仅在长休期间为持有者刷新。在长休期间未持有该武器的角色装备该武器不会允许此被动触发。此外，当消耗[深邃沉眠药水](Potion_of_Angelic_Slumber.md "深邃沉眠药水")或受[神圣干预：光耀复苏](Divine_Intervention_colon__Opulent_Revival.md "神圣干预：光耀复苏")影响时，洛山达的祝福不会重置。

## 画廊

- 概念艺术由 Andy Ho 提供

---
*Source: [The Blood of Lathander](https://bg3.wiki/wiki/The_Blood_of_Lathander)*