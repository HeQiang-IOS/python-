# coding=utf-8

import pandas as pd
import  numpy as np

# 直接创建Series，采用默认的索引值
# 开区间 (a,b)不包含a，b两点
# 闭区间 [a, b] 包含啊a，b两点
print("直接创建Series，采用默认的索引值")
series1 = pd.Series([1,2,4,8,9])
print(series1)
print(series1.values)
print(series1.index)

# 创建指定索引值得Series
print("创建指定索引值得Series")
series2 = pd.Series([2,4,6,8],index=['a','b','c',1])
print(series2)
print(series2.index)
print(series2.values)
print(series2[1])
print(series2[['a','b','c']])

# numpy数组运算（布尔型数组进行过滤、标量乘法、应用数学函数等）都会保留索引和值之间的连接
print("numpy数组运算（布尔型数组进行过滤、标量乘法、应用数学函数等）都会保留索引和值之间的连接")
print(series2[series2>5])
print(series2*2)
print(np.exp(series2))

# 可以将Series看成是一个有定长的有序字典，因为它是索引值到数据值的一个映射，因此，一些字典函数也可以在这里使用
print("可以将Series看成是一个有定长的有序字典，因为它是索引值到数据值的一个映射")
print('a' in series2)
print('z' in series2)
print(2 in series2.values)

# 利用字典创建Series
print("利用字典创建Series")
dic = {"l":1, "z":2, "h":3}
series3 =pd.Series(dic)
print(series3)

"""
若索引比字典的索引多，则与字典索引相比配的则会被找到，并放置到相应的位置中，而对应值找不到索引，其结果则为NaN(即非数字
not a number
)
"""
print("若索引比字典的索引多，则与字典索引相比配的则会被找到，并放置到相应的位置中，而对应值找不到索引，其结果则为NaN")
ind = ['l','z','h','a']
series4 = pd.Series(dic, index=ind)
print(series4)

# pandas中isnull和notnull函数用于检测缺失数据
print("pandas中isnull和notnull函数用于检测缺失数据")
print(pd.isnull(series4))
print(pd.notnull(series4))

# 算术运算中自动对齐不同索引的数据
print("算术运算中自动对齐不同索引的数据")
print(series4 * series3)

# Series对象本身及其索引都有一个name属性
print("Series对象本身及其索引都有一个name属性")
print(series4.name)
print(series4.index.name)
series4.name = "myname"
series4.index.name = 'letter'
print(series4.name)
print(series4.index.name)
print(series4)

# 索引可以通过赋值的方式进行改变
print("索引可以通过赋值的方式进行改变")
series4.index = ["li",'lz','hua','a']
print(series4)
