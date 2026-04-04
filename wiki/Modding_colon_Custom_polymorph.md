# Modding:Custom polymorph

## [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources")

| [Community](bg3wiki_colon_Community.md "bg3wiki:Community") • [Guides](Guide_colon_Guides.md "Guide:Guides") • [Modding](Modding_colon_Modding_resources.md "Modding:Modding resources") |  |
| --- | --- |
| [Modding guides](Category_colon_Modding.md "Category:Modding") | [BG3 Mini Tool](Modding_colon_BG3_Mini_Tool.md "Modding:BG3 Mini Tool") [Blender Export Settings](Modding_colon_Blender_Export_Settings.md "Modding:Blender Export Settings") [Code Snippets](Modding_colon_Code_Snippets.md "Modding:Code Snippets") [Coding An Item](Modding_colon_Coding_An_Item.md "Modding:Coding An Item") [Compatibility Framework](Modding_colon_Compatibility_Framework.md "Modding:Compatibility Framework") [Creating a custom cloth collider](Modding_colon_Creating_a_custom_cloth_collider.md "Modding:Creating a custom cloth collider") [Creating and Exporting Meshes in Blender](Modding_colon_Creating_and_Exporting_Meshes_in_Blender.md "Modding:Creating and Exporting Meshes in Blender") [Creating Item Icons](Modding_colon_Creating_Item_Icons.md "Modding:Creating Item Icons") [Creating meta.lsx](Modding_colon_Creating_meta.lsx.md "Modding:Creating meta.lsx") [Creating mods](Modding_colon_Creating_mods.md "Modding:Creating mods") [Editing a Character Creation Preset](Modding_colon_Editing_a_Character_Creation_Preset.md "Modding:Editing a Character Creation Preset") [Editing Equipment.txt](Modding_colon_Editing_Equipment.txt.md "Modding:Editing Equipment.txt") [How To Find A Virtual Texture](Modding_colon_How_To_Find_A_Virtual_Texture.md "Modding:How To Find A Virtual Texture") [Installing mods](Modding_colon_Installing_mods.md "Modding:Installing mods") [Localization](Modding_colon_Localization.md "Modding:Localization") [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") [Packaging mods](Modding_colon_Packaging_mods.md "Modding:Packaging mods") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Treasure Tables](Modding_colon_Treasure_Tables.md "Modding:Treasure Tables") [Understanding Mod Folder Structure](Understanding_Mod_Folder_Structure.md "Understanding Mod Folder Structure") [Unpacking and converting files](Modding_colon_Unpacking_and_converting_files.md "Modding:Unpacking and converting files") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |
| [Modding resources](Modding_colon_Modding_resources.md "Modding:Modding resources") | [Armor/Clothing Texture Maps](Modding_colon_Armor/Clothing_Texture_Maps.md "Modding:Armor/Clothing Texture Maps") [Body Models](Modding_colon_Body_Models.md "Modding:Body Models") [Custom polymorph](Modding_colon_Custom_polymorph.md "Modding:Custom polymorph") [Dependencies](Modding_colon_Dependencies.md "Modding:Dependencies") [Face and body textures](Modding_colon_Face_and_body_textures.md "Modding:Face and body textures") [Fixing bone errors](Modding_colon_Fixing_bone_errors.md "Modding:Fixing bone errors") [Fixing neck seams](Modding_colon_Fixing_neck_seams.md "Modding:Fixing neck seams") [Fixing UV errors](Modding_colon_Fixing_UV_errors.md "Modding:Fixing UV errors") [Getting Started with BG3 Modding](Modding_colon_Getting_Started_with_BG3_Modding.md "Modding:Getting Started with BG3 Modding") [Hair Meshes](Modding_colon_Hair_Meshes.md "Modding:Hair Meshes") [Head Models](Modding_colon_Head_Models.md "Modding:Head Models") [Mod troubleshooting](Modding_colon_Mod_troubleshooting.md "Modding:Mod troubleshooting") [Modding class icons](Modding_colon_Modding_class_icons.md "Modding:Modding class icons") [NPC Head Models](Modding_colon_NPC_Head_Models.md "Modding:NPC Head Models") [Tiefling Horn Models](Tiefling_Horn_Models.md "Tiefling Horn Models") [Non-VT Shaders](Modding_colon_Non-VT_Shaders.md "Modding:Non-VT Shaders") [Race UUID](Modding_colon_Race_UUID.md "Modding:Race UUID") [Sample Templates](Modding_colon_Sample_Templates.md "Modding:Sample Templates") [Spell flags](Spell_flags.md "Spell flags") [Texture formatting](Modding_colon_Texture_formatting.md "Modding:Texture formatting") [Tools](Modding_colon_Tools.md "Modding:Tools") [TreasureTables References](Modding_colon_TreasureTables_References.md "Modding:TreasureTables References") [Tutorials](Modding_colon_Tutorials.md "Modding:Tutorials") [VertexColorMaskSlots](Modding_colon_VertexColorMaskSlots.md "Modding:VertexColorMaskSlots") [Working with LSX files](Modding_colon_Working_with_LSX_files.md "Modding:Working with LSX files") |

[Modding index](Modding_colon_Index.md "Modding:Index")

本教程来自 [tyvianpear](https://www.nexusmods.com/baldursgate3/users/73681713) 在 DbtR Discord 服务器分享的帖子。

## 模板

`Status_POLYMORPHED.txt` 中的 **TemplateID**。

new entry "DISGUISE_SELF_TIEFLING_MALE"
type "StatusData"
data "StatusType" "POLYMORPHED"
data "DisplayName" "Shared_Status_POLYMORPHED_DISGUISE_SELF_TIEFLING_MALE_DisplayName"
data "Description" "Shared_Status_POLYMORPHED_DISGUISE_SELF_TIEFLING_MALE_Description"
data "Icon" "Spell_Illusion_DisguiseSelf"
data "StackId" "DISGUISE_SELF"
data "Boosts" "UnlockSpell(Shout_DisguiseSelf_Cancel)"
data "TemplateID" "**cc71e73a-53eb-4f49-ab31-e80d5d5f1ef2**"
data "Rules" "c7c3381e-b901-416e-a0c4-bc745e1ff54a"
data "StatusGroups" "SG_Polymorph;SG_Disguise"
data "StatusEffect" "43248db1-c7e1-424d-935e-516d8071cf66"

与 `RootTemplates/_merged.lsx` 中的 **MapKey** 相同。

<node id="GameObjects">
<attribute id="CharacterVisualResourceID" type="FixedString" value="a178a41d-05c3-3bc8-4879-15d2effe3300" />
<attribute id="Icon" type="FixedString" value="a178a41d-05c3-3bc8-4879-15d2effe3300-(Icon_Tiefling_Male)" />
<attribute id="LevelName" type="FixedString" value="" />
**<attribute id="MapKey" type="FixedString" value="cc71e73a-53eb-4f49-ab31-e80d5d5f1ef2" />**
<attribute id="Name" type="LSString" value="" />
<attribute id="ParentTemplateId" type="FixedString" value="6f881126-478f-43a4-ba02-c024cf03a212" />
<attribute id="SpellSet" type="FixedString" value="CommonPlayerActions" />
<attribute id="Stats" type="FixedString" value="HeroTieflingMale" />
<attribute id="Type" type="FixedString" value="character" />
<attribute id="OriginalFileVersion" type="int64" value="144115198813274112" />
<children>
<node id="LocomotionParams" />
<node id="SpeakerGroupList">
<children>
<node id="SpeakerGroup">
<attribute id="Object" type="guid" value="02cdc15e-1dc3-5eb4-3cf7-5894f9b49f0b" />
</node>
<node id="SpeakerGroup">
<attribute id="Object" type="guid" value="e0d1ff71-04a8-4340-64ae-849646d883eb" />
</node>
</children>
</node>
<node id="Tags">
<children>
<node id="Tag">
<attribute id="Object" type="guid" value="25bf5042-5bf6-4360-f88d-10abcb7c370d" />
</node>
</children>
</node>
</children>
</node>

然后在 `[PAK]_CharacterVisuals/_merged.lsx` 的 **Name** 中，您会看到这个，我们在这里更改身体网格、头发等。

<node id="Resource">
<attribute id="BaseVisual" type="FixedString" value="17eb4495-aeb5-a417-83a1-79b39313cba2" />
<attribute id="BodySetVisual" type="FixedString" value="9d618ae2-7993-5cea-bfea-887a010e2c2b" />
<attribute id="ID" type="FixedString" value="a178a41d-05c3-3bc8-4879-15d2effe3300" />
<attribute id="Localized" type="bool" value="False" />
<attribute id="Name" type="LSString" value="Tieflings_Male_Asmodeus_Player_cc71e73a-53eb-4f49-ab31-e80d5d5f1ef2" />
<attribute id="ShowEquipmentVisuals" type="bool" value="True" />
<attribute id="OriginalFileVersion" type="int64" value="144115188075855921" />
<children>
...

---
*Source: [Modding:Custom polymorph](https://bg3.wiki/wiki/Modding:Custom_polymorph)*