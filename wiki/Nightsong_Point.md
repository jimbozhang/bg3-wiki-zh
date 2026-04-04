# 暗夜之歌点数

关于任务，请参阅 [寻找暗夜之歌](Find_the_Nightsong.md "寻找暗夜之歌")；关于其他好感度系统，请参阅 [好感度](Approval.md "好感度")。

## 目录

- [1 关于暗夜之歌点数](#about-nightsong-points)
- [2 获取暗夜之歌点数](#obtaining-nightsong-points)
  - [2.1 点数 1 与 2](#points-1-&_2)
    - [2.1.1 点数 1](#point-1)
    - [2.1.2 点数 2](#point-2)
    - [2.1.3 获取点数 1 和 2 的正确顺序](#the-right-order-of-acquiring-points-1-and-2)
  - [2.2 点数 3](#point-3)
  - [2.3 点数 4](#point-4)
  - [2.4 点数 5](#point-5)
  - [2.5 点数 6](#point-6)
- [3 对话变化](#changes-to-dialogue)
- [4 暗夜之歌](#the-nightsong)
- [5 另见](#see-also)
- [6 外部链接](#external-links)

## 关于暗夜之歌点数

**暗夜之歌点数** 是一个特殊的好感度系统，专属于 [影心](Shadowheart.md "影心")。

该系统影响在任务 ⁠[寻找暗夜之歌](Find_the_Nightsong.md "寻找暗夜之歌") 的第二幕 [第二幕](Act_Two.md "第二幕") 最终阶段与 [艾琳女士](Dame_Aylin.md "艾琳女士") 的遭遇如何展开。它们也影响 [影心](Shadowheart.md "影心") 个人任务 ⁠[黑暗之女](Daughter_of_Darkness.md "黑暗之女") 的最终决定。

在前两幕中总共有六个暗夜之歌点数可供获取。获得至少四个点数会使影心开始怀疑她对 ⁠[莎尔](Shar.md "莎尔") 的奉献，并在遭遇暗夜之歌时解锁原本隐藏的对话。

暗夜之歌点数的内部标志是 `ORI_Shadowheart_State_NightsongPoint_FLAG`。

## 获取暗夜之歌点数

### 点数 1 与 2

前两个点数可以在影心的闪回场景后获得，在该场景中，她向玩家角色展示她年轻时的样子，当时一群莎尔信徒在树林里围堵了一匹狼。

点数一和二有一个额外的障碍，因为它们只有在影心的记忆之后才可用。

要解锁此事件，必须至少获得三个 **狼之梦点数**。这些点数可以在推进故事时获得：

1.  在鹦鹉螺上拯救影心 (`ORI_Shadowheart_State_WolfDreamPoint_NautiloidSaved`)
1.  在营地对话中，当影心透露自己是莎尔的信徒时，遵循以下路径： (`ORI_Shadowheart_State_WolfDreamPoint_WorshipGood`)
    - 影心：_“我们褪去那些斗篷。在莎尔面前，我们荣耀地赤裸，超越凡人的虚荣。”_
    - 玩家角色：_“当你这么说时，听起来奇怪地令人安心。”_
    - 影心：_“通常会有痛苦——甚至是死亡。许多人在拥抱莎尔的真理之前就崩溃了。”_
    - 玩家角色：_“如果我说这听起来不令人信服，那是在撒谎。你应该找个时间多告诉我一些。”_
1.  在营地对话中，询问影心是否可以帮忙处理她的手。 (`ORI_Shadowheart_State_WolfDreamPoint_WoundFlarePositive`)
1.  在营地对话中，要求影心告诉你更多关于她自己的事。 (`ORI_Shadowheart_State_WolfDreamPoint_LearnedPersonalKnowledge`)
1.  在营地对话中，发现她被压抑的记忆。 (`ORI_Shadowheart_State_WolfDreamPoint_MissingMemories`)
1.  将 [莎尔神像](Idol_of_Shar.md "莎尔神像") 交给影心 (`ORI_Shadowheart_State_WolfDreamPoint_FoundIdolOfShar`)
1.  在影心与 [莱埃泽尔](Lae'zel.md "莱埃泽尔") 的战斗中支持她 (`ORI_Shadowheart_State_WolfDreamPoint_LaezelFight`)

要获得这两个暗夜之歌点数，必须以正确的顺序做出正确的选择。

#### 点数 1

选项 1：在影心的闪回之后，与影心交谈时，使用以下对话选项成功通过被动 DC 18 [宗教](Religion.md "宗教") [检定](Ability_Check.md "属性检定")：
    - _“你看起来像是戴着月长石……那不是塞伦涅信徒常戴的吗？”_

选项 2：在触发此对话之前，在 ⁠[枭熊巢穴](Owlbear_Nest.md "枭熊巢穴") 阅读 [塞伦涅仪式](Sel%C3%BBnite_Rite.md "塞伦涅仪式")，会揭示知识以跳过被动属性检定。 (`ORI_Shadowheart_State_NightsongPoint_MadeSeluniteConnection`)

选项 3：塞伦涅的 [牧师](Cleric.md "牧师") 即使不阅读 [塞伦涅仪式](Sel%C3%BBnite_Rite.md "塞伦涅仪式") 也能跳过被动属性检定，并获得略有不同的叙述台词。

#### 点数 2

_完成_ 点数 1 后，继续与影心对话：
    - 玩家角色：_“难怪你如此忠于莎尔——你感觉欠她一条命。”_
    - 影心：_“她造就了我……至少，据我所记得的。她教导我，训练我，在我失败时惩罚我——而我经常失败。”_

现在选择：
    - 玩家角色：_“听起来像是虐待。”_
    (`ORI_Shadowheart_State_NightsongPoint_AbuseEmancipation`)

#### 获取点数 1 和 2 的正确顺序

如果在点数 1 之前选择了点数 2 所需的对话路径，那么点数 1 将变得无法获得。未阅读 [塞伦涅仪式](Sel%C3%BBnite_Rite.md "塞伦涅仪式") 的塞伦涅牧师的对话树**没有**此对话选项，这使得塞伦涅角色除非在触发闪回之前也阅读了它，否则无法获得此点数。

### 点数 3

此点数仅在影心的伤口爆发四次后可用。会出现一个新的对话选项：
    - _“你的伤口让你太痛苦了，影心。一定有办法治愈它。”_

如果好感度为 20 或更高，<sup>[\[1\]](#cite_note-med_approval-1)</sup> 玩家角色可以通过 DC 10 [宗教](Religion.md "宗教") [检定](Ability_Check.md "属性检定") 或 DC 12 [游说](Persuasion.md "游说") [检定](Ability_Check.md "属性检定") 来获得暗夜之歌点数。 (`ORI_Shadowheart_State_NightsongPoint_CureIncurableWound`)

### 点数 4

说服影心吃下 [箴言菇](Noblestalk.md "箴言菇")，触发 ⁠[熟悉面孔](A_Familiar_Face.md "熟悉面孔") 并奖励第四个点数。 (`ORI_Shadowheart_State_NightsongPoint_AteNoblestalk`)

### 点数 5

给影心一朵 [夜兰花](Night_Orchid.md "夜兰花") 会奖励另一个点数。 (`ORI_Shadowheart_State_NightsongPoint_GaveNightOrchid`)

### 点数 6

当队伍在 ⁠[莎尔铁手神殿](Gauntlet_of_Shar.md "莎尔铁手神殿") 时，可以通过以下对话获得此点数：
    - 影心：_“我曾梦到过这个地方。这是我的命运——我必须完成试炼。”_
    - 玩家角色：_“好吧，如果我能帮上忙，我会的。”_

或者，同意让影心激活三个试炼中的任何一个也会授予相同的点数。 (`ORI_Shadowheart_State_NightsongPoint_AgreedToTrials`)

## 对话变化

一个沉思的影心站在营地，她一反常态地双臂交叉在胸前。她对自己的信仰以及与莎尔的关系心存疑虑。

获得 4 个暗夜之歌点数后，玩家角色会自动收到 `ORI_Shadowheart_State_NightsongPoint_HasEnoughPoints` 标志，影心可能会立即触发关于她内心矛盾的对话。如果其他事件已排队，这可能不会立即触发。通常，新对话会在她头顶显示一个 `!`。

此外，在下次前往营地后，会解锁新的对话机会，但除了影心改变的肢体语言外，没有指示这些机会可用的标志。

如果在与她交谈之前长休或离开营地，她的营地姿势会恢复正常，此对话将不可用。

## 暗夜之歌

在与暗夜之歌遭遇期间，以下条件决定了哪些对话选项可用：
    - 4 个或更多暗夜之歌点数
    - 20-39 [好感度](Shadowheart/Approval.md "影心/好感度")
    - 40 或更高 [好感度](Shadowheart/Approval.md "影心/好感度")

可以通过在第一组对话选择中选择 _“这真的是你想要的吗？”_ 来检查影心当前的好感度：
    - 好感度低于 20 导致：_“如果你了解我，你甚至不会问。这是我女士想要的——我只是她的仆人。”_
    - 好感度 20-39 导致：_“当然，为什么不是呢？这是我的目的。”_
    - 好感度 40 或更高导致：_“我……是的，我想是的。我一生都在为此做准备。现在无法回头了。”_

在此之后，根据所做的选择，影心的好感度总共可以变化 +10、+5 或 -5。

好感度达到 40 或更高时，以下任何选项都可以在不进行技能检定的情况下饶恕暗夜之歌：
    - 她知道一些关于你的事。饶了她，看看她有什么要说的。
    - 这是你的选择。我不能替你做决定。<sup>[\[2\]](#cite_note-2)</sup>
    - _一言不发。_<sup>[\[3\]](#cite_note-3)</sup>

如果与影心的好感度低于 40，无论有多少暗夜之歌点数，她总是会杀死暗夜之歌，除非通过以下游说检定之一：
    - [游说] 她知道一些关于你的事。饶了她，看看她有什么要说的。(DC 14)
    - [游说] 别这么做，影心。别杀她——你会后悔的 (DC 21)
    - [游说] 别这么做，影心。别杀她——你会后悔的 [DC 21 ]<sup>[\[4\]](#cite_note-4)</sup>

如果与影心的好感度为 20-39 并且获得了足够的暗夜之歌点数，则上述游说检定不可用。因此，所有剩余的选择都会导致影心杀死暗夜之歌。这很可能是一个错误。

以下所有对话选项都会导致影心杀死暗夜之歌，无论好感度或暗夜之歌点数如何：
    - 杀了她。让我们完成这个仪式。
    - [塞伦涅] 也许她值得死亡的安宁。结束她的痛苦。
    - [塞伦涅] 让她活着。莎尔永远不会停止要求你献祭。

## 另见

- [黑暗之女](Daughter_of_Darkness.md "黑暗之女")
- [寻找暗夜之歌](Find_the_Nightsong.md "寻找暗夜之歌")
- [影心](Shadowheart.md "影心")
- [影心/好感度](Shadowheart/Approval.md "影心/好感度")

## 外部链接

| - [影心的隐藏分数 | “暗夜之歌点数” 解释](https://youtu.be/YdNEya-Np5U?si=JiCoXo-gIvkEPAe8) by SlimX |

1. [↑](#cite_ref-med_approval_1-0) 在控制器模式和主机上，这表示为“中级”或更好的好感度
1. [↑](#cite_ref-2) 如果玩家角色有足够的暗夜之歌点数，使得影心说 _“我……你怎么想？我该怎么办？”_
1. [↑](#cite_ref-3) 如果玩家角色没有足够的暗夜之歌点数，使得影心说 _“无论你认为你了解我什么，一旦我成为我注定要成为的人，都不重要了。”_
1. [↑](#cite_ref-4) 如果玩家角色没有足够的暗夜之歌点数并且与影心的好感度低于 20

---
*Source: [Nightsong Point](https://bg3.wiki/wiki/Nightsong_Point)*