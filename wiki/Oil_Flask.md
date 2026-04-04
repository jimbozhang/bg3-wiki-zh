# 油瓶

**油瓶**是一种[消耗品](Consumables.md "消耗品")（[手雷](Grenades.md "手雷")）物品，可以[投掷](Throw.md "投掷")。

这个瓶子装得马马虎虎——外面沾满了干涸的油，黏糊糊的。

## 属性

- [手雷](Grenades.md "手雷")
- 单次使用
- 稀有度：普通
- 重量：0.3 kg (0.6 lb)
- 价格：7 gp
- UID `LOOT_GEN_Throwable_Oil_Flask_A` UUID `91947f48-4368-4794-8429-2f57172dc53d` Stats `OBJ_OilBottle` ### 效果

[动作](Actions.md#Resources "动作")

- 投掷此瓶以创建一个可燃的油地表。
  - 范围：18 m (60 ft)
  - 创建区域：油

## 区域：油

**[油](Oil.md "油")**

范围效果：3 m (10 ft) 半径

可燃。

类型：[地表](Area.md#Surface "地表")

## 获取地点

- 在第三幕的各个监狱中

## 备注

- 当被[火焰](Fire.md "火焰")伤害摧毁，或投掷到[火焰](Fire_(surface).md "火焰 (地表)")地表上时，油瓶似乎会爆炸。实际上，创建的油地表会立即转换为火焰地表；并没有像[油桶](Oil_Barrel.md "油桶")那样的真正[爆炸](Explosives.md "爆炸")。
- 当被火焰伤害摧毁时，创建的油地表比投掷时要小得多。

---
*Source: [Oil Flask](https://bg3.wiki/wiki/Oil_Flask)*