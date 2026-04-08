---
id: mhapp3r8gkdq
title: 关键行为
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhapp3r8gkdq
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhapp3r8gkdq
description: undefined
language: zh
scope: guide
crawledAt: 2026-04-08T02:16:33.371Z
---

# 一、关键行为的定义

_关键行为_是一种纯客户端的数据，奇匠可以在技能施放的过程中主动通过节点图进行定义并记录，系统会将记录的关键行为列表和其触发的客户端时间保存在_关键行为记录板_内，并可以通过节点图获取已记录的关键行为列表

关键行为可以视为一个简化的指令序列，奇匠可以基于此实现有时效性需求的技能连段或者组合技能

# 二、关键行为的基础概念介绍

_关键行为ID_：关键行为的唯一标识，在节点图调用时依赖该ID

_客户端时间_：添加时在客户端的时间

# 三、使用节点图设置关键行为

添加关键行为

清空关键行为记录板

获取当前关键行为

获取当前关键行为(高精度)

客户端时间受到浮点数精度的影响，如果需要更高的精度则推荐使用高精度版本的节点