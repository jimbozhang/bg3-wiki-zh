# 指南：规避荣誉模式游戏存档限制

这是一个[社区指南](Guide_colon_Index.md "Guide:Index")，任何人都可以编辑。请参阅[样式手册](Help_colon_Style_manual.md "Help:Style manual")以获取指导方针。

#### 规避存档限制

通过在游戏会话之间手动备份游戏存档，可以规避[荣誉模式](Difficulty.md#Honour "Difficulty")的*单存档*系统。如果在荣誉模式中出现问题，可以关闭游戏，恢复之前的存档文件，然后重新启动游戏，从备份的存档继续。

虽然使用此技巧定期加载旧游戏状态会违背荣誉模式的初衷，但一个合法的用例可能是恢复因玩家控制之外的原因（例如游戏错误，或猫踩到键盘导致的意外按键）而变糟的进度。

此技巧在 MS Windows、GNU/Linux 和 MacOS 上特别容易实现，因为可以通过文件管理器或 shell 命令轻松访问游戏存档。如果游戏机可以访问和覆盖存档文件，也可能在游戏机上实现。[[_验证_](bg3wiki_colon_Verification.md "bg3wiki:Verification")]

具体步骤如下：

- 确保云存档已关闭。
- 在加载存档之前，将当前存档文件复制到不同的文件夹。
- 继续您的荣誉模式进度并随意游玩。
- 要重新加载：关闭游戏，删除新的荣誉模式存档文件，并将之前的副本放回原位。
  - **注意：必须在队伍全灭之前完成此操作。**

如果云存档已开启，仍可按以下方式恢复备份的荣誉模式存档：

- 启动游戏后，点击*加载游戏*按钮。
- 在游戏处于此菜单时，用您备份的存档覆盖当前的荣誉模式存档。

游戏存档位置如下：

- MS Windows: `%LOCALAPPDATA%\Larian Studios\Baldur's Gate 3\PlayerProfiles\Public\Savegames\Story`
- MacOS: `$HOME/Documents/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/Savegames/Story`

还有其他涉及游戏文件操作的方法，例如：

- [如何修复失败的荣誉模式存档（Reddit）](https://www.reddit.com/r/BaldursGate3/comments/18d3fks/how_to_fix_a_failed_honour_mode_save/)
- [在 MS Windows 中重新激活荣誉模式的工具（GitHub）](https://github.com/nay-cat/HonourSaver)

---
*Source: [Guide:Circumventing Honour Mode Save File Restrictions](https://bg3.wiki/wiki/Guide:Circumventing_Honour_Mode_Save_File_Restrictions)*