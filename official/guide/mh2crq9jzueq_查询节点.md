---
id: mh2crq9jzueq
title: 查询节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2crq9jzueq
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh2crq9jzueq
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:49:45.498Z
---

# **一、列表相关**

## **1\. 获取列表对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/872526d3-ab5f-4727-a977-e68a4fd3d9be.undefined)

**节点功能**

返回列表中指定序号对应的值。列表中序号从0开始

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 序号 | 整数 |  |
| 入参 | 数据列表 | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **2\. 获取列表长度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/524c4280-7958-4d34-bcbb-28d09497d34b.undefined)

**节点功能**

获取列表长度（列表中的元素个数）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入列表 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **3\. 列表是否包含该值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/4ac136e5-699a-4d08-8aa6-d2f7c2709674.undefined)

**节点功能**

返回列表中是否包含指定值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 值 | 泛型 |  |
| 入参 | 列表 | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **4\. 获取列表最大值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9a41b4de-36f0-44d8-9010-da9d7512bf24.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最大值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最大值 | 泛型 |  |

## **5\. 获取列表最小值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/06225683-c2e4-470f-9e34-8323451b6af4.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最小值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最小值 | 泛型 |  |

## **6\. 获取实体类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/aa47f593-5f98-4069-b3a2-fef0d1bc30af.undefined)

**节点功能**

将所需的实体类型拼装为一个列表。类型分为关卡、物件、玩家、角色、造物

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

## **7\. 获取射线筛选类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/b4d83c06-c587-4d03-9d5c-2289f18ee7a2.undefined)

**节点功能**

将所需的射线筛选类型拼装为一个列表。可筛选项有受击盒、场景、物件自身碰撞

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

# **二、自定义变量**

## **1\. 获取自定义变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9f19b53e-e732-4665-a168-03cd7f02ee8d.undefined)

**节点功能**

获取目标实体的指定自定义变量的值

如果变量不存在，则返回类型的默认值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 变量名 | 字符串 |  |
| 出参 | 变量值 | 泛型 |  |

# **三、预设状态**

## **1\. 获取预设状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/a810d240-928b-4481-a90d-0be21922d0c7.undefined)

**节点功能**

获取指定实体的预设状态值。如果该实体没有指定的预设状态，则返回0

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 入参 | 预设状态索引 | 整数 |  |
| 出参 | 预设状态值 | 整数 |  |

# **四、实体相关**

## **1\. 以GUID查询实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/50b41d88-74e2-4a5c-a327-f32fd9668894.undefined)

**节点功能**

根据GUID查询实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | GUID | GUID |  |
| 出参 | 实体 | 实体 |  |

## **2\. 获取实体位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/063d05ec-5a9d-454d-99b5-851e26a167fc.undefined)

**节点功能**

获取指定实体的位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 位置 | 三维向量 |  |

## **3\. 获取实体旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/90f7c8f3-8859-43b0-b570-04006169f1cd.undefined)

**节点功能**

获取指定实体以欧拉角表示的旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 旋转 | 三维向量 |  |

## **4\. 获取自身实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/81d1f69b-e777-4a3d-b773-eaffbfba29a8.undefined)

**节点功能**

返回该节点图所关联的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 自身实体 | 实体 |  |

## **5\. 获取目标实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9093568a-6fad-49e2-afab-badb75be326d.undefined)

**节点功能**

获取目标实体，根据过滤器节点图被引用的功能模块不同，其指代含义会有区别

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 目标实体 | 实体 |  |

## **6\. 筛选球体范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/ee841fbe-1237-438d-a703-aa55a0a51ac7.undefined)

**节点功能**

以特定的规则和数量上限筛选在球形范围内的实体，满足条件的实体会组成实体列表输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 半径 | 浮点数 |  |
| 入参 | 中心位置 | 三维向量 |  |
| 入参 | 筛选数量上限 | 整数 |  |
| 入参 | 筛选规则 | 枚举 | 分为默认排序、随机排序、从近到远排序 |
| 出参 | 筛选结果 | 实体列表 |  |

## **7\. 筛选方形范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/2c467fec-7c19-4714-8e1f-07834f3539eb.undefined)

**节点功能**

以特定的规则和数量上限筛选在方形范围内的实体，满足条件的实体会组成实体列表输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 宽度 | 浮点数 |  |
| 入参 | 高度 | 浮点数 |  |
| 入参 | 长度 | 浮点数 |  |
| 入参 | 中心位置 | 三维向量 |  |
| 入参 | 筛选数量上限 | 整数 |  |
| 入参 | 筛选规则 | 枚举 | 分为默认排序、随机排序、从近到远排序 |
| 出参 | 筛选结果 | 实体列表 |  |

## **8\. 获取实体的类型**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/28e76f47-d045-4bc0-b0fc-fc09b845e1d5.undefined)

**节点功能**

获取指定实体的类型

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 实体类型 | 枚举 |  |

## **9\. 获取单位攻击目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/56a6d3cf-e65c-482b-91ee-73d478b3c38e.undefined)

**节点功能**

获取单位实体当前正在攻击的目标实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位实体 | 实体 |  |
| 出参 | 攻击目标实体 | 实体 |  |

## **10\. 获取目标挂接点位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/6ab91e92-ac34-465b-a285-02daa9f48bc4.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点位置 | 三维向量 |  |

## **11\. 查询实体是否在场**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9c107216-aa70-4c21-bec4-c144501dd455.undefined)

**节点功能**

查询指定实体是否在场

注意角色实体即使处于倒下状态，仍然认为在场

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 是否在场 | 布尔值 |  |

## **12\. 查询复杂造物的预设状态值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/a97e4217-5521-4588-b834-769c2576decf.undefined)

**节点功能**

查询目标造物对应预设状态索引下的预设状态值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标造物 | 实体 |  |
| 入参 | 预设状态索引 | 整数 |  |
| 出参 | 预设状态值 | 整数 |  |

# **五、阵营相关**

## **1\. 查询实体阵营**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/396c3e79-89e9-4478-805c-c2efac8ccf23.undefined)

**节点功能**

查询目标实体的阵营

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 阵营 | 阵营 |  |

## **2\. 查询阵营是否敌对**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/16836c27-41fc-4a5b-857a-da7283786926.undefined)

**节点功能**

查询阵营1和阵营2是否敌对

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 阵营1 | 阵营 |  |
| 入参 | 阵营2 | 阵营 |  |
| 出参 | 是否敌对 | 布尔值 |  |

# **六、玩家与角色相关**

## **1\. 获取指定玩家的角色实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/cbdc0f9b-7185-4801-acad-6aabe3f841ac.undefined)

**节点功能**

获取指定玩家实体的角色实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色实体 | 实体 |  |

## **2\. 获取角色归属的玩家实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/f02e8d35-b94f-4dbc-8855-a55396fcd2b8.undefined)

**节点功能**

获取角色实体所归属的玩家实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角色实体 | 实体 |  |
| 出参 | 所属玩家实体 | 实体 |  |

## **3\. 获取在场玩家实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/2cacfb51-2af2-4c7d-b3c2-9176fa0b52bc.undefined)

**节点功能**

获取在场所有玩家实体组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 玩家实体列表 | 实体列表 |  |

## **4\. 以实体查询GUID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/45cfb07a-de09-4e9a-a4e3-cbf61aaa747a.undefined)

**节点功能**

查询指定实体的GUID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | GUID | GUID |  |

## **5\. 查询自身是否已入战**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/c02b34ad-2cf5-4e8b-98d0-c3287eef3b09.undefined)

**节点功能**

查询该节点图关联的实体是否入战

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否入战 | 布尔值 |  |

## **6\. 获取当前角色**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/7defe497-d0a4-4aac-8f15-6118eb2c3bfb.undefined)

**节点功能**

获取该玩家客户端当前控制的角色实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 角色实体 | 实体 |  |

## **7\. 获得玩家客户端输入设备类型**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9e3ff04e-0b1b-441f-b35f-b7740934fb1e.undefined)

**节点功能**

获得玩家的客户端输入设备类型，根据用户界面的映射方式决定

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 输入设备类型 | 枚举 | 分为键盘鼠标、手柄、触屏 |

## **8\. 获取玩家移动输入**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/cdb7be60-ad7d-4deb-9e7a-9bb472ca93d7.undefined)

**节点功能**

获取当前客户端玩家移动的输入方向和输入力度

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 输入方向 | 浮点数 |  |
| 出参 | 输入力度 | 浮点数 |  |

## **9\. 查询技能变量对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/967a42ee-45b1-40e6-b75e-3f6f46a08180.undefined)

**节点功能**

根据技能变量配置ID查询对应的变量值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能变量配置ID | 配置ID |  |
| 出参 | 变量值 | 浮点数 |  |

## **10\. 获取当前关键行为**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/c2e4ecb1-3ee6-4ca7-954a-9d5c772801a1.undefined)

**节点功能**

获取当前关键行为记录板上所有的关键行为ID以及对应的录入时间

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 行为ID列表 | 整数列表 |  |
| 出参 | 录入时间列表 | 浮点数列表 |  |

## **11\. 获取当前关键行为（高精度）**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9ea4925a-2b0f-4eb3-9df2-f3b1fc88a5e0.undefined)

**节点功能**

获取当前关键行为记录板上所有的关键行为ID以及对应的录入时间，由于浮点数的精度问题，想要获取更高精度的录入时间应该选用此节点

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 行为ID列表 | 整数列表 |  |
| 出参 | 录入时间列表（s） | 整数列表 |  |
| 出参 | 录入时间列表（ms） | 整数列表 |  |

## **12\. 获取当前客户端时间**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/97c6f2bb-0594-4e4a-b481-c233865aaea6.undefined)

**节点功能**

获取当前客户端的时间

如需对玩家展示节点内容，奇匠应在简介等处提前告知玩家获取客户端时间后的相关效果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 客户端时间 | 浮点数 |  |

## **13\. 获取当前客户端时间（高精度）**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/50124c66-995a-4920-98f1-2cc6f5e2affa.undefined)

**节点功能**

获取当前客户端的时间，由于浮点数的精度问题，想要获取更高精度的客户端时间应该选用此节点

如需对玩家展示节点内容，奇匠应在简介等处提前告知玩家获取客户端时间后的相关效果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 客户端时间（s） | 整数 |  |
| 出参 | 客户端时间（ms） | 整数 |  |

## **14\. 查询玩家是否正在语音聊天**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/80adea05-bfdf-48f7-bdb0-6a76aa64d6dc.undefined)

**节点功能**

当检测到该玩家客户端有麦克风输入时，会返回是

注意该节点必须在多人游戏(多人试玩、多人正式游玩)中逻辑才会生效，单人游戏(单人试玩、单人正式游玩)均不会生效

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 是否正在语音 | 布尔值 |  |

## **15\. 根据技能实例ID获取技能配置ID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/346a5d3e-c9f1-4c1e-b794-853feec4065e.undefined)

**节点功能**

根据技能实例ID获取对应的技能配置ID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能实例ID | 整数 |  |
| 出参 | 技能配置ID | 配置ID |  |

## **16\. 查询指定槽位的技能实例列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/13be226e-6c4a-4dab-bb8c-dbc030e5d41c.undefined)

**节点功能**

查询指定槽位的所有技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 出参 | 技能实例ID列表 | 整数列表 |  |

## **17\. 查询指定槽位当前生效的技能实例**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/88e9359b-4e4c-47b9-a0dc-99c9a15c30dc.undefined)

**节点功能**

查询指定槽位当前位于前台的技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 出参 | 技能实例ID | 整数 |  |

## **18\. 以技能槽位和技能配置ID查询技能实例ID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/61194c89-e679-452d-a9c1-949d531405f0.undefined)

**节点功能**

根据技能槽位和技能配置ID查询对应的技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 入参 | 技能配置ID | 配置ID |  |
| 出参 | 技能实例ID | 整数 |  |

## **19\. 获取玩家的角色列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/9aebaefd-5625-43cb-b9d9-bb54a229859f.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的角色列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色列表 | 实体列表 |  |

## **20\. 获取指定玩家的前台角色**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/891eb14f-b9b7-459e-98b8-82e979477eb0.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的前台角色

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色实体 | 实体 |  |

## **21\. 查询经典模式角色编号**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/4e338670-7540-4f36-b585-14afe9af8a42.undefined)

**节点功能**

仅经典模式可用，查询目标角色的角色编号，可以查看附录对应具体是哪位角色 [经典模式角色编号一览](https://act.mihoyo.com/ys/ugc/tutorial//detail/mh4imrrhzdzi)

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标角色 | 实体 |  |
| 出参 | 角色编号 | 整数 |  |

# **七、预瞄准**

## **1\. 获取指定预瞄准的基准对象**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/d112e49c-d6cf-48b5-9db7-78db0951b5a0.undefined)

**节点功能**

获取指定预瞄准序号的基准对象，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 基准对象 | 实体 |  |

## **2\. 获取预瞄结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/92af40da-770a-4004-932a-4c5148013dfe.undefined)

**节点功能**

获取指定预瞄准的命中位置、范围内位置、最优合法目标与合法目标列表，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 命中位置 | 三维向量 |  |
| 出参 | 范围内位置 | 三维向量 |  |
| 出参 | 最优合法目标 | 实体 |  |
| 出参 | 合法目标列表 | 实体列表 |  |

## **3\. 获取预瞄持续时长**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/8c4e9b0c-801d-4b1f-9d2d-b525420e6764.undefined)

**节点功能**

获取指定预瞄准已经持续的时长（秒），仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 持续时长（s） | 浮点数 |  |

## **4\. 获取当前生效的预瞄准序号**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/7b22dd5e-0b66-4211-a22f-3e468aec2554.undefined)

**节点功能**

获取当前技能上下文中正在生效的预瞄准序号，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 预瞄准序号 | 整数 |  |

## **5\. 获取预瞄碰撞检测结果数量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/04285425-3b51-4fe0-844f-0cacd61d853b.undefined)

**节点功能**

获取指定预瞄准的碰撞检测结果数量，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 结果数量 | 整数 |  |

## **6\. 获取预瞄射线命中信息**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/2d8f9358-12e6-4c31-acb5-bd0bab0bc3a2.undefined)

**节点功能**

获取指定预瞄准的射线命中信息，包含命中位置与命中实体，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 命中位置 | 三维向量 |  |
| 出参 | 命中实体 | 实体 |  |

## **7\. 获取预瞄准摇杆是否处于死区**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/f2de4151-fbcd-4952-aa83-165305151527.undefined)

**节点功能**

获取指定预瞄准的输入摇杆是否处于死区，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 入参 | 获取类型 | 枚举 |  |
| 出参 | 是否处于死区 | 布尔值 |  |

## **8\. 查询预瞄准结束原因**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/bbff51fe-1b74-4415-839e-b2821a2d5b2a.undefined)

**节点功能**

查询指定预瞄准的结束原因（无/完成/取消），仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 结束原因 | 枚举 |  |

# **八、光标**

## **1\. 获取光标是否激活**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/711ad333-b25d-45cd-baff-17de3c22ba11.undefined)

**节点功能**

获取本机持久光标是否处于激活状态，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否激活 | 布尔值 |  |

## **2\. 获取光标命中结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/c817709b-10ca-4f38-a407-2bee2b422145.undefined)

**节点功能**

获取本机持久光标的命中结果，包含命中实体列表、命中位置列表与命中数量，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 命中实体列表 | 实体列表 |  |
| 出参 | 命中位置列表 | 三维向量列表 |  |
| 出参 | 命中数量 | 整数 |  |

## **3\. 获取光标屏幕坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/48db6827-34c3-4f4b-91a3-c19adf6d4e32.undefined)

**节点功能**

获取本机持久光标的屏幕坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

## **4\. 获取光标视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/fd9bba8b-5aaa-4a32-99ee-295c07355ba2.undefined)

**节点功能**

获取本机持久光标的视口坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 视口X | 浮点数 |  |
| 出参 | 视口Y | 浮点数 |  |

# **九、挂接点**

## **1\. 获取目标挂接点旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/a50df29b-3d38-4e2a-bf2f-e0e8c58b99b0.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点旋转 | 三维向量 |  |

# **十、触发器**

## **1\. 获取碰撞触发器内所有实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/2cb7003d-e40e-4179-9d73-9e77ee0eee11.undefined)

**节点功能**

获取目标实体上碰撞触发器组件中特定序号对应的碰撞触发器内的所有实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 触发器序号 | 整数 |  |
| 出参 | 实体列表 | 实体列表 |  |

# **十一、射线**

## **1\. 获取射线检测结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/23702f32-d6ca-46bc-b54f-927e4bcdfce8.undefined)

**节点功能**

获取射线检测结果，会根据射线命中从近到远的顺序返回满足筛选条件的第一个目标或命中位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 检测发起者实体 | 实体 |  |
| 入参 | 出射位置 | 三维向量 |  |
| 入参 | 出射方向 | 三维向量 |  |
| 入参 | 射线最大长度 | 浮点数 |  |
| 入参 | 阵营筛选 | 枚举 |  |
| 入参 | 实体类型筛选 | 枚举列表 | 分为关卡、物件、玩家、角色、造物 |
| 入参 | 命中层筛选 | 枚举列表 | 分为受击盒、场景、物件自身碰撞 |
| 出参 | 命中位置 | 三维向量 |  |
| 出参 | 命中实体 | 实体 |  |

# **十二、扫描**

## **1\. 获取扫描组件当前扫描到的实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/f8d66410-66d3-427b-85a6-50d7fd38d99c.undefined)

**节点功能**

获取扫描组件当前扫描到的实体，指扫描状态为“激活状态”的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 对应实体 | 实体 |  |
| 出参 | 扫描标签配置ID | 配置ID |  |

## **2\. 获取扫描组件可扫描的所有合法对象**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/579285d0-6824-465f-910f-349b3cd196e4.undefined)

**节点功能**

获取扫描组件可扫描的所有合法对象，此处的合法对象指代所有携带扫描组件且过滤器返回为“是”的单位，与单位的可扫描状态无关

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 对象列表 | 实体列表 |  |

## **3\. 获取实体扫描状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/8ca8ee7d-0b2d-481b-b071-c5c2bd42ef55.undefined)

**节点功能**

获取实体扫描状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 扫描状态 | 枚举 | 分为不可见、当前扫描目标、候选目标、不满足条件 |

## **4\. 获取实体当前生效的扫描标签**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/2a20f161-dd03-4d28-93ff-07911d66d4b5.undefined)

**节点功能**

获取目标实体当前生效的扫描标签

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 扫描标签配置ID | 配置ID |  |

# **十三、字典**

## **1\. 以键查询字典值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/00c46316-1012-4e82-8cd1-9683aefc81a5.undefined)

**节点功能**

根据键查询字典中对应的值，如果键不存在，则返回类型默认值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 入参 | 键 | 泛型 |  |
| 出参 | 值 | 泛型 |  |

## **2\. 查询字典是否包含特定键**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/cacb420d-4ca6-473a-9602-de01fc70ec00.undefined)

**节点功能**

查询指定字典是否包含特定的键

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 入参 | 键 | 泛型 |  |
| 出参 | 是否包含 | 布尔值 |  |

## **3\. 查询字典是否包含特定值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/c4d158c4-a931-440b-8555-cad239ed065c.undefined)

**节点功能**

查询指定字典是否包含特定的值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 入参 | 值 | 泛型 |  |
| 出参 | 是否包含 | 布尔值 |  |

## **4\. 查询字典长度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/6f3b1bef-af8c-4caf-a7a1-efe00c210218.undefined)

**节点功能**

查询字典中键值对的数量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **5\. 获取字典中值组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/084ad873-5b29-4c48-b3dc-bd711ab76327.undefined)

**节点功能**

获取字典中所有值组成的列表。由于字典中键值对是无序排列的，所以取出的值列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 值列表 | 泛型 |  |

## **6\. 获取字典中键组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/b148c904-1bf7-49a4-bc1f-be463e86dcb3.undefined)

**节点功能**

获取字典中所有键组成的列表。由于字典中键值对是无序排列的，所以取出的键列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 键列表 | 泛型 |  |

# **十四、单位状态**

## **1\. 实体是否携带指定单位状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh2crq9jzueq/be211d7f-124d-404b-8c4f-2cc9b79cc781.undefined)

**节点功能**

查询目标实体是否携带指定的单位状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 单位状态 | 配置ID |  |
| 出参 | 是否携带 | 布尔值 |  |