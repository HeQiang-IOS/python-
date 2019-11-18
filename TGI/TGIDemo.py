# coding=utf-8

import os
import pandas as pd

os.chdir('/Users/heqiang/PycharmProjects/Python数据分析/TGI')

df = pd.read_excel("TGI指数案例数据.xlsx")
print(df.head())

print(df.info())

# 计算单个用户平均支付金额
gp_user = df.groupby('买家昵称')['实付金额'].mean().reset_index()
print(gp_user.head())

# 基于用户支付金额，判断用户是属于低客单还是高客单
def if_high(x):
    if x > 50:
        return '高客单'
    else:
        return '低客单'

gp_user['客单类别'] = gp_user['实付金额'].apply(if_high)
print(gp_user.head(10))

# 将客单数据和地狱数据合并
# 先去重
df_dup = df.loc[df.duplicated('买家昵称') == False, :]
print(df_dup.head())
# 再合并
df_merge = pd.merge(gp_user, df_dup, left_on='买家昵称', right_on='买家昵称', how='inner')

# 用透视表的方法来统计每个省市低客单、高客单人数
#先筛选出我们需要的列
df_merge = df_merge[['买家昵称','客单类别','省份','城市']]

#再用透视表
result = pd.pivot_table(df_merge,index =['省份','城市'],columns = '客单类别',aggfunc = 'count')
print(result.head())

# 将低客单和高客单数据转化为我们熟悉的DF格式
tgi = pd.merge(result['买家昵称']['高客单'].reset_index(),result['买家昵称']['低客单'].reset_index(),
               left_on = ['省份','城市'],right_on = ['省份','城市'],how = 'inner')
print(tgi.head())

# 计算总人数，以及每个城市对应的高客单占比
tgi['总人数'] = tgi['高客单'] + tgi['低客单']
tgi['高客单占比'] = tgi['高客单'] / tgi['总人数']

print(tgi.head())

# 核查数据空值情况
print(tgi.info())

# 去除空值
tgi = tgi.dropna()

# 计算总体高客单人数占比
total_percentage = tgi['高客单'].sum() / tgi['总人数'].sum()
print(total_percentage)
# 计算每个城市高客单TGI指数
tgi['高客单TGI指数'] = tgi['高客单占比'] / total_percentage * 100
tgi = tgi.sort_values('高客单TGI指数',ascending = False)
print(tgi.head(10))

# 筛选出人数大于平均值的人数，再计算更合理的TGI指数
print(tgi.loc[tgi['总人数'] > tgi['总人数'].mean(),:].head(10))