# 帮助:上传文件

## 上传前

### 检查清单

- 如果您不是文件的创建者，您拥有上传该文件的权利是基于何种许可？
  - 维基的[版权政策](bg3wiki_colon_Copyrights.md "bg3wiki:Copyrights")
  - [帮助:许可](Help_colon_Licenses.md "Help:Licenses") - 维基支持的许可
- 文件格式是否合适？
  - 维基不支持大于 50 MB 的文件
  - 维基无法从大于 12.5 MP（如果为正方形则约为 3,500x3,500 像素）的图像创建缩略图
  - 维基支持以下文件格式：
    - 图像：png, gif, jpg, jpeg, webp
    - 视频：webm, mp4, flac, mkv, mov
    - 音频：mp3, oga, ogg, ogv, wav
- 您是否查看过该文件是否已存在于维基上，或者是否有可更新的类似文件？
- 您上传的文件是否有使用场景？
- 是否符合其类型的媒体方案？
  - 例如，肖像画为："Portrait [Name].png"
  - 参见：[bg3wiki:图片政策](bg3wiki_colon_Image_policy.md "bg3wiki:Image policy")
  - 一些模板会明确查找给定的名称和文件扩展名，即使不是这种情况，一致的命名也能让未来的编辑者更容易找到您的文件。

## 移除背景

有时需要或希望移除图像的背景，例如从[属性块](Template_colon_CharacterInfo.md "Template:CharacterInfo")创建[角色模型](Category_colon_Character_models.md "Category:Character models")图像时。如果您无法使用或不熟悉更强大的工具（如 Photoshop），有两种简单且免费的选择：

### Microsoft Photos

默认的 Windows 照片查看器可以用来以惊人的精度移除背景：

- 打开图像
- 点击左上角的编辑
- 在顶部窗格中选择“背景”选项
- 根据需要使用“背景画笔工具”进行调整 - 可选
- 点击“移除”
- 将图像保存为 .png - 重要提示：仅当图像显示为棋盘格背景时才保存图像

### Remove.bg

如何使用 Remove.bg 网站

第二个替代方案是免费的 [Remove.bg](https://www.remove.bg/) 网站。与 Microsoft Photos 不同，它会缩小图像，但这对于信息框用途来说影响不大。

- 访问 [Remove.bg](https://www.remove.bg/)。
- 上传需要移除背景的图像（通过拖放或简单地使用 Ctrl+C 和 Ctrl+V）。
- 等待结果。
- 点击蓝色的下载按钮。
- 将图像上传到维基，并记得将其重命名为 Character_name_Model.png

如果结果删除过多或不足，您可以在网站上编辑以擦除/恢复功能。

## 上传

您可以使用左侧导航工具栏中的[上传文件](Special_colon_Upload.md "Special:Upload")功能从计算机上传图像。有一个[批量上传工具](Special_colon_BatchUpload.md "Special:BatchUpload")，但应谨慎使用。如果您选择使用批量工具，请务必在选择要上传的文件**之前**，将任何描述、分类标签和版权模板添加到“描述：”字段中。

### 分类

请编辑图像以将其添加到一个或多个分类中。这可以极大地帮助其他贡献者将来找到图像。如果没有合适的分类，请随时创建一个。

### 添加到页面

角色页面应使用以下格式作为 Infobox creature 模板的一部分：

| image = <gallery> Name.jpg | In-game Name Model.png | Model Portrait Name.png | Portrait</gallery> |

---
*Source: [Help:Uploading files](https://bg3.wiki/wiki/Help:Uploading_files)*