# coding=utf-8
# 多张表

import os
import pandas as pd
import time

os.chdir("/Users/heqiang/PycharmProjects/Python数据分析/批量处理Excel/源数据128张表格")

# 开始时间
start = time.time()
# 存储汇总的结果
result = pd.DataFrame()

# 循环遍历表格名称
for name in os.listdir():
    df = pd.read_excel(name)
    # 计算销售额字段
    df['销售额'] = df['访客数']*df['转化率'] * df['客单价']
    # 按品牌对细分行业销售额进行汇总
    df_sum = df.groupby('品牌')['销售额'].sum().reset_index()
    df_sum['类目'] = name.replace('.xlsx','')
    result = pd.concat([result, df_sum])

# 对最终结果按销售额进行排序
final = result.groupby('品牌')['销售额'].sum().reset_index().sort_values('销售额', ascending=False)

pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(final.head())
# 结束时间
end = time.time()

print('用python操作所花费时间：{}s'.format(end-start))
print('用python操作所花费时间：%ss'%format(end-start))

# 将结果写出
pathName = os.getcwd()
print(pathName)
pathNameFather = os.path.abspath(os.path.dirname(pathName))
print(pathNameFather)

os.chdir(pathNameFather)
pathName = os.getcwd()
print(pathName)
writer = pd.ExcelWriter('最终总销售额表.xlsx')
final.to_excel(writer)
writer.save()



