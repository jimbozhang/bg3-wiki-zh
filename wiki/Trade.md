# 交易与物品定价

本文提供计算器：[Widget:价格计算器](Widget_colon_PriceCalculator.md "Widget:价格计算器")。

博德之门3中的交易界面（右下角显示商人的态度）。

**交易**是[博德之门3](Baldur's_Gate_3.md "博德之门3")中围绕[物品](Items.md "Items")和[金币](Gold.md "Gold")买卖的核心[游戏机制](Gameplay_mechanics.md "游戏机制")。根据与特定[商人](Trader.md "商人")对话的[角色](Characters.md "角色")，包括商人对该角色的[态度](Attitude.md "态度")、角色的[游说](Persuasion.md "游说")值以及游戏的[难度](Difficulty.md "难度")设置，会计算一个交易价格乘数。该乘数随后应用于每个物品的固有价值，从而给出该角色的交易价格。

价格调整值的计算公式为：

`P = max(1.0, 2.5 - 游说调整值 - 难度调整值 - 态度调整值)`

物品价值在购买时乘以价格调整值，在出售时除以调整值。换言之，总价格调整值越小，对交易角色越有利。

## 目录

- [1 调整值](#modifiers)
  - [1.1 游说调整值](#persuasion-modifier)
  - [1.2 游戏难度](#game-difficulty)
    - [1.2.1 探索者难度](#explorer-difficulty)
    - [1.2.2 硬核难度](#tactician-difficulty)
  - [1.3 商人态度](#trader-attitude)
    - [1.3.1 何时赠送最优？](#when-is-it-optimal-to-gift?)
- [2 对话角色](#talking-character)
- [3 另见](#see-also)
- [4 参考文献](#references)

## 调整值

### 游说调整值

角色的[游说](Persuasion.md "游说")值会影响价格。正值会使价格更有利（出售时更高，购买时更低），反之亦然。在[探索者难度](Difficulty.md#Explorer "难度")下，如果角色在游说上[熟练](Proficiency.md "熟练项")，由于该难度下[熟练项加值](Proficiency_Bonus.md "熟练项加值")更高，角色会获得更高的游说值。每个游说值点数会使总调整值变化0.1，详情如下。

`游说调整值 = 游说值 × 0.1`

### 游戏难度

根据设定的游戏难度，角色会获得某些优势或劣势。

#### 探索者难度

在[探索者难度](Difficulty.md#Explorer "难度")下，难度调整值为0.5。

如果角色在[游说](Persuasion.md "游说")上[熟练](Proficiency.md "熟练项")，他们会受益于该难度提供的更高[熟练项](Proficiency.md "熟练项")加值，具体取决于其[角色等级](Character_level.md "角色等级")，如下表所示。这反过来会增加游说调整值。

#### 硬核难度

在硬核难度下，难度调整值为-0.5，意味着总调整值增加，使购买更昂贵，出售价格更低。

### 商人态度

显示商人态度的计量条。悬停在计量条上会显示确切的态度值。

商人的[态度](Attitude.md "态度")分数代表商人NPC对某个角色的友好程度。每个态度点数会使总调整值变化0.005，在态度达到100时，态度调整值最大为0.5。

`态度调整值 = 态度 × 0.005`

[态度](Attitude.md "态度")在交易界面中商人模型下方可见。悬停在计量条上会显示确切的态度分数。态度是按角色计算的，可以通过对NPC（或附近NPC）采取友好或敌对行为来修改。获得态度的最简单方法之一是使用议价界面向商人赠送[金币](Gold.md "金币")或其他物品。获得态度所需的金币数量根据角色等级而定。

7 | 18 | 1800
8 | 24 | 2400
9 | 30 | 3000
10 | 36 | 3600
11 | 45 | 4500
12 | 45 | 4500

#### 何时赠送最优？

假设只打算从商人处购买一次，计算临界值，超过该值赠送节省的金额将超过赠送物品的价值。

`每次赠送减少的价格 = 基础价值 / 等级调整值 × 0.005 > 1`

如果该值大于1，则每赠送一枚金币在折扣中价值更高，因此将态度提升至100可节省更多。

`基础价值 > 200 × 等级调整值`

例如，在等级4时，临界值为200 × 8 = 1600。如果打算购买超过1600总基础价值的物品，实际上通过赠送800金币将商人态度提升至100，总花费会更少。请注意，这指的是物品的**基础价值**，而非在态度为0时看到的价格，后者通常是基础价值的2倍以上（参见文章顶部的价格调整值）。

另一种可能性是使用[守墓人](Withers.md "守墓人")重新分配角色属性。然后，在仍为等级1时，访问相关商人并赠送400金币。此时花费临界值为200 × 4 + 100 × 2 = 1000。其中100 × 2是因为100态度可将价格降低至基础价格的一半。

关于定价考虑因素的更详细分析及其效用讨论，可在[reddit](https://www.reddit.com/r/BaldursGate3/comments/15rcyhm/ive_decoded_merchant_pricing/)上找到。

## 对话角色

使用的交易价格调整值仅基于与商人*发起*对话的角色。即使在商人界面中切换了活动角色，第一个角色的交易价格调整值仍会保持使用。因此，最好（即使有些繁琐）由具有最佳交易乘数的角色发起所有交易对话。

例如：可以在营地中保留一个[雇佣兵](Hireling.md "雇佣兵")用于此特定目的，并仅在交易时让其加入活动队伍。在不重新分配属性的情况下，最佳选择是[布里娜·明歌](Brinna_Brightsong.md "布里娜·明歌")和[杰斯林](Jacelyn.md "杰斯林")，因为他们具有高[魅力](Charisma.md "魅力")和在[游说](Persuasion.md "游说")上的[熟练项](Proficiency.md "熟练项")。将他们保持在等级1可最小化从商人处获得100好感度的成本（400金币）。相反，布里娜可以在等级3时获得游说[专精](Expertise.md "专精")，在等级4时提升魅力，并在等级5时获得更高的熟练项加值，此时100好感度成本为1000金币。鉴于这些事实，必须权衡各种机会成本和结果。

如果交易队伍成员在态度变化时处于[伪装术](Disguise_Self.md "伪装术")状态，这些变化仅影响该特定伪装形式——而非角色整体。具体而言，如果对话角色在态度变化时处于伪装状态，这些变化*仅在该特定伪装形式下生效*，在伪装解除后不会反映在角色的正常形态中。要实现这些变化，必须重新应用相同的伪装。例如，如果以女性龙裔形态伪装时捐赠金币提升态度，解除伪装（或应用其他伪装）后，用同一角色再次与商人对话将不会显示改善后的态度，而是未伪装形态的态度。重新获得女性龙裔的伪装形态将再次提供伪装期间调整的态度。换言之，*游戏引擎会为角色在任何商人处、任何地点（永久）所扮演的每个方面（或伪装形式）保留单独的态度分数——除非在该伪装形式下再次更改。*

## 另见

- [Widget:价格计算器](Widget_colon_PriceCalculator.md "Widget:价格计算器")

## 参考文献

1. GaRy van Thos Gaming, _["How Merchant and Traders Attitude work and effect Prices in Baldur's Gate 3"](https://youtu.be/GkQ5U7fQeuQ). youtube.com_
1. Annie Shi, _["Baldur’s Gate 3: How To Raise Merchant Attitude"](https://www.thegamer.com/baldurs-gate-3-bg3-how-to-raise-merchant-attitude/). thegamer.com_
1. desirecampbell, [I've decoded merchant pricing](https://www.reddit.com/r/BaldursGate3/comments/15rcyhm/ive_decoded_merchant_pricing) reddit.com

---
*Source: [Trading and item pricing](https://bg3.wiki/wiki/Trading_and_item_pricing)*