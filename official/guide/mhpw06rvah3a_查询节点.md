---
id: mhpw06rvah3a
title: 查询节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpw06rvah3a
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpw06rvah3a
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:48:33.289Z
---

# **一、技能**

## **1\. 获取复杂造物当前施放的技能**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/ed7d2923-67ec-47a1-972e-a6dd84453e2f.undefined)

**节点功能**

返回复杂造物当前正在施放的技能的序号

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 技能序号 | 整数 |  |

## **2\. 查询技能变量对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/1170e6b1-9d09-4546-9e15-c4f736af1afd.undefined)

**节点功能**

根据技能变量配置ID查询对应的变量值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 技能变量配置ID | 配置ID |  |
| 出参 | 变量值 | 浮点数 |  |

# **二、列表相关**

## **1\. 获取列表对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/2c21daa4-8add-402d-8f1c-429bddb55dea.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/4a4da6e0-935a-4db9-b6f1-a57cedd7560f.undefined)

**节点功能**

获取列表长度（列表中的元素个数）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入列表 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **3\. 获取列表最大值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/6f5c75dd-a07a-46f3-8190-b6fd512938d8.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最大值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最大值 | 泛型 |  |

## **4\. 获取列表最小值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/26190108-99e7-4dfd-9877-ec88bbea97d3.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最小值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最小值 | 泛型 |  |

## **5\. 获取实体类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a4610d1c-b332-4a80-82cb-1a59a47382e2.undefined)

**节点功能**

将所需的实体类型拼装为一个列表。类型分为关卡、物件、玩家、角色、造物

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

## **6\. 列表是否包含该值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a4675d1b-fdcb-4a8a-8298-f6c998829e41.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/6be0f1f0-0a4c-44a8-9940-e8f650118561.undefined)

**节点功能**

将所需的射线筛选类型拼装为一个列表。可筛选项有受击盒、场景、物件自身碰撞

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

# **三、自定义变量**

## **1\. 获取自定义变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/7afdbe12-e84c-4420-8073-e12d383b5e20.undefined)

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

# **四、预设状态**

## **1\. 获取预设状态**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/b52afacd-7332-469b-b133-4efed727aa3b.undefined)

**节点功能**

获取指定实体的预设状态值。如果该实体没有指定的预设状态，则返回0

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 入参 | 预设状态索引 | 整数 |  |
| 出参 | 预设状态值 | 整数 |  |

# **五、实体相关**

## **1\. 以GUID查询实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/ef8a3f46-fabd-4ec6-85a4-7fb205288367.undefined)

**节点功能**

根据GUID查询实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | GUID | GUID |  |
| 出参 | 实体 | 实体 |  |

## **2\. 获取实体位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/16bfe192-0c25-49cd-bb89-b254c34820d7.undefined)

**节点功能**

获取指定实体的位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 位置 | 三维向量 |  |

## **3\. 获取实体旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/e983a107-ace2-42eb-a309-4f874364ec3b.undefined)

**节点功能**

获取指定实体以欧拉角表示的旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 旋转 | 三维向量 |  |

## **4\. 获取自身实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/3c34d32b-4240-48e0-b850-5c60d6f38ebf.undefined)

**节点功能**

返回该节点图所关联的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 自身实体 | 实体 |  |

## **5\. 获取单位攻击目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/ca556744-1010-4847-bfcc-a010c69d0076.undefined)

**节点功能**

获取单位实体当前正在攻击的目标实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位实体 | 实体 |  |
| 出参 | 攻击目标实体 | 实体 |  |

## **6\. 获取目标挂接点位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/b958998e-4b74-441d-a6da-8790c3c20d58.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点位置 | 三维向量 |  |

## **7\. 获取目标挂接点旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/152bea13-060a-411e-a48a-df9e6eb854e3.undefined)

**节点功能**

获取指定目标实体上对应挂接点名称的挂接点旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 挂接点名称 | 字符串 |  |
| 出参 | 挂接点旋转 | 三维向量 |  |

## **8\. 获取实体的类型**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/94307ff5-e88b-42ad-8dab-8a14c72a2652.undefined)

**节点功能**

获取指定实体的类型

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 实体类型 | 枚举 |  |

## **9\. 筛选球体范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/323bd625-5a83-4cee-b94d-3e1ef6f2eb46.undefined)

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

## **10\. 筛选方形范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/849ac8ba-406d-4e7e-b270-ea64dda05129.undefined)

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

## **11\. 查询实体是否在场**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/7b6735ba-e535-4c3e-b2f9-251ffe9a9926.undefined)

**节点功能**

查询指定实体是否在场

注意角色实体即使处于倒下状态，仍然认为在场

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 是否在场 | 布尔值 |  |

## **12\. 获取子实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/98941078-56de-4c62-9018-a8e9705f311f.undefined)

**节点功能**

返回目标实体的子实体列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 子实体列表 | 实体列表 |  |

## **13\. 获取造物当前目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/d65246f0-50df-4f44-856f-f5b33cf0c08e.undefined)

**节点功能**

返回指定造物当前的目标

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 造物 | 实体 |  |
| 出参 | 目标实体 | 实体 |  |

## **14\. 查询复杂造物的预设状态值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/cf7c93ab-178c-432f-a9e5-1558990ca9fb.undefined)

**节点功能**

查询目标造物对应预设状态索引下的预设状态值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标造物 | 实体 |  |
| 入参 | 预设状态索引 | 整数 |  |
| 出参 | 预设状态值 | 整数 |  |

## **15\. 获取角色归属的玩家实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/8280c889-5dfc-405d-a8b2-1f7155b7cc2c.undefined)

**节点功能**

获取角色实体所归属的玩家实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角色实体 | 实体 |  |
| 出参 | 所属玩家实体 | 实体 |  |

## **16\. 获取在场玩家实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/0dcb03ad-7ecf-48ba-bda5-b3878603abad.undefined)

**节点功能**

获取在场所有玩家实体组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 玩家实体列表 | 实体列表 |  |

## **17\. 以实体查询GUID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/15ec56a8-a5d2-4a05-99e8-13f8d70ec31c.undefined)

**节点功能**

查询指定实体的GUID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | GUID | GUID |  |

## **18\. 获取玩家的角色列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/26197362-6e5f-4cde-9197-bece365f920a.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的角色列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色列表 | 实体列表 |  |

## **19\. 获取指定玩家的前台角色**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/4887d7e0-bba5-4015-8e7e-01f74f9fb39e.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的前台角色

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色实体 | 实体 |  |

## **20\. 查询经典模式角色编号**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/d3665141-85a4-4049-991a-0b850792b463.undefined)

**节点功能**

仅经典模式可用，查询目标角色的角色编号，可以查看附录对应具体是哪位角色 [经典模式角色编号一览](https://act.mihoyo.com/ys/ugc/tutorial//detail/mh4imrrhzdzi)

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标角色 | 实体 |  |
| 出参 | 角色编号 | 整数 |  |

# **六、阵营相关**

## **1\. 查询实体阵营**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/90a3f329-d92c-4052-b737-8cf40071858a.undefined)

**节点功能**

查询目标实体的阵营

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 阵营 | 阵营 |  |

## **2\. 查询阵营是否敌对**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/113b49ba-db4b-4b0a-9bf6-3576a7ff77b1.undefined)

**节点功能**

查询阵营1和阵营2是否敌对

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 阵营1 | 阵营 |  |
| 入参 | 阵营2 | 阵营 |  |
| 出参 | 是否敌对 | 布尔值 |  |

# **七、光标**

## **1\. 获取光标是否激活**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/188e47a9-834a-43a3-88c5-af3263a07196.undefined)

**节点功能**

获取本机持久光标是否处于激活状态，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否激活 | 布尔值 |  |

## **2\. 获取光标命中结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/1fbe8eb2-fd05-4304-be27-265d29ba4978.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/45ddb6e5-8e34-4cf0-8c92-633e6deab441.undefined)

**节点功能**

获取本机持久光标的屏幕坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

## **4\. 获取光标视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/dbae47ef-d552-4a5d-bd4c-5709455c2135.undefined)

**节点功能**

获取本机持久光标的视口坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 视口X | 浮点数 |  |
| 出参 | 视口Y | 浮点数 |  |

# **八、标签**

## **1\. 获取实体的单位标签列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/2949e2dc-27c4-4716-865a-cdd8709ec0e4.undefined)

**节点功能**

获取目标实体上携带的所有单位标签组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 列表 | 整数列表 |  |

## **2\. 获取单位标签的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/b6dba992-9eb1-4bd8-8054-eaecae17c635.undefined)

**节点功能**

获取在场所有携带该单位标签的实体列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位标签索引 | 整数 |  |
| 出参 | 实体列表 | 实体列表 |  |

# **九、通用**

## **1\. 获取局部变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/155bf018-860a-444d-bf9d-214598fa4b72.undefined)

**节点功能**

获取特定局部变量的变量值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 变量名 | 字符串 |  |
| 出参 | 变量值 | 泛型 |  |

# **十、自定义仇恨**

## **1\. 获取指定实体的仇恨目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/f9439e9f-8b53-4bb9-8459-18f27f05b867.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/29df49a2-9445-4d8e-8557-06fad5033929.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/6619c65e-54a6-4cc7-aeac-66983a210fad.undefined)

**节点功能**

仅自定义仇恨模式可用

查询指定实体是否已经入战

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 是否入战 | 布尔值 |  |

# **十一、触发器**

## **1\. 获取碰撞触发器内所有实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a7e12db4-65ea-419c-95bd-6def365f8a50.undefined)

**节点功能**

获取目标实体上碰撞触发器组件中特定序号对应的碰撞触发器内的所有实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 触发器序号 | 整数 |  |
| 出参 | 实体列表 | 实体列表 |  |

# **十二、射线**

## **1\. 获取射线检测结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/e63fa2fc-5a5c-4797-ae36-9daa49f23da1.undefined)

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

# **十三、字典**

## **1\. 以键查询字典值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/c6ae9fc8-ce64-41f6-a5e4-75a764876cff.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/e37394af-c93e-4d30-bf10-e6b03db3bda1.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/f19cabd0-b867-4624-810a-1c94da27165f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/ac050342-9df8-4738-8fa3-c6c39b2196e7.undefined)

**节点功能**

查询字典中键值对的数量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **5\. 获取字典中值组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/78aa4cc4-5e7f-4e6d-a027-633c34da6b1b.undefined)

**节点功能**

获取字典中所有值组成的列表。由于字典中键值对是无序排列的，所以取出的值列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 值列表 | 泛型 |  |

## **6\. 获取字典中键组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/31fb5014-326c-4299-a7ce-279b1aca5cec.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/72e9b08e-bddf-4c85-a1b3-361d102eac2e.undefined)

**节点功能**

查询目标实体是否携带指定的单位状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 单位状态 | 配置ID |  |
| 出参 | 是否携带 | 布尔值 |  |