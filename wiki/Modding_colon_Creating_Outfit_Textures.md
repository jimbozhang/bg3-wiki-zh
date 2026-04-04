# Modding:Creating Outfit Textures

## [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources")

| [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources") |  |
| --- | --- |
| [Modding guides](Category_colon_Modding.md "Category:Modding") | [BG3 Mini Tool](Modding_colon_BG3_Mini_Tool.md "Modding:BG3 Mini Tool") [Blender Export Settings](Modding_colon_Blender_Export_Settings.md "Modding:Blender Export Settings") [Code Snippets](Modding_colon_Code_Snippets.md "Modding:Code Snippets") [Coding An Item](Modding_colon_Coding_An_Item.md "Modding:Coding An Item") [Compatibility Framework](Modding_colon_Compatibility_Framework.md "Modding:Compatibility Framework") [Creating a custom cloth collider](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:Creating a custom cloth collider") [Creating and Exporting Meshes in Blender](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:Creating and Exporting Meshes in Blender") [Creating Item Icons](Modding_colon_Creating_Item_Icons.md "Modding:Creating Item Icons") [Creating meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:Creating meta.lsx") [Creating mods](Modding_colon_Creating_mods.md "Modding:Creating mods") [Editing a Character Creation Preset](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:Editing a Character Creation Preset") [Editing Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:Editing Equipment.txt") [How To Find A Virtual Texture](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture") [Installing mods](Modding_colon_Installing_mods.md "Modding:Installing mods") [Localization](Modding_colon_Localization.md "Modding:Localization") [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") [Packaging mods](Modding_colon_Packaging_mods.md "Modding:Packaging mods") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Treasure Tables](Modding_colon_Treasure_Tables.md "Modding:Treasure Tables") [Understanding Mod Folder Structure](Understanding_Mod_Folder_Structure.md "Understanding Mod Folder Structure") [Unpacking and converting files](Modding_colon_Unpacking_and_converting_files.md "Modding:Unpacking and converting files") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |
| [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") | [Armor/Clothing Texture Maps](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:Armor/Clothing Texture Maps") [Body Models](Modding_colon_Body_Models.md "Modding:Body Models") [Custom polymorph](Modding_colon_Custom_polymorph.md "Modding:Custom polymorph") [Dependencies](Modding_colon_Dependencies.md "Modding:Dependencies") [Face and body textures](Modding_colon_Face_and_body_textures.md "Modding:Face and body textures") [Fixing bone errors](Modding_colon_Fixing_bone_errors.md "Modding:Fixing bone errors") [Fixing neck seams](Modding_colon_Fixing_neck_seams.md "Modding:Fixing neck seams") [Fixing UV errors](Modding_colon_Fixing_UV_errors.md "Modding:Fixing UV errors") [Getting Started with BG3 Modding](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:Getting Started with BG3 Modding") [Hair Meshes](Modding_colon_Hair_Meshes.md "Modding:Hair Meshes") [Head Models](Modding_colon_Head_Models.md "Modding:Head Models") [Mod troubleshooting](Modding_colon_Mod_troubleshooting.md "Modding:Mod troubleshooting") [Modding class icons](Modding_colon_Modding_class_icons.md "Modding:Modding class icons") [NPC Head Models](Modding_colon_NPC_Head_Models.md "Modding:NPC Head Models") [Tiefling Horn Models](Tiefling_Horn_Models.md "Tiefling Horn Models") [Non-VT Shaders](Modding_colon_Non-VT_Shaders.md "Modding:Non-VT Shaders") [Race UUID](Modding_colon_Race_UUID.md "Modding:Race UUID") [Sample Templates](Modding_colon_Sample_Templates.md "Modding:Sample Templates") [Spell flags](Spell_flags.md "Spell flags") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Tools](Modding_colon_Tools.md "Modding:Tools") [TreasureTables References](Modding_colon_TreasureTables_References.md "Modding:TreasureTables References") [Tutorials](Modding_colon_Tutorials.md "Modding:Tutorials") [VertexColorMaskSlots](Modding_colon_VertexColorMaskSlots.md "Modding:VertexColorMaskSlots") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |

[Modding index](Modding_colon_Index.md "Modding:Index")

本指南将介绍如何为[你的自定义服装](Modding_colon_Creating_Armor_Mods.md "Modding:Creating Armor Mods")制作纹理。

## 目录

- [1 软件](#软件)
- [2 概述](#概述)
- [3 基础色/基础贴图](#基础色-基础贴图)
- [4 法线贴图](#法线贴图)
- [5 物理贴图](#物理贴图)
  - [5.1 红色通道：金属度](#红色通道金属度)
  - [5.2 绿色通道：粗糙度](#绿色通道粗糙度)
  - [5.3 蓝色通道：环境光遮蔽](#蓝色通道环境光遮蔽)
- [6 MSK](#MSK)
  - [6.1 使用 Blender 制作 MSK 文件](#使用-Blender-制作-MSK-文件)
- [7 GM](#GM)
- [8 如何打开纹理并提取其文件](#如何打开纹理并提取其文件)
  - [8.1 物理贴图](#物理贴图)
  - [8.2 BM 和 MSK](#BM-和-MSK)
  - [8.3 法线贴图](#法线贴图)
- [9 文件大小](#文件大小)
- [10 如何保存纹理](#如何保存纹理)
- [11 记住你的 Mipmap](#记住你的-Mipmap)
- [12 工具](#工具)

## 软件

本教程需要 GIMP 和 Blender，但你也可以使用任何可以组合通道或保存为 DDS 的程序，例如 Photoshop。

在平面上看起来不错的东西在模型上可能就不好看了。理想情况下，你需要一些可以直接在模型上绘画的软件。例如 Blender 的纹理绘制模式、Armorpaint 或 Quixel Mixer，当然还有 Substance Painter，都值得研究。

建议导出 UV 映射的副本，以便将其用作参考。在 Blender 中打开你的物品，转到 UV 编辑选项卡。点击 UV，选择导出 UV 布局。勾选所有 UV。你现在将获得一个半透明的图像，可用作纹理的模板。

## 概述

这是伊索贝尔的饰环的 BM、NM、PM 和 MSKcloth。

一个通用护甲物品有四种纹理。有时是 3 种，因为物品没有 MSK，所有颜色都在 BM 上（例如米佐拉的服装）。有时是 4-5 种，因为物品可能有 GM（辉光贴图）。

## 基础色/基础贴图

这控制颜色强度。它是平坦的白色或灰色，因为颜色通过 MSK 叠加在其上。游戏的着色器功能强大，因此许多 BM 不太详细。如果没有透明度，它将被称为 BM；如果有，则称为 BMA。A 代表 alpha，因为透明度需要 alpha 通道。

## 法线贴图

BG3 法线贴图格式的通道。

蓝色透明贴图。这使得游戏的着色引擎以使物体看起来比实际更有深度的方式从物品上反射光线。这是最重要的纹理。

通常使用 2 种类型的法线贴图。一种，OpenGL，看起来是正面朝外。另一种，DirectX，看起来是内翻（例如按钮会向内凹陷）。

OpenGL 和 DirectX 纹理格式之间的差异。

BG3 使用 DirectX 的修改版本，其中红色通道（X 轴）被放入 alpha 通道，以节省文件格式空间。

_通道：_

红色 - 未使用，填充为全黑

绿色 - Y（绿色通道）

蓝色 - Z（蓝色通道）

Alpha - X（红色通道）

## 物理贴图

物理贴图示例。

物理贴图是 3 张贴图合而为一，组合成一张图像。很容易识别，它将是粉色、绿色和蓝色，或这些颜色的某种组合。

### 红色通道：金属度

决定对象是否使用金属着色器。

此贴图的白色部分是金属。黑色部分不是。你可能希望尝试一下——游戏中的大多数金属 MSK 不是纯白色，而是具有纹理，以使物品看起来更有趣。一些非金属物品，如宝石、天鹅绒和丝绸，也使用金属着色器来增加光泽。

### 绿色通道：粗糙度

决定对象的哪些部分是闪亮的，哪些不是。

此贴图越白，越哑光。黑暗增加光泽。添加噪点以增加视觉趣味。

如果将其设置得太白，可能会出现错误，使其变得闪亮。

### 蓝色通道：环境光遮蔽

一种着色/光照数据。

有些程序可以为你烘焙环境光遮蔽，或者你的纹理创建软件可能会烘焙它。

如果不确定，请保留为纯白色。

## MSK

这决定了通过染料和材料预设叠加的颜色色调，为服装提供不同的颜色选择。请参阅此处的[遮罩颜色](Modding_colon_Armor/Clothing_Texture_Maps.md#Parameters_and_corresponding_colours_inside_MSKColor/MSKcloth "Modding:Armor/Clothing Texture Maps")列表。

这就是我们导出的 UV 映射模板派上用场的地方，因为我们可以简单地追踪 UV 块周围以添加颜色，并使用填充工具粘贴进去。

如果你打算将整个服装做成纯色，只需将 MSK 设为 4x4 以节省空间。

#### 使用 Blender 制作 MSK 文件

你可以通过为每个网格分配正确的颜色（通过材质）并将其导出为纹理来使用 Blender 制作 MSK 文件。

## GM

很少有物品可能有 GM——辉光贴图，它控制其视觉效果。这通常是黑色的，带有白色部分以让辉光透出。

## 如何打开纹理并提取其文件

首先，使用 multitool 从文件中提取纹理。[参见此处了解方法。](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture")

在 GIMP 中打开这些文件。取消选中加载 Mipmap，因为你不需要它们堵塞工作区，并且你将在重新保存时创建新的 Mipmap。

### 物理贴图

首先打开物理贴图。转到 颜色>组件>分解>RGB

这应该会留下 3 个单独的通道。

将每个通道保存为 PNG。（确保未压缩以获得最佳质量）

### BM 和 MSK

你可以直接打开并保存 BM 和 MSK。

如果 BM 具有透明度，你可能希望分解文件并单独保存 alpha 通道。

### 法线贴图

**颜色 >组件>分解>颜色模型 RGBA**

选择绿色通道，然后**值反转**。这应该会使其翻转为正面朝外，而不是内翻。

**颜色 >组件>合成>选择“RGB”** 并将 alpha 通道放入红色槽中。它应该变成紫色。保存为 PNG。

这是一个 OpenGL 法线贴图。反转的绿色通道将其从 DIRECTX 转换为 OPENGL。如果需要，你可以在其上叠加 PBR 材质。

请记住，要以相反的顺序执行所有这些步骤，以导出正确格式的纹理。

- 你应该会看到此框提示。

- 颜色>组件>分解

- 分解为 RBGA。这很重要，因为法线贴图的一半在红色通道中。

- 如何反转绿色通道

- 绿色通道示例 - 反转此通道以使法线贴图变为 OpenGL。

## 文件大小

纹理需要是完美的正方形或完美的矩形。这是因为计算机以 2 的幂次方工作，并且更喜欢这种方式。不记住这一点可能会导致人们的游戏崩溃。

这些规则不适用于图标物品，它们遵循自己的规则。

大多数物品的游戏默认纹理对于服装是 2048x2048。

你也可以有 2048 x 1024 等。

_示例尺寸：_

4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096

游戏目前不支持 8k 纹理。

低于 4x4 像素会导致游戏困难，游戏将不接受 1 像素贴图。

## 如何保存纹理

- DXT1 - 用于 BM、PM、MSK

- DXT5 - 用于法线贴图和 BMA 的设置。

## 记住你的 Mipmap

你需要在任何可能靠近或远离摄像机移动的东西上使用 Mipmap，唯一不需要的情况是静态元素，如 UI。没有 Mipmap 的东西往往有一种奇怪的“静态”感，而不是平滑干净的外观。

_纹理从虚拟纹理导出时不附带 Mipmap！_ 即使你没有编辑某些贴图，你也需要将它们导入 GIMP 并重新保存以生成新的 Mipmap。

建议使用 Kaiser 滤镜 Mipmap，因为它们比默认 Mipmap 更清晰，但任何 Mipmap 都可以使用。

## 工具

[Druu 视频教程 - 包含关于纹理的部分。](https://www.youtube.com/watch?v=IbivHL2lPrc&list=PLG6GyipNkD2ptAp16VXs8BiTNEaMlgKhO&index=1)

[放大服装纹理](https://www.nexusmods.com/baldursgate3/mods/1827)- 基础游戏纹理的高质量放大版本。免费许可在任何模组中使用。

[Adobe 关于 Substance 中 BG3 纹理的访谈 - 为传奇注入生命](https://www.adobe.com/products/substance3d/magazine/bringing-life-to-legends-character-art-in-baldurs-gate-3.md)（注意文章中的 MSK 颜色文件不正确，不应使用颜色拾取）

[这是法线 - 关于法线贴图的文章](https://www.artstation.com/blogs/typhen/GMyG)

[Volno 纹理绘制 Blender 工具集](https://www.nexusmods.com/baldursgate3/mods/4310)

[Bounding box software- materialise – 用于从头制作法线贴图](https://boundingboxsoftware.com/materialize/)

[BG3 法线贴图转换 Photoshop 动作 - 在 Photoshop 中自动进行法线贴图转换](https://www.nexusmods.com/baldursgate3/mods/504)

[优化器纹理 (Ordenador)- 快速处理纹理，你可以在短时间内为许多物品提供 Mipmap/压缩它们](https://www.nexusmods.com/skyrim/mods/12801)

[Photoshop 替代品 -Photopea](https://www.photopea.com/)

[符文字体](https://www.fontspace.com/barazhad-font-f20325)

[纹理 Alpha 印章](https://www.nexusmods.com/baldursgate3/mods/4337)

---
*Source: [Modding:Creating Outfit Textures](https://bg3.wiki/wiki/Modding:Creating_Outfit_Textures)*