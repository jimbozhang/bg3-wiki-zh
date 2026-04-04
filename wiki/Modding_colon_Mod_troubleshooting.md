# Modding:Mod troubleshooting

## [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources")

| [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources") |  |
| --- | --- |
| [Modding guides](Category_colon_Modding.md "Category:Modding") | [BG3 Mini Tool](Modding_colon_BG3_Mini_Tool.md "Modding:BG3 Mini Tool") [Blender Export Settings](Modding_colon_Blender_Export_Settings.md "Modding:Blender Export Settings") [Code Snippets](Modding_colon_Code_Snippets.md "Modding:Code Snippets") [Coding An Item](Modding_colon_Coding_An_Item.md "Modding:Coding An Item") [Compatibility Framework](Modding_colon_Compatibility_Framework.md "Modding:Compatibility Framework") [Creating a custom cloth collider](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:Creating a custom cloth collider") [Creating and Exporting Meshes in Blender](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:Creating and Exporting Meshes in Blender") [Creating Item Icons](Modding_colon_Creating_Item_Icons.md "Modding:Creating Item Icons") [Creating meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:Creating meta.lsx") [Creating mods](Modding_colon_Creating_mods.md "Modding:Creating mods") [Editing a Character Creation Preset](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:Editing a Character Creation Preset") [Editing Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:Editing Equipment.txt") [How To Find A Virtual Texture](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture") [Installing mods](Modding_colon_Installing_mods.md "Modding:Installing mods") [Localization](Modding_colon_Localization.md "Modding:Localization") [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") [Packaging mods](Modding_colon_Packaging_mods.md "Modding:Packaging mods") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Treasure Tables](Modding_colon_Treasure_Tables.md "Modding:Treasure Tables") [Understanding Mod Folder Structure](Understanding_Mod_Folder_Structure.md "Understanding Mod Folder Structure") [Unpacking and converting files](Modding_colon_Unpacking_and_converting_files.md "Modding:Unpacking and converting files") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |
| [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") | [Armor/Clothing Texture Maps](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:Armor/Clothing Texture Maps") [Body Models](Modding_colon_Body_Models.md "Modding:Body Models") [Custom polymorph](Modding_colon_Custom_polymorph.md "Modding:Custom polymorph") [Dependencies](Modding_colon_Dependencies.md "Modding:Dependencies") [Face and body textures](Modding_colon_Face_and_body_textures.md "Modding:Face and body textures") [Fixing bone errors](Modding_colon_Fixing_bone_errors.md "Modding:Fixing bone errors") [Fixing neck seams](Modding_colon_Fixing_neck_seams.md "Modding:Fixing neck seams") [Fixing UV errors](Modding_colon_Fixing_UV_errors.md "Modding:Fixing UV errors") [Getting Started with BG3 Modding](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:Getting Started with BG3 Modding") [Hair Meshes](Modding_colon_Hair_Meshes.md "Modding:Hair Meshes") [Head Models](Modding_colon_Head_Models.md "Modding:Head Models") [Mod troubleshooting](Modding_colon_Mod_troubleshooting.md "Modding:Mod troubleshooting") [Modding class icons](Modding_colon_Modding_class_icons.md "Modding:Modding class icons") [NPC Head Models](Modding_colon_NPC_Head_Models.md "Modding:NPC Head Models") [Tiefling Horn Models](Tiefling_Horn_Models.md "Tiefling Horn Models") [Non-VT Shaders](Modding_colon_Non-VT_Shaders.md "Modding:Non-VT Shaders") [Race UUID](Modding_colon_Race_UUID.md "Modding:Race UUID") [Sample Templates](Modding_colon_Sample_Templates.md "Modding:Sample Templates") [Spell flags](Spell_flags.md "Spell flags") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Tools](Modding_colon_Tools.md "Modding:Tools") [TreasureTables References](Modding_colon_TreasureTables_References.md "Modding:TreasureTables References") [Tutorials](Modding_colon_Tutorials.md "Modding:Tutorials") [VertexColorMaskSlots](Modding_colon_VertexColorMaskSlots.md "Modding:VertexColorMaskSlots") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |

[Modding index](Modding_colon_Index.md "Modding:Index")

此列表已根据 [LostSoul](https://www.nexusmods.com/baldursgate3/users/55895062) 在 Larian 的 Discord 服务器中分享的原始列表进行编辑和调整。

## 目录

- [1 通用技巧](#general-tips)
- [2 自我提问](#questions-to-ask-yourself)
- [3 常见错误](#common-bugs)
  - [3.1 站在田野中，周围是裸男和1个龙裔。](#standing-in-a-field-surrounded-by-naked-men-and-1-dragonborn.)

## 通用技巧

1. 仅使用与[当前游戏版本](Patch_notes.md "Patch notes")兼容的模组。
2. 不要在游戏过程中卸载模组，尤其是那些添加了新法术、物品或状态效果的模组。这可能导致存档在加载时崩溃。
3. 如果你遇到多人游戏问题，请确保所有玩家拥有相同顺序的相同模组。
4. 逐一移除模组并将其添加到游戏中，以识别任何损坏的模组或冲突。
5. 如果你发现问题，请向模组作者报告。尽可能提供详细信息，并附上截图（如果可能）。在报告前，请确保你已彻底阅读模组文档、其要求和评论，以防解决方案就在其中。

## 自我提问

1. 没有模组时游戏能正常运行吗？
2. 我是否彻底阅读了安装说明？
3. 我安装的模组有要求吗？
4. 我是否拥有模组及其要求的最新版本？
5. 我是否检查了当前的错误或已报告的问题？
6. 我是否安装了 [Mod Fixer](https://www.nexusmods.com/baldursgate3/mods/141)？
7. 我是否正确[安装了它们](Guide_colon_Installing_Mods.md "Guide:Installing Mods")？
8. 我是否在使用 Vortex？（Vortex 可能导致问题）

## 常见错误

#### 站在田野中，周围是裸男和1个龙裔

你需要 [Mod Fixer](https://www.nexusmods.com/baldursgate3/mods/141)。

---
*Source: [Modding:Mod troubleshooting](https://bg3.wiki/wiki/Modding:Mod_troubleshooting)*