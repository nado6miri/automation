import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

# Data 병합 
print("[Data 병합-Data Join]")

df1 = pd.DataFrame({'key' : [ 'b', 'b', 'a', 'c', 'a', 'a', 'b' ], 'data1' : range(7)})
df2 = pd.DataFrame({'key' : [ 'a', 'b', 'd' ], 'data2' : range(3)})

print("\n df1 = \n", df1)
print("\n df2 = \n", df2)

#merge 함수는 기본적으로 내부-inner Join이 된다. 교집합의 결과를 받아낸다.
print("\n pd.merge(df1, df2) = \n", pd.merge(df1, df2), "\n")
print("\n pd.merge(df1, df2, on = 'key') = \n", pd.merge(df1, df2, on = 'key'), "\n")

print("\n pd.merge(df1, df2, how='outer') = \n", pd.merge(df1, df2, how='outer'), "\n")
print("\n pd.merge(df1, df2, how='left') = \n", pd.merge(df1, df2, how='left'), "\n")
print("\n pd.merge(df1, df2, how='right') = \n", pd.merge(df1, df2, how='right'), "\n")
print("\n pd.merge(df1, df2, how='inner') = \n", pd.merge(df1, df2, how='inner'), "\n")


print("[Data 병합-Data Join : Key 이름이 다른경우]")

df3 = pd.DataFrame({'Lkey' : [ 'b', 'b', 'a', 'c', 'a', 'a', 'b' ], 'data1' : range(7)})
df4 = pd.DataFrame({'Rkey' : [ 'a', 'b', 'd' ], 'data2' : range(3)})

print("\n df3 = \n", df3)
print("\n df4 = \n", df4)

print("\n pd.merge(df3, df4, left_on='Lkey', right_on='Rkey') = \n", pd.merge(df3, df4, left_on='Lkey', right_on='Rkey'), "\n")

# 축 병합 
print("[축 병합- concat 함수]")
s1 = pd.Series([0, 1], index = ['a', 'b'])
s2 = pd.Series([2, 3, 4], index = ['c', 'd', 'e'])
s3 = pd.Series([5, 6], index = ['f', 'g'])

print("s1 = \n", s1)
print("s2 = \n", s2)
print("s3 = \n", s3)

print("pd.concat([s1, s2, s3], axis = 0) = \n", pd.concat([s1, s2, s3], axis = 0), "\n")
print("pd.concat([s1, s2, s3], axis = 1, sort = False) = \n", pd.concat([s1, s2, s3], axis = 1, sort = False), "\n")

# 재형성 
print("[재형성 - 피벗 - stack, unstack, level]")
data = pd.DataFrame(np.arange(6).reshape((2,3)), index = pd.Index(['Ohio', 'Colorado'], name = 'state'), columns = pd.Index(['one', 'two', 'three'], name = 'number'))

print("\ndata = \n", data, "\n")
result = data.stack()
print("\ndata.stack() = \n", result, "\n")

print("\nresult.unstack() = \n", result.unstack(), "\n")
print("\nresult.unstack(level = 0) = \n", result.unstack(level = 0), "\n")
print("\nresult.unstack(level = 1) = \n", result.unstack(level = 1), "\n")
print("\nresult.unstack('state') = \n", result.unstack('state'), "\n")

print("\nconcat unstack")
s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('cde'))
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print("\ns1 = \n", s1)
print("\ns2 = \n", s2)
print("\ndata2 = \n", data2)
print("\ndata2.unstack() = \n", data2.unstack()) #unstack은 기본적으로 level = 1임.


