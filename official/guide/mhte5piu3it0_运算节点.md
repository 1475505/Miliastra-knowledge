---
id: mhte5piu3it0
title: 运算节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhte5piu3it0
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhte5piu3it0
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:56:41.228Z
---

# **一、通用**

## **1\. 是否相等**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/352eb5a0-d85b-47b6-84a4-84cccafbb752.undefined)

**节点功能**

判断两个输入是否相等

部分参数类型有较为特殊的判定规则：

浮点数：浮点数采用近似相等进行比较，当两个浮点数小于一个极小值时，这两个浮点数认为相等。例如：2.0000001与2.0认为相等

三维向量：三维向量的x、y、z分别采用浮点数近似相等比较

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **2\. 数据类型转换**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/fe1ba958-6693-48ff-be59-756e2d7c7e63.undefined)

**节点功能**

将输入的参数类型转换为另一种类型输出。具体规则见 [基础概念](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhk23ora1wom)-【基础数据类型之间的转换规则】

在客户端节点中对于浮点数转整数，会截尾取整

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 转换结果 | 泛型 |  |

## **3\. 枚举匹配**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/b5082c29-dcf4-43cb-be7b-a85e557b73cb.undefined)

**节点功能**

确认枚举的类型后，判断两个输入的值是否相等

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 枚举1 | 泛型 |  |
| 入参 | 枚举2 | 泛型 |  |
| 出参 | 结果 | 布尔值 | 相等输出“是”，不相等输出“否” |

# **二、数学**

## **1\. 加法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/6e18edd2-a486-4657-a6c0-fc3637ab859f.undefined)

**节点功能**

计算两个浮点数或整数的加法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **2\. 减法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/bbb2a57c-a63c-49cb-b3b6-9c87d11db8f0.undefined)

**节点功能**

计算两个浮点数或整数的减法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **3\. 乘法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/a0b7188d-1da0-426f-82b9-6f43f796d52b.undefined)

**节点功能**

乘法运算，支持浮点数乘法和整数乘法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **4\. 除法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/6a9bf4e2-dc01-4e3b-b587-6d9f64ec1200.undefined)

**节点功能**

除法运算，支持浮点数除法和整数除法。整数除法返回整除结果

除数不应为0，否则可能返回非法值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **5\. 绝对值运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/3bce799a-6c6f-41f9-b7f4-61ef72b8ec6b.undefined)

**节点功能**

返回输入的绝对值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **6\. 获取随机数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/9879e0fd-9229-45df-870e-e5d75b3c422d.undefined)

**节点功能**

获取一个大于等于下限，小于等于上限的随机数。注意该节点生成的随机数包含上下限

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 下限 | 泛型 |  |
| 入参 | 上限 | 泛型 |  |
| 出参 | 随机数 | 泛型 |  |

## **7\. 三维向量内积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/fb49bcbb-5542-4a4e-bfe1-0b38d1f516b6.undefined)

**节点功能**

计算两个输入三维向量的内积（点乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 浮点数 |  |

## **8\. 三维向量外积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/e88ccc86-b915-4659-9277-9932b0d33049.undefined)

**节点功能**

计算两个三维向量的外积（叉乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **9\. 拆分三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/015b1f20-426d-4ce3-b89f-df612d1fb389.undefined)

**节点功能**

将三维向量的x、y、z分量输出为三个浮点数

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | X分量 | 浮点数 |  |
| 出参 | Y分量 | 浮点数 |  |
| 出参 | Z分量 | 浮点数 |  |

## **10\. 三维向量缩放**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/a8278136-450d-4f56-802c-8294e2c431e1.undefined)

**节点功能**

将输入的三维向量缩放后输出（三维向量数乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 缩放倍率 | 浮点数 |  |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **11\. 三维向量夹角**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/e50b06f9-aa1e-482b-aa30-5d40eb3f5979.undefined)

**节点功能**

计算两个三维向量之间的夹角，以角度输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 夹角(角度) | 浮点数 |  |

## **12\. 三维向量旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/340c9f41-5ae6-4212-8890-b82a3c6844ee.undefined)

**节点功能**

将被旋转的三维向量，按照旋转所表示的欧拉角进行旋转后返回结果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 被旋转的三维向量 | 三维向量 |  |
| 入参 | 旋转 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **13\. 三维向量模运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/d5d9d550-5fa5-4b21-b091-7e0fcebfe1a3.undefined)

**节点功能**

计算输入三维向量的模

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 浮点数 |  |

## **14\. 创建三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/95a73f94-722b-4142-9a0d-dc06e65d4502.undefined)

**节点功能**

根据x、y、z分量创建一个三维向量

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | X分量 | 浮点数 |  |
| 入参 | Y分量 | 浮点数 |  |
| 入参 | Z分量 | 浮点数 |  |
| 出参 | 三维向量 | 三维向量 |  |

## **15\. 三维向量加法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/983b12b8-c30f-42bd-b472-959ede537e15.undefined)

**节点功能**

计算两个三维向量的加法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **16\. 三维向量减法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/bb8cb845-5aaa-4631-8a9f-10293299dc92.undefined)

**节点功能**

计算两个三维向量的减法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **17\. 方向向量转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/a799f19d-733f-4e8f-b6e9-e07a20b08674.undefined)

**节点功能**

给定向前向量和向上向量，转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 向前向量 | 三维向量 | 表示单位期望的朝向 |
| 入参 | 向上向量 | 三维向量 | 定义单位的上方向（用于确定旋转的旋转角度），默认值为世界坐标系Y轴正方向 |
| 出参 | 旋转 | 三维向量 |  |

## **18\. 朝向转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/886a1eae-aef5-46b9-a4b9-4330840032cb.undefined)

**节点功能**

将方向向量转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 朝向 | 三维向量 |  |
| 出参 | 旋转 | 三维向量 |  |

## **19\. 正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/553b1483-a7bd-472f-887b-955efbf49b5f.undefined)

**节点功能**

计算输入弧度的正弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **20\. 余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/a3c0cfcf-68a0-41dd-ae48-2e64ddd88534.undefined)

**节点功能**

计算输入弧度的余弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **21\. 正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/dea3230a-32a5-4a4f-b82c-472e9e896d0a.undefined)

**节点功能**

计算输入弧度的正切

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **22\. 反正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/6e3d9f0d-e270-4f6d-a641-2fc1f3546c51.undefined)

**节点功能**

计算输入的反正弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **23\. 反余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/5e0eca7d-5042-4bcc-b557-5ac6ecfec109.undefined)

**节点功能**

计算输入的反余弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **24\. 反正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/35468bbf-c62e-4fa7-bb3a-02107b3ee495.undefined)

**节点功能**

计算输入的反正切值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **25\. 三维向量归一化**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/1c2c3ae2-da08-4011-80f4-00d4fa75cf0d.undefined)

**节点功能**

将三维向量的长度归一化后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **26\. 弧度转角度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/e31f8879-fbdb-4723-8a0f-8dc6de26fbae.undefined)

**节点功能**

将弧度值转为角度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 角度 | 浮点数 |  |

## **27\. 角度转弧度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/40d509bc-4432-4729-860c-8531f2d11ec5.undefined)

**节点功能**

将角度值转为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角度 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **28\. 逻辑与运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/6ef7c2d2-2614-475d-a01d-f779af28080c.undefined)

**节点功能**

对输入的两个布尔值进行与运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **29\. 逻辑或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/dd0b7b3b-4801-4f49-b97b-64fee8c6d8df.undefined)

**节点功能**

对输入的两个布尔值进行或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **30\. 逻辑非运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/7d9809b0-5b0e-44df-93af-1a57a00751d6.undefined)

**节点功能**

对输入的布尔值进行非运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **31\. 逻辑异或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/31f8362d-2385-40a8-84ee-2fde540dd7d6.undefined)

**节点功能**

对输入的两个布尔值进行异或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **32\. 是否大于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/ab3b8a48-f4b3-483e-9c3c-5f841ec23df7.undefined)

**节点功能**

返回左值是否大于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **33\. 是否小于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/55357ae5-4993-43fd-bcf1-2c6cc46932e4.undefined)

**节点功能**

返回左值是否小于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **34\. 是否小于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/7a215ee4-8ed7-4a8d-a7dc-cd126d42ea01.undefined)

**节点功能**

返回左值是否小于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **35\. 是否大于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/30f03cec-ec24-48a7-920b-66732924575c.undefined)

**节点功能**

返回左值是否大于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **36\. 屏幕坐标转视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/5d1ceefb-7e1a-403c-bbca-c84a4f572428.undefined)

**节点功能**

将屏幕坐标转换为视口坐标（归一化0-1），仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 屏幕X | 浮点数 |  |
| 入参 | 屏幕Y | 浮点数 |  |
| 出参 | 视口X | 浮点数 |  |
| 出参 | 视口Y | 浮点数 |  |

## **37\. 视口坐标转屏幕坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/0b995f32-5b3c-477f-b84e-85e7dedbbe8f.undefined)

**节点功能**

将视口坐标（归一化0-1）转换为屏幕坐标，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 视口X | 浮点数 |  |
| 入参 | 视口Y | 浮点数 |  |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

## **38\. 屏幕坐标转世界坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/f40a0890-8f14-40cf-b364-3f88a9ca2f07.undefined)

**节点功能**

将屏幕坐标加上深度值，转换为世界坐标，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 屏幕X | 浮点数 |  |
| 入参 | 屏幕Y | 浮点数 |  |
| 入参 | 深度值 | 浮点数 |  |
| 出参 | 世界坐标 | 三维向量 |  |

## **39\. 世界坐标转屏幕坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/3750887b-5745-485f-a89d-02f9367f3481.undefined)

**节点功能**

将世界坐标转换为屏幕坐标，仅在超限模式可用

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 世界坐标 | 三维向量 |  |
| 出参 | 屏幕X | 浮点数 |  |
| 出参 | 屏幕Y | 浮点数 |  |

# **三、列表**

## **1\. 拼装列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/6091ab3f-3358-43d3-a144-b241cc511a4a.undefined)

**节点功能**

将多个类型相同的入参(至多10个)拼装为一个列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 泛型 | 拼装成的列表 |
| 入参 | 0~9 | 泛型 | 将至多10个参数拼装为一个列表 |

# **四、结构体**

## **1\. 拼装结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/159d1a20-10b8-42ee-9f82-cd0062ab96db.undefined)

**节点功能**

将多个参数拼合为一个结构体类型的值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 结构体 | 结构体 |  |

## **2\. 拆分结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/434e6599-58c0-4930-a07a-326af25a5891.undefined)

**节点功能**

获取指定结构体的所有参数

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 结构体 | 结构体 |  |

# **五、字典**

## **1\. 拼装字典**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/3c6be309-6c19-421e-bdae-8c565ea2f976.undefined)

**节点功能**

将至多50个键值对拼合为一个字典

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 字典 | 泛型 |  |
| 入参 | 键0~49 | 泛型 |  |
| 入参 | 值0~49 | 泛型 |  |

## **2\. 建立字典**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhte5piu3it0/75cb181a-1c7c-489d-8574-410a3fe5d780.undefined)

**节点功能**

根据输入的键和值列表的顺序依次建立键值对。

此节点会按照键和值列表中较短的一个进行字典创建，多余的部分会被截断

如果键列表中存在重复值，则会创建失败，返回空字典

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 键列表 | 泛型 |  |
| 入参 | 值列表 | 泛型 |  |
| 出参 | 字典 | 泛型 |  |