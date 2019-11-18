# coding=utf-8
import pandas as pd
import numpy as np

# 构建DataFrame
# 最常用的一种是直接传入一个由等长列表或numpy数组组成的字典

data = {
    'names':['Bob', 'Jane', 'Jack', 'Ann'],
    'sex':['M', 'F', 'M', 'F'],
    'age':[21, 30, 26, 28]
}

df1 = pd.DataFrame.from_dict(data) # 和下句等价
df2 = pd.DataFrame(data)
# 没有指定索引，会自动加上索引，并且全部列会被有序排列
print(df1)
print(df2)

# 若指定列序列，则会按照指定顺序排列
print('若指定列序列，则会按照指定顺序排列')
df2 = pd.DataFrame(data, columns=['names','age','sex'])
print(df2)

# 若传入列在数据中找不到，会返回NaN值，指定列和索引
df3 = pd.DataFrame(data, columns=['names', 'sex', 'age', 'id'], index=['a', 'b', 'c', 'd'])
print(df3)

# 通过类似字典标记或属性的方式，可以获取Series（列数据）
df4 = df3['sex']
print(df4)
print(df3.age)

# 嵌套的嵌套序列数据结构
city_data = {
    '城市': pd.Series(['北京', '上海', '深圳', '成都', '长沙'], index=['a', 'b', 'c', 'd', 'e']),
    '人口/千万': pd.Series([2171, 2415, 1191, 901, 9912], index=['a', 'b', 'c', 'd', 'e']),
    '年份': pd.Series([2015, 2016, 2016, 2016, 2015], index=['a', 'b', 'c', 'd', 'e'])

}

df5 = pd.DataFrame(city_data)
print(df5)


def aa():
    pass
