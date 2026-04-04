# 模组制作：修复UV错误

## [社区](bg3wiki_colon_Community.md "bg3wiki:Community") • [指南](Guide_colon_Guides.md "Guide:Guides") • [模组制作](Modding_colon_Modding_resources.md "Modding:Modding resources")

| [社区](bg3wiki_colon_Community.md "bg3wiki:Community") • [指南](Guide_colon_Guides.md "Guide:Guides") • [模组制作](Modding_colon_Modding_resources.md "Modding:Modding resources") |  |
| --- | --- |
| [模组制作指南](Category_colon_Modding.md "Category:Modding") | [BG3 Mini Tool](Modding_colon_BG3_Mini_Tool.md "Modding:BG3 Mini Tool") [Blender导出设置](Modding_colon_Blender_Export_Settings.md "Modding:Blender Export Settings") [代码片段](Modding_colon_Code_Snippets.md "Modding:Code Snippets") [为物品编码](Modding_colon_Coding_An_Item.md "Modding:Coding An Item") [兼容性框架](Modding_colon_Compatibility_Framework.md "Modding:Compatibility Framework") [创建自定义布料碰撞体](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:Creating a custom cloth collider") [在Blender中创建和导出网格](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:Creating and Exporting Meshes in Blender") [创建物品图标](Modding_colon_Creating_Item_Icons.md "Modding:Creating Item Icons") [创建meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:Creating meta.lsx") [创建模组](Modding_colon_Creating_mods.md "Modding:Creating mods") [编辑角色创建预设](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:Editing a Character Creation Preset") [编辑Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:Editing Equipment.txt") [如何查找虚拟纹理](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture") [安装模组](Modding_colon_Installing_mods.md "Modding:Installing mods") [本地化](Modding_colon_Localization.md "Modding:Localization") [模组制作资源](Modding_colon_Modding_resources.md "Modding:Modding resources") [打包模组](Modding_colon_Packaging_mods.md "Modding:Packaging mods") [纹理格式](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [宝藏表](Modding_colon_Treasure_Tables.md "Modding:Treasure Tables") [理解模组文件夹结构](Understanding_Mod_Folder_Structure.md "Understanding Mod Folder Structure") [解包和转换文件](Modding_colon_Unpacking_and_converting_files.md "Modding:Unpacking and converting files") [使用LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |
| [模组制作资源](Modding_colon_Modding_resources.md "Modding:Modding resources") | [护甲/服装纹理贴图](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:Armor/Clothing Texture Maps") [身体模型](Modding_colon_Body_Models.md "Modding:Body Models") [自定义变形术](Modding_colon_Custom_polymorph.md "Modding:Custom polymorph") [依赖项](Modding_colon_Dependencies.md "Modding:Dependencies") [面部和身体纹理](Modding_colon_Face_and_body_textures.md "Modding:Face and body textures") [修复骨骼错误](Modding_colon_Fixing_bone_errors.md "Modding:Fixing bone errors") [修复颈部接缝](Modding_colon_Fixing_neck_seams.md "Modding:Fixing neck seams") [修复UV错误](Modding_colon_Fixing_UV_errors.md "Modding:Fixing UV errors") [BG3模组制作入门](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:Getting Started with BG3 Modding") [头发网格](Modding_colon_Hair_Meshes.md "Modding:Hair Meshes") [头部模型](Modding_colon_Head_Models.md "Modding:Head Models") [模组故障排除](Modding_colon_Mod_troubleshooting.md "Modding:Mod troubleshooting") [模组职业图标](Modding_colon_Modding_class_icons.md "Modding:Modding class icons") [NPC头部模型](Modding_colon_NPC_Head_Models.md "Modding:NPC Head Models") [提夫林号角模型](Tiefling_Horn_Models.md "Tiefling Horn Models") [非VT着色器](Modding_colon_Non-VT_Shaders.md "Modding:Non-VT Shaders") [种族UUID](Modding_colon_Race_UUID.md "Modding:Race UUID") [示例模板](Modding_colon_Sample_Templates.md "Modding:Sample Templates") [法术标志](Spell_flags.md "Spell flags") [纹理格式](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [工具](Modding_colon_Tools.md "Modding:Tools") [宝藏表参考](Modding_colon_TreasureTables_References.md "Modding:TreasureTables References") [教程](Modding_colon_Tutorials.md "Modding:Tutorials") [顶点颜色遮罩槽](Modding_colon_VertexColorMaskSlots.md "Modding:VertexColorMaskSlots") [使用LSX文件](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |

[模组制作索引](Modding_colon_Index.md "Modding:Index")

自正式发布以及[Norbyte](https://github.com/Norbyte/dos2de_collada_exporter)制作的插件以来，直接从Blender导出为GR2时不再需要以下步骤。但是，如果您希望导出为DAE并遇到UV错误，以下方法将有效。

本教程来自[tyvianpear](https://www.nexusmods.com/baldursgate3/users/73681713)在DbtR Discord服务器分享的帖子。

## 步骤

1. 打开两个Blender实例：2.79b和3.X（最新版）
2. 将**LaughingLeaders' Blender Helpers for 2.79b**安装到2.79b中
3. 首先在3.X中打开您的模型
4. 将整个模型及其所有网格复制并粘贴到2.79b中
5. 最小化（或关闭）3.X，直到最后我们不再需要它
6. 通过拖动顶部角落的条纹三角形之一，在**属性选项卡**旁边打开另一个窗口
7. 在新窗口中，点击**项目大纲**下的**属性**按钮，选择**UV/图像编辑器**
8. 点击您要首先检查的网格（为安全起见，请逐个检查每个网格）
9. 按**TAB**进入**编辑模式**
10. 点击垂直的**辅助选项卡**，确保**选择所有问题**框已勾选
11. 点击**检查UV三角形**
12. 在Blender的最顶部，您会看到一条通知，告知发现了多少个UV问题。它们还会在您的网格上以橙色高亮显示，并在右侧的图表中显示
13. 在模型的左侧，您会在**工具选项卡**中看到**移除重复项**
14. 点击它，您会在顶部看到一条消息，_移除了0个顶点_，因为合并距离太短，无法合并任何重叠的顶点
15. 尝试逐步更改合并距离，尽可能小。在0.0004左右，您会在顶部看到_移除了X个顶点_
16. 注意您的网格，确保它没有变得过于扭曲
17. 每次顶点移除/合并后，选择并取消选择（编辑模式下按CTRL-A）网格，并重复之前的**检查UV三角形**和**移除重复顶点**步骤
18. 并非所有UV错误都会显示在图表上，因此请注意顶部的通知，它会告知您有多少个UV错误
19. 当您合并了所有导致问题的顶点后，您会在顶部看到_未发现UV问题_
20. 对模型中的每个网格完成此操作后，将整个内容复制并粘贴回3.X
21. 导出为`.DAE`

---
*Source: [Modding:Fixing UV errors](https://bg3.wiki/wiki/Modding:Fixing_UV_errors)*