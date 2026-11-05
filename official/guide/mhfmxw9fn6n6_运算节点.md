---
id: mhfmxw9fn6n6
title: 运算节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhfmxw9fn6n6
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mhfmxw9fn6n6
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:53:43.652Z
---

# **一、通用**

## **1\. 是否相等**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/9b30a2a8-c03e-4dae-a4b5-3a190e96dda0.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/eb340865-8161-4856-a803-2eb2cf2a4a29.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/d53145aa-bd00-4265-bf6c-0b90649fe35b.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/98f68f48-29ae-40fa-b01f-bd0822fc527f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/647343f0-8845-4cb0-9d73-d49b6f34e71c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/1cba90aa-1ca1-4226-bd50-8bf6c2837688.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/020f31c2-6914-4bf2-af1c-a2c1c0615932.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/fa73931c-12c6-4635-bd38-0a912ae7c26e.undefined)

**节点功能**

返回输入的绝对值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **6\. 获取随机数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/bd2c5bb5-deca-4b73-a052-eef966d41b76.undefined)

**节点功能**

获取一个大于等于下限，小于等于上限的随机数。注意该节点生成的随机数包含上下限

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 下限 | 泛型 |  |
| 入参 | 上限 | 泛型 |  |
| 出参 | 随机数 | 泛型 |  |

## **7\. 三维向量夹角**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/129c0345-6abe-4fdf-93c8-0959f280a72a.undefined)

**节点功能**

计算两个三维向量之间的夹角，以角度输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 夹角(角度) | 浮点数 |  |

## **8\. 三维向量模运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/9074ed3b-0e37-4630-ac08-f6584ddaf0a3.undefined)

**节点功能**

计算输入三维向量的模

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 浮点数 |  |

## **9\. 三维向量缩放**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/ca06a93f-f1a9-497b-8746-19555739c73d.undefined)

**节点功能**

将输入的三维向量缩放后输出（三维向量数乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 缩放倍率 | 浮点数 |  |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **10\. 三维向量旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/055180ec-197c-46f4-8530-9facd3649aa4.undefined)

**节点功能**

将被旋转的三维向量，按照旋转所表示的欧拉角进行旋转后返回结果

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 被旋转的三维向量 | 三维向量 |  |
| 入参 | 旋转 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **11\. 三维向量加法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/af087611-41ed-4b8c-8d32-9b738e8a58ab.undefined)

**节点功能**

计算两个三维向量的加法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **12\. 三维向量减法**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/2927a98b-72ef-47a4-848f-21dd3dc5fdce.undefined)

**节点功能**

计算两个三维向量的减法

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **13\. 三维向量内积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/0d54ea01-2953-430f-9cd2-2d2e558a7c0b.undefined)

**节点功能**

计算两个输入三维向量的内积（点乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 浮点数 |  |

## **14\. 三维向量外积**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/2195a5fb-566a-4ee8-b272-5d63f6b708ae.undefined)

**节点功能**

计算两个三维向量的外积（叉乘）

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量1 | 三维向量 |  |
| 入参 | 三维向量2 | 三维向量 |  |
| 出参 | 计算结果 | 三维向量 |  |

## **15\. 方向向量转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/42734f29-34ba-4ad7-a4d8-a17e5264ed83.undefined)

**节点功能**

给定向前向量和向上向量，转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 向前向量 | 三维向量 | 表示单位期望的朝向 |
| 入参 | 向上向量 | 三维向量 | 定义单位的上方向（用于确定旋转的旋转角度），默认值为世界坐标系Y轴正方向 |
| 出参 | 旋转 | 三维向量 |  |

## **16\. 朝向转旋转**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/2470c6bd-c6b2-4ca0-9603-fc93dbe75a9c.undefined)

**节点功能**

将方向向量转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 朝向 | 三维向量 |  |
| 出参 | 旋转 | 三维向量 |  |

## **17\. 拆分三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/b4095213-4edd-4255-93a7-118c39758295.undefined)

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

## **18\. 正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/88dc0025-c425-4060-bd47-967dca629081.undefined)

**节点功能**

计算输入弧度的正弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **19\. 余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/4bd84755-32e8-4763-acfd-de5ab5a17a5c.undefined)

**节点功能**

计算输入弧度的余弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **20\. 正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/acf85003-7ed1-436b-a20b-d9ce52f371b8.undefined)

**节点功能**

计算输入弧度的正切

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **21\. 反正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/5ed52bb8-9f0b-4b21-b75e-53fa7248e207.undefined)

**节点功能**

计算输入的反正弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **22\. 反余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/15791777-800e-49ce-b54b-4f7b59712028.undefined)

**节点功能**

计算输入的反余弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **23\. 反正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/73ae853c-1db9-4e44-86d4-2beb91376fbb.undefined)

**节点功能**

计算输入的反正切值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **24\. 三维向量归一化**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/33c790fb-4dd5-4468-8db2-9c087152b448.undefined)

**节点功能**

将三维向量的长度归一化后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **25\. 弧度转角度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/70b048aa-dc29-40de-add6-0830fac30f5d.undefined)

**节点功能**

将弧度值转为角度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 角度 | 浮点数 |  |

## **26\. 角度转弧度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/19c051de-b066-45f8-ae60-1275e9f79568.undefined)

**节点功能**

将角度值转为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角度 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **27\. 逻辑与运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/1e393ab7-980c-4193-9a45-e3572d5721a5.undefined)

**节点功能**

对输入的两个布尔值进行与运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **28\. 逻辑或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/cc410b9d-12b6-4ea6-af83-9ea218fd0c0d.undefined)

**节点功能**

对输入的两个布尔值进行或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **29\. 逻辑非运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/abfe688b-41b1-4780-9332-0950071a5a88.undefined)

**节点功能**

对输入的布尔值进行非运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **30\. 逻辑异或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/22417412-f597-49bc-83de-040e99809c6c.undefined)

**节点功能**

对输入的两个布尔值进行异或运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件1 | 布尔值 |  |
| 入参 | 条件2 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **31\. 是否大于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/4d6c512b-cc55-4f4b-a313-983c6d8dbadc.undefined)

**节点功能**

返回左值是否大于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **32\. 是否小于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/3cd6848b-5d20-403f-ae4c-f0b49e005e2c.undefined)

**节点功能**

返回左值是否小于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **33\. 是否小于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/05ec94a2-f137-4f1a-80cb-e6bd640d87a0.undefined)

**节点功能**

返回左值是否小于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **34\. 是否大于等于**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/ed41d214-49b9-481f-ad07-60bafb5ccedc.undefined)

**节点功能**

返回左值是否大于等于右值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 |  | 泛型 |  |
| 入参 |  | 泛型 |  |
| 出参 | 结果 | 布尔值 |  |

## **35\. 创建三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/9dca869c-c214-408e-94f0-5ee997743fe3.undefined)

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

## **36\. 屏幕坐标转视口坐标**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/ff0ff31c-6ccf-437d-a636-9c31cec0d246.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/cdaacb14-f230-42dc-9296-84c20e91cbd7.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/82898b6e-b9b4-4ab8-a513-6d6d7b551d5e.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/9eeb4f7b-9f5f-4e06-8f54-6b7de1491d86.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/f447f02c-3d6a-41c4-bc72-64c3c5fbf6cb.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/7aa91e0d-8d2e-4cdf-9855-154041ea2129.undefined)

**节点功能**

将多个参数拼合为一个结构体类型的值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 结构体 | 结构体 |  |

## **2\. 拆分结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/91e841cc-1d57-4869-b5a5-e29357b1c876.undefined)

**节点功能**

获取指定结构体的所有参数

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 结构体 | 结构体 |  |

# **五、字典**

## **1\. 拼装字典**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/49da7a5d-9be5-4820-bee4-2c882ca819dd.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mhfmxw9fn6n6/32677401-9d5e-48d3-8039-cffd15a5ac9a.undefined)

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