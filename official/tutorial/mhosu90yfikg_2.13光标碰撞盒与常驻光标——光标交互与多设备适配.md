---
id: mhosu90yfikg
title: 2.13光标碰撞盒与常驻光标——光标交互与多设备适配
url: https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhosu90yfikg
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhosu90yfikg
description: undefined
language: zh
scope: tutorial
crawledAt: 2026-11-04T16:00:21.663Z
---

# 前言

## 课程说明：

**课程内容：** 光标碰撞盒组件的配置、常驻光标与使用案例

**学习目标：** 学会通过配置光标碰撞盒与常驻光标，实现玩家点击实体后销毁目标实体的功能（如点击放置在场景中的实体即可将其销毁），并掌握不同输入设备（键鼠/触屏）下的光标适配规则。

_\*\*该课程中涉及【局内编辑器面板配置】和【千星沙箱节点图】两个模块内容，并且相互关联，阅读时建议按照课程顺序完整阅读_

## 相关信息：

**推荐学习顺序：**【前置课程】→【当前课程】→【综合指南】

_\*\*如课程中遇到概念不清等问题或想要了解更多相关信息，根据需要查询【综合指南】即可_

**前置课程：** 该课程与以下前置课程所讲述的功能知识点相关 _（建议首次使用时，优先学习_ **_【前置课程】_** _，学习体验更流畅）_

> [3.5单位状态——让某物获得增益或减益的效果](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhd7nxrfa8im)
>
> [3.6信号通信——一对多的信号广播，触发多物体产生不同行为](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhjwjrr5n73i)

**关联知识点：** 课程中将涉及以下基础概念 _（建议优先根据该课程学习即可，如遇到概念不清等问题或想要了解更多相关信息，再根据需要查阅_ **_【综合指南】_** _相关章节）_

> [光标碰撞盒](https://act.mihoyo.com/ys/ugc/tutorial/detail/mhso200yz3h4)
>
> [玩家——常驻光标](https://act.mihoyo.com/ys/ugc/tutorial/detail/mhctmgi51lpo)

* * *

# 光标碰撞盒与常驻光标——光标交互制作

## 功能示例-1：光标点击销毁实体

### 1.概念简述

**光标碰撞盒：** 挂载在实体/元件上的组件，用于定义实体接收光标检测的响应区域。决定哪些区域能被光标命中，是后续实现光标点击、选择等交互的前提。

**常驻光标：** 游戏局内持续显示在界面中并保持激活状态的光标。使玩家无需呼出特定菜单，即可随时通过键鼠、触屏或手柄控制光标，对场景中的实体进行射线检测、点击等交互。

### 2.教学内容

**功能效果：** 在场景中放置一个带有光标碰撞盒的实体，玩家在局内将光标移动到该实体上并点击后，触发对应技能逻辑，由客户端向服务端发送命中结果信息，最终将该实体销毁。

**效果演示：**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/81252302-a106-45ce-88a1-65a2318e5c8c.gif)

### 3.操作步骤

**1.【局内编辑器】元件添加「光标碰撞盒」通用组件**

创建一个元件作为光标碰撞盒载体，在面板中点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/dda82681-a0b1-4997-9cde-0a5d97fc8db6.png)>>>进入组件页，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/90b3994f-bfe6-46fd-abc0-87fb2c09d66b.png)>>>选择【光标碰撞盒】即可成功添加。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/c23831ee-5164-4cfa-9be3-a2a691c67df7.png)

**2.【局内编辑器】配置光标碰撞盒区域**

在展开的光标碰撞盒详细编辑页中，配置生效规则与碰撞区域：

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/4d10b088-291e-418f-83de-ff1d38a38d5b.png)

**3.【局内编辑器】常驻光标设置**

设置游戏内光标常驻显示，在面板中点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/f6054c5a-7c2a-45ac-8fcd-633a54393105.png)>>>进入【战斗预设】，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/85bca277-6099-4119-bd2c-0c432ce76233.png)>>>在玩家编辑中找到光标配置，开启“光标常驻”选项：

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/f35bf45c-d85d-449c-9f39-5d19ca63bea5.png)

**4.【局内编辑器】光标点击技能创建**

进入【战斗预设】，选择![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/f91b942c-d149-48ba-b712-8985f1336d6c.png)>>>进入技能页，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/45d3c642-bf7b-46d2-b148-95873afff415.png)>>>设置技能名称后，即可添加（教学中直接命名为光标点击，实际可自由配置）。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/4757bbcb-196b-4887-b73a-5fbb4903e37f.gif)

**5.【千星沙箱】节点图配置**

实现「光标点击销毁实体」的核心在于 **客户端判定与服务端执行的分工**：



**为什么点击在客户端？** 玩家的光标点击属于本地客户端的输入动作，需要在【客户端节点图】中进行监听并识别选中的目标。



**为什么销毁在服务端？** 实体的存在与销毁属于服务端数据，需要由【服务端节点图】统一接收信号并执行销毁。

**a)角色技能节点图配置**

在角色技能节点图中，添加并配置对应技能的节点（设置参考见下图），为达到预期的功能效果教程中配置如下：

_\*\*该节点图需添加到【自定义技能】上_

|     |     |     |     |
| --- | --- | --- | --- |
|  |  | 要做的功能 | 对应的配置项 |
| 功能-1（客户端） | 触发场景 | 玩家按下鼠标左键/交互键 | 【事件节点】：【客户端】输入按键按下 |
|  | 条件 | 检查当前光标是否有命中目标 | 【查询节点】：使用【获取光标命中结果】查询光标点击的实体<br>【流程控制节点】：判断是否为“物件”类型实体 |
|  | 结果 | 取出被命中的实体并发送信号给服务端 | 【执行节点】：发送自定义信号“光标点击实体”到服务端，传入目标实体参数 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/02c0aed1-dfa8-41c1-ab0d-b9e01fc2a184.png)

**b)实体节点图配置**

在实体节点图中，添加并配置对应销毁逻辑的节点（设置参考见下图），为达到预期的功能效果教程中配置如下：

_\*\*该节点图需挂载在【关卡实体】上_

|     |     |     |     |
| --- | --- | --- | --- |
|  |  | 要做的功能 | 对应的配置项 |
| 功能-2（服务端） | 触发场景 | 收到客户端发来的销毁信号请求 | 【事件节点】：【监听信号】收到“光标点击实体”信号 |
|  | 条件 | 判断传入的目标实体是否存在 | 【流程控制节点】：判断实体是否在场 |
|  | 结果 | 执行实体销毁 | 【执行节点】：销毁实体（输入目标为自定义信号传递的实体参数） |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/dbd8bdc8-5e35-4b6f-862f-92906a5b5904.png)

**6.【局内编辑器】挂载节点图**

将配置的节点图挂载在关卡实体和角色自定义技能上，保存存档设置。

**7.【局内编辑器】放置元件与测试**

将配置好光标碰撞盒的元件拖入场景，保存关卡并进入试玩，移动光标指向该实体并点击，验证实体是否被成功销毁。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/81252302-a106-45ce-88a1-65a2318e5c8c.gif)

# 光标交互响应制作——触屏/手柄

## 功能示例-2：触屏/手柄点击销毁实体

### 1.概念简述

在实际开发中，不同输入设备（键鼠/触屏/手柄）在光标的显示与操作模式上存在显著差异，手柄与键鼠在光标基础设置上相同，触屏设备则需添加单位状态来实现光标点击效果。

### 2.教学内容

**实现效果：** 在功能示例-1的光标设置基础上，分别给角色挂载「光标点击施放技能」状态，给气球实体挂载描边状态，实现玩家在触屏设备点击选中场景中气球实体时，气球会高亮显示描边并启动倒计时，定时器触发后销毁气球实体的功能。

**效果演示：**

_\*\*演示中点击气球实体成功后会绿色描边_

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/3cf0ee39-c549-446d-933b-19a48415e64d.gif)

### 3.操作步骤

**1.【局内编辑器】添加单位状态**

新建一个状态作为“光标点击施放技能”状态，在面板中点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/e74d508d-3e4d-43f9-b57c-edfbdf2dbb1c.png)>>>进入【战斗预设】，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/07591798-97ba-40f9-b45f-38cde7fa0134.png)>>>选择![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/97c364e1-320c-4fd7-83bf-0386791e9ad8.png)即可添加。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/084024b7-85e6-4dd2-aba2-f1095d5826d4.png)

**2.【局内编辑器】制作“光标点击施放技能”和“描边”效果**

添加状态后可对状态的名称、叠加层数上限、持续时间、状态规则等进行调整，为达到预期功能效果，教程中配置如下：

**a)“光标点击施放技能”效果制作**

|     |     |     |
| --- | --- | --- |
|  | 要做的功能 | 对应的配置项 |
| 通用信息 | 状态持续时间无上限 | 【无限持续时间】选项开启 |
| 效果详细信息 | 配置技能槽位 | 槽位选择普通攻击 |
| 配置对应自定义技能 | 选择【功能示例-1】中设置的自定义技能 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/82733e0c-21b0-4723-9f06-ac8e10247475.gif)

**b)“挂载描边效果”状态制作**

|     |     |     |
| --- | --- | --- |
|  | 要做的功能 | 对应的配置项 |
| 通用信息 | 运行时间设置 | 将初始运行时长设置为5s |
| 效果详细信息 | 添加状态描边效果 | 效果选择为【挂载描边效果】 |
| 设置描边颜色 | 效果选择【自定义颜色】，指定颜色为“绿色” |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/8e203601-5b73-4157-adc9-fd40ffa21d68.png)

**3.【千星沙箱】节点图设置**

**a)角色技能节点图配置**

触屏设备在节点图配置上与键鼠/手柄设备一致，同样包含「技能节点图」。具体节点的搭建与参数设置请直接参考 【功能示例-1】步骤 5。

**b)实体节点图配置**

|     |     |     |     |
| --- | --- | --- | --- |
|  |  | 要做的功能 | 对应的配置项 |
| 功能-1 点击气球后添加描边效果，延迟销毁气球实体 | 触发场景 | 收到客户端发来的销毁信号请求 | 【事件节点】：【监听信号】收到“光标点击实体”信号 |
| 条件 | 判断传入的目标实体是否存在 | 【流程控制节点】：判断实体是否在场 |
| 结果-1 | 启动定时器计算延迟销毁时间，倒计时结束后销毁实体 | 【执行节点】：使用【启动定时器】记录点击气球后的时间 |
| 结果-2 | 添加描边【单位状态】 | 【执行节点】：使用【添加单位状态】添加描边效果 |
| 结果-3 | 用自定义变量记录目标实体 | 【执行节点】：判断气球实体在场后，使用【设置自定义变量】记录目标实体 |
| 功能-2 定时器触发后销毁实体 | 触发场景 | 定时器触发 | 【事件节点】：定时器触发事件 |
| 条件 | 判断定时器是否一致 | 【流程控制节点】：判断触发的定时器是否和功能-1中创建的定时器一致 |
| 结果 | 销毁实体 | 【执行节点】：定时器触发后销毁选中的气球实体 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/905cae32-310e-4e39-88a3-23b5171b7929.png)

**4.【局内编辑器】挂载单位状态，试玩体验**

将单位状态挂载到角色身上，进入试玩即可体验该功能。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhosu90yfikg/5d5bcdc6-4bdd-47cc-8fa2-ef3179e72338.gif)

* * *

# 课程总结及辅助课件

**课程作业：** 可根据课程教学内容尝试进行以下功能复刻/拓展。

**功能复刻：** 创建一个附带光标碰撞盒的宝箱实体，配置常驻光标并在玩家点击宝箱时，通过判定实现宝箱的销毁与奖励掉落。

**进阶拓展：** 结合触屏设备适配逻辑，为角色配置「光标点击施放技能」单位状态，实现在触屏设备上点击地面指定位置召唤法阵的逻辑。

**课程回顾：** 学习如何通过配置光标碰撞盒与常驻光标，结合超限模式下的客户端查询节点，实现多端销毁实体功能。

### 辅助课件

我们提供了上述课程内容相关的工程文件，可结合 **【教学存档-光标碰撞盒与常驻光标】** 对照学习。

![](https://webstatic.mihoyo.com/upload/static-resource/2022/10/14/64e71b8a5e28fbdbc3d3df5d311e4154_847866555738962172.svg)

光标碰撞盒与常驻光标.gil

34.6 KB