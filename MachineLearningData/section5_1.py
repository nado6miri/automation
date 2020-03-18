import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt
import seaborn as sns


print("[데이터 수집 및 그룹연산]")
print("1. groupby 함수")

np.random.seed(1234)

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'], 
                    'key2' : ['one', 'two', 'one', 'two', 'one'],
                    'data1' : np.random.randn(5),
                    'data2' : np.random.randn(5)})

grouped = df['data1'].groupby(df['key1'])

print("\ngrouped = \n", grouped)
print("\ngrouped.mean() = \n", grouped.mean())

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print("\nmeans = \n", means)

print("2. groupby 순회 - groupby 객체는 이터레이션을 지원함")
for name, group in df.groupby('key1') :
    print("\nname = \n", name)
    print("\ngroup = \n", group)

print("\n3. group선택 - 칼럼으로 선택")
mean3 = df.groupby(['key1', 'key2'])['data2'].mean()
print("\nmean3 = \n", mean3)

s_grouped = df.groupby(['key1', 'key2'])['data2']
print("\ns_grouped = {0}, \ns_grouped.mean() = \n {1}\n".format(s_grouped, s_grouped.mean()))

print("\n4. dictionary 와 series를 이용한 선택")
# 그룹정보는 배열이 아닌 형태로 존재하기도 하기 때문에 사전이나 Series를 이용하여 그룹화를 진행할 수 있다.

people = pd.DataFrame(np.random.randn(5, 5),
                    columns = list('abcde'), index = ['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

print("\npeople= \n", people)
'''
print("\npeople.loc[2:3, ['b', 'c']]= \n", people.loc[2:3, ['b', 'c']])

people.loc[2:3, ['b', 'c']] = np.nan
print("\npeople.loc[2:3, ['b', 'c']]= \n", people.loc[2:3, ['b', 'c']])
'''

mapping = { 'a' : 'red', 'b' : 'red', 'c' : 'blue', 'd' : 'blue', 'e' : 'red' }
by_column = people.groupby(mapping, axis = 1)
print("by_column.sum() = \n", by_column.sum())

map_series = pd.Series(mapping)
print("\nmap_series = \n", map_series)


print("\n5. 함수를 이용한 선택")
print("\npeople= \n", people)
print("people.groupby(len).sum() = \n", people.groupby(len).sum()) # len 은 index에 대한 문자열의 length를 return한다.
key_list = ['one', 'one', 'one', 'two', 'two']
print("people.groupby([len, key_list]).min() = \n", people.groupby([len, key_list]).min())
