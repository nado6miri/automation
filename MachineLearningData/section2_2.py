import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

# 재색인 (재 인덱싱)
print("[재색인, 재 인덱싱 - reindex() ]")

print("[재색인 : Series ]")
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
print("obj = ", obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print("obj.reindex = ", obj2)

obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
print("obj3 = ", obj3)

print("obj3.reindex(range(6), method = 'ffill') = ", obj3.reindex(range(6), method = 'ffill'))

print("[재색인 : DataFrame ]")
frame = pd.DataFrame(np.arange(9).reshape(3,3), index = ['a', 'c', 'd'], columns = ['Ohio', 'Texas', 'California'])
print("frame = ", frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print("frame2 = ", frame2)

states = ['Texas', 'Utah', 'California']
print("\n frame.reindex(columns=states) = ", frame.reindex(columns=states))


obj = pd.Series(np.arange(4), index = ['a', 'b', 'c', 'd'])
print("\nobj =\n", obj)
print("obj['b'] = ", obj['b'])
print("obj[1] = ", obj[1])
print("obj[2:4] = ", obj[2:4]) # 2 <= value < 4
print("obj[[1, 3]] = ", obj[[1, 3]])
print("obj[obj<2] = ", obj[obj < 2])
print("obj['b':'c'] = ", obj['b':'c']) # 주의 : 'b' <= value <= 'c'


print("[재색인 : drop() ]")

obj = pd.Series(np.arange(5), index = ['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c') # 'c' index를 가진 data 삭제한다.
print("obj = ", obj)
print("new_obj = ", new_obj)
print("obj.drop(['d', 'c'] = ", obj.drop(['d', 'c']))