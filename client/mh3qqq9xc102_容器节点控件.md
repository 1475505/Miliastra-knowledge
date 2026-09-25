---
id: mh3qqq9xc102
title: 容器节点控件
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh3qqq9xc102
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh3qqq9xc102
description: undefined
language: zh
scope: client
crawledAt: 2026-09-25T17:54:09.605Z
---

# 一、容器节点控件的功能

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3qqq9xc102/2c738ac8-99d7-4276-b809-f700d078afcb.png)

主要作为其他客户端控件的挂点，可以使光标常驻显示、屏蔽按键和点击事件

容器节点控件是客户端控件，可以挂载_客户端脚本_，支持通过_客户端脚本_进行调用

查询接口：可通过`ContainerControl`在API文档里查询关联脚本接口

# 二、容器节点控件的配置

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3qqq9xc102/e23de4f3-6d66-48f8-bbc9-a1af48ee5be7.png)

## 1.功能设置

_隔离手柄导航：_手柄按照距离最近控件导航时，内外相互不穿透

_屏蔽按键事件穿透：_容器节点内的按键事件交互不会穿透到界面外

_屏蔽区域内光标事件穿透：_容器节点内的点击事件不会穿透到界面外

_显示常驻光标：_使光标常驻显示

## 2.手柄导航

- _可被手柄摇杆导航选中：_控制手柄导航是否可选中此控件

开启后可编辑手柄四向移动时选中的其他控件

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3qqq9xc102/a7da7d77-051d-4136-963d-7d067cf47353.png)
