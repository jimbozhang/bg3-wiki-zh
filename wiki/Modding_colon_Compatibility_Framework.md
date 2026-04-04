此页面为[模组页面](Modding_colon_Modding_resources.md "Modding:Modding resources")，遵循其独立于Wiki其余部分的规则和标准。

[模组索引](Modding_colon_Index.md "Modding:Index")

# 兼容性框架

首先非常感谢 NellsRelo 和 perseidipity

要使用兼容性框架，您需要将其与您的模组一起安装。但 CF 需要位于加载顺序的底部。也就是列表的末尾。

## Json

对于使用兼容性框架来使您对 Races.lsx 的编辑与其他模组兼容，这被认为是更容易设置的格式。部分原因是它更容易响应多个部分来定义每个种族并具有多个值。

您不需要向兼容性框架模组发送任何内容进行添加，只需记住将其放在加载顺序的底部，并且如果制作公共模组，请提醒人们将 CF 放在底部。

首先，您需要创建一些新文件夹：

Modname/Mods/YourShared/ScriptExtender

在 Script extender 文件夹中，您需要创建一个 CompatibilityFrameworkConfig.json，您可以通过创建一个 txt 文件并将其重命名并将其扩展名更改为 CompatibilityFrameworkConfig.json 来完成。

使用我们在此处给出的部分代码示例：但已编辑。

{
"FileVersion": 1,
"Races": \[
{
"UUID": "Race's UUID",
"Children": \[
{
"Type": "Visuals",
"modGuid": "UUID of required mod (Optional)",
"Values": ["bdf9b779-002c-4077-b377-8ea7c1faa795", "3e4d5829-7bfd-446a-9e7d-ac8d0948c1e4"],
"Action": "Insert"
}
\]
}
\]
}

"UUID": "Race's UUID",

在这一行中，我们希望将其更改为我们要添加到 Races.lsx 文件中的种族。最常用的是 Humanoid（类人生物），用于头发/胡须模组。其 UUID 为 899d275e-9893-490a-9cd5-be856794929f。这将将其应用于所有种族，包括使用它作为父级的模组种族。有关其他情况，请参阅 [此处 Races.lsx 部分](Modding_colon_Race_UUID.md "Modding:Race UUID")，例如，如果您只想将其添加到人类和精灵，您的代码将如下所示。

{
"FileVersion": 1,
"Races": \[
{
"UUID": "0eb594cb-8820-4be6-a58d-8be7a1a98fba", 这是人类种族的 uuid
"Children": \[
{
"Type": "Visuals",
"modGuid": "UUID of required mod (Optional)",
"Values": ["bdf9b779-002c-4077-b377-8ea7c1faa795"],
"Action": "Insert"
}
\]
},
{
"UUID": "6c038dcb-7eb5-431d-84f8-cecfaf1c0c5a", 这是精灵种族的 uuid
"Children": \[
{
"Type": "Visuals",
"modGuid": "UUID of required mod (Optional)",
"Values": ["bdf9b779-002c-4077-b377-8ea7c1faa795"],
"Action": "Insert"
}
\]
}
\]
}

现在继续解释其他行：

"Type": "Visuals",

Visuals 涉及资产，如头发、胡须、尾巴、角等。基本上是我们添加到 SharedVisuals 的资产。

"modGuid": "UUID of required mod (Optional)",

正如这一行所说，它是可选的，但我个人会添加它。我们在 meta 中添加的 UUID。

"Values": ["bdf9b779-002c-4077-b377-8ea7c1faa795"],

此 UUID 必须与您在 CharacterCreationSharedVisuals 中为 UUID 行指定的 UUID 匹配。如果您有多个资产，请在最后一个 " 后添加一个 ,，然后创建一个新的 " "，并在其中放入您的 uuid，例如从第一个示例中：

"Values": ["bdf9b779-002c-4077-b377-8ea7c1faa795", "3e4d5829-7bfd-446a-9e7d-ac8d0948c1e4"],

现在我们来看最后一行：

"Action": "Insert"

出于 SharedVisual 模组的目的，我们可能不会更改此行，但是，如果您想从 Races.lsx 的某个部分中删除某些内容而不是添加某些内容，请将 Insert 更改为 Remove

恭喜您通过 json 设置了您的模组以使用兼容性框架。只需记住始终将兼容性框架加载在加载顺序的底部。

## Lua

这是兼容性框架的一种可能用法，但建议使用 json 方法。两者都不需要直接向框架添加任何内容，它们可以开箱即用地与框架一起工作。

首先，您需要创建一些新文件夹：

Modname/Mods/YourShared/ScriptExtender/Lua

在 Script extender 文件夹中，您需要创建一个 Config.json，您可以通过创建一个文本文件并将其重命名为 Config.json 来完成。在 json 中，您需要：

{
"RequiredVersion": 9,
"ModTable": "YOUR_MOD_NAME_HERE",
"FeatureFlags": ["Lua"]
}

在 YOUR_MOD_NAME_HERE 处，写下您的模组名称。

现在在 Lua 文件夹中，再次执行相同操作，创建一个新的 txt 文件，但这次将其重命名为 BootstrapClient.lua

if Ext.Mod.IsModLoaded("67fbbd53-7c7d-4cfa-9409-6d737b4d92a9") then
local raceChildData = {
ModName = {
modGuid = "the UUID you gave in your meta.lsx",
raceGuid = "899d275e-9893-490a-9cd5-be856794929f",
children = {
entry1 = {
Type = "Visuals",
Value = "3ae3e4fc-e792-473a-8853-43520dfc1147",
},
}
}
}
local function OnStatsLoaded()
Mods.SubclassCompatibilityFramework.Api.InsertRaceChildData(raceChildData)
end

Ext.Events.StatsLoaded:Subscribe(OnStatsLoaded)
end

raceGuid = "899d275e-9893-490a-9cd5-be856794929f",

您希望这是您要添加头发的种族。目前在那的是 humanoid（类人生物）。这将将其应用于所有种族，包括使用它作为父级的模组种族。有关其他情况，请参阅 [此处](Modding_colon_Race_UUID.md "Modding:Race UUID")

Type = "Visuals",

这一行是您要添加到的内容。Visuals 是 SharedVisuals 文件中定义的头发、胡须或其他资产。

Value = "3ae3e4fc-e792-473a-8853-43520dfc1147",

此 UUID 必须与您在 CharacterCreationSharedVisuals 中为 UUID 行指定的 UUID 匹配

如果想创建多个头发，请复制并粘贴此部分：

entry1 = {
Type = "Visuals",
Value = "3ae3e4fc-e792-473a-8853-43520dfc1147",
},

将 entry1 更改为 entry2，依此类推。您也可以使用 entrya、entryb。

Mods.SubclassCompatibilityFramework.Api.InsertRaceChildData(raceChildData)

与本教程不完全相关，但以防您想出用途，如果要从 Races.lsx 中删除行而不是添加，请将 InsertRaceChildData 替换为 RemoveRaceChildData

恭喜您通过 lua 设置了您的模组以使用兼容性框架。只需记住始终将兼容性框架加载在加载顺序的底部。

---
*Source: [Modding:Compatibility Framework](https://bg3.wiki/wiki/Modding:Compatibility_Framework)*