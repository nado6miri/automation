import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

# Data 변경
print("[Data 변형]")
print("1. Data의 중복제거와 함수 매핑")
data = pd.DataFrame({'k1' : ['one'] * 3 + ['two']*4, 
                    'k2' : [1,1,2,3,3,4,4]})

print("\ndata = \n", data)
print("\ndata.duplicated() = \n", data.duplicated())
print("\ndata.drop_duplicates() = \n", data.drop_duplicates())
print("\ndata.drop_duplicates(['k1']) = \n", data.drop_duplicates(['k1']))
print("\ndata.drop_duplicates(['k1, k2']) = \n", data.drop_duplicates(['k1', 'k2']))
print("\ndata.drop_duplicates(['k1, k2'], keep = 'last) = \n", data.drop_duplicates(['k1', 'k2'], keep = 'last))

