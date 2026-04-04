# 猎犬预兆 (状态)

**猎犬预兆**

- 一种黑暗预兆，可以是 ⁠[强酸](Acid.md "强酸")、⁠[寒冷](Cold.md "寒冷")、⁠[火焰](Fire.md "火焰")、⁠[闪电](Lightning.md "闪电")、⁠[中毒](Poison.md "中毒") 或 ⁠[雷鸣](Thunder.md "雷鸣")。
- 当对受影响实体造成该类型的伤害时，猎犬的所有者将恢复 1 [术法点](Sorcery_Point.md "术法点")。

## 猎犬预兆的来源

_维基数据库中未定义_

## 拥有猎犬预兆的生物

_维基数据库中未定义_

## 预兆掷骰及其运作方式

状态 `OMEN_ROLL` 使用了一个补丁 8 新增的 khn 函数 `OmenRolling()`，该函数首先检查目标是否已拥有尝试施加的类型的预兆状态（例如 `OMEN_ACID`）。如果目标没有，则函数调用另一个补丁 8 新增的 khn 函数 `RollDieAgainstPercent()`，该函数似乎由 Larian 使用旧的 `RollDieAgainstDC()` 代码半实现。`RollDieAgainstPercent()` 仍然有一个 DC 值的条目，但在执行过程中并未实际使用。然后，函数进行所选类型的骰子掷骰，将数字除以 2，并检查该商数是否有余数。如果没有余数，则函数返回 "true"，如果有余数，则函数返回 "false"。这实际上使得 `RollDieAgainstPercent()` 函数始终只返回一个 50/50 的掷骰结果，在 `OMEN_ROLL` 的情况下，它忽略了所有单独的骰子掷骰和 DC 检查，并在为每个预兆状态进行掷骰时给予其 50% 的施加几率。然而，由于强酸是第一个进行掷骰的状态，其施加几率（50%）远高于雷鸣或中毒（3.125%）等最后进行掷骰的状态，这是由于复合依赖概率所致。

### 有错误的不祥啃咬

### 预期的不祥啃咬

---
*Source: [Hound's Omen (Condition)](https://bg3.wiki/wiki/Hound's_Omen_(Condition)*