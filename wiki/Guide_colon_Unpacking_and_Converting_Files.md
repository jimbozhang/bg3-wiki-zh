# Modding:解包与转换文件

## [社区](bg3wiki_colon_Community.md "bg3wiki:Community") • [指南](Guide_colon_Guides.md "Guide:Guides") • [模组](Modding_colon_Modding_resources.md "Modding:Modding resources")

| [社区](bg3wiki_colon_Community.md "bg3wiki:Community") • [指南](Guide_colon_Guides.md "Guide:Guides") • [模组](Modding_colon_Modding_resources.md "Modding:Modding resources") |  |
| --- | --- |
| [模组指南](Category_colon_Modding.md "Category:Modding") | [BG3 Mini Tool](Modding_colon_BG3_Mini_Tool.md "Modding:BG3 Mini Tool") [Blender导出设置](Modding_colon_Blender_Export_Settings.md "Modding:Blender Export Settings") [代码片段](Modding_colon_Code_Snippets.md "Modding:Code Snippets") [编写物品代码](Modding_colon_Coding_An_Item.md "Modding:Coding An Item") [兼容性框架](Modding_colon_Compatibility_Framework.md "Modding:Compatibility Framework") [创建自定义布料碰撞体](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:Creating a custom cloth collider") [在Blender中创建和导出网格](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:Creating and Exporting Meshes in Blender") [创建物品图标](Modding_colon_Creating_Item_Icons.md "Modding:Creating Item Icons") [创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:Creating meta.lsx") [创建模组](Modding_colon_Creating_mods.md "Modding:Creating mods") [编辑角色创建预设](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:Editing a Character Creation Preset") [编辑Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:Editing Equipment.txt") [如何查找虚拟纹理](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture") [安装模组](Modding_colon_Installing_mods.md "Modding:Installing mods") [本地化](Modding_colon_Localization.md "Modding:Localization") [模组资源](Modding_colon_Modding_resources.md "Modding:Modding resources") [打包模组](Modding_colon_Packaging_mods.md "Modding:Packaging mods") [纹理格式](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [宝藏表](Modding_colon_Treasure_Tables.md "Modding:Treasure Tables") [理解模组文件夹结构](Understanding_Mod_Folder_Structure.md "Understanding Mod Folder Structure") [解包与转换文件](Modding_colon_Unpacking_and_converting_files.md "Modding:Unpacking and converting files") [处理LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |
| [模组资源](Modding_colon_Modding_resources.md "Modding:Modding resources") | [护甲/服装纹理贴图](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:Armor/Clothing Texture Maps") [身体模型](Modding_colon_Body_Models.md "Modding:Body Models") [自定义变形术](Modding_colon_Custom_polymorph.md "Modding:Custom polymorph") [依赖项](Modding_colon_Dependencies.md "Modding:Dependencies") [面部和身体纹理](Modding_colon_Face_and_body_textures.md "Modding:Face and body textures") [修复骨骼错误](Modding_colon_Fixing_bone_errors.md "Modding:Fixing bone errors") [修复颈部接缝](Modding_colon_Fixing_neck_seams.md "Modding:Fixing neck seams") [修复UV错误](Modding_colon_Fixing_UV_errors.md "Modding:Fixing UV errors") [BG3模组入门](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:Getting Started with BG3 Modding") [头发网格](Modding_colon_Hair_Meshes.md "Modding:Hair Meshes") [头部模型](Modding_colon_Head_Models.md "Modding:Head Models") [模组故障排除](Modding_colon_Mod_troubleshooting.md "Modding:Mod troubleshooting") [模组职业图标](Modding_colon_Modding_class_icons.md "Modding:Modding class icons") [NPC头部模型](Modding_colon_NPC_Head_Models.md "Modding:NPC Head Models") [提夫林角模型](Tiefling_Horn_Models.md "Tiefling Horn Models") [非虚拟纹理着色器](Modding_colon_Non-VT_Shaders.md "Modding:Non-VT Shaders") [种族UUID](Modding_colon_Race_UUID.md "Modding:Race UUID") [示例模板](Modding_colon_Sample_Templates.md "Modding:Sample Templates") [法术标志](Spell_flags.md "Spell flags") [纹理格式](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [工具](Modding_colon_Tools.md "Modding:Tools") [宝藏表参考](Modding_colon_TreasureTables_References.md "Modding:TreasureTables References") [教程](Modding_colon_Tutorials.md "Modding:Tutorials") [顶点颜色遮罩槽](Modding_colon_VertexColorMaskSlots.md "Modding:VertexColorMaskSlots") [处理LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |

[模组索引](Modding_colon_Index.md "Modding:Index")

## 目录

- [1 必要工具](#必要工具)
- [2 解包流程](#解包流程)
  - [2.1 索引](#索引)
    - [2.1.1 索引搜索解包](#索引搜索解包)
  - [2.2 手动解包](#手动解包)
- [3 文件转换](#文件转换)
  - [3.1 .lsf → .lsx](#.lsf-→-.lsx)
  - [3.2 .gr2 → .dae](#.gr2-→-.dae)
  - [3.3 .dds](#.dds)
  - [3.4 .gts → .dds](#.gts-→-.dds)
  - [3.5 .wem → .ogg](#.wem-→-.ogg)
  - [3.6 .loca → .xml](#.loca-→-.xml)

## 必要工具

- LSLIB by Norbyte
- _注意：此步骤主要是为了从旧版LSLIB中获取**granny2.dll**。最新发布版本可能已包含此文件，如果是这样，您可以直接安装最新版本。_
  - 首先安装 [1.15.13](https://github.com/Norbyte/lslib/releases/tag/v1.15.13)，然后安装 [最新](https://github.com/Norbyte/lslib/releases) 版本。
- Modders Multitool by ShinyHobo
  - 安装 [最新](https://github.com/ShinyHobo/BG3-Modders-Multitool/releases) 版本。
  - 确保您用于Multitool的文件夹与LSLIB文件夹分开。

**该工具有一个官方Wiki，现在分解了解包和工具的其他部分：[BG3 Modders Multitool Wiki](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki)**

请使用该Wiki获取最新信息。

现在来看ExportTool。

此项目需要 **granny2.dll** 文件才能正常工作。由于许可问题，Norbyte在之后的某些版本中移除了此文件，但它存在于旧版本中，例如v1.15.13，链接如上。

验证 **granny2.dll** 文件是否存在于ExportTool的**根文件夹**和**Tools**子文件夹中。如果文件在这两个文件夹中都存在，那么您无需对ExportTool进行任何其他操作，可以直接跳到本指南的下一节。

如果最新版本的ExportTool的**根文件夹**和/或**Tools**子文件夹中缺少**granny2.dll**文件，那么您需要从旧版本v1.15.13复制该文件。打开存档 **ExportTool-v1.15.13.zip**，复制 **granny2.dll** 文件，并将其粘贴到您解压最新版本ExportTool的**根文件夹**和**Tools**子文件夹中。无需对ExportTool进行任何其他操作。

要运行ExportTool，请打开ConverterApp.exe。

## 解包流程

目前，由于Multitool的更新，我们不再需要直接解包游戏pak文件。相反，您可以索引文件并根据需要解包文件。这可以节省一些硬盘空间，因为BG3有很多文件。

### 索引

**[Multitool关于索引和搜索的Wiki文章](https://github.com/ShinyHobo/BG3-Modders-Multitool/wiki/Index-Search)**

在Multitool中，转到 工具 > 索引 > 索引Pak文件，这将索引所有已解包的pak文件。比解包所有pak更快、更易于维护。

- 当我们获得新的热修复时，请按照上述步骤再次索引新的热修复pak。

但是，每当获得完整补丁版本时，建议首先清除索引并使用以下方法重新索引：工具 > 索引 > 清除索引，然后工具 > 索引 > 索引Pak文件

如果您仍然想手动解包游戏pak，而不是通过新方法解包单个文件，可以使用：**工具** > **游戏文件操作** > **解包游戏文件**。

- - 自补丁4起，当新补丁发布时，热修复pak会合并到主pak中。

#### 索引搜索解包

如果您知道要解包资产的常用名称，可以使用索引搜索（在索引完成后）解包特定资产。例如，假设我们要创建头部模组，因此需要从资产中解包头部模型。

这里我们使用过滤器仅显示GR2资产，如下所示：

然后我们搜索NKD_Head，如下所示：

现在选择全部并提取所选内容。

请注意，这将提取的不仅仅是我们可以扮演的种族，但与提取整个models.pak相比，它占用的空间要少得多，如果我们只想创建头部模组的话。您也可以使用此功能浏览列表以选择要提取的特定资产。这不仅限于GR2，只需选择要过滤的资产，然后提取即可。

- 请注意放置Multitool的硬盘空间，因为它会在提取文件的位置创建一个UnpackedData文件夹。

### 手动解包

如果您仍然想手动解包游戏pak，而不是通过新方法解包单个文件，可以使用 **工具** > **游戏文件操作** > **解包游戏文件**。

- 通常，只有当您有足够的硬盘空间专门用于解包文件时，才建议这样做，因为它们可能占用相当多的空间。
- 将出现一个类似于以下内容的菜单：
  - （自补丁4起，当新补丁发布时，热修复包会合并到主pak中）

常见文件：

- English.pak — 本地化文件所在位置，即游戏中显示的所有文本字符串。
- Gustav.pak — .lsf格式的文本文件。关卡数据、对话文件、装备属性、法术。
- Materials.pak — 材质（着色器）。它本身无用，但您可以查看游戏中有哪些材质，以便将其分配给您的模型。
- Models.pak — .gr2格式的模型。头部、头发、护甲、建筑等。
- Textures.pak — .dds格式的纹理。这里没有太多纹理，因为大多数纹理都保存在虚拟纹理中。这些主要是颜色ID遮罩，用于将护甲划分为着色区域。但也有面部、头发、纹身的纹理。一些环境纹理。
- Shared.pak — .lsf格式的文本文件。在某些方面与Gustav重叠。分配了材质的模型数据、皮肤、头发、眼睛颜色等，用于角色编辑器，还有装备属性、法术。
- VirtualTextures.pak — 游戏中的大部分纹理都在这里，打包在虚拟纹理中以提高性能。
- Voice.pak — 语音台词。

选中您需要的框，然后单击**确认**。解包可能需要一段时间。

## 文件转换

大多数解压后的文件无法直接查看或编辑，因此您必须将它们转换为可读格式。

### .lsf → .lsx

来自 **Gustav.pak** 和 **Shared.pak** 的大多数文件。Modders Multitool可以将它们转换为可读的 .lsx。解包文件完成后，您需要单击**解压文件**并等待文件自动转换。

### .gr2 → .dae

来自 **Models.pak** 的模型（网格）文件。这些可以使用ExportTool转换。在GR2 Tools程序的第一个选项卡中指定所需 `.gr2` 文件的路径，以及下方转换后文件保存的路径。**!!!** 您必须在名称后添加 `.dae` **!!!**

首先单击导入按钮导入游戏 `.gr2` 模型，然后导出以将其转换为 `.dae` 格式。`.dae` 可以使用任何3D编辑器打开。

您也可以将 `.gr2` 直接导入 Blender 3.x.x+。Norbyte更新了他们的导入和导出模型插件，最新版本可以在[这里](https://github.com/Norbyte/dos2de_collada_exporter)找到。在插件设置中，我们指定ExportTool的 **divine.exe** 路径。

现在您可以将 `.gr2` 直接导入 Blender。

### .dds

来自 **Textures.pak** 的纹理文件。可以通过安装Nvidia网站的 [Adobe Photoshop插件](https://developer.nvidia.com/nvidia-texture-tools-exporter) 来打开。对于没有Photoshop的用户，免费的 [Gimp](https://www.gimp.org/downloads/) 从2.10.10版本开始支持 .dds。[Paint.net](https://www.getpaint.net/) 也可以打开 .dds 文件，并且是免费的。
如果您需要将纹理导入其他程序或引擎（Substance Painter、Blender、Unreal、Unity），最好将它们保存为Targa (.tga) 格式。这将保留alpha通道。

### .gts → .dds

来自 **VirtualTextures.pak** 的虚拟纹理。它们也可以使用ExportTool解包（从1.17.0版本开始）。转到**虚拟纹理**选项卡，指定 `.gts` 文件、导出路径，然后单击**提取纹理**。它将生成一堆 `.dds` 文件。

### .wem → .ogg

来自 **Voice.pak** 的音频文件。对于 `.wem`，您需要来自Nexus Mods的 [Automatic .wem to .ogg Converter](https://www.nexusmods.com/monsterhunterworld/mods/1912?tab=description) 脚本。它是为Monster Hunter: World制作的，但与BG3文件完美兼容。存档内有一个文件夹 WEM to OGG Converter。您需要将其中的文件放入 .wem 文件所在的文件夹，并运行 `script.bat`。脚本会自动将所有 `.wem` 转换为 `.ogg` 文件，这些文件可以用标准媒体播放器打开。

### .loca → .xml

来自 **English.pak** 的本地化文本（其他语言相同）。`.loca` 文件可以使用Export Tool转换。选择 `.loca` 文件并指定用作输出的 `.xml` 文件的名称。

---
*Source: [Modding:Unpacking and converting files](https://bg3.wiki/wiki/Modding:Unpacking_and_converting_files)*