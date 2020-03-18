import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt
import seaborn as sns

'''
print("[데이터 수집 및 변경]")
print("1. 데이터 수집을 위한 함수활용]")

tips = pd.read_csv('tips.csv')

tips['tip_pct'] = tips['tip'] / tips['total_bill']
print("\ntips[:6] = \n", tips[:6])
grouped = tips.groupb(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']

print("\n grouped_pct.agg('mean') = \n", grouped_pct.agg('mean'))
print("\n grouped_pct.agg(['mean', 'std']) = \n", grouped_pct.agg(['mean', 'std']))
print("\n grouped_pct.agg([('s_mean', 'mean'), ('sm_mean', 'std')]) = \n", grouped_pct.agg([('s_mean', 'mean'), ('sm_mean', 'std')]))
print("\n grouped_pct.agg(dictionary) = \n", grouped_pct.agg({'tip_pct' : ['min', 'max', 'std'], 'size' : ['summ', 'mean']}))

print("2. 데이터 분리, 적용과 병함 - apply함수이용시 함수의 매개변수 전달 가능")

def top(df, n=5, column = 'tip_pct'):
    return df.sort_values(by=column)[-n:]
print("\n", tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))
'''

print("3. 데이터 분리, 적용과 병함 - apply함수이용시 함수의 매개변수 전달 가능")
states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print("data = \n", data)
print("group_key = \n", group_key)

fill_mean = lambda g : g.fillna(g.mean())
print("\ndata.groupby(group_key) = \n", data.groupby(group_key), "\n")
print(data.groupby(group_key).apply(fill_mean), "\n")

fill_values = { 'East' : 0.5, 'West' : -1 }
fill_func = lambda g: g.fillna(fill_values[g.name])
print("\ndata.groupby(group_key) = \n", data.groupby(group_key), "\n")
print(data.groupby(group_key).apply(fill_func))

print("4. 피벗 테이블")
tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

print("\n", tips.pivot_table(index=['sex', 'smoker']))
print("\n", tips.pivot_table(index=['sex', 'day'], columns='smoker'))
print("\n", tips.pivot_table(['tip_pct', 'size'], index=['sex', 'day'], columns='smoker'))
print("\n", tips.pivot_table('tip_pct', index=['sex', 'day'], columns='smoker', aggfunc=len))
