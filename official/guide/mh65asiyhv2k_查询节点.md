---
id: mh65asiyhv2k
title: 查询节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh65asiyhv2k
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh65asiyhv2k
description: undefined
language: zh
scope: guide
crawledAt: 2026-07-01T08:27:15.813Z
---

# **一、列表相关**

## **1\. 获取列表对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2ee6733e-4d8e-4fac-96f7-f82568e952f4.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/aca32e25-c5a9-4492-8172-e665ccf40d76.undefined)

**节点功能**

获取列表长度（列表中的元素个数）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入列表 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **3\. 获取列表最大值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7162a170-e3cd-44cd-8efb-5beba0da4dd3.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最大值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最大值 | 泛型 |  |

## **4\. 获取列表最小值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/733ec56c-5d9a-4d75-a507-2e2778aa8d16.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最小值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最小值 | 泛型 |  |

## **5\. 获取实体类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/68b5138a-43fb-4819-86bf-be6bbcaff362.undefined)

**节点功能**

将所需的实体类型拼装为一个列表。类型分为关卡、物件、玩家、角色、造物

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

## **6\. 列表是否包含该值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/a62174be-ca80-48e8-b4ef-2905dbac6050.undefined)

**节点功能**

返回列表中是否包含指定值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 值 | 泛型 |  |
| 入参 | 列表 | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **7\. 获取射线筛选类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7ad05365-142f-4911-8b9b-3d956364ff98.undefined)

**节点功能**

将所需的射线筛选类型拼装为一个列表。可筛选项有受击盒、场景、物件自身碰撞

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

# **二、自定义变量**

## **1\. 获取自定义变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/6cbf2134-fc94-493b-9fca-04204592d7f1.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/d49e0aba-06ae-45fa-88b4-8bf92417cfa3.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/f4024145-b5c9-473f-abae-5e5f2a832d35.undefined)

**节点功能**

根据GUID查询实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | GUID | GUID |  |
| 出参 | 实体 | 实体 |  |

## **2\. 获取实体位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/8d181603-2ed2-4390-bb74-500e04b28124.undefined)

**节点功能**

获取指定实体的位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 位置 | 三维向量 |  |

## **3\. 获取实体旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/13f9250f-0234-4aee-9d60-ddd22e0fb4b7.undefined)

**节点功能**

获取指定实体以欧拉角表示的旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 旋转 | 三维向量 |  |

## **4\. 获取自身实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/c114caa5-6fb8-461d-9bd3-eae6f903b4fe.undefined)

**节点功能**

返回该节点图所关联的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 自身实体 | 实体 |  |

## **5\. 获取目标实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/860bc841-9bdd-49eb-8b8e-f2e70c3399da.undefined)

**节点功能**

获取目标实体，根据过滤器节点图被引用的功能模块不同，其指代含义会有区别

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 目标实体 | 实体 |  |

## **6\. 获取单位攻击目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/bcdcd010-6f43-4c16-8b27-c090a0c799f0.undefined)

**节点功能**

获取单位实体当前正在攻击的目标实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位实体 | 实体 |  |
| 出参 | 攻击目标实体 | 实体 |  |

## **7\. 获取目标挂接点位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/3e5c075b-0876-4b95-b20a-5cf8490bd67b.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点位置 | 三维向量 |  |

## **8\. 获取目标挂接点旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/3e8b7b57-fe3d-42d9-92b7-a6e1cb71b898.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点旋转 | 三维向量 |  |

## **9\. 获取实体的类型**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/63b55ebd-9243-448e-af8c-440ccfdb578b.undefined)

**节点功能**

获取指定实体的类型

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 实体类型 | 枚举 |  |

## **10\. 筛选球体范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7aa35e28-c360-4dac-bc86-2d3f310ac19a.undefined)

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

## **11\. 筛选方形范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/f423882d-bc0b-47bb-a275-453f2c07f8c8.undefined)

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

## **12\. 查询实体是否在场**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/056dc50b-eb48-4dfe-9892-0a5fe0fbe0bf.undefined)

**节点功能**

查询指定实体是否在场

注意角色实体即使处于倒下状态，仍然认为在场

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 是否在场 | 布尔值 |  |

## **13\. 查询复杂造物的预设状态值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2b451a30-3011-4d89-a538-4085c60e0fbb.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/22a2815f-266d-442a-bbf7-24ab36dd9e64.undefined)

**节点功能**

查询目标实体的阵营

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 阵营 | 阵营 |  |

## **2\. 查询阵营是否敌对**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/bb3c0590-70a3-4106-ab07-181761ce31b5.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/e5086b90-a667-434c-b728-d6c55e23332c.undefined)

**节点功能**

获取指定玩家实体的角色实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色实体 | 实体 |  |

## **2\. 获取角色归属的玩家实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/bf44bc8e-9ebf-4010-88cf-489a0cae6b5d.undefined)

**节点功能**

获取角色实体所归属的玩家实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角色实体 | 实体 |  |
| 出参 | 所属玩家实体 | 实体 |  |

## **3\. 获取在场玩家实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/a3da182c-d646-464a-aae8-b50ef8c157d5.undefined)

**节点功能**

获取在场所有玩家实体组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 玩家实体列表 | 实体列表 |  |

## **4\. 以实体查询GUID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/3028dbb1-ae1c-4c0a-a03a-891be9266793.undefined)

**节点功能**

查询指定实体的GUID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | GUID | GUID |  |

## **5\. 查询自身是否已入战**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/a8541e47-6b34-4cd8-b3ad-b11707d40377.undefined)

**节点功能**

查询该节点图关联的实体是否入战

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否入战 | 布尔值 |  |

## **6\. 获取当前角色**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/4a25da7c-ce78-4335-ba5f-57e6fdfe9344.undefined)

**节点功能**

获取该玩家客户端当前控制的角色实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 角色实体 | 实体 |  |

## **7\. 获得玩家客户端输入设备类型**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/614b494a-6896-4343-87f6-34f6d1fa770f.undefined)

**节点功能**

获得玩家的客户端输入设备类型，根据用户界面的映射方式决定

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 输入设备类型 | 枚举 | 分为键盘鼠标、手柄、触屏 |

## **8\. 获取玩家移动输入**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/263f1859-a643-472f-a003-a5bdaa9ac356.undefined)

**节点功能**

获取当前客户端玩家移动的输入方向和输入力度

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 输入方向 | 浮点数 |  |
| 出参 | 输入力度 | 浮点数 |  |

## **9\. 查询技能变量对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/6fec7dc3-9c3e-4f4f-804e-bc47fa2255c1.undefined)

**节点功能**

根据技能变量配置ID查询对应的变量值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能变量配置ID | 配置ID |  |
| 出参 | 变量值 | 浮点数 |  |

## **10\. 获取当前关键行为**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/6a025692-a386-43f1-89b7-b9a5656331a1.undefined)

**节点功能**

获取当前关键行为记录板上所有的关键行为ID以及对应的录入时间

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 行为ID列表 | 整数列表 |  |
| 出参 | 录入时间列表 | 浮点数列表 |  |

## **11\. 获取当前关键行为（高精度）**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/5a5e22e4-e2a5-4cea-a9f0-1ec398aa257c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7bfc05eb-b251-4933-bf08-74990c9e0620.undefined)

**节点功能**

获取当前客户端的时间

如需对玩家展示节点内容，奇匠应在简介等处提前告知玩家获取客户端时间后的相关效果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 客户端时间 | 浮点数 |  |

## **13\. 获取当前客户端时间（高精度）**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/06b6e5d4-8ef6-4100-b489-7937de7d0bd6.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/e67d7e17-0359-4e2a-a9dc-9b7519f6101e.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2a48d121-299e-47e8-9ff7-7aa60ce05314.undefined)

**节点功能**

根据技能实例ID获取对应的技能配置ID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能实例ID | 整数 |  |
| 出参 | 技能配置ID | 配置ID |  |

## **16\. 查询指定槽位的技能实例列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7254b369-26db-4e2b-993b-dd2111c81df2.undefined)

**节点功能**

查询指定槽位的所有技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 出参 | 技能实例ID列表 | 整数列表 |  |

## **17\. 查询指定槽位当前生效的技能实例**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7bb8f3c0-b725-49e5-9e02-f9e251c270c1.undefined)

**节点功能**

查询指定槽位当前位于前台的技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 出参 | 技能实例ID | 整数 |  |

## **18\. 以技能槽位和技能配置ID查询技能实例ID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/91f58c65-3d68-452f-ad6a-4a40a54e795f.undefined)

**节点功能**

根据技能槽位和技能配置ID查询对应的技能实例

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能槽位 | 枚举 |  |
| 入参 | 技能配置ID | 配置ID |  |
| 出参 | 技能实例ID | 整数 |  |

# **七、预瞄准**

## **1\. 获取指定预瞄准的基准对象**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/25dbe28c-1504-4faa-b44f-ed9ddb2f04e6.undefined)

**节点功能**

获取指定预瞄准序号的基准对象，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 基准对象 | 实体 |  |

## **2\. 获取预瞄结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7c74d146-53ac-4d77-b583-9b11ad380843.undefined)

**节点功能**

获取指定预瞄准的命中位置、范围内位置、最优合法目标与合法目标列表，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 命中位置 | 三维向量 |  |
| 出参 | 范围内位置 | 三维向量 |  |
| 出参 | 最优合法目标 | 实体 |  |
| 出参 | 合法目标列表 | 实体列表 |  |

## **3\. 获取预瞄持续时长**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/eb6d951b-1a0b-4670-881c-5144778a55c6.undefined)

**节点功能**

获取指定预瞄准已经持续的时长（秒），仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 持续时长（s） | 浮点数 |  |

## **4\. 获取当前生效的预瞄准序号**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/5d1f7ddd-d10b-4c70-a440-1cd3950ae50b.undefined)

**节点功能**

获取当前技能上下文中正在生效的预瞄准序号，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 预瞄准序号 | 整数 |  |

## **5\. 获取预瞄碰撞检测结果数量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/673d5ca9-e286-4346-9708-b333e49c321a.undefined)

**节点功能**

获取指定预瞄准的碰撞检测结果数量，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 结果数量 | 整数 |  |

## **6\. 获取预瞄射线命中信息**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/6ad38575-8df8-4cec-aa02-ea3193a7e73c.undefined)

**节点功能**

获取指定预瞄准的射线命中信息，包含命中位置与命中实体，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 命中位置 | 三维向量 |  |
| 出参 | 命中实体 | 实体 |  |

## **7\. 获取预瞄准摇杆是否处于死区**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/3531a1d2-f7ca-4c82-a120-c84340cb72f6.undefined)

**节点功能**

获取指定预瞄准的输入摇杆是否处于死区，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 预瞄准序号 | 整数 |  |
| 出参 | 是否处于死区 | 布尔值 |  |

## **8\. 查询预瞄准结束原因**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/5cc98f4a-a44c-431c-a539-abd6d17268e4.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7d790e46-a2df-4143-b3fd-b49d6de250e3.undefined)

**节点功能**

获取本机持久光标是否处于激活状态，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否激活 | 布尔值 |  |

## **2\. 获取光标命中结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/347073f7-2df6-4781-ace4-e7ca1c0aa512.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/a1761dfb-364f-4e7c-9681-369914e4c8fa.undefined)

**节点功能**

获取本机持久光标的屏幕坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

## **4\. 获取光标视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/9a4a3b72-9c4d-4355-9012-ca944ca91dfe.undefined)

**节点功能**

获取本机持久光标的视口坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 视口X | 浮点数 |  |
| 出参 | 视口Y | 浮点数 |  |

# **九、标签**

## **1\. 获取实体的单位标签列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/b598e8d6-cdfb-4eda-8c03-6781b3212082.undefined)

**节点功能**

获取目标实体上携带的所有单位标签组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 列表 | 整数列表 |  |

## **2\. 获取单位标签的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/1243be4b-d72f-4ed9-856b-ae11c08ca3af.undefined)

**节点功能**

获取在场所有携带该单位标签的实体列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位标签索引 | 整数 |  |
| 出参 | 实体列表 | 实体列表 |  |

# **十、通用**

## **1\. 获取局部变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/361ba32d-45dc-422b-8e15-88718648fc7e.undefined)

**节点功能**

获取特定局部变量的变量值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 变量名 | 字符串 |  |
| 出参 | 变量值 | 泛型 |  |

# **十一、自定义仇恨**

## **1\. 获取指定实体的仇恨目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/1f919a41-bb04-4d42-ac90-0276c324eb17.undefined)

**节点功能**

仅自定义仇恨模式可用

获取指定实体的仇恨目标

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 指定实体 | 实体 |  |
| 出参 | 仇恨目标 | 实体 |  |

## **2\. 获取指定实体的仇恨列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/58b555ab-8c8f-4a91-8a69-5eb9ec8ea2b7.undefined)

**节点功能**

仅自定义仇恨模式可用

获取指定实体的仇恨列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 指定实体 | 实体 |  |
| 出参 | 仇恨列表 | 实体列表 |  |

## **3\. 查询指定实体是否入战**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2e5ef6d9-7569-4c40-8b8a-c9857396cf7a.undefined)

**节点功能**

仅自定义仇恨模式可用

查询指定实体是否已经入战

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 是否入战 | 布尔值 |  |

# **十二、触发器**

## **1\. 获取碰撞触发器内所有实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/f9b1c945-bb01-403b-a221-5733435cd08a.undefined)

**节点功能**

获取目标实体上碰撞触发器组件中特定序号对应的碰撞触发器内的所有实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 触发器序号 | 整数 |  |
| 出参 | 实体列表 | 实体列表 |  |

# **十三、射线**

## **1\. 获取射线检测结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/d1793691-6a34-46e3-a5a1-eb17a68b35d7.undefined)

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

# **十四、扫描**

## **1\. 获取扫描组件当前扫描到的实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/a2470ad4-6af1-42c4-8044-6520bb6e3b0d.undefined)

**节点功能**

获取扫描组件当前扫描到的实体，指扫描状态为“激活状态”的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 对应实体 | 实体 |  |
| 出参 | 扫描标签配置ID | 配置ID |  |

## **2\. 获取扫描组件可扫描的所有合法对象**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2957ea67-35bb-493c-b9e6-885951667ba6.undefined)

**节点功能**

获取扫描组件可扫描的所有合法对象，此处的合法对象指代所有携带扫描组件且过滤器返回为“是”的单位，与单位的可扫描状态无关

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 对象列表 | 实体列表 |  |

## **3\. 获取实体扫描状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/cda8f076-4e58-46c6-b9a2-f9747a1fe947.undefined)

**节点功能**

获取实体扫描状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 扫描状态 | 枚举 | 分为不可见、当前扫描目标、候选目标、不满足条件 |

## **4\. 获取实体当前生效的扫描标签**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/85d7dbbc-26d1-4e05-939c-81751ea93074.undefined)

**节点功能**

获取目标实体当前生效的扫描标签

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 扫描标签配置ID | 配置ID |  |

# **十五、字典**

## **1\. 以键查询字典值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/9d1251e1-f327-4ff1-b846-fd5f0c41701d.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/df98c1ba-7b7e-4fce-b1f8-a6d564d6c19a.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/7fe45b22-9b90-4b54-8a39-797d09abe128.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/2b5e8d9c-8f9f-4254-afc0-98f7380a0774.undefined)

**节点功能**

查询字典中键值对的数量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **5\. 获取字典中值组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/f0665da9-578a-41fd-a6d4-f110555defd6.undefined)

**节点功能**

获取字典中所有值组成的列表。由于字典中键值对是无序排列的，所以取出的值列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 值列表 | 泛型 |  |

## **6\. 获取字典中键组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/c26374de-a28c-42a0-a8f2-e37e74b654ed.undefined)

**节点功能**

获取字典中所有键组成的列表。由于字典中键值对是无序排列的，所以取出的键列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 键列表 | 泛型 |  |

# **十六、单位状态**

## **1\. 实体是否携带指定单位状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/b2e4d197-3282-48c9-91d6-45c309e86233.undefined)

**节点功能**

查询目标实体是否携带指定的单位状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 单位状态 | 配置ID |  |
| 出参 | 是否携带 | 布尔值 |  |

# **十七、操控运动器**

## **1\. 获取当前激活操控运动器列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/4df3ee42-a9ee-4eb5-b93b-1c3f9af38515.undefined)

**节点功能**

获取当前激活操控运动器列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 操控运动器列表 | 实体列表 |  |

## **2\. 获取当前跟随操控运动器**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/4b37f6eb-d33b-4941-90bc-a1137f7d0aa3.undefined)

**节点功能**

获取当前跟随操控运动器

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 跟随操控运动器 | 实体 |  |

## **3\. 获取操控运动器运动参数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/03bc84d8-2f4a-4bbf-976b-e3d530549d33.undefined)

**节点功能**

获取指定操控运动器的运动参数，包含临时运动参数。临时值的添加将在下一帧生效，因此无法在当前执行流中通过获取节点查到值的变化。

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 操控运动器 | 实体 |  |
| 出参 | 前进加速度 | 浮点数 |  |
| 出参 | 后退加速度 | 浮点数 |  |
| 出参 | 转向速率 | 浮点数 |  |
| 出参 | 基础阻力减速度 | 浮点数 |  |
| 出参 | 阻力系数 | 浮点数 |  |
| 出参 | 最大前进速度 | 浮点数 |  |
| 出参 | 最大后退速度 | 浮点数 |  |

## **4\. 获取操控运动器当前速度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/fc409cf5-806c-4e0e-9866-cec94a77d633.undefined)

**节点功能**

获取指定操控运动器的当前速度（速度大小及单位方向向量）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 操控运动器 | 实体 |  |
| 出参 | 速度大小 | 浮点数 |  |
| 出参 | 速度方向 | 三维向量 |  |

## **5\. 获取操控运动器前向**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/06f6e8bf-d39b-4af3-97e0-03db562dc4ca.undefined)

**节点功能**

获取指定操控运动器的前向方向向量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 操控运动器 | 实体 |  |
| 出参 | 前向 | 三维向量 |  |

## **6\. 获取操控运动器目标转向方向**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/84dab105-9b8c-4e4c-b4ce-85f6698bd017.undefined)

**节点功能**

获取操控运动器目标转向方向（移动轮盘输入后，转换成操控运动器的目标转向）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 操控运动器 | 实体 |  |
| 出参 | 目标转向方向 | 三维向量 |  |

## **7\. 获取操控运动器是否接地**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh65asiyhv2k/b36261b6-8e2f-437d-a03d-8a70c5ae6663.undefined)

**节点功能**

获取指定操控运动器当前是否接地

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标操控运动器 | 实体 |  |
| 出参 | 是否接地 | 布尔值 |  |