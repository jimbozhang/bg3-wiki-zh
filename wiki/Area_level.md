# 区域等级

**区域等级**（也称为**地点等级**或**区域等级**）指的是游戏开发者为游戏中某些[区域](Region.md "Region")和[地点](List_of_locations.md "List of locations")分配的1到12的数字。该等级会影响整个游戏中的[经验值](Experience.md "Experience")奖励。区域等级在用户界面中不可见。

## 目录

- [1 经验值奖励](#经验值奖励)
  - [1.1 击败生物](#击败生物)
  - [1.2 完成任务步骤](#完成任务步骤)
- [2 按等级划分的区域](#按等级划分的区域)
- [3 备注](#notes)

## 经验值奖励

主条目：[经验值](Experience.md "Experience")

区域等级会影响击败[生物](Creatures.md "Creatures")和完成[任务](Quests.md "Quests")步骤时的经验值奖励。

### 击败生物

当队伍击败一个生物时，如果该生物的等级低于其被击败区域的等级，则游戏会使用该区域等级来选择经验值奖励。例如，在等级3的[染疫村落](Blighted_Village.md "Blighted Village")区域击败一个等级1的[地精](Goblin.md "Goblin")生物时，游戏将使用区域等级，并将该生物视为等级3。这将经验值奖励从10点变为20点。<sup>[\[1\]](#cite_note-1)</sup>

### 完成任务步骤

任务本身在完成时不会授予经验值，但其步骤会。完成一个步骤所奖励的经验量由触发完成的区域等级决定。例如，在[第一幕](Act_One.md "Act_One")中发生的任务[寻找洛山达之血](Find_the_Blood_of_Lathander.md "Find_the Blood of Lathander")中，其中一个步骤是“我们得知一件强大的圣物，洛山达之血，可能就在附近。我们在探索修道院时应该留意它。”。其完成触发点位于等级5的[瑰晨修道院](Rosymorn_Monastery.md "Rosymorn Monastery")区域内。因此，完成此步骤将获得30点经验值。

## 按等级划分的区域

开发者为99个区域分配了等级。

下表显示了这些区域及其等级：

| 等级 | UID | UUID | 父区域 | 区域UID | 任务/步骤/[[#cite_note-2 "[")2] | 包含的地点 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 1 | CRA_CrashSite | UUID cb127a10-8570-4e9c-9efa-85c8234929b7 | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸") [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩") |
| 2 | DEN_Tunnels | UUID 6be608ff-3117-4a60-bbd3-1e2e7d2eb5d2 | DEN_Sitra'sDen | WLD_Main_A | 2 | [地下通道](Underground_Passage.md "地下通道") |
| 2 | DEN_Tunnels | UUID 6be608ff-3117-4a60-bbd3-1e2e7d2eb5d2 | DEN_Sitra'sDen | WLD_Main_A | 2 | [地下通道](Underground_Passage.md "地下通道") |
| 2 | DEN_Tunnels | UUID 6be608ff-3117-4a60-bbd3-1e2e7d2eb5d2 | DEN_Sitra'sDen | WLD_Main_A | 2 | [地下通道](Underground_Passage.md "地下通道") |
| 2 | DEN_Tunnels | UUID 6be608ff-3117-4a60-bbd3-1e2e7d2eb5d2 | DEN_Sitra'sDen | WLD_Main_A | 2 | [地下通道](Underground_Passage.md "地下通道") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 3 | GOB_GoblinThrone | UUID 8afe55c9-911e-4ba8-86be-5f9b366a2949 | GOB_GoblinCamp | WLD_Main_A | 20 | [破碎圣所](Shattered_Sanctum.md "破碎圣所") [座狼兽栏](Worg_Pens.md "座狼兽栏") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 4 | UND_Underdark | UUID 55dab4d2-f41f-440c-8204-3adf9a8f3c97 | - | WLD_Main_A | 48 | [幽暗地域](Underdark.md "幽暗地域") [奥法高塔](Arcane_Tower.md "奥法高塔") [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴") [破败村落](Decrepit_Village.md "破败村落") [恐怖窟窿](Dread_Hollow.md "恐怖窟窿") [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站") [仓库](Storehouse.md "仓库") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 5 | SCL_Camp | UUID e16bf254-d775-449b-a5b4-8d9cdd7b6eb4 | SCL_RuinedBattlefield | SCL_Main_A | 2 | [营地](Campsite.md "营地") |
| 6 | TWN_Subs | UUID 06d9861d-441d-4c75-98ed-b3b44f85d745 | TWN_Town | SCL_Main_A | 0 |  |
| 6 | TWN_Subs | UUID 06d9861d-441d-4c75-98ed-b3b44f85d745 | TWN_Town | SCL_Main_A | 0 |  |
| 6 | TWN_Subs | UUID 06d9861d-441d-4c75-98ed-b3b44f85d745 | TWN_Town | SCL_Main_A | 0 |  |
| 6 | TWN_Subs | UUID 06d9861d-441d-4c75-98ed-b3b44f85d745 | TWN_Town | SCL_Main_A | 0 |  |
| 6 | TWN_Subs | UUID 06d9861d-441d-4c75-98ed-b3b44f85d745 | TWN_Town | SCL_Main_A | 0 |  |
| 7 | MOO_MoonriseTowers | UUID 4a1cbd6d-15d3-48be-9669-94c5e32bf4dd | - | SCL_Main_A | 26 | [月出之塔](Moonrise_Towers.md "月出之塔") |
| 7 | MOO_MoonriseTowers | UUID 4a1cbd6d-15d3-48be-9669-94c5e32bf4dd | - | SCL_Main_A | 26 | [月出之塔](Moonrise_Towers.md "月出之塔") |
| 7 | MOO_MoonriseTowers | UUID 4a1cbd6d-15d3-48be-9669-94c5e32bf4dd | - | SCL_Main_A | 26 | [月出之塔](Moonrise_Towers.md "月出之塔") |
| 7 | MOO_MoonriseTowers | UUID 4a1cbd6d-15d3-48be-9669-94c5e32bf4dd | - | SCL_Main_A | 26 | [月出之塔](Moonrise_Towers.md "月出之塔") |
| 7 | MOO_MoonriseTowers | UUID 4a1cbd6d-15d3-48be-9669-94c5e32bf4dd | - | SCL_Main_A | 26 | [月出之塔](Moonrise_Towers.md "月出之塔") |
| 8 | COL_MindflayerColony | UUID 1e61e53c-3c83-48ae-8696-566904237c67 | - | SCL_Main_A | 6 | [夺心魔殖民地](Mind_Flayer_Colony.md "夺心魔殖民地") |
| 8 | COL_MindflayerColony | UUID 1e61e53c-3c83-48ae-8696-566904237c67 | - | SCL_Main_A | 6 | [夺心魔殖民地](Mind_Flayer_Colony.md "夺心魔殖民地") |
| 8 | COL_MindflayerColony | UUID 1e61e53c-3c83-48ae-8696-566904237c67 | - | SCL_Main_A | 6 | [夺心魔殖民地](Mind_Flayer_Colony.md "夺心魔殖民地") |
| 9 | WYR_WyrmsRock | UUID d1082b10-8440-47e1-9742-32bd97e3f865 | WYR_WyrmsCrossing | BGO_Main_A | 27 | [飞龙岩要塞](Wyrm's_Rock_Fortress.md "飞龙岩要塞") |
| 9 | WYR_WyrmsRock | UUID d1082b10-8440-47e1-9742-32bd97e3f865 | WYR_WyrmsCrossing | BGO_Main_A | 27 | [飞龙岩要塞](Wyrm's_Rock_Fortress.md "飞龙岩要塞") |
| 9 | WYR_WyrmsRock | UUID d1082b10-8440-47e1-9742-32bd97e3f865 | WYR_WyrmsCrossing | BGO_Main_A | 27 | [飞龙岩要塞](Wyrm's_Rock_Fortress.md "飞龙岩要塞") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 10 | CMP_Slums | UUID 81fbb859-b3f7-4e80-88eb-e14458e6bc75 | - | CTY_Main_A | 0 | [营地](Campsite.md "营地") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 11 | IRN_IronThrone | UUID 49a51492-f32e-4c24-ae60-6b92f827edad | - | IRN_Main_A | 3 | [钢铁王座](Iron_Throne.md "钢铁王座") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |
| 12 | END_BrainBattle | UUID 2fae42f0-74a8-42f8-81be-5460ce1111b4 | END_HighHall | END_Main | 1 | [塑境秘潭](Morphic_Pool.md "塑境秘潭") |

- [营地](Campsite.md "营地")

| 1 | CAMP_DungeonAbbey | UUID `a400aab1-6412-438c-8e08-74c77aa9ef98` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CAMP_CaveSandstone | UUID `cd89c5fd-78d4-4818-9fd1-60ae46e90711` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CAMP_GraniteCave | UUID `0e2d3423-bcb5-4848-9436-6900bfeaaac6` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CAMP_Basement | UUID `573926dc-345e-4092-a57c-b17f7fb5ecba` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CAMP_DungeonShar | UUID `b657fea0-3d0e-42ce-9e3f-34989267e313` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CAMP_Underdark | UUID `81fbd0dd-f3c7-4374-a929-4a5edd7552d2` | CAMP | WLD_Main_A | 0 |

- [营地](Campsite.md "营地")

| 1 | CRA_CrashSite | UUID `cb127a10-8570-4e9c-9efa-85c8234929b7` | - | WLD_Main_A | 16 | 与 CHA_ChapelForest 重叠 |

- [鹦鹉螺残骸](Nautiloid_Wreck.md "鹦鹉螺残骸")
- [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩")

| 2 | CHA_ChapelForest | UUID `705ad4b5-33e1-44bd-8aff-5807c845ac3c` | - | WLD_Main_A | 6 |

- [疮痍的海滩](Ravaged_Beach.md "疮痍的海滩")
- [蔓生废墟](Overgrown_Ruins.md "蔓生废墟")

| 2 | CHA_Crypt | UUID `5d3e3012-af9b-462a-8aac-4c44d058f2b9` | - | WLD_Main_A | 10 |

- [礼拜堂入口](Chapel_Entrance.md "礼拜堂入口")
- [卧室](Refectory.md "卧室")
- [阴暗墓穴](Dank_Crypt.md "阴暗墓穴")

| 2 | DEN_Base | UUID `2cc671cd-051b-425c-924e-caf1cb5dea74` | DEN_Sitra'sDen | WLD_Main_A | 7 | 与 DEN_Sitra'sDen 重叠 |

- [空谷](The_Hollow.md "空谷")
- [圣池](Sacred_Pool.md "圣池")
- [内殿](Inner_Sanctum.md "内殿")

| 2 | DEN_Tunnels | UUID `6be608ff-3117-4a60-bbd3-1e2e7d2eb5d2` | DEN_Sitra'sDen | WLD_Main_A | 2 |

- [地下通道](Underground_Passage.md "地下通道")

| 3 | DEN_Sitra'sDen | UUID `e5d891cc-6819-4c0b-bafe-d91526e35a13` | - | WLD_Main_A | 55 |

- [翠绿林地](Emerald_Grove.md "翠绿林地")
- [空谷](The_Hollow.md "空谷")
- [圣池](Sacred_Pool.md "圣池")
- [内殿](Inner_Sanctum.md "内殿")
- [隐秘河湾](Secluded_Cove.md "隐秘河湾")

| 3 | FOR_Forest | UUID `3642c1ba-d4e9-4c50-8be6-b8e0b20df4f8` | - | WLD_Main_A | 18 |

- [森林](Forest.md "森林")
- [染疫村落](Blighted_Village.md "染疫村落")

| 3 | FOR_OwlbearCave | UUID `c5470bb1-87ab-438c-bd8f-856fda6e8f7a` | - | WLD_Main_A | 1 |

- [枭熊巢穴](Owlbear_Nest.md "枭熊巢穴")

| 3 | FOR_MillCellar | UUID `c0ca3838-ebaf-40d2-a9d4-8000b2a796d3` | FOR_Forest | WLD_Main_A | 0 |

- [风车地窖](Blighted_Village.md#Windmill_Cellar "染疫村落")

| 3 | FOR_ThayanCellar | UUID `b544afce-44eb-4310-afec-c134b5048b13` | FOR_Forest | WLD_Main_A | 8 |

- [药材店地窖](Apothecary's_Cellar.md "药材店地窖")

| 3 | FOR_Bottomless | UUID `d9fb501a-9220-4dec-bce3-66963ae49e5f` | FOR_Forest | WLD_Main_A | 0 |

- [低语深地](Whispering_Depths.md "低语深地")

| 3 | GOB_GoblinCamp | UUID `4fc1a11a-c4d7-4d66-aa6e-ffbafac8d747` | - | WLD_Main_A | 17 |

- [地精营地](Goblin_Camp.md "地精营地")

| 3 | GOB_GoblinThrone | UUID `8afe55c9-911e-4ba8-86be-5f9b366a2949` | GOB_GoblinCamp | WLD_Main_A | 20 |

- [破碎圣所](Shattered_Sanctum.md "破碎圣所")
- [座狼兽栏](Worg_Pens.md "座狼兽栏")

| 4 | HAG_HagForest | UUID `85932019-f45a-4b42-936f-e0ed9a6ec9e1` | - | WLD_Main_A | 7 |

- [日照湿地](Sunlit_Wetlands.md "日照湿地")
- [破败的庇护所](Decrepit_Sanctuary.md "破败的庇护所")
- [河边茶室](Riverside_Teahouse.md "河边茶室")

| 4 | HAG_HagLair | UUID `c70e6802-6ecc-43c1-bd90-7365ef30f218` | - | WLD_Main_A | 6 |

- [蔓生地道](Overgrown_Tunnel.md "蔓生地道")

| 4 | PLA_Plains | UUID `81fb552a-982c-4ea8-939c-aebecb7b33d8` | - | WLD_Main_A | 30 |

- [晋升之路](The_Risen_Road.md "晋升之路")
- [渥金的休眠地](Waukeen's_Rest.md "渥金的休眠地")
- [山隘](Mountain_Pass.md "山隘")

| 4 | PLA_TollhouseCellar | UUID `d979d91b-de9c-4994-905e-40dd9131f823` | PLA_Plains | WLD_Main_A | 0 |

- [晋升之路收费站](The_Risen_Road.md#Toll_House "晋升之路")

| 4 | PLA_ZhentHideout | UUID `8e3b6144-219d-41a6-b93c-530cb5e4b970` | PLA_Plains | WLD_Main_A | 9 |

- [散塔林会地下室](Zhentarim_Basement.md "散塔林会地下室")

| 4 | UND_Underdark | UUID `55dab4d2-f41f-440c-8204-3adf9a8f3c97` | - | WLD_Main_A | 48 |

- [幽暗地域](Underdark.md "幽暗地域")
- [奥法高塔](Arcane_Tower.md "奥法高塔")
- [黑檀湖洞穴](Ebonlake_Grotto.md "黑檀湖洞穴")
- [破败村落](Decrepit_Village.md "破败村落")
- [恐怖窟窿](Dread_Hollow.md "恐怖窟窿")
- [塞伦涅信徒哨站](Selûnite_Outpost.md "塞伦涅信徒哨站")
- [仓库](Storehouse.md "仓库")

| 5 | UND_KuotoaVillage | UUID `739d67ac-d72e-4b85-aa9d-089a7d6cc648` | UND_Underdark | WLD_Main_A | 1 |

- [溃烂洞穴](The_Festering_Cove.md "溃烂洞穴")

| 5 | UND_KethericCity | UUID `99328fe1-ee8e-4053-a472-66906307dc9f` | - | WLD_Main_A | 34 |

- [复仇之炉](Grymforge.md "复仇之炉")

| 5 | UND_Rafts | UUID `cfe3a440-0435-4d49-bc6c-e29c0ff6cfe3` | UND_KethericCity | WLD_Main_A | 0  5 | CRE_GithCreche | UUID `54938b37-e81d-49f6-901b-81794c2fbb2e` | - | CRE_Main_A | 45 |

- [瑰晨修道院小径](Rosymorn_Monastery_Trail.md "瑰晨修道院小径")
- [瑰晨修道院](Rosymorn_Monastery.md "瑰晨修道院")
- [伊雷珂养育间](Crèche_Y'llek.md "伊雷珂养育间")

| 5 | SCL_RuinedBattlefield | UUID `f4ec7b66-d1e7-4212-b989-bb4330c9135b` | - | SCL_Main_A | 18 |

- [废弃战场](Ruined_Battlefield.md "废弃战场")

| 5 | SCL_KethericEntrance | UUID `a6c012df-e151-4f5a-ae0a-a27ac3e0f3a5` | SCL_RuinedBattlefield | SCL_Main_A | 0  5 | SCL_Camp | UUID `e16bf254-d775-449b-a5b4-8d9cdd7b6eb4` | SCL_RuinedBattlefield | SCL_Main_A | 2 |

- [营地](Campsite.md "营地")

| 6 | HAV_Haven | UUID `4d717266-a5d1-4859-ab70-8e8ad94f1fd2` | - | SCL_Main_A | 11 |

- [终焉光芒旅店](Last_Light_Inn.md "终焉光芒旅店")

| 6 | HAV_Basement | UUID `c4b1987a-5ad8-4044-a676-640f1b4c645e` | HAV_Haven | SCL_Main_A | 0 |

- [终焉光芒旅店 - 地窖](Last_Light_Inn_-_Cellar.md "终焉光芒旅店 - 地窖")

| 6 | HAV_Camp | UUID `c1fb63b0-5dc8-4aab-942c-2c49faefec0e` | HAV_Haven | SCL_Main_A | 0 |

- [营地](Campsite.md "营地")

| 6 | TWN_Town | UUID `c80c2c55-ce44-4997-b38c-3ed5c51fefad` | - | SCL_Main_A | 8 |

- [雷斯文小镇](Reithwin_Town.md "雷斯文小镇")

| 6 | TWN_Subs | UUID `06d9861d-441d-4c75-98ed-b3b44f85d745` | TWN_Town | SCL_Main_A | 0  7 | TWN_Mausoleum | UUID `5419d632-b082-46b3-8b03-a3d821efb36a` | TWN_Town | SCL_Main_A | 0 |

- [大陵寝](Grand_Mausoleum.md "大陵寝")

| 7 | SHA_SharTemple | UUID `27578949-7c0f-4faf-b2bc-702190c101f0` | - | SCL_Main_A | 18 |

- [莎尔铁手神殿](Gauntlet_of_Shar.md "莎尔铁手神殿")

| 7 | SHA_Nightsong | UUID `69fae777-0736-4321-8f7e-6c5eef53315e` | SHA_SharTemple | SCL_Main_A | 4 | 与 SHA_SharTemple 重叠 |

- [莎尔铁手神殿](Gauntlet_of_Shar.md "莎尔铁手神殿")

| 7 | SHA_Camp | UUID `25c3b101-d4fc-4f72-b46d-ed9849e61227` | SHA_SharTemple | SCL_Main_A | 0 |

- [营地](Campsite.md "营地")

| 7 | MOO_MoonriseTowers | UUID `4a1cbd6d-15d3-48be-9669-94c5e32bf4dd` | - | SCL_Main_A | 26 |

- [月出之塔](Moonrise_Towers.md "月出之塔")

| 8 | MOO_Camp | UUID `b444c04c-95af-4b9b-8d9c-e2f0a278686c` | MOO_MoonriseTowers | SCL_Main_A | 0 |

- [营地](Campsite.md "营地")

| 8 | MOO_MoonriseDungeon | UUID `2d30b88b-f311-4d85-9835-a0971fc304ab` | MOO_MoonriseTowers | SCL_Main_A | 43 |

- [月出之塔监狱](Moonrise_Towers_Prison.md "月出之塔监狱")

| 8 | COL_MindflayerColony | UUID `1e61e53c-3c83-48ae-8696-566904237c67` | - | SCL_Main_A | 6 |

- [夺心魔殖民地](Mind_Flayer_Colony.md "夺心魔殖民地")

| 9 | INT | UUID `1e61e53c-3c83-48ae-8696-566904237c67` | - | INT_Main_A | 1  9 | WYR_WyrmsCrossing | UUID `e359a849-5032-4c15-adc5-10af78edeb85` | - | BGO_Main_A | 84 |

- [飞龙关](Wyrm's_Crossing.md "飞龙关")

| 9 | WYR_WyrmsRock | UUID `d1082b10-8440-47e1-9742-32bd97e3f865` | WYR_WyrmsCrossing | BGO_Main_A | 27 |

- [飞龙岩要塞](Wyrm's_Rock_Fortress.md "飞龙岩要塞")

| 10 | CMP_CTY_Elfsong | UUID `a4f39099-da53-4e84-a0e2-4c7c496745db` | - | CTY_Main_A | 0 |

- [营地](Campsite.md "营地")

| 10 | CTY_ElfsongBasement | UUID `c326b55e-32ea-4327-aed2-3b2fbe4bd98c` | - | CTY_Main_A | 3 |

- [精灵之歌酒馆](Elfsong_Tavern.md "精灵之歌酒馆")

| 10 | CTY_BaldursMouth_Basement | UUID `9fd595c0-5ed2-406a-b635-fa4b02f7ce29` | - | CTY_Main_A | 0 |

- [博德之口](Baldur's_Mouth.md "博德之口")

| 10 | CTY_Heapside_Prison | UUID `d187573b-34bf-4c82-831b-8fa0832ebb67` | - | CTY_Main_A | 0 |

- [石化蜥蜴之门营房](Basilisk_Gate_Barracks.md "石化蜥蜴之门营房")

| 10 | CTY_DjinniLamp | UUID `11911fb3-65b0-4501-9931-67fec8bbc644` | - | CTY_Main_A | 0  10 | CTY_GuildhallBasement | UUID `0fe924c3-9387-416f-ad00-710fadb37212` | - | CTY_Main_A | 0 |

- [公会大厅](Guildhall.md "公会大厅")

| 10 | CTY_LowerCity | UUID `4d9acf0c-d5ac-4f53-8f9b-d74379b5e72d` | - | CTY_Main_A | 160 |

- [下城区](Lower_City.md "下城区")

| 10 | CTY_BloodMerchantLab | UUID `48929bda-2ccf-4f21-8e7a-1a11ecd85faa` | CTY_LowerCity | CTY_Main_A | 0 |

- [腥红跳棋](Crimson_Draughts.md "腥红跳棋")

| 10 | CTY_BonecloaksApothecary_Basement | UUID `ec0cbc96-50d8-47fe-9d3a-5863aac782ab` | CTY_LowerCity | CTY_Main_A | 0 |

- [白骨斗篷药材店](Bonecloak's_Apothecary.md "白骨斗篷药材店")

| 10 | CTY_Catacombs | UUID `cbfc19c2-3fbd-4f73-85d2-1e8de2e3b2cb` | CTY_LowerCity | CTY_Main_A | 0  10 | CTY_DevilandSmithBasement | UUID `fa170e45-4806-47fc-809c-348ca5495a1b` | CTY_LowerCity | CTY_Main_A | 0 |

- [九层锻炉](Forge_of_the_Nine.md "九层锻炉")

| 10 | CTY_FigaroBasement | UUID `472179fc-9c00-4c63-9a3a-9c1832127a4d` | CTY_LowerCity | CTY_Main_A | 0 |

- [焕颜精品店](Facemaker's_Boutique.md "焕颜精品店")

| 10 | CTY_FireWorks_Basement | UUID `2a3a7e6e-2626-4805-a08e-cea3e203b92b` | CTY_LowerCity | CTY_Main_A | 0 |

- [费洛杰尔烟花铺](Felogyr's_Fireworks.md "费洛杰尔烟花铺")

| 10 | CTY_GardenTools | UUID `40c8a60f-65cf-4321-9854-b9c1c8ba75d0` | CTY_LowerCity | CTY_Main_A | 0  10 | CTY_Golbraith_Basement | UUID `5171e6bb-bf50-455f-9bf0-510a81c729d7` | CTY_LowerCity | CTY_Main_A | 0 |

- [加尔布雷斯地窖](Golbraith's_Cellar.md "加尔布雷斯地窖")

| 10 | CTY_Groundkeeper_Basement | UUID `61d83d13-e0ba-4909-b754-31871c59b4d4` | CTY_LowerCity | CTY_Main_A | 0 |

- [拉韦尔尼卡之家](Lavernica's_Home.md "拉韦尔尼卡之家")

| 10 | CTY_HagSurvivor_Basement | UUID `7e6c06c4-f425-4045-a93a-5a6284070395` | CTY_LowerCity | CTY_Main_A | 0 |

- [老加洛之家](Old_Garlow's_Place.md "老加洛之家")

| 10 | CTY_Highberrys_Cellar | UUID `28e72471-ada8-41c9-b9e6-24bcaef3e3d7` | CTY_LowerCity | CTY_Main_A | 0 |

- [海伯瑞之家](Highberry's_Home.md "海伯瑞之家")

| 10 | CTY_LodgeBasement | UUID `65f52ab3-c87d-4bbe-bfd2-00a60cc51c80` | CTY_LowerCity | CTY_Main_A | 0 |

- [会馆](The_Lodge.md "会馆")

| 10 | CTY_MusicStore_Basement | UUID `5b37bcc7-632f-450e-acb8-bea10067681d` | CTY_LowerCity | CTY_Main_A | 0 |

- [半音商店](Chromatic_Scale.md "半音商店")

| 10 | CTY_Peartree_Basement | UUID `11640b67-8ee3-4b5d-9a77-f68916059b56` | CTY_LowerCity | CTY_Main_A | 0 |

- [梨木之家](Peartree_House.md "梨木之家")

| 10 | CTY_PhilgraveBasement | UUID `c4a272c5-1d72-47d0-b29b-c8222851a1cc` | CTY_LowerCity | CTY_Main_A | 0 |

- [菲尔格雷弗宅邸](Philgrave's_Mansion.md "菲尔格雷弗宅邸")

| 10 | CTY_Rainforest_Basement | UUID `f4122a31-1eef-47e6-8795-12f9782b48cc` | CTY_LowerCity | CTY_Main_A | 0 |

- [雨林之家](Rainforest's_Home.md "雨林之家")

| 10 | CTY_Tabernacle_Basement | UUID `1c21a150-eab0-40c6-b5b0-41c8a6a17d81` | CTY_LowerCity | CTY_Main_A | 0 |

- [风暴海岸礼拜堂](Stormshore_Tabernacle.md "风暴海岸礼拜堂")

| 10 | CTY_Thumbo_Basement | UUID `22f30832-2b96-48d6-b66a-72a87aadadcf` | CTY_LowerCity | CTY_Main_A | 0 |

- [沃纳伊之家](Vonayn's_Home.md "沃纳伊之家")

| 10 | CMP_Slums | UUID `81fbb859-b3f7-4e80-88eb-e14458e6bc75` | - | CTY_Main_A | 0 |

- [营地](Campsite.md "营地")

| 11 | CTY_BlushingMermaidCellar | UUID `1f4ea69b-ec6a-4fdd-a3a1-b5bac41f5ebe` | - | CTY_Main_A | 6 |

- [脸红的美人鱼](The_Blushing_Mermaid.md "脸红的美人鱼")

| 11 | CTY_DockwarehouseBasement | UUID `bb6ae7b3-b078-4cad-a57a-d21248fb6434` | - | CTY_Main_A | 0 |

- [弗莱姆货运](Flymm_Cargo.md "弗莱姆货运")

| 11 | CTY_JaheiraBasement | UUID `115be7b7-8ba6-41db-a1b0-1e214c5e38c7` | - | CTY_Main_A | 0 |

- [戈尔布雷斯之家](Elerrathin's_Home.md "戈尔布雷斯之家")

| 11 | CTY_MurderTribunal | UUID `cf15ae3f-2811-4d4c-bffe-fe8b170be15b` | - | CTY_Main_A | 4 |

- [坎德哈洛墓碑店](Candulhallow's_Tombstones.md "坎德哈洛墓碑店")

| 11 | CTY_SharranGrotto | UUID `3123c265-bcc8-4431-9a44-585d81ec5747` | - | CTY_Main_A | 0 |

- [哀伤之邸](House_of_Grief.md "哀伤之邸")

| 11 | CTY_Sewers | UUID `52cba64e-747e-4e2a-a944-85a9292636a5` | - | CTY_Main_A | 2 |

- [下城区下水道](Lower_City_Sewers.md "下城区下水道")

| 11 | CTY_SteelWatchLabControlCenter | UUID `34843511-217f-4f5f-b8f8-f473ee6e19f3` | - | CTY_Main_A | 43 |

- [钢铁卫士铸造厂](Steel_Watch_Foundry.md "钢铁卫士铸造厂")

| 11 | CTY_WQH_Basement | UUID `d56754e9-3694-4ec7-89bc-871a1725f620` | - | CTY_Main_A | 11 |

- [水女王之家](Water_Queen's_House.md "水女王之家")

| 11 | CTY_AncientLair | UUID `1bcba602-1572-4788-9464-6c390a7ab5d9` | CTY_Sewers | CTY_Main_A | 0 |

- [古代密室](Ancient_Lair.md "古代密室")

| 11 | CTY_CountingHouseVaultConnection | UUID `faf4f3ed-e9a5-460c-ba46-131b021ae13b` | - | CTY_Main_A | 0 |

- [清账屋](The_Counting_House.md "清账屋")

| 11 | CTY_Submersible | UUID `2f76d70e-a899-4225-b438-53764cc3b716` | - | CTY_Main_A | 0 |

- [潜水器](Submersible.md "潜水器")

| 11 | IRN_IronThrone | UUID `49a51492-f32e-4c24-ae60-6b92f827edad` | - | IRN_Main_A | 3 |

- [钢铁王座](Iron_Throne.md "钢铁王座")

| 12 | CTY_CazadorChapel | UUID `9f923966-15bf-41bb-bbe5-0d142b46f458` | - | CTY_Main_A | 22 |

- [扎尔宅邸](Szarr_Palace.md "扎尔宅邸")
- [卡扎多尔的地牢](Cazador's_Dungeon.md "卡扎多尔的地牢")

| 12 | CTY_CazadorPalace | UUID `aaa1eeea-74af-490d-8350-a36c110c1072` | - | CTY_Main_A | 0 |

- [扎尔宅邸](Szarr_Palace.md "扎尔宅邸")

| 12 | CTY_CazAttic | UUID `fbf0e037-a1a1-47ab-ad27-03ab31d161e2` | CTY_CazadorPalace | CTY_Main_A | 0 |

- [扎尔宅邸](Szarr_Palace.md "扎尔宅邸")

| 12 | CTY_CazSideroom | UUID `c363282d-08de-4974-991c-4e5dbdbaeb4e` | CTY_CazadorPalace | CTY_Main_A | 0 |

- [扎尔宅邸](Szarr_Palace.md "扎尔宅邸")

| 12 | CTY_BhaalsTemple | UUID `96d29e10-01cb-4133-8715-18c567cfcb9e` | - | CTY_Main_A | 16 |

- [巴尔神殿](Bhaal_Temple.md "巴尔神殿")

| 12 | CTY_HouseOfHope | UUID `e9e4d04f-e450-46ab-b1cf-bf7997c411b3` | - | CTY_Main_A | 32 |

- [希望之邸](House_of_Hope.md "希望之邸")

| 12 | CTY_Ramazith | UUID `d79d67f1-cac9-48d9-acd5-20d5839d585c` | - | CTY_Main_A | 3 |

- [拉玛吉斯高塔](Ramazith's_Tower.md "拉玛吉斯高塔")

| 12 | CTY_SorcerousSundriesBasement | UUID `dea64172-1891-4086-8b95-57e735b3fd35` | CTY_Ramazith | - | 0 |

- [巫术杂物店](Sorcerous_Sundries.md "巫术杂物店")

| 12 | END_HighHall | UUID `0cdf1ef6-8a39-48af-b16c-3279ab9c2d1c` | - | END_Main | 0 |

- [至高大殿](High_Hall.md "至高大殿")

| 12 | END_HighHallSewer | UUID `71ce22c9-073f-433d-8605-df0585c98f01` | - | END_Main | 0 |

- [上城区下水道](Upper_City_Sewers.md "上城区下水道")

| 12 | END_MorphicPool | UUID `5dcbf925-c04c-49d1-8cec-d7d9f6e22e55` | - | END_Main | 0 |

- [塑境秘潭](Morphic_Pool.md "塑境秘潭")

| 12 | END_BrainBattle | UUID `2fae42f0-74a8-42f8-81be-5460ce

---
*Source: [Area level](https://bg3.wiki/wiki/Area_level)*
