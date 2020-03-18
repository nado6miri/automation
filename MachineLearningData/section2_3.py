import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

print("[ Pandas 핵심기술2 ]")
print("1. 함수 적용과 매핑")

frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'),
        index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print("\n np.abs(frame) = \n", np.abs(frame))

f = lambda x : x.max() - x.min()

print("f = ", f)
print("\n frame.apply(f) = ", frame.apply(f))
print("\n frame.apply(f, axis=1) = ", frame.apply(f, axis=1))

def f1(x):
    return pd.Series([x.min(), x.max()], index = ['min', 'max'])

print("\n frame.apply(f1) = ", frame.apply(f1))