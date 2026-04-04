# Modding:面部与身体纹理

本页面为[模组页面](Modding_colon_Modding_resources.md "Modding:模组资源")，遵循与Wiki其余部分不同的独立规则和标准。

## 目录

- [1 类人生物](#类人生物)
- [2 编辑 CLEA/HMVY](#编辑-CLEA-HMVY)
- [3 CLEA](#CLEA)
- [4 HMVY](#HMVY)
- [5 NORMAL](#NORMAL)
- [6 MSK](#MSK)
- [7 图库](#图库)
- [8 纹身与化妆图集](#纹身与化妆图集)
  - [8.1 纹身](#纹身)
  - [8.2 化妆](#化妆)
- [9 龙裔](#龙裔)
- [10 CTLO](#CTLO)
- [11 HMVY](#HMVY)
- [12 NORMAL](#NORMAL)
- [13 MSK](#MSK)
- [14 DMSK](#DMSK)
- [15 龙族血脉 DMSK](#龙族血脉-DMSK)
- [16 灵吸怪 MSK](#灵吸怪-MSK)

## 类人生物

## bg3.wiki 模组

模组主页

- [模组资源](Modding_colon_Modding_resources.md "Modding:模组资源")

模组资源 - 网格、模型、工具等。
[护甲/服装纹理贴图](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:护甲/服装纹理贴图") [身体模型](Modding_colon_Body_Models.md "Modding:身体模型") [自定义变形术](Modding_colon_Custom_polymorph.md "Modding:自定义变形术") [依赖项](Modding_colon_Dependencies.md "Modding:依赖项") [面部与身体纹理](Modding_colon_Face_and_body_textures.md "Modding:面部与身体纹理") [修复骨骼错误](Modding_colon_Fixing_bone_errors.md "Modding:修复骨骼错误") [修复颈部接缝](Modding_colon_Fixing_neck_seams.md "Modding:修复颈部接缝") [修复UV错误](Modding_colon_Fixing_UV_errors.md "Modding:修复UV错误") [BG3模组入门](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:BG3模组入门") [头发网格](Modding_colon_Hair_Meshes.md "Modding:头发网格") [头部模型](Modding_colon_Head_Models.md "Modding:头部模型") [模组故障排除](Modding_colon_Mod_troubleshooting.md "Modding:模组故障排除") [模组职业图标](Modding_colon_Modding_class_icons.md "Modding:模组职业图标") [NPC头部模型](Modding_colon_NPC_Head_Models.md "Modding:NPC头部模型") [提夫林号角模型](Tiefling_Horn_Models.md "提夫林号角模型") [非VT着色器](Modding_colon_Non-VT_Shaders.md "Modding:非VT着色器") [种族UUID](Modding_colon_Race_UUID.md "Modding:种族UUID") [示例模板](Modding_colon_Sample_Templates.md "Modding:示例模板") [法术标志](Spell_flags.md "法术标志") [纹理格式](Modding_colon_Texture_formatting.md "Modding:纹理格式") [工具](Modding_colon_Tools.md "Modding:工具") [宝藏表参考](Modding_colon_TreasureTables_References.md "Modding:宝藏表参考") [教程](Modding_colon_Tutorials.md "Modding:教程") [顶点颜色遮罩槽](Modding_colon_VertexColorMaskSlots.md "Modding:顶点颜色遮罩槽") [处理LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:处理LSX文件")
模组指南
[BG3迷你工具](Modding_colon_BG3_Mini_Tool.md "Modding:BG3迷你工具") [Blender导出设置](Modding_colon_Blender_Export_Settings.md "Modding:Blender导出设置") [代码片段](Modding_colon_Code_Snippets.md "Modding:代码片段") [编写物品代码](Modding_colon_Coding_An_Item.md "Modding:编写物品代码") [兼容性框架](Modding_colon_Compatibility_Framework.md "Modding:兼容性框架") [创建自定义布料碰撞体](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:创建自定义布料碰撞体") [在Blender中创建和导出网格](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:在Blender中创建和导出网格") [创建物品图标](Modding_colon_Creating_Item_Icons.md "Modding:创建物品图标") [创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建meta.lsx") [创建模组](Modding_colon_Creating_mods.md "Modding:创建模组") [编辑角色创建预设](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:编辑角色创建预设") [编辑Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:编辑Equipment.txt") [如何查找虚拟纹理](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:如何查找虚拟纹理") [安装模组](Modding_colon_Installing_mods.md "Modding:安装模组") [本地化](Modding_colon_Localization.md "Modding:本地化") [模组资源](Modding_colon_Modding_resources.md "Modding:模组资源") [打包模组](Modding_colon_Packaging_mods.md "Modding:打包模组") [纹理格式](Modding_colon_Texture_formatting.md "Modding:纹理格式") [宝藏表](Modding_colon_Treasure_Tables.md "Modding:宝藏表") [理解模组文件夹结构](Understanding_Mod_Folder_Structure.md "理解模组文件夹结构") [解包和转换文件](Modding_colon_Unpacking_and_converting_files.md "Modding:解包和转换文件") [处理LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:处理LSX文件")
头发模组
[使用头发工具创建自定义头发](Modding_colon_Creating_Custom_Hair_with_Hair_Tool.md "Modding:使用头发工具创建自定义头发") [使用自定义纹理创建头发合并.lsf](Modding_colon_Creating_hair_merged.lsf_with_custom_texture.md "Modding:使用自定义纹理创建头发合并.lsf") [创建头发模组](Modding_colon_Creating_Hair_Mods.md "Modding:创建头发模组") [创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建meta.lsx") [自定义头发高光](Modding_colon_Custom_Hair_Highlights.md "Modding:自定义头发高光") [头发网格](Modding_colon_Hair_Meshes.md "Modding:头发网格") [头发模组文件设置](Guide_colon_Hair_Mod_File_Setup.md "指南:头发模组文件设置") [头发模组网格设置](Modding_colon_Hair_Mod_Mesh_Setup.md "Modding:头发模组网格设置")
头部模组
[创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建meta.lsx") [面部与身体纹理](Modding_colon_Face_and_body_textures.md "Modding:面部与身体纹理") [修复颈部接缝](Modding_colon_Fixing_neck_seams.md "Modding:修复颈部接缝") [头部模组](Modding_colon_Head_Modding.md "Modding:头部模组") [头部模型](Modding_colon_Head_Models.md "Modding:头部模型") [头部故障排除](Modding_colon_Head_Troubleshooting.md "Modding:头部故障排除") [NPC头部模型](Modding_colon_NPC_Head_Models.md "Modding:NPC头部模型")
物品模组 - 护甲、服装、武器等。
[护甲/服装纹理贴图](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:护甲/服装纹理贴图") [编写物品代码](Modding_colon_Coding_An_Item.md "Modding:编写物品代码") [在Blender中创建和导出网格](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:在Blender中创建和导出网格") [创建护甲模组](Modding_colon_Creating_Armor_Mods.md "Modding:创建护甲模组") [创建物品图标](Modding_colon_Creating_Item_Icons.md "Modding:创建物品图标") [创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:创建meta.lsx") [创建服装纹理](Modding_colon_Creating_Outfit_Textures.md "Modding:创建服装纹理") [修复骨骼错误](Modding_colon_Fixing_bone_errors.md "Modding:修复骨骼错误") [如何查找虚拟纹理](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:如何查找虚拟纹理") [纹理格式](Modding_colon_Texture_formatting.md "Modding:纹理格式") [宝藏表参考](Modding_colon_TreasureTables_References.md "Modding:宝藏表参考") [使用服装构建器重新调整服装](Modding_colon_Use_Outfit_Builder_To_Refit_Outfits.md "Modding:使用服装构建器重新调整服装") [顶点颜色遮罩槽](Modding_colon_VertexColorMaskSlots.md "Modding:顶点颜色遮罩槽")
种族/职业模组
[创建种族模组](Modding_colon_Creating_Race_Mods.md "Modding:创建种族模组") [编辑角色创建预设](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:编辑角色创建预设")

## 编辑 CLEA/HMVY

要编辑 CLEA/HMVY 纹理，最好将它们分解为 RGBA 通道并单独编辑每个通道。

例如在 GIMP 中将它们分离到各个通道，您可以这样做：

1. 在 GIMP 中打开纹理
2. 转到 颜色 > 组件 > 分解 > 将颜色模型切换为 RGBA
3. 选择颜色模型后按确定。
4. 这将打开另一个窗口/页面，每个通道作为图层。现在您可以使用下面的指南单独编辑每个通道，了解每个通道的作用。
5. 完成编辑后，转到：颜色 > 组件 > 合成 > 将颜色模型切换为 RGBA。
6. 选择颜色模型后，按确定。
7. 现在将打开另一个窗口/页面，其中纹理已重新打包，通道合并在一起。现在您可以导出纹理。导出纹理时，请确保扩展名为 .DDS 而不是 .dds，压缩格式为 BC3/DXT5 或 BC1/DXT1，如下所示。

## CLEA

DDS 格式：BC3/DXT5 线性

- 红色通道 - 凹陷/毛孔
- 绿色通道 - 眉毛
- 蓝色通道 - 嘴唇
- Alpha 通道 - 环境光遮蔽

## HMVY

DDS 格式：BC3/DXT5 线性
皮肤着色

- 红色通道 - 血红蛋白
- 绿色通道 - 黑色素（雀斑）
- 蓝色通道 - 血管
- Alpha 通道 - 黄化

## NORMAL

DDS 格式：BC3/DXT5 线性
皱纹、疤痕、皮肤上的任何凹陷

要将“常规”法线贴图转换为 BG3，请将红色通道放入 Alpha 通道，并将红色通道设置为黑色

## MSK

DDS 格式：BC1/DXT1 线性

- 红色通道 - 非皮肤（号角、指甲颜色）
- 绿色通道 - 色素沉着（越浅 = 越少，也用于白癜风）
- 蓝色通道 - 泪痕/唇纹

## 图库

- CLEA

- HMVY

- NM

## 纹身与化妆图集

DDS 格式：BC1/DXT1 线性

### 纹身

- 红色、绿色和蓝色都是不同的纹身设计。可以在任何通道上设计。

### 化妆

- 红色通道 - 化妆选项
- 绿色通道 - 吉斯印记
- 蓝色/Alpha - 未使用

## 龙裔

## CTLO

**CTLO - 凹陷.厚度.嘴唇.遮蔽**

DDS 格式：BC3/DXT5 线性

- 红色通道 - 凹陷
- 绿色通道 - 厚度
- 蓝色通道 - 嘴唇
- Alpha 通道 - 环境光遮蔽

厚度 - 与 Marmoset 中的相反，并且更浅

AO - 比您在 Marmoset 或 Substance 中烘焙的要白得多，因此如果您想与您的混合，请调整它们

## HMVY

**HMVY - 血红蛋白.黑色素.血管.黄化**

DDS 格式：BC3/DXT5 线性

- 红色通道 - 血红蛋白
- 绿色通道 - 黑色素（色素量）
- 蓝色通道 - 血管
- Alpha 通道 - 黄化

## NORMAL

DDS 格式：BC3/DXT5 线性

要将“常规”法线贴图转换为 BG3，请将红色通道放入 Alpha 通道，并将红色通道设置为黑色

## MSK

DDS 格式：BC1/DXT1 线性

- 红色通道 - 非皮肤（号角、鳞片、任何角蛋白部分）
- 绿色通道 - 凸性图
- 蓝色通道 - 空黑色（在身体纹理中用于指甲的白色）

这只是为了显示 MSK 通道的确切工作方式：

\+ 小测试以更明显地显示 R 通道的工作方式

## DMSK

RGB - 每个通道都是装饰性遮罩（通过它们您可以制作镀金遮罩、添加细节，即强调遮罩）

在第二张图片中，您可以看到 DMSK 蓝色通道作为黄色镀金：

本文档还可以让您更好地理解 [龙裔肤色参考](https://docs.google.com/document/d/1nE4QjTKedF0KkKwOsVVAI87GgXxdQiJSsLYOnWO5YdA/edit#heading=h.zb542upz0efo) 由 Padme4000 提供

## 龙族血脉 DMSK

RGB - 每个通道都是龙族血脉装饰性遮罩 - 如果玩家选择龙族血脉副职，它们将替换 DMSK，请记住这一点

您可以在此处查看每个单独的通道文件 [龙裔头部 Substance Painter 资源](https://www.nexusmods.com/baldursgate3/mods/11111) 所有现有的 DGB 头部纹理已按通道解包到单独的文件夹中

您还可以使用此模组查看每个 DGB 头部材质，包括 NPC [龙裔头部材质检查器 - 模组作者工具](https://www.nexusmods.com/baldursgate3/mods/11011)。

## 灵吸怪 MSK

_格式：_ _BC3/DXT5 线性_

红色通道 - X 轴法线

绿色通道 - Y 轴法线

蓝色通道 - 遮罩

Alpha 通道 - 不存在

注意：

对于头部，它是 1x1 比例图像，对于身体，它是 1x2。如果您有任何 UV 部分超出 1x1 但按 1 计算，这些部分将从纹理的第二部分获取信息。

---
*来源: [Modding:面部与身体纹理](https://bg3.wiki/wiki/Modding:Face_and_body_textures)*

---
*Source: [Modding:Face and body textures](https://bg3.wiki/wiki/Modding:Face_and_body_textures)*
