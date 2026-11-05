---
id: mh3lmk9tmrky
title: 战斗文字提示过滤器
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh3lmk9tmrky
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh3lmk9tmrky
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:43:20.106Z
---

# 一、战斗文字提示过滤器的功能

战斗文字提示过滤器可以屏蔽玩家看到的战斗文字提示或修改文字大小

只有玩家实体可以添加该组件

该组件支持配置多个过滤器模板，但同时只能生效一个过滤器模板

# 二、战斗文字提示过滤器的编辑

## 1.添加组件

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3lmk9tmrky/06f45708-fb2d-4538-b5b6-ac9579539b4f.png)

(1)在玩家编辑界面中，打开组件编辑页签

(2)点击下方的"添加通用组件"，选择并点击“战斗文字提示过滤器”

(3)点击“详细编辑”，展开编辑页

## 2.详情编辑

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3lmk9tmrky/13057dae-0c2f-4c10-959f-cc06947ca86c.png)

_过滤器模板序号_：每个过滤器模板可以包含多个过滤器，可通过节点切换正在生效的过滤器模板

_过滤器名称_：该过滤器模板的名称

_释放者实体_：指本次行为的释放者

_目标实体_：指本次行为的目标

_释放者的拥有者_：指释放者实体的最上层拥有者，若无拥有者，则为释放者实体

_目标的拥有者_：指目标实体的最上层拥有者，若无拥有者，则为目标实体

_字号调整上限_：运行时字体大小有上限，若达到上限，则会按照字号上限显示

筛选条件备注：

a.友善阵营：指除自身阵营外的所有友善阵营

b.实体标签包含：指包含所有选出的标签时生效

c.实体标签不包含：指包含任意选出的标签时不生效

# 三、通过节点图管理战斗文字提示过滤器

切换战斗文字提示过滤模板

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh3lmk9tmrky/55a83858-f165-46a1-a9cf-1d83e1dc6117.png)