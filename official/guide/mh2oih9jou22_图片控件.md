---
id: mh2oih9jou22
title: 图片控件
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2oih9jou22
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2oih9jou22
description: undefined
language: zh
scope: guide
crawledAt: 2026-08-12T17:37:26.849Z
---

# 一、图片的功能

_图片_可以配置在界面布局中，并在界面布局中显示对应的图片，是用于美化、丰富表现而使用的一种界面控件

在关卡运行中，可通过节点图唤起图片控件

# **二、图片的编辑**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/efe4f077-36ff-4639-98f0-df8583c450a8.png)

## **1.添加图片**

在_界面控件组编辑窗口_，添加界面控件模板-图片

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/db9bd0a4-d658-4e99-bfb6-5fcd77dab95f.png)

## 2.图片设置

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/2cae5a53-4604-4c93-a625-d29b0f606efe.png)

|     |     |
| --- | --- |
| 配置参数 | 说明 |
| _图片源_ | 枚举，支持配置静态引用、动态引用、道具、状态、技能、单位状态<br>根据选择不同，影响后续配置参数 |

### **(1)当图片源配置为静态引用时**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/ea398b37-480e-4ba0-b0b9-be90bb1bf84b.png)

_引用素材资产：_选择预设素材，部分素材支持配置颜色

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/1c1d9706-a659-4824-bfd7-4b6afcbb2931.png)

_填充颜色：_图片资产分为单色和彩色两类，可以通过选色器修改资产的颜色，单色的资产在修改颜色时具有更好的表现

_图片类型：_支持配置基础、拉伸。部分图片资产具有拉伸属性，可以通过图片资产库中的筛选项进行查找

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/0998253a-1f58-4d09-9f16-569236f3e974.png)

|     |     |     |
| --- | --- | --- |
| 图片属性 | 特性 | 常见用途 |
| _普通_ | 图片拉伸时四角会跟随形变 | 拼接特定形状或基础图案 |
| _三宫格_ | 图片在横向或纵向的其中一个方向拉伸时，四角会维持原有的形状不变 | 自定义样式的按钮，页签项等控件的底板图片 |
| _九宫格_ | 图片在横向或纵向拉伸时，四角都会保持原有的形状不变 | 单选项视窗中列表项底板，或页签，单选项视窗等控件的背景图片 |

### **(2)当图片源配置为其他类型时**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/867f91fa-c984-4c6b-973d-4b96371bf69c.png)

支持奇匠配置自定义变量，作为对应图片的标识使用

### **(3)** 图片控件的颜色配置

所有图片源类型均支持配置颜色

注：若为素材组，则无法被填充颜色

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2oih9jou22/323156cf-c9f9-46f4-a45b-3a9e7398ad50.png)