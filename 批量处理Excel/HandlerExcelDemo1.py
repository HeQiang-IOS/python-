# coding=utf-8

# 当个文件处理

import os
import time
import pandas as pd

os.chdir("/Users/heqiang/PycharmProjects/Python数据分析/批量处理Excel/源数据128张表格")
name = '垂钓装备&绑钩器.xlsx'
df = pd.read_excel(name)
# head()默认读取5条数据
print(df.head(6))
# 查看日期范围
print(df['日期'].unique())
# 计算销售额
df['销售额'] = df['访客数'] * df['转化率'] * df['客单价']
print(df.head())

# 单表销售额合并
df_sum = df.groupby('品牌')['销售额'].sum().reset_index()
print(df_sum.head())

# 增加行业标签
df_sum['行业'] = name.replace('.xlsx','')
print(df_sum.head())

print(name.replace('.xlsx',''))
# 导出excel表
# xlrd 、xlwt 、 openyxl库
writer = pd.ExcelWriter(name.replace('.xlsx','')+'销售总额.xlsx')
df_sum.to_excel(writer)
writer.save()