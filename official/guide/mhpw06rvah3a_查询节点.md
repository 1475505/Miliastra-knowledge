---
id: mhpw06rvah3a
title: 查询节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpw06rvah3a
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhpw06rvah3a
description: undefined
language: zh
scope: guide
crawledAt: 2026-07-01T08:26:59.853Z
---

# **一、技能**

## **1\. 获取复杂造物当前施放的技能**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/c15efbc2-f465-4421-88b0-0cf9537fc3da.undefined)

**节点功能**

返回复杂造物当前正在施放的技能的序号

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 技能序号 | 整数 |  |

## **2\. 查询技能变量对应值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/1d1ee005-4431-43de-be77-19248a27aeef.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/272bd385-33cf-4baf-83ef-0de18be61490.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/3e78b6f1-cba4-4438-92e4-75f3961d00d6.undefined)

**节点功能**

获取列表长度（列表中的元素个数）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入列表 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **3\. 获取列表最大值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/2d7a2f1e-ef3b-4c9e-8aa2-95eac387d062.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最大值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最大值 | 泛型 |  |

## **4\. 获取列表最小值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/83394376-4bc9-48f4-98ed-e9182670438f.undefined)

**节点功能**

仅对浮点数列表和整数列表有意义，返回列表中的最小值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 列表 | 泛型 |  |
| 出参 | 最小值 | 泛型 |  |

## **5\. 获取实体类型列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/45ad4934-8592-4f8e-bbd6-a125e1df165e.undefined)

**节点功能**

将所需的实体类型拼装为一个列表。类型分为关卡、物件、玩家、角色、造物

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

## **6\. 列表是否包含该值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/4716df92-1c5f-4039-b6d4-976d3344f48a.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/9a56b6dc-7dda-41d8-8b7d-13b6d121be4d.undefined)

**节点功能**

将所需的射线筛选类型拼装为一个列表。可筛选项有受击盒、场景、物件自身碰撞

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 枚举列表 |  |

# **三、自定义变量**

## **1\. 获取自定义变量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/2a5f0948-5352-4b0e-8d64-8ffbd24ecb4a.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/bf9f6ce2-983b-4209-b48b-ea1562418dae.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/521e76c4-4222-40ba-a485-cf88a851f5cb.undefined)

**节点功能**

根据GUID查询实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | GUID | GUID |  |
| 出参 | 实体 | 实体 |  |

## **2\. 获取实体位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/bf38b0df-2a6b-4e6e-a4df-55127a7aa692.undefined)

**节点功能**

获取指定实体的位置

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 位置 | 三维向量 |  |

## **3\. 获取实体旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/01a17176-b1be-4536-8942-8a102447a496.undefined)

**节点功能**

获取指定实体以欧拉角表示的旋转

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | 旋转 | 三维向量 |  |

## **4\. 获取自身实体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/23587cff-ed11-4b3d-a743-8814631e54d8.undefined)

**节点功能**

返回该节点图所关联的实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 自身实体 | 实体 |  |

## **5\. 获取单位攻击目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/470d29af-2153-4ae2-8f86-07dab3099308.undefined)

**节点功能**

获取单位实体当前正在攻击的目标实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 单位实体 | 实体 |  |
| 出参 | 攻击目标实体 | 实体 |  |

## **6\. 获取目标挂接点位置**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/6e6f4d79-94d3-4abb-ab1b-d7f7f98e615c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/62f27382-907d-4560-82ad-eac1353dda45.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/4f84f668-6388-48d4-a9cb-b7591c71cb67.undefined)

**节点功能**

获取指定实体的类型

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 实体类型 | 枚举 |  |

## **9\. 筛选球体范围内的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/e4959e3f-f76d-40ae-b05a-a80f8bb47f6f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a0dc8016-aa0d-4d3a-911b-f5dca8dcd4c8.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/51f4ea3d-f722-4d5c-957f-ba6f675ba650.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/9d5791b4-48c8-4766-a82c-ef2a990585e4.undefined)

**节点功能**

返回目标实体的子实体列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 子实体列表 | 实体列表 |  |

## **13\. 获取造物当前目标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/7053fa80-ed7c-4cf2-a1a2-e0332843d5f8.undefined)

**节点功能**

返回指定造物当前的目标

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 造物 | 实体 |  |
| 出参 | 目标实体 | 实体 |  |

## **14\. 查询复杂造物的预设状态值**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/f789caa2-b37b-4de3-9f02-e34877defddc.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/fc78d83a-4d28-4609-ae26-38969aebfa78.undefined)

**节点功能**

获取角色实体所归属的玩家实体

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角色实体 | 实体 |  |
| 出参 | 所属玩家实体 | 实体 |  |

## **16\. 获取在场玩家实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/3027fd4d-06b4-4514-b560-4b0a3369dc87.undefined)

**节点功能**

获取在场所有玩家实体组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 玩家实体列表 | 实体列表 |  |

## **17\. 以实体查询GUID**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/2a7b7913-3824-4871-98a8-6f5b75bec9bf.undefined)

**节点功能**

查询指定实体的GUID

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 实体 | 实体 |  |
| 出参 | GUID | GUID |  |

## **18\. 获取玩家的角色列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/1c64c902-009f-4887-8885-6a2187e3e4f8.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的角色列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色列表 | 实体列表 |  |

## **19\. 获取指定玩家的前台角色**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/895e422c-7153-4568-b52a-1536792de9c2.undefined)

**节点功能**

仅经典模式可用，获取玩家队伍内的前台角色

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 玩家实体 | 实体 |  |
| 出参 | 角色实体 | 实体 |  |

## **20\. 查询经典模式角色编号**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/76726e9b-7afa-4f83-b0c1-4cf218a92752.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/6acb5a4f-32a6-4524-8f84-cf1851766eb2.undefined)

**节点功能**

查询目标实体的阵营

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 阵营 | 阵营 |  |

## **2\. 查询阵营是否敌对**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/0bed06a7-0795-4d40-99ea-d8d6b27a36a2.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/5d6870a4-5817-4eda-a269-594d89d8a600.undefined)

**节点功能**

获取本机持久光标是否处于激活状态，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 是否激活 | 布尔值 |  |

## **2\. 获取光标命中结果**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/0db98f04-1aae-4ca8-88f5-89c09ea91961.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/dc9a8cd7-ebbf-4daa-9fd6-9017e1e25078.undefined)

**节点功能**

获取本机持久光标的屏幕坐标X与Y，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

## **4\. 获取光标视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/9a7ab878-2e31-4b05-94c4-8b839544335f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/97d473c4-177a-46ae-999c-2f8ba6aec65f.undefined)

**节点功能**

获取目标实体上携带的所有单位标签组成的列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 出参 | 列表 | 整数列表 |  |

## **2\. 获取单位标签的实体列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a0850936-6866-4656-902e-758431a07ad1.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/3405c0a1-63a7-4896-9bbf-b82f2604326e.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/77ccadc8-436b-4447-bab8-fc469609fd43.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/0d49014b-4d36-4f1d-a6d3-49823036c019.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/c9439eb6-e73e-499b-b2a1-9ff1d921747a.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a1c1627d-35ef-42e3-b0a5-db7a9e64044d.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/040d856f-d7cf-4a2a-843c-81dbf33c2a15.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/23538a7e-3afc-4e9b-b940-d92f16dd493b.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/22572e4c-0564-430f-bf0d-5777440467aa.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a7e66586-dd9e-4f56-aeec-18a41cd8400e.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/04a168af-c5ca-41b8-9881-0dd175243bb3.undefined)

**节点功能**

查询字典中键值对的数量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 长度 | 整数 |  |

## **5\. 获取字典中值组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/a9e3d43f-108c-4422-ac7f-15590c2125fa.undefined)

**节点功能**

获取字典中所有值组成的列表。由于字典中键值对是无序排列的，所以取出的值列表也不一定按照其插入顺序排列

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 字典 | 泛型 |  |
| 出参 | 值列表 | 泛型 |  |

## **6\. 获取字典中键组成的列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/7bc1970f-f37a-4b60-b495-8b727ba6d2c1.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhpw06rvah3a/bbb9d561-b8f0-4fb8-916a-bb4bf65ee74c.undefined)

**节点功能**

查询目标实体是否携带指定的单位状态

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 目标实体 | 实体 |  |
| 入参 | 单位状态 | 配置ID |  |
| 出参 | 是否携带 | 布尔值 |  |