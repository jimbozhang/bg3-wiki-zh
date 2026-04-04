# 理解模组文件夹结构

## 通用模组的文件夹结构

以下是典型模组的文件夹结构示例。其目的并非详尽无遗，而是展示一般模组中最核心部分的文件夹结构。大括号 `{}` 中的文本需由模组作者自行填写。

- {模组名称} (根目录/工作区文件夹)
- Generated
- Public
- {模组名称}
- [PAK]_{模组名称} (包含模型和纹理)
  - Localization
- {语言} (通常仅称为 _English_)
- `{模组名称}.loca.xml` (包含物品和法术的显示文本)
- Mods
- {模组名称}
- `meta.lsx` (更多信息请参见 [创建 meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建 meta.lsx"))
  - Public (使用 [示例模组](https://bg3.wiki/wiki/Modding:Sample_Templates) 之一作为此文件夹的模板)
    - Game (图标和其他UI元素)
    - {模组名称} (纯文本或XML格式的模组文件)
  - ScriptExtender (仅当使用 [Norbyte的Script Extender](https://github.com/Norbyte/bg3se) 时才会出现此文件夹及其内容)
    - Config.json

## 带有新网格和纹理的护甲模组的文件夹结构

以下是BG3模组的结构示例。您可以将其与 [示例模组](https://bg3.wiki/wiki/Modding:Sample_Templates) 进行比较和对比。

您的模组名为 **MySweetMod**

- MySweetMod
- Generated
- Public
- MySweetMod
- Assets <- 模型和纹理
  - Localization
- Language <- 通常为 _English_
- `MySweetMod.loca` <- 物品和法术的文本
- Mods
- MySweetMod
- `meta.lsx` <- 参见 [创建 meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建 meta.lsx")
- Public
- Game
- Assets
        - ControllerItems
- items_png <--- 144 x 144 .DDS 服装和武器图标文件
- skills_png <--- 144 x 144 .DDS 法术和被动图标文件
- Tooltips
- ItemIcons <--- 380 x 380 .DDS 服装和武器图标文件
- Icons <--- 380 x 380 .DDS 法术和被动图标文件
- MySweetMod
- Assets
- Textures
- Icons <--- 图标的 .dds 纹理图集
- Content
- - Assets
- Characters
- [PAK]\_Armor <-- 自定义服装和武器的材质和网格 LSX。
- UI
- [PAK]\_UI <--- 包含 '_merged.lsx'。这告诉游戏纹理图集 dds 的名称和位置。
- GUI <--- Icons_Items.lsx。这设置了图标纹理图集的位置。
- RootTemplates <--- 您的 Roottemplate lsx 放置于此。MySweetMod.Lsx
- Stats
- - Generated <--- TreasureTable.txt - 这告诉游戏物品的生成位置。
- Data <--- Armor.txt, Object.txt, Passive.txt, Weapon.txt 和其他 TXT 文件。这些包含统计数据。

---
*Source: [Understanding Mod Folder Structure](https://bg3.wiki/wiki/Understanding_Mod_Folder_Structure)*