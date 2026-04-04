# 模组：编辑角色创建预设

此页面为[模组页面](Modding_colon_Modding_resources.md "模组：模组资源")，并遵循其自身独立于Wiki其余部分的规则和标准。

文件路径：Shared\\Public\\Shared\\Content\\[PAK]\_CharacterVisuals\\\_merged.lsf

使用查找功能，按照格式 `RACE_GENDER_SUBRACE_Player` 查找您偏好的预设。

示例：Elves_Female_High_Player

我们找到一个类似的资源节点：

<node id="Resource">
<attribute id="BaseVisual" type="FixedString" value="c05cb1dc-81eb-647b-3e03-e9bf4301fcc4" />
<attribute id="BodySetVisual" type="FixedString" value="9e43f0e4-d063-d85c-87b4-470d569645db" />
<attribute id="ID" type="FixedString" value="d67bd924-3c1f-c33a-5298-feca5bbdc284" /> <!--如果想覆盖原版，请保持此ID不变-->
<attribute id="Name" type="LSString" value="Elves_Female_High_Player_f08563b3-748d-4783-837b-b8620bc60b22" /> <!--示例玩家条目-->
<attribute id="ShowEquipmentVisuals" type="bool" value="True" />
<attribute id="_OriginalFileVersion_" type="int64" value="144115207403209034" />
<children>
<node id="MaterialOverrides">
<attribute id="MaterialResource" type="FixedString" value="" />
<children>
<node id="MaterialPresets">
<children>
<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="True" />
<attribute id="GroupName" type="FixedString" value="02Skin Properties" /> <!--皮肤颜色-->
<attribute id="MapKey" type="FixedString" value="02Skin Properties" />
<attribute id="MaterialPresetResource" type="FixedString" value="73d00e6d-d66e-8a39-e1ae-5f6e47ab5a2e" />
</node>
<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="True" />
<attribute id="GroupName" type="FixedString" value="06Eyes" /> <!--眼睛颜色-->
<attribute id="MapKey" type="FixedString" value="06Eyes" />
<attribute id="MaterialPresetResource" type="FixedString" value="5be2f4a9-7f1b-673b-8d90-f10bf748215b" />
</node>
<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="True" />
<attribute id="GroupName" type="FixedString" value="05Makeup" /> <!--眼妆-->
<attribute id="MapKey" type="FixedString" value="05Makeup" />
<attribute id="MaterialPresetResource" type="FixedString" value="e22ca76f-ff27-ee34-4fea-266a2a8d8ee3" />
</node>
<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="True" />
<attribute id="GroupName" type="FixedString" value="03Hair" /> <!--头发颜色-->
<attribute id="MapKey" type="FixedString" value="03Hair" />
<attribute id="MaterialPresetResource" type="FixedString" value="742499c5-9a8c-ce4c-974f-78f3d652e10e" />
</node>
<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="False" />
<attribute id="GroupName" type="FixedString" value="02 Colour" /> <!--发饰颜色(?)-->
<attribute id="MapKey" type="FixedString" value="02 Colour" />
<attribute id="MaterialPresetResource" type="FixedString" value="00000000-0000-0000-0000-000000000000" />
</node>
</children>
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="DetailNormalStrength" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Reflectance" />
<attribute id="Value" type="float" value="0.6" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Opacity" />
<attribute id="Value" type="float" value="2" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="UseOcclusion" />
<attribute id="Value" type="float" value="0.7" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_Scatter" />
<attribute id="Value" type="float" value="0.5" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_RoughnessContrast" />
<attribute id="Value" type="float" value="0.6" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_Roughness" />
<attribute id="Value" type="float" value="0.45" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_ColorDepthContrast" />
<attribute id="Value" type="float" value="0.7" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_DepthColorIntensity" />
<attribute id="Value" type="float" value="0.1" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_DepthColorExponent" />
<attribute id="Value" type="float" value="0.1" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_ColorTransitionSoftness" />
<attribute id="Value" type="float" value="0.6" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_IDContrast" />
<attribute id="Value" type="float" value="1" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_HornMaskWeight" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_Graying_Intensity" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Scalp_ColorTransitionMidPoint" />
<attribute id="Value" type="float" value="0.1" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="FrecklesWeight" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Highlight_Intensity" /> <!--头发高光强度-->
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="doBodyHide" />
<attribute id="Value" type="float" value="1" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="doDrawMakeup" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="True" />
<attribute id="Parameter" type="FixedString" value="NonSkinColor" />
<attribute id="Value" type="fvec3" value="0.04439873 0.01316299 0.0006657844" />
</node>
<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="AddedColor" />
<attribute id="Value" type="fvec3" value="0.02570003 0 0" />
</node>
<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="True" />
<attribute id="Parameter" type="FixedString" value="Color_01" />
<attribute id="Value" type="fvec3" value="0.2518036 0.4229639 0.1540255" />
</node>
<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Color_02" />
<attribute id="Value" type="fvec3" value="1 0.5234432 0.3344578" />
</node>
<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="Color_03" />
<attribute id="Value" type="fvec3" value="0.1572807 0.09151835 0.3488648" />
</node>
</children>
</node>
<node id="Materials">
<attribute id="MapKey" type="FixedString" value="489d7f2c-9839-e1d0-67c5-260294337785" />
<children>
<node id="MaterialOverrides">
<attribute id="MaterialResource" type="FixedString" value="489d7f2c-9839-e1d0-67c5-260294337785" />
<children>
<node id="MaterialPresets" />
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="MakeUpIndex" />
<attribute id="Value" type="float" value="3" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="MakeupIntensity" />
<attribute id="Value" type="float" value="0.7" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="HemoglobinAmount" />
<attribute id="Value" type="float" value="0.8" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="VeinAmount" />
<attribute id="Value" type="float" value="0.5" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="MelaninAmount" />
<attribute id="Value" type="float" value="0.3" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="MelaninRemovalAmount" />
<attribute id="Value" type="float" value="0" />
</node>
<node id="ScalarParameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="False" />
<attribute id="Enabled" type="bool" value="False" />
<attribute id="Parameter" type="FixedString" value="YellowingAmount" />
<attribute id="Value" type="float" value="0.2" />
</node>
</children>
</node>
</children>
</node>
<node id="RealMaterialOverrides" />
<node id="Slots">
<attribute id="Bone" type="FixedString" value="" />
<attribute id="Slot" type="FixedString" value="Head" /> <!--头部网格-->
<attribute id="VisualResource" type="FixedString" value="555b1e26-9a79-c11b-134d-a557b317bd93" />
</node>
<node id="Slots">
<attribute id="Bone" type="FixedString" value="" />
<attribute id="Slot" type="FixedString" value="Hair" /> <!--头发网格-->
<attribute id="VisualResource" type="FixedString" value="588b3a58-bcf1-b2be-ba70-98bc821c64d3" />
</node>
<node id="Slots">
<attribute id="Bone" type="FixedString" value="" />
<attribute id="Slot" type="FixedString" value="Private Parts" />
<attribute id="VisualResource" type="FixedString" value="1f07d7e4-e0a1-3114-93ae-dd2f0bdfc0b0" />
</node>
<node id="Slots">
<attribute id="Bone" type="FixedString" value="" />
<attribute id="Slot" type="FixedString" value="ModestyLeaf" />
<attribute id="VisualResource" type="FixedString" value="dec25989-ed08-895e-4ae0-5c9b44352bf0" />
</node>
<node id="Slots">
<attribute id="Bone" type="FixedString" value="" />
<attribute id="Slot" type="FixedString" value="ModestyLeaf" />
<attribute id="VisualResource" type="FixedString" value="13bb4168-a5e4-fe82-f3df-57721a1ffed3" />
</node>
</children>
</node>

MaterialPresetResource 和 VisualResource 的 ID 可以在多个地方找到。其中一些在 Wiki 上：[头发网格](Modding_colon_Hair_Meshes.md "模组：头发网格")、[头部模型](Modding_colon_Head_Models.md "模组：头部模型")、[NPC 头部模型](Modding_colon_NPC_Head_Models.md "模组：NPC 头部模型")，另一些是外部资源：[眼妆参考](https://docs.google.com/spreadsheets/d/1xb7Hh1KjVRARdmu7A_YlcoqS8tklEoFjwA1oYLn1Etk/edit)。

最后，通过一些巧妙的搜索，您通常可以使用 Multitool 并搜索游戏文件来找到所需内容。

其他一些用于自定义角色创建预设的有用参数：

头发高光颜色：

<node id="Vector3Parameters">
<attribute id="Color" type="bool" value="False" />
<attribute id="Custom" type="bool" value="True" />
<attribute id="Enabled" type="bool" value="True" />
<attribute id="Parameter" type="FixedString" value="Highlight_Color" />
<attribute id="Value" type="fvec3" value="0.6392157 0.2392157 0" /> <!--头发高光颜色（SRGB 格式）-->
</node>

面部纹身：（注意：似乎存在一个问题，预设仅使用前 16 个面部纹身，目前尚无已知修复方法）

<node id="Object">
<attribute id="ForcePresetValues" type="bool" value="True" />
<attribute id="GroupName" type="FixedString" value="04Tattoo" />
<attribute id="MapKey" type="FixedString" value="04Tattoo" />
<attribute id="MaterialPresetResource" type="FixedString" value="2c477c0d-15a8-0591-bd94-6acc583666ea" /> <!--面部纹身 ID-->
</node>

---
*Source: [Modding:Editing a Character Creation Preset](https://bg3.wiki/wiki/Modding:Editing_a_Character_Creation_Preset)*