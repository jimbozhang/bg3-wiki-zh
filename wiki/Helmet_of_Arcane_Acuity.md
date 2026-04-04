# 战法师的骄傲

战法师的骄傲是一个[头盔](Headwear.md "Headwear")，当佩戴者用武器攻击造成伤害时，会赋予其[奥术敏锐](Arcane_Acuity_(Condition).md)>。

这件头盔的皮革面板中编织着微妙的魔法——因为强大的进攻有时仍是最佳的防御。

## 属性

- [头盔](Helmets.md "Helmets")
- 所需熟练项：[轻甲](Light_Armour.md "Light_Armour")
- 稀有度：不常见
- 重量：0.5 千克 (1 磅)
- 价格：70 金币
- UID `MAG_ElementalGish_ArcaneAcuity_Helmet` UUID `df71a665-a179-43b3-89ee-2e355166fa9b` Stats `MAG_ElementalGish_ArcaneAcuity_Helmet` ### 特殊效果

此物品的佩戴者获得：

- [敏捷](Dexterity.md "Dexterity") [豁免检定](Saving_throw.md "Saving Throw") +1

[战法师的敏锐](Battle_Acuity.md "Battle Acuity")
每当你用武器攻击造成伤害时，你获得持续2回合的[奥术敏锐](Arcane_Acuity_(Condition).md "奥术敏锐 (状态)")。

## 获取地点

- [石匠公会](Mason's_Guild.md "Mason's Guild") X: 107 Y: -758：在秘密地下室区域的一个上锁且设有陷阱的**镀金箱子**中

## 备注

- 箱子可以用DC 14的[巧手](Sleight_of_Hand.md "Sleight_of_Hand") [检定](Ability_Check.md "属性检定")打开，并且可以用DC 15的[察觉技能](Perception.md "Perception") [检定](Ability_Check.md "属性检定")感知到陷阱，然后用DC 21的[巧手](Sleight_of_Hand.md "Sleight_of_Hand") [检定](Ability_Check.md "属性检定")解除陷阱。如果在解除陷阱前撬锁，陷阱会触发一个DC 15豁免检定的4级[曳光弹](Guiding_Bolt.md "Guiding Bolt")以抵消它。
- 地下室通过石匠公会中的一个活板门进入，秘密区域可以通过撬锁或对**钥匙孔信使**使用[塔型钥匙](Tower-Shaped_Key.md "Tower-Shaped Key")来打开。

## 错误

_关于战法师的敏锐：_

- **战法师的敏锐**缺少 `OncePerAttack` 标志。因此，对于被视为武器攻击并包含多个 `DealDamage` 函数的法术（如[轰鸣剑](Booming_Blade.md "Booming Blade")和各种[至圣斩](Smite.md "Smite")法术），它可能在单次攻击中触发多次。

## 图库

- 游戏内外观

---
*Source: [Helmet of Arcane Acuity](https://bg3.wiki/wiki/Helmet_of_Arcane_Acuity)*