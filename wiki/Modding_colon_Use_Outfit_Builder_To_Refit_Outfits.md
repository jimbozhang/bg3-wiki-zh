# Modding:使用服装构建器重制服装

此页面为[模组页面](Modding_colon_Modding_resources.md "Modding:模组资源")，遵循其独立于Wiki其余部分的规则和标准。

使用服装构建器工具，您可以将服装从一种体型重制为另一种体型。这使得为不同体型重制服装变得容易得多。以下是操作方法！

### 所需工具

[Blender 3.6](https://www.blender.org/download/lts/3-6/)

[服装构建器](https://www.nexusmods.com/baldursgate3/mods/3683) 由 ReallyLazyIcarus 制作

[Blender 网格数据传输](https://mmemoli.gumroad.com/l/tOKEh) 免费插件

### 重制服装

打开随服装构建器附带的 body_templates.blend 文件。决定您想要构建的网格，以及您想要从哪个形状传输到哪个形状。例如，假设我们想将野蛮人服装 (HUM_F_ARM_Barbarian_A_Body.GR2) 从 HUM F 转换为 HUM FS。将野蛮人服装 GR2 加载到 Blender 中。如果需要，可以删除 LOD。

现在选择野蛮人服装的所有网格部件。打开服装构建器选项卡，使用截图中的设置，然后点击构建服装。看起来什么都没发生——现在您需要清除形变键。

选择您的第一个网格部件，点击对象数据属性的绿色三角形，然后移除形变键，始终从移除 Basis 开始。您的网格将发生变换！

您的网格现已重制，但可能需要重新绑定权重以适应变换。也可能需要一些轻微的手动重塑以修复穿模问题。

### 创建自定义形变键

---
*Source: [Modding:Use Outfit Builder To Refit Outfits](https://bg3.wiki/wiki/Modding:Use_Outfit_Builder_To_Refit_Outfits)*