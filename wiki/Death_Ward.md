# 死亡防护

**死亡防护**是一个[4级防护学派法术](Spells.md "Spells")。它允许施法者防止目标死亡。

## 描述

保护一个生物免于死亡。下次受到伤害使其生命值降至0时，它将保持意识，剩余1点生命值。

## 属性

消耗
[动作](Actions.md#Resources "动作") + [4级法术位](Spells.md#Spell_slots "法术位")
细节
近战：1.5米（5英尺）

## 高等级施法

以更高法术位施放此法术不会获得额外收益。

## 技术细节

UID

`Target_DeathWard`

法术标志

`[HasSomaticComponent](HasSomaticComponent_(spell_flag).md)`, `[HasVerbalComponent](HasVerbalComponent_(spell_flag).md)`, `[IsMelee](IsMelee_(spell_flag).md)`, `[IsSpell](IsSpell_(spell_flag).md)`

## 状态：死亡防护

**[死亡防护](Death_Ward_(Condition).md "死亡防护 (状态)")**

持续时间：直至[长休](Long_Rest.md "长休")

- 下次受到伤害使受影响实体生命值降至0时，它将保持意识，剩余1点生命值。

## 如何习得

职业：

- 职业等级7：[牧师](Cleric.md "牧师")、[生命领域](Life_Domain.md "生命领域")（领域法术）和[死亡领域](Death_Domain.md "死亡领域")（领域法术）
- 职业等级10：[吟游诗人](Bard.md "吟游诗人")（通过[魔法秘密](Magical_Secrets.md "魔法秘密")）

## 备注

- 当受影响的生物受到[魔法飞弹](Magic_Missile.md "魔法飞弹")等法术攻击，并作为单个法术的一部分受到多次攻击时，假设第一次攻击足以使具有死亡防护的生物[倒地](Downed_(Condition).md "倒地 (状态)")，第二次攻击似乎会在死亡防护激活前生效。这意味着在2次攻击后，生物失去死亡防护但仍剩余1点生命值：
  - 如果初始攻击有3次应用，生物在第2次攻击时倒地，并在第3次攻击时实际死亡。
  - 对于具有死亡防护的队友，他们需要受到6次攻击应用才会实际死亡：2次打破防护，1次使其倒地，再3次使其3次死亡豁免失败。此效果似乎适用于所有多次应用攻击，如[灼热射线](Scorching_Ray.md "灼热射线")和[魔能爆](Eldritch_Blast.md "魔能爆")。
- 如果由[牧师](Cleric.md "牧师")施放，此法术必须保持[准备](Spells.md#Prepared_Spells "法术")状态；从施法者的准备法术列表中移除死亡防护会移除所有施法者施加过死亡防护的队友的状态。将施法者从队伍中移除不会移除该状态。
- 如果一个生物在自己的回合倒地，被死亡防护复活后，其所有动作都会恢复。
- 死亡防护不能防止被推击、投掷或以其他方式强行移位至深渊。
- 死亡防护_确实_保护队友免受[巴尔的法令](Bhaal's_Edict.md "巴尔的法令")的影响，尽管在这种情况下，他们会失去所有当前增益和状态，如同短暂死亡一样。
- 死亡防护的咒语是 **Quod Dico Face**，拉丁语意为“照我说的做”。

## 错误

- 死亡防护使用[求生直觉](Survival_Instinct_(Condition).md "求生直觉 (状态)")作为`父`状态，并因此继承其拥有的动作点恢复效果。这可以被角色利用，通过对自己施放死亡防护，只要他们能够使自己倒地并在同一回合多次重新施放死亡防护，就可以持续恢复动作点。

## 外部链接

- > )[死亡防护（法术）](https://forgottenrealms.fandom.com/wiki/Death_ward_(spell)) 在 [被遗忘的国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page)

---
*Source: [Death Ward](https://bg3.wiki/wiki/Death_Ward)*