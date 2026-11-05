---
id: mhb5tu05hgfc
title: 运算节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhb5tu05hgfc
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhb5tu05hgfc
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:54:27.668Z
---

# **一、通用**

## **1\. 枚举匹配**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/c73d3d83-0f86-4d42-a8eb-209e2097312e.undefined)

**节点功能**

确认枚举的类型后，判断两个输入的值是否相等

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 枚举1 | 泛型 |  |
| 入参 | 枚举2 | 泛型 |  |
| 出参 | 结果 | 布尔值 | 相等输出“是”，不相等输出“否” |

## **2\. 是否相等**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/f05561a9-3c18-44fd-8a02-d604c01c5adc.undefined)

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

## **3\. 数据类型转换**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/12bbb2c0-d137-42af-866f-379364505ab4.undefined)

**节点功能**

将输入的参数类型转换为另一种类型输出。具体规则见 [基础概念](https://act.mihoyo.com/ys/ugc/tutorial//detail/mhk23ora1wom)-【基础数据类型之间的转换规则】

在客户端节点中对于浮点数转整数，会截尾取整

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 转换结果 | 泛型 |  |

# **二、数学**

## **1\. 逻辑与运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/bce2dc3f-b786-4d7d-a0ef-8526b9cecf8f.undefined)

**节点功能**

对输入的两个布尔值进行与运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **2\. 逻辑或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/5cb636a4-c83d-4245-9301-a9cc57b4c89a.undefined)

**节点功能**

对输入的两个布尔值进行或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **3\. 逻辑非运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/a7d80554-ff0f-47cb-b3e9-d6b787fa11b6.undefined)

**节点功能**

对输入的布尔值进行非运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **4\. 逻辑异或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/e0863349-f657-4947-adff-a5f6e5aff890.undefined)

**节点功能**

对输入的两个布尔值进行异或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **5\. 是否大于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/82a02519-7393-4bd8-aca4-2a415f6fa272.undefined)

**节点功能**

返回左值是否大于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **6\. 是否小于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/b094d995-63df-49f0-93ae-99150f3b2770.undefined)

**节点功能**

返回左值是否小于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **7\. 是否小于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/57d7f81e-b0ea-4766-af81-32836b0671c3.undefined)

**节点功能**

返回左值是否小于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **8\. 是否大于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/ec28627b-5d69-4857-88e2-9309d1e4c3bc.undefined)

**节点功能**

返回左值是否大于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **9\. 加法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/1839ef42-c177-4774-9cb9-8f0d599ed75b.undefined)

**节点功能**

计算两个浮点数或整数的加法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **10\. 减法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/15f31ef7-35e1-4c37-a94f-b1953b615fa9.undefined)

**节点功能**

计算两个浮点数或整数的减法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **11\. 乘法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/34b2aca3-f26d-4adf-9600-007ef6850308.undefined)

**节点功能**

乘法运算，支持浮点数乘法和整数乘法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **12\. 除法运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/a70084b7-5810-450e-a960-b2ccd71f841f.undefined)

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

## **13\. 绝对值运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/8ac28049-cf96-42ef-bdae-12d38e2cf3b9.undefined)

**节点功能**

返回输入的绝对值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **14\. 获取随机数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/f8080c3f-1e50-46d9-84c3-be75bde34438.undefined)

**节点功能**

获取一个大于等于下限，小于等于上限的随机数。注意该节点生成的随机数包含上下限

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 下限 | 泛型 |  |
| 入参 | 上限 | 泛型 |  |
| 出参 | 随机数 | 泛型 |  |

## **15\. 拼装列表**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/f1e5766d-0090-412a-a6cd-9b1eb56bb20c.undefined)

**节点功能**

将多个类型相同的入参(至多10个)拼装为一个列表

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 列表 | 泛型 | 拼装成的列表 |
| 入参 | 0~9 | 泛型 | 将至多10个参数拼装为一个列表 |

## **16\. 三维向量内积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/ca9c0454-80cb-4c19-97a2-709b9cf54134.undefined)

**节点功能**

计算两个输入三维向量的内积（点乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 浮点数 |  |

## **17\. 三维向量外积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/7e3d9d0e-07d0-4d5e-9e93-1bc02ae8a80b.undefined)

**节点功能**

计算两个三维向量的外积（叉乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **18\. 拆分三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/e5a91d40-45db-4920-9781-353c6a846fe7.undefined)

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

## **19\. 三维向量缩放**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/d9b2770b-5cfd-4d6f-8784-d28d3c1c97bf.undefined)

**节点功能**

将输入的三维向量缩放后输出（三维向量数乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 缩放倍率 | 浮点数 |  |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **20\. 三维向量夹角**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/8cb5b6e4-7e07-416a-a357-16454e131f04.undefined)

**节点功能**

计算两个三维向量之间的夹角，以角度输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 夹角(角度) | 浮点数 |  |

## **21\. 三维向量旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/b7c74d12-2155-47e1-8638-2896a2bb51e6.undefined)

**节点功能**

将被旋转的三维向量，按照旋转所表示的欧拉角进行旋转后返回结果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 被旋转的三维向量 | 三维向量 |  |
| 入参 | 旋转 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **22\. 三维向量模运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/bf58be89-9395-4a17-87b3-acef849cdaae.undefined)

**节点功能**

计算输入三维向量的模

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 浮点数 |  |

## **23\. 创建三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/b87e3668-604c-4ea1-8efa-0a0f7f3f300a.undefined)

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

## **24\. 三维向量加法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/6a6ee45e-caa6-4eba-9134-68706ba2cac9.undefined)

**节点功能**

计算两个三维向量的加法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **25\. 三维向量减法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/2693e4fa-d81a-4ba5-bcda-6eb5c1ecc7f6.undefined)

**节点功能**

计算两个三维向量的减法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **26\. 方向向量转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/2de6cad8-57a5-4753-8622-ae1a087bd490.undefined)

**节点功能**

给定向前向量和向上向量，转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 向前向量 | 三维向量 | 表示单位期望的朝向 |
| 入参 | 向上向量 | 三维向量 | 定义单位的上方向（用于确定旋转的旋转角度），默认值为世界坐标系Y轴正方向 |
| 出参 | 旋转 | 三维向量 |  |

## **27\. 朝向转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/3a26bc55-8b8e-4524-8540-9511b5f23191.undefined)

**节点功能**

将方向向量转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 朝向 | 三维向量 |  |
| 出参 | 旋转 | 三维向量 |  |

## **28\. 正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/0233e60e-78eb-4fa5-9dcc-61ab38e97f39.undefined)

**节点功能**

计算输入弧度的正弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **29\. 余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/c0a0db9e-4512-4f90-b304-1b2ee842d18d.undefined)

**节点功能**

计算输入弧度的余弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **30\. 正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/1c6e7764-c24b-4263-b106-9133715f1f2b.undefined)

**节点功能**

计算输入弧度的正切

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **31\. 反正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/39da3d53-f736-4354-ad3e-bb59ffde60fa.undefined)

**节点功能**

计算输入的反正弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **32\. 反余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/734e6e04-e990-42f7-80d5-4a4c7f554bbe.undefined)

**节点功能**

计算输入的反余弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **33\. 反正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/20481676-07c7-40c2-bf7f-18c2e3f7ee37.undefined)

**节点功能**

计算输入的反正切值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **34\. 三维向量归一化**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/27a9a17b-f6d8-4709-b878-bcdef80e1640.undefined)

**节点功能**

将三维向量的长度归一化后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **35\. 弧度转角度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/160b8813-5c6f-4650-9877-c7dc790ff9bb.undefined)

**节点功能**

将弧度值转为角度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 角度 | 浮点数 |  |

## **36\. 角度转弧度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/2f60d698-5896-461d-bec5-b023bdf5ad7a.undefined)

**节点功能**

将角度值转为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角度 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

# **三、字典**

## **1\. 拼装字典**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/d0f4446a-ee43-4ee8-b40d-16326c9d4585.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/c5297c2e-ee5b-49fb-8577-287621e19b7a.undefined)

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

# **四、结构体**

## **1\. 拼装结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/6f480de2-23f3-4ad4-9262-d9eebcd8d895.undefined)

**节点功能**

将多个参数拼合为一个结构体类型的值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 结构体 | 结构体 |  |

## **2\. 拆分结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhb5tu05hgfc/82978afa-a81a-4b11-b5b1-d6ff5df21db1.undefined)

**节点功能**

获取指定结构体的所有参数

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 结构体 | 结构体 |  |