# Widget talk:PriceCalculator

游说和态度的效果都只有应有值的一半。

正确的计算方式是：游说 \*0.1，态度 \* 0.005

我刚做了个测试来确认。飞行药剂：价值30，硬核难度，游说调整值7，态度100。根据“我的计算”，总调整值是2.5+0.5-0.7-0.5=1.8。预测售价：30/1.8=17，预测买价：30\*1.8=54。与游戏内数值相符。

— [未署名评论](https://www.mediawiki.org/wiki/Help:Signatures) 由 [81.82.46.46](https://bg3.wiki/w/index.php?title=User:81.82.46.46&action=edit&redlink=1 "User:81.82.46.46 (page does not exist)") ([对话](User_talk_colon_81.82.46.46.md "User talk:81.82.46.46")) 2023年11月22日 21:26

感谢指出。我会修复。 - [Sky](User_colon_Sky.md "User:Sky") ([对话](https://bg3.wiki/w/index.php?title=User_talk:Sky&action=edit&redlink=1 "User talk:Sky (page does not exist)")) [2023年11月22日 22:02 (CET)](https://bg3.wiki/wiki/Widget_talk:PriceCalculator#c-Sky-20231122210200)回复

公式现在正确了，但存在舍入误差。使用上述测试案例的数字，小部件给出53和16，而不是54和17。游戏内售价17是16.666...的舍入值，但小部件使用了“floor”命令。买价差异让我困惑。54是精确值（30\*1.8）。你会认为计算中一定有某些中间步骤发生了舍入，但在代码中没看到。类似错误也发生在游说值为12时，它给出买价38而不是39。更奇怪的是，使用游说值11.99999时得到39，符合预期，但输入12时会降到38。 — [未署名评论](https://www.mediawiki.org/wiki/Help:Signatures) 由 [81.82.46.46](https://bg3.wiki/w/index.php?title=User:81.82.46.46&action=edit&redlink=1 "User:81.82.46.46 (page does not exist)") ([对话](User_talk_colon_81.82.46.46.md "User talk:81.82.46.46")) 2023年11月22日 22:28

啊...这是编程中的一个大问题。我把math.floor换成了math.round，现在对于给定的测试案例似乎能提供精确值了。-[Sky](User_colon_Sky.md "User:Sky") ([对话](https://bg3.wiki/w/index.php?title=User_talk:Sky&action=edit&redlink=1 "User talk:Sky (page does not exist)")) [2023年11月22日 22:37 (CET)](https://bg3.wiki/wiki/Widget_talk:PriceCalculator#c-Sky-20231122213700-Sky-20231122210200)回复

---
*Source: [Widget talk:PriceCalculator](https://bg3.wiki/wiki/Widget_talk:PriceCalculator)*