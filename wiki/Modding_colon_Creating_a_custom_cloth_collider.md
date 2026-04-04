# Modding:创建自定义布料碰撞器

此页面为 [modding 页面](Modding_colon_Modding_resources.md "Modding:Modding resources")，并遵循其自身规则和标准，与Wiki其余部分不同。

如果制作自定义身体，您可能需要为其创建自定义布料碰撞器。您可以查阅任何原版布料碰撞器作为基础，但这里有一个示例：

<region id="ClothColliderBank">
<node id="ClothColliderBank">
<children>
<node id="Resource">
<attribute id="ID" type="FixedString" value="a16538a0-69f3-4537-8b3a-192e9e958026" />
<attribute id="Name" type="LSString" value="FS_NKD_Body_ClothCollider" />
<attribute id="_OriginalFileVersion_" type="int64" value="144537400540921856" />
<children>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Ankle_R" />
<attribute id="Name" type="FixedString" value="Ankle_R" />
<attribute id="Position" type="fvec3" value="0.02408487 0.008219436 0.0002600327" />
<attribute id="Radius" type="float" value="0.115" />
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Knee_R" />
<attribute id="Name" type="FixedString" value="Knee_R" />
<attribute id="Position" type="fvec3" value="0.1842566 0.01101419 -0.2196186" />
<attribute id="Radius" type="float" value="0.12" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_R_Twist_02" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_R_Twist_02" />
<attribute id="Name" type="FixedString" value="Hip_R_Twist_02" />
<attribute id="Position" type="fvec3" value="0.2335134 -0.009342965 0.0003812611" />
<attribute id="Radius" type="float" value="0.12" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_R" />
</node>
<node id="Links">
<attribute id="Link" type="FixedString" value="Ankle_R" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_R_Twist_01" />
<attribute id="Name" type="FixedString" value="Hip_R_Twist_01" />
<attribute id="Position" type="fvec3" value="0.2496572 -0.03000538 0.009381257" />
<attribute id="Radius" type="float" value="0.12" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_R" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_R" />
<attribute id="Name" type="FixedString" value="Hip_R" />
<attribute id="Position" type="fvec3" value="0.03671718 0.02558749 -0.03661869" />
<attribute id="Radius" type="float" value="0.175" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Root_M" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Ankle_L" />
<attribute id="Name" type="FixedString" value="Ankle_L" />
<attribute id="Position" type="fvec3" value="-0.02430184 -0.008254398 -5.885959E-07" />
<attribute id="Radius" type="float" value="0.115" />
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Knee_L" />
<attribute id="Name" type="FixedString" value="Knee_L" />
<attribute id="Position" type="fvec3" value="-0.183996 -0.01075782 -4.082918E-06" />
<attribute id="Radius" type="float" value="0.12" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_L_Twist_02" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_L_Twist_02" />
<attribute id="Name" type="FixedString" value="Hip_L_Twist_02" />
<attribute id="Position" type="fvec3" value="-0.2332943 0.009374093 -6.183982E-07" />
<attribute id="Radius" type="float" value="0.12" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_L" />
</node>
<node id="Links">
<attribute id="Link" type="FixedString" value="Ankle_L" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_L_Twist_01" />
<attribute id="Name" type="FixedString" value="Hip_L_Twist_01" />
<attribute id="Position" type="fvec3" value="-0.249878 0.0301131 -0.00954318" />
<attribute id="Radius" type="float" value="0.125" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Hip_L" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Hip_L" />
<attribute id="Name" type="FixedString" value="Hip_L" />
<attribute id="Position" type="fvec3" value="-0.03669894 -0.02522373 0.0368407" />
<attribute id="Radius" type="float" value="0.175" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Root_M" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Chest_M" />
<attribute id="Name" type="FixedString" value="Chest_M" />
<attribute id="Position" type="fvec3" value="0.1746373 0.009826064 1.951149E-05" />
<attribute id="Radius" type="float" value="0.2" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Spine2_M" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Spine2_M" />
<attribute id="Name" type="FixedString" value="Spine2_M" />
<attribute id="Position" type="fvec3" value="0.1052495 0.02236807 9.536742E-07" />
<attribute id="Radius" type="float" value="0.15" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Spine1_M" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Spine1_M" />
<attribute id="Name" type="FixedString" value="Spine1_M" />
<attribute id="Position" type="fvec3" value="0.0001251698 -0.005512714 4.768372E-07" />
<attribute id="Radius" type="float" value="0.15" />
<children>
<node id="Links">
<attribute id="Link" type="FixedString" value="Root_M" />
</node>
</children>
</node>
<node id="Spheres">
<attribute id="AttachedName" type="FixedString" value="Root_M" />
<attribute id="Name" type="FixedString" value="Root_M" />
<attribute id="Position" type="fvec3" value="-0.04438829 -0.04123938 -2.205372E-06" />
<attribute id="Radius" type="float" value="0.18" />
</node>
</children>
</node>
</children>
</node>
</region>

Radius 属性控制每个碰撞“球体”的大小。您可以使其变大或变小，以使布料物理在碰撞时表现不同。

将此 bank 放置在您的身体 \_merged.lsf.lsx 文件中。

---
*Source: [Modding:Creating a custom cloth collider](https://bg3.wiki/wiki/Modding:Creating_a_custom_cloth_collider)*