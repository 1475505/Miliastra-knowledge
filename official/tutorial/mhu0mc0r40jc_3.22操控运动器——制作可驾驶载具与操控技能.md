---
id: mhu0mc0r40jc
title: 3.22操控运动器——制作可驾驶载具与操控技能
url: https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhu0mc0r40jc
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhu0mc0r40jc
description: undefined
language: zh
scope: tutorial
crawledAt: 2026-11-04T16:02:25.644Z
---

# 前言

## 课程说明：

**课程内容：** 操控运动器组件与角色操控技能的配置与使用案例。

**学习目标：** 学会配置【操控运动器】打造可驾驶的物理载具（如小车、速度参数与自定义轮胎动效），并掌握【角色操控技能】的制作与绑定，实现玩家操控载具时发射子弹等战斗能力。

_\*\*该课程中涉及【局内编辑器面板配置】和【千星沙箱节点图】两个模块内容，并且相互关联，阅读时建议按照课程顺序完整阅读_

## 相关信息：

**推荐学习顺序：**【前置课程】→【当前课程】→【综合指南】

_\*\*如课程中遇到概念不清等问题或想要了解更多相关信息，根据需要查询【综合指南】即可_

**前置课程：** 该课程与以下前置课程所讲述的功能知识点相关 _（建议首次使用时，优先学习【前置课程】，学习体验更流畅）_

> [3.8投射运动器——制作一个能发射的子弹](https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhn4nsiz7k18)
>
> [3.10命中与受击——制作攻击命中的效果](https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhsdgyi53pz0)

**关联知识点：** 课程中将涉及以下基础概念 _（建议优先根据该课程学习即可，如遇到概念不清等问题或想要了解更多相关信息，再根据需要查阅【综合指南】相关章节）_

> [操控运动器](https://act.mihoyo.com/ys/ugc/tutorial//detail/mh1ytk9631fm)
>
> [角色操控技能](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhj4a0rzu4pi)
>
> [主镜头](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhfua005zpeg)

* * *

# 操控运动器——打造自由驾驶的载具

## 功能示例-1：制作一辆具备自定义轮胎的载具小车

### 1.概念简述

**操控运动器：** 挂载在元件上的通用运动组件，允许运行时通过玩家操控轮盘控制元件移动、转向与施放操控技能。操控运动器支持配置碰撞盒、接地位置、角度上限以及装饰物运动表现（如轮胎旋转与左右偏转）。

### 2.教学内容

**功能效果：** 制作一个玩家可进入并操控移动的载具小车，小车具备自定义前进/后退加速度与阻力参数，且移动与转向时四个轮胎会自动滚动与偏转。

**效果演示：**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/ef87d368-481e-4a0d-9ab1-6be4ad1e4bb4.gif)

### 3.操作步骤

**1.【局内编辑器】创建载具元件并添加【操控运动器】组件**

进入元件库选择制作好的载具小车元件，在面板中点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/54704ecd-f087-4712-840c-0b8e20eec88f.png)>>>进入组件页，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/114144ee-6446-451f-80b2-822f20f658e3.png)>>>选择【操控运动器】即可添加。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/00ca2074-e43f-4f11-8130-b0baa7fbd266.png)

**2.【局内编辑器】配置操控运动器基础参数**

打开【组件-操控运动器-基础】页签，可以对“实体接地位置”、“角色退出点”进行设置：

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/9056e2a1-36e9-4d77-9a90-0424a2d0fd09.png)

为了使小车运动效果更加逼真，还需为其配置轮胎装饰物，教程中配置如下：

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 设置装饰物挂接点 | 新增4个自定义挂接点，将挂接点位置分别设置在小车的四角 |
| 添加轮胎装饰物 | 设置轮胎模型，挂载到对应挂接点上 |
| 添加装饰物运动设置 | 新增装饰物运动表现，关联对应装饰物挂接点 |

**a)添加【自定义挂接点】组件，新增4个自定义挂接点并命名**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/5e4e756d-f751-40b5-95b4-056bee6b9db4.png)

**b)在【装饰物管理】中添加轮胎装饰物**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/1128b671-6fd8-4eaa-beb0-dbe13ddfdb34.png)

**c)在【装饰物运动表现】中关联装饰物挂接点**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/cdb91ba8-97e1-4773-bb32-0c14c50eb1b7.png)

**3.【局内编辑器】配置载具动力与速度参数**

进入【组件-操控运动器-运动】页签，对小车的操控方式与动力/阻力进行详细配置：

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 按载具车头朝向行驶 | 【方向输入类型】选择“操控实体朝向” |
| 提升小车的灵敏度与转向速度 | 【转向速度】设置为“180.00”；【前进加速度】设置为“25.00” |
| 限制最高车速 | 【最大前进速度】设置为“20.00” |
| 设置独立且较慢的倒车速度 | 开启【区分前进后退速度】，【后退加速度】设为“12.00”，【最大后退速度】设为“8.00” |
| 设置自然滑行与速度阻力 | 【阻力减速度】设置为“5.00”；开启【跟随移动速度变化】，【减速系数】设为“0.05” |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/921396aa-351d-4c6f-b47b-f18fd10ecf24.png)

_\*\*以上数值为演示示例，实际使用可根据具体需求调整_

**4.【局内编辑器】制作载具小车的物件镜头并挂载**

**a)在主镜头管理中新建一个物件镜头，调整“详细设置”和“运动修正设置”参数，具体的功能和对应配置项见下表：**

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 限制俯仰视角范围 | 【俯仰角度范围】设置为“-21.78~89.00” |
| 镜头跟随旋转 | 开启【镜头跟随旋转】并使用默认参数，同时开启【仅在移动时修正】和【镜头延迟跟随】选项，在满足条件后会根据配置速度与基准角度修正物件镜头 |
| 根据小车实际运动速度修正镜头大小 | 【正向最大视野变化量】调整为“15.00”；<br>【正向速率最大参考值】调整为“40.00”；<br>【逆向最大视野变化量】调整为“10.00”；<br>【逆向速率最大参考值】调整为“10.00” |
| 开启自定义运动阻尼，延缓镜头跟随小车的跟随速度 | 【运动阻尼参数】XYZ轴的值均设置为“0.15” |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/1969cfad-8281-4476-b67f-bfb93f4006e3.png)

_\*\*以上数值为演示示例，实际使用可根据具体需求调整，对应节点使用可在课程提供存档中查看_

**b)添加物件镜头组件并挂载制作好的镜头视角**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/6347cc3c-262b-4bce-8128-82feadce1044.gif)

**5.【千星沙箱】实体节点图配置**

靠近载具小车后会显示“上车”选项卡，玩家选中选项卡时需要设置玩家跟随并且激活载具小车，为达到预期的功能效果课程中配置如下：

|     |     |     |     |
| --- | --- | --- | --- |
|  |  | 要做的功能 | 对应的配置项 |
| 功能 玩家坐上载具小车 | 触发场景 | 点击“上车”选项 | 【事件节点】：选项卡选中时 |
|  | 条件 | / | / |
|  | 结果 | 玩家坐上载具小车并切换镜头视角 | 【查询节点】：获取角色对应的玩家实体；<br>【执行节点】：设置玩家跟随并激活操控运动器，设置玩家镜头跟随载具小车 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/e5e5480e-17c9-419d-b43e-8998c50c10b0.png)

_\*\*需在载具小车组件页中添加【选项卡】组件，并新增一个命名为“上车”的交互选项。_

**6.【局内编辑器】放置元件，试玩体验**

将制作好的载具小车放置在场景中，进入试玩即可进行驾驶体验，测试行驶、转向及轮胎滚动偏转效果。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/8f8a58de-829e-42e3-82e7-d57523cdf7bc.gif)

_\*\*更多相关信息可自行查阅【综合指南-操控运动器】_

* * *

# 角色操控技能——载具小车操控技能制作

## 功能示例-2：为载具小车装备角色操控技能

### 1.概念简述

**角色操控技能：** 角色在处于操控状态下（如驾驶载具）才可以使用的特殊类别角色技能。释放期间角色无技能动画表现，奇匠可自定义空动画槽位时长，并通过节点图事件轨道触发角色操控技能节点图实现各种战斗逻辑（如开火发射子弹）。

### 2.教学内容

**功能效果：** 为载具小车装备专属操控技能，驾驶小车时可按下“技能E”按键，向前方发射可造成伤害的子弹，长按“技能Q”会离开小车。

**效果演示：**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/de38e599-da87-4311-990b-df18448439cf.gif)

### 3.目标拆解

## 功能逻辑

以下为制作完整的【载具操控技能】所需的功能点，课程中将根据这些功能点进行组合讲解：



制作可发射的子弹投射物



制作载具小车的角色操控技能（发射子弹和长按按键下船技能）



将操控技能装配到载具小车并试玩

#### 1.制作可发射的子弹投射物

**操作步骤**

**a)【局内编辑器】新建本地投射物元件**

创建一个本地投射物作为子弹（课程以空物件为例），在![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/0e0419ac-891e-4f89-84a9-f9572faec5b7.png)战斗面板中点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/5d03fc20-e96e-4650-9ca2-b204d84ae232.png)>>>进入本地投射物，点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/580c3612-f379-4890-99b8-26040ce10961.png)即可添加。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/31cf770d-752a-4638-bdf5-c366d3777ed5.png)

**b)【局内编辑器】设置本地投射物参数**

创建好本地投射物元件后，我们需要定义投射物的相关参数，具体的功能和对应配置项见下表：

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 子弹不会与载具小车挤压碰撞 | 【原生碰撞】关闭初始生效 |
| 子弹不会因为飞行过远/高而消失 | 【生命周期设置】-【X分量/Z分量轴销毁距离(m)】和【Y分量轴销毁距离(m)】设置为“100.00” |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/eac7e622-a584-4d99-92cf-5ef7ee8b8260.png)

_\*\*以上数值为演示示例，实际使用可根据具体需求调整_

**c)【局内编辑器】本地投射物组件设置**

在本地投射物组件设置中，为达到预期的功能效果课程中配置如下：

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 子弹外观表现为特效“黄色球形光晕” | 【特效】组件选择循环特效，挑选“黄色球形光晕”资产 |
| 子弹运动轨迹为抛物线投射 | 【投射运动器】-【投射物类型】为“抛物线投射”，同时将Y轴速度调整为“6.00”，将Z轴速度调整为“30.00” |
| 子弹有命中判定，对进入判定区的每个对象发起命中事件，子弹创建时不立即检测，以免将自身纳入判定范围。 | 【命中检测】-配置和特效宽度一致的命中区域；<br>【触发类型】调整为不重复触发；<br>【延迟检测】调整为“0.50” |
| 子弹命中其他对象后，调用能力单元发起攻击 | 【能力单元】创建“直接攻击”能力单元，配置伤害数值 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/d8eb4709-c0a6-4612-a58f-bec7379461b8.png)

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/221922e8-0f11-4788-8dad-2c3c3791bf59.png)

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/61cebf83-b73d-4b66-bdf7-b0f0e78df1a2.png)

_\*\*以上数值为演示示例，实际使用可根据具体需求调整_

#### 2.制作载具小车的角色操控技能

**操作步骤**

**a)【局内编辑器】新建角色操控技能**

进入【战斗预设】，选择![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/99628dd7-dfd6-4476-9868-a9225e928d5d.png)>>>进入技能页，点击【角色操控技能】页签>>>新建技能![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/4053e3ec-5e42-4de7-b5df-80f807d5a77a.png)>>>设置技能名称，即可添加（同理，再次新建一个技能，命名为“离开载具”，用于后续配置下车逻辑）

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/3c2ef83a-44b3-4109-a679-c69d8114ec3f.gif)

**b)【局内编辑器】配置技能基础参数与数值**

在技能参数面板中配置技能基础信息与冷却属性：

|     |     |
| --- | --- |
| 要做的功能 | 对应的配置项 |
| 设置【发射子弹】技能类型 | 【技能类型】选择“瞬发技能” |
| 设置【离开载具】技能类型 | 【技能类型】选择“长按技能” |
| 设置技能冷却时间 | 【数值配置】中修改冷却时间为“5.00”秒 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/fd7ff089-114c-4aa8-9f5a-6b37ac2163e4.png)

**c)【千星沙箱】配置开火发射子弹逻辑和离开载具小车逻辑**

打开【客户端节点图资源管理器-角色操控技能节点图】，新建一个角色操控技能节点图，配置如下：

|     |     |     |     |
| --- | --- | --- | --- |
|  |  | 要做的功能 | 对应的配置项 |
| 功能 技能触发时发射子弹 | 触发场景 | 技能触发 | 【事件节点】：节点图开始 |
|  | 条件 | / | / |
| 结果 | 在载具小车位置发射子弹投射物 | 【查询节点】：获取实体位置/旋转；<br>【执行节点】：顶点发射投射物，填入子弹元件ID并设置投射物阵营 |
| 功能 技能长按后离开载具小车 | 触发场景 | 技能长按 | 【事件节点】：节点图开始 |
|  | 条件 | / | / |
| 结果 | 角色退出并停止激活载具小车 | 【执行节点】：设置玩家离开并停止激活载具小车操控运动器 |

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/56e19497-b614-4d20-b2a5-012f23e0850c.png)

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/d9cb31e1-84ef-423e-ad61-730a4b348595.png)

_\*\*上述节点图挂载在角色操控技能对应【动画编辑-事件轨道】上_

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/76c279ea-3550-49cc-b47d-0b2a4fa2acbc.png)

#### 3.将操控技能装配到载具小车并试玩

**操作步骤**

**a)【局内编辑器】为载具小车绑定操控技能**

进入【战斗预设】>>>点击![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/aab39e78-5b46-4dce-8ac1-57772a726088.png)进入玩家模板页签>>>选择![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/a594ca8a-7f42-46f7-a619-dc29405e3b1b.png)>>>在技能设置-主动技能中添加制作好的角色操控技能“发射子弹”和“离开载具”

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/651c24f9-ba47-47a4-8a8d-44532a12b19d.gif)

**b)【局内编辑器】放置载具小车与标靶，进入试玩**

将小车与受击标靶拖入场景中，进入试玩驾驶小车并按下技能按键“E”，成功发射子弹并命中目标；长按技能按键“Q”即可离开载具小车。

![](https://act-webstatic.mihoyo.com/ugc-tutorial/course/cn/zh-cn/mhu0mc0r40jc/32ef0586-b8db-4be5-9350-306ffe897a8d.gif)

_\*\*更多相关信息可自行查阅【综合指南-角色操控技能】_

* * *

# 课程总结及辅助课件

**课程作业：** 可根据课程教学内容尝试进行以下功能复刻/拓展

> 功能复刻：制作一辆具备独立前进/倒车加速度，且能通过按键施放减速冲击波技能的操控小车。

**课程回顾：** 学会如何通过操控运动器组件配置载具碰撞、接地与轮胎偏转效果，并学会通过角色操控技能及节点图为操控载具扩展丰富的战斗开火能力。

### 辅助课件

我们提供了上述课程内容相关的工程文件，可结合 **【教学存档-操控运动器与角色操控技能】** 对照学习

![](https://webstatic.mihoyo.com/upload/static-resource/2022/10/14/64e71b8a5e28fbdbc3d3df5d311e4154_847866555738962172.svg)

操控运动器与角色操控技能.gil

89.8 KB