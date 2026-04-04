# 角色等级

## 定义

**角色等级**指的是玩家角色的总等级。如果角色正在[身兼多职](Multiclassing.md "Multiclassing")，那么这就是其所有职业等级的总和。否则，这仅仅是其职业的等级。例如，一个角色是2级[战士](Fighter.md "Fighter")、3级[游荡者](Rogue.md "Rogue")和3级[术士](Sorcerer.md "Sorcerer")，那么其角色等级为8级。

## 游戏机制

只有有限数量的[游戏机制](Gameplay_mechanics.md "Gameplay mechanics")受角色等级影响。以下是已知示例：

- [熟练项加值](Proficiency_Bonus.md "Proficiency bonus")在角色等级1至4级时为+2；在5至8级时增加到+3，在9至12级时为+4。
- 造成伤害的[戏法](Cantrip.md "Cantrip")在角色等级5级时获得一个额外的伤害骰，在10级时再获得一个。例如，[毒气喷溅](Poison_Spray.md "Poison Spray")起始伤害为1d12；在5级时增加到2d12，在10级时增加到3d12。此规则有两个已知例外：
    1. [魔能爆](Eldritch_Blast.md "Eldritch Blast")——不是每道光束造成更多伤害，而是发射额外的光束：5级时2道，10级时3道。
    1. [轰鸣剑](Booming_Blade.md "Booming Blade")——其初始伤害和次级效果伤害均增加1d8。它在11级而非10级获得最终升级。
- [生命值](Hit_Points.md "Hit points")随每个额外的角色等级增加，但每级获得的数值取决于升级时选择的职业。
- [生命领域](Life_Domain.md "Life Domain")牧师职业动作[维持生命](Preserve_Life.md "Preserve Life")治疗盟友的生命值基于牧师的角色等级。
- 一些[种族](Race.md "Race")特定特性基于角色等级。这些包括：
    - [卓尔](Drow.md "Drow")、[灰矮人](Duergar.md "Duergar")、[提夫林](Tiefling.md "Tiefling")和[吉斯洋基人](Githyanki.md "Githyanki")在1、3和5级时学习的固有法术。
    - [龙裔](Dragonborn.md "Dragonborn")的吐息攻击，其伤害缩放方式类似于戏法，但在6级和11级时增加。
  - 发现[地点](List_of_locations.md "List of locations")所奖励的[经验值](Experience.md "Experience")基于领队队伍成员的角色等级。例如，当发现[伊雷珂养育间](Cr%C3%A8che_Y'llek.md "Crèche Y'llek")时，如果领队角色为4级，游戏授予120经验值；如果为5级，则授予240经验值；如果为6级，则授予280经验值；如果为7级，则授予300经验值。
  - 商人[库存](Traders.md#Trade_inventory "Traders")中的某些物品基于在库存刷新后第一个与之交易（或扒窃）的队伍成员的角色等级。商人库存会在每次长休或任何角色升级时刷新，但先前出售或交易给他们的物品通常仍可用。
    - 例如，一个在[治疗药水表](Healing_Potion_Table.md "Healing Potion Table")上滚动五次的商人，在3级时实际上保证有五个[治疗药水](Potion_of_Healing.md "Potion of Healing")，但在5级时可能有[治疗药水](Potion_of_Healing.md "Potion of Healing")和[高等治疗药水](Potion_of_Greater_Healing.md "Potion of Greater Healing")的混合。
    - 示例二：第一个与[出售护甲](Armour_Trader_Table.md "Armour Trader Table")的商人交谈的队伍成员角色等级为4级；他们可能能够购买（或[偷窃](Sleight_of_Hand.md "Sleight of hand")）[环甲](Ring_Mail_Armour.md "Ring Mail Armour")。
    - 在4级角色之后，另一个队伍成员升级到角色等级5级并与同一商人交谈；这可能会解锁[鳞甲](Scale_Mail.md "Scale Mail")的可用性，直到下次刷新。4级角色现在也可以购买此护甲。
    - 之后，另一个队伍成员升级到6级并与同一商人交谈；他们可能能够购买[半身甲](Half_Plate_Armour.md "Half Plate Armour")。4级和5级角色现在也可以购买此护甲（至少在下次长休之前）。
  - 提高与商人交易的个别队伍成员的[态度](Attitude.md "Attitude")分数（以获得更优惠的价格）会随着与之交易的角色等级提高而[变得更加昂贵](Trading_and_item_pricing.md#Trader_attitude "Trading and item pricing")。
  - 对于在[法师](Wizard.md "Wizard")等级上有多重职业的身兼多职角色，[抄录卷轴](Transcribing_scrolls.md "Transcribing scrolls")基于角色可用的[法术位](Spell_slots.md "Spell slots")，而非其法师等级。
    - 如果队伍成员试图抄录等级过高的法师法术卷轴，消息会说其法师等级不够高，但这不一定正确。相反，要抄录法术卷轴，该角色施法职业的[有效施法者等级](Spells.md#Spellcasting "Spells")必须足够高以施放该法术。角色只需要一级法师等级即可抄录卷轴上包含的任何法师法术。<sup>[\[1\]](#cite_note-1)</sup> 例如，一个拥有1级法师和2级吟游诗人的角色拥有2级法术位，因此可以抄录2级法师法术[侦测思想](Detect_Thoughts.md "Detect Thoughts")（尽管他们在升级过程中无法从任一职业学习2级法术）。
    - 在考虑有效施法者等级和从卷轴抄录法师法术时，记住哪些[施法者职业](Spellcaster.md "Spellcaster")是完整施法者、一半施法者和三分之一施法者可能会有所帮助。

## 注释

1. [↑](#cite_ref-1) 参见[D&D 5e规则变更](D&D_5e_rule_changes.md "D&D 5e rule changes")。

---
*Source: [Character level](https://bg3.wiki/wiki/Character_level)*