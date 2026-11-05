---
id: mh7ys59fhtvu
title: 运算节点
url: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7ys59fhtvu
sourceURL: https://act.mihoyo.com/ys/ugc/tutorial/detail/mh7ys59fhtvu
description: undefined
language: zh
scope: guide
crawledAt: 2026-11-04T15:53:58.074Z
---

# **一、通用**

## **1\. 是否相等**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/14e7815b-bc7a-4345-8a0f-1b0480b2fdab.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/dfed7786-7dc8-4f61-81e5-5d006dd52279.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/90670de2-8080-4c3c-aeb3-19f1a447ec40.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/6da839b6-2270-4568-b9e9-ebc0bfa502d5.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/457dbb36-71be-4d2b-af60-a830019bb832.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/fb25ca3e-2143-4ea7-8828-327fcca94576.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/ee5d3edb-f6a1-4255-abd4-29135d0d9439.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/c93eebe7-18aa-4ccf-8a24-89c71289ab1c.undefined)

**节点功能**

返回输入的绝对值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 泛型 |  |
| 出参 | 结果 | 泛型 |  |

## **6\. 获取随机数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/7193ce13-0f43-4b96-956a-afd3536a50df.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/79f1d1e7-3e28-4ad8-97e5-529d4dad003c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/ada6cce1-d45e-4640-a56a-19fe1be03890.undefined)

**节点功能**

计算输入三维向量的模

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 浮点数 |  |

## **9\. 三维向量缩放**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/330a9866-b536-48db-9b3b-b2c8ed9d1c1f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/a04cca35-7529-4692-8f3f-ade7f2b8083c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/536cc75c-0a97-4a8a-9a55-fc24646a0cf3.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/06f197b8-ad50-4423-8079-0be9e25ca8af.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/99c1b9bb-bddc-401c-b27d-817af657079c.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/df31fe6f-c8ef-4f59-811d-5b1e1acadcbc.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/fad67dbd-525f-4bfb-9db5-7fba30937d3f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/3296896d-fe9c-45a1-ad09-7410c8a11714.undefined)

**节点功能**

将方向向量转化为欧拉角

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 朝向 | 三维向量 |  |
| 出参 | 旋转 | 三维向量 |  |

## **17\. 拆分三维向量**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/d7ae00ce-c36f-4088-abea-af56d26d71db.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/f4463131-85aa-4bc0-9382-6402e4e1c724.undefined)

**节点功能**

计算输入弧度的正弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **19\. 余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/d3890221-eea3-4537-a8ec-68da8a8b3da9.undefined)

**节点功能**

计算输入弧度的余弦

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **20\. 正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/99b0f008-33de-4308-b201-2a7c05336156.undefined)

**节点功能**

计算输入弧度的正切

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 结果 | 浮点数 |  |

## **21\. 反正弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/68f3e691-4001-4260-8874-a3f78e843d72.undefined)

**节点功能**

计算输入的反正弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **22\. 反余弦函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/c3168b98-083d-4931-a640-5295235dde73.undefined)

**节点功能**

计算输入的反余弦值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **23\. 反正切函数**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/a3e2c1d1-c217-4f3e-8b00-7b4578e1c6bc.undefined)

**节点功能**

计算输入的反正切值，返回为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 输入 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **24\. 三维向量归一化**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/f4f58a4e-0621-4b6c-b264-778bb530aac7.undefined)

**节点功能**

将三维向量的长度归一化后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 三维向量 | 三维向量 |  |
| 出参 | 结果 | 三维向量 |  |

## **25\. 弧度转角度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/9fa20ea8-e7f1-42eb-a51a-9cf58c5c251f.undefined)

**节点功能**

将弧度值转为角度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 弧度 | 浮点数 |  |
| 出参 | 角度 | 浮点数 |  |

## **26\. 角度转弧度**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/73cc26ce-be0c-4ca2-bec6-66f1735c875c.undefined)

**节点功能**

将角度值转为弧度值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 角度 | 浮点数 |  |
| 出参 | 弧度 | 浮点数 |  |

## **27\. 逻辑与运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/f9c8e563-45e2-47db-a50d-689c2361abd3.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/91dcf13b-b029-4745-b92c-057755984f52.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/5cae7adb-8b95-4601-a0a9-f28fd158bcce.undefined)

**节点功能**

对输入的布尔值进行非运算后输出

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 条件 | 布尔值 |  |
| 出参 | 结果 | 布尔值 |  |

## **30\. 逻辑异或运算**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/6ecb5893-9f59-4d10-8e90-f41dfe8a3015.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/71efbecf-a8fb-463f-9712-316df16c10ea.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/95314ad4-d898-47b7-a254-fcae17c7af7b.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/bbba58f6-aba9-484e-a85b-fdd4e901ff8a.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/28222336-0d07-4c67-aaa4-07949b2d9636.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/cd3c7c86-93f3-415d-a5c1-04df01ef0849.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/7f199e6b-caa0-4e58-906c-60723ffd26e9.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/ee47bef9-1216-4e4c-9914-98aa97b3d745.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/018ac0cc-dbfe-4023-876f-97eb5eea7959.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/7e10bd45-a448-43de-ab15-d5b57a7caf01.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/940c3a2e-de74-485b-93cd-9f1c00d8fb09.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/eeed7daa-6c10-42dc-af26-dabfcd3528b7.undefined)

**节点功能**

将多个参数拼合为一个结构体类型的值

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 出参 | 结构体 | 结构体 |  |

## **2\. 拆分结构体**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/6ca4f247-66a2-485c-b657-d208a60bc8b7.undefined)

**节点功能**

获取指定结构体的所有参数

**节点参数**

|     |     |     |     |
| --- | --- | --- | --- |
| **参数类型** | **参数名** | **类型** | **说明** |
| 入参 | 结构体 | 结构体 |  |

# **五、字典**

## **1\. 拼装字典**

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/1262a592-4cee-4e9f-b14c-e4a7f807f01f.undefined)

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

![](https://act-webstatic.mihoyo.com/ugc-tutorial/knowledge/cn/zh-cn/mh7ys59fhtvu/09a7848a-d6bc-4ec7-b944-1781a7b6ec72.undefined)

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