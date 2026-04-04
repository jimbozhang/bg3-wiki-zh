# 塞尔死灵法术

塞尔死灵法术是与任务 [搜查地窖](Search_the_Cellar.md "搜查地窖")、[解锁古代典籍](Unlock_the_Ancient_Tome.md "解锁古代典籍") 和 [摧毁古代典籍](Destroy_the_Ancient_Tome.md "摧毁古代典籍") 相关的 [故事道具](Story_Item.md "故事道具") [书籍](Books.md "书籍")。

它。还。不。算。太。晚。

## 属性

- [书籍](Books.md "书籍")

- 稀有度：故事道具

- 重量：0.5 千克 (1 磅)

- 价格：14 金币

- UID `S_FOR_DangerousBook_Tome` UUID `73ea8888-ed82-4ca5-b9f9-0c9119873507` *UID `UNI_FOR_ThayanTome_Unsocketed` UUID `feecea9b-c091-46fd-9795-738e9c0e3019`* UID `UNI_FOR_ThayanTome_Socketed` UUID `215dc202-2b77-4825-b6d1-c72954f6394a` ## 位置

- 在 [染疫村落](Blighted_Village.md "染疫村落") 下方的 [死灵法师的实验室](Apothecary's_Cellar.md#死灵法师的实验室 "药剂师的地窖") 中，位于一个被陷阱的祭坛上，坐标 X: -648 Y: -362，位于一扇上锁的大门后方

  - 请参阅 [解锁古代典籍](Unlock_the_Ancient_Tome.md "解锁古代典籍") 以获取进入方法

## 用法

- _将书籍交给阿斯代伦：_ +5 -5
  - 一旦他获得这本书，就无法将其转移给其他 [伙伴](Companion.md "伙伴") 或玩家角色。
- _摧毁书籍：_ +1 +1 +1 -5 -5
  - 这本书只能被 [光耀](Radiant.md "光耀") 伤害摧毁，这会生成三个敌对的 [暗影](Shadow.md "暗影")。
- _使用敲击术：_ 对书籍使用 [敲击术](Knock.md "Knock") 法术会召唤一个 [暗影](Shadow.md "暗影")。
- _阅读书籍以获取其黑暗秘密：_ -5 -1 -1
  - 必须通过将 [暗紫水晶](Dark_Amethyst.md "暗紫水晶") 放入其封面来解锁这本书，之后最多可以翻动三页，这会触发逐渐变难的 [感知](Wisdom.md "感知") [豁免检定](Saving_throw.md "豁免检定") ([难度等级](Difficulty_Class.md "难度等级") 10、15 和 20)。
  - 一次豁免检定失败会使读者受到 [疯狂低语](Whispers_of_Madness_(Condition).md "疯狂低语 (状态)") 的诅咒，第二次失败会使读者受到 [有害知识](Baleful_Knowledge_(Condition).md "有害知识 (状态)") 的诅咒。两者都会对感知检定施加 [劣势](Disadvantage.md "劣势")，但前者可以通过 [长休](Long_Rest.md "长休") 清除，而后者只能通过 [移除诅咒](Remove_Curse.md "移除诅咒") 清除。
  - 某些职业和某些队伍成员有特殊选项可以修改或降低这些难度等级；使用任何这些选项都会导致相同的结果。
    - [吟游诗人](Bard.md "吟游诗人") 可以进行难度等级 5、10 和 15 的 [表演](Performance.md "表演") [属性检定](Ability_Check.md "属性检定")。
    - [术士](Sorcerer.md "术士") 可以进行难度等级 5、10 和 15 的 [魅力](Charisma.md "魅力") [属性检定](Ability_Check.md "属性检定")。
    - [邪术师](Warlock.md "邪术师") 可以为第一页进行一次难度等级 5 的 [魅力](Charisma.md "魅力") [属性检定](Ability_Check.md "属性检定")。其他页面使用默认的感知豁免。
    - [法师](Wizard.md "法师") 可以为第一页进行一次难度等级 5 的 [智力](Intelligence.md "智力") [属性检定](Ability_Check.md "属性检定")。其他页面使用默认的感知豁免。
    - 邪恶阵营神祇的 [牧师](Cleric.md "牧师") 为第三页获得一次难度等级 10 的 [感知](Wisdom.md "感知") [属性检定](Ability_Check.md "属性检定")。这包括作为 [莎尔](Shar.md "莎尔") 牧师的 [影心](Shadowheart.md "影心")。
- [阿斯代伦](Astarion.md "阿斯代伦") 有一个特殊选项：_“啜饮黑暗，拥抱它，然后翻页，”_ 用于翻动第三页，需要一次难度等级 15 的 [感知](Wisdom.md "感知") [属性检定](Ability_Check.md "属性检定")。
  - 翻动至少一页会永久授予读者 [死者交谈](Speak_with_Dead.md "死者交谈")。该法术可以作为 [仪式](Spells.md#仪式法术 "法术") 施放，并且不消耗 [法术位](Spell_Slot.md "法术位")。
  - 翻动三页，无论成功与否，都会授予 _禁忌的知识_ [标签](Tags.md "标签") 和 [禁忌的知识](Forbidden_Knowledge.md "禁忌的知识") 被动特性。
  - 在翻动三页之前关闭书籍会使任务 [搜查地窖](Search_the_Cellar.md "搜查地窖") 未完成，并允许读者稍后重新打开书籍。

## 注释

- 拿起书籍会触发陷阱。要避免这种情况，可以在基座上放置一个重量相似的物品（如另一本书），或者在通过 [察觉技能](Perception.md "察觉技能") 检定揭示陷阱后将其解除，或者解除附近的两座雕像。拿书的角色也可以进入回合制模式以避免陷阱，确保队伍在离开回合制模式前处于其范围之外。
- 要阅读这本书，必须从 [低语深地](Whispering_Depths.md "低语深地") 坐标 X: -550 Y: -350 处获得 [暗紫水晶](Dark_Amethyst.md "暗紫水晶")，可以从 [染疫村落](Blighted_Village.md "染疫村落") 的水井或铁匠铺地下室进入。紫水晶由 [相位蜘蛛女王](Phase_Spider_Matriarch.md "相位蜘蛛女王") 守卫。
- 阅读 _塞尔死灵法术_ ：
  - 不会破坏 [古贤之誓](Oath_of_the_Ancients.md "古贤之誓")
  - 永久将其锁定在读者的物品栏中
- 将物品引文从 _“它。还。不。算。太。晚。”_ 更改为 _“别。看。”_
  - 阻止任何其他人尝试阅读它
- 一旦翻动所有三页，这本书将拒绝为任何人再次打开，直到在 [第三幕](Act_Three.md "第三幕") 中获得更多知识。请参阅：[萨奇亚特法典](The_Tharchiate_Codex.md "萨奇亚特法典")。
- 可以牺牲 [禁忌的知识](Forbidden_Knowledge.md "禁忌的知识") 被动特性，以允许读者 _安全地_ 从 [哀伤之邸](House_of_Grief.md "哀伤之邸") 中的 [失落之镜](Mirror_of_Loss.md "失落之镜") 获得永久加成；请参阅 [永久加成](Permanent_bonuses.md#Mirror_of_Loss "永久加成")。

## 外部链接

- [遗忘国度维基](https://forgottenrealms.fandom.com/wiki/Main_Page) 上的 [塞尔死灵法术](https://forgottenrealms.fandom.com/wiki/The_Necromancy_of_Thay)

---
*Source: [Necromancy of Thay](https://bg3.wiki/wiki/Necromancy_of_Thay)*