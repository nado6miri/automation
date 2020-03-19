import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

print("[기간연산]")
print("1. Period의 빈도 변환 및 분기 빈도")
p = pd.Period(2010, freq='A-DEC')

print("p = pd.Period(2010, freq='A-DEC') = \n", p)
print("p+5 = \n", p+5)
print("p-2 = \n", p-2)
print("pd.Period('2017', freq='A-DEC') - p = \n", pd.Period('2017', freq='A-DEC') - p)

p.asfreq('M', how='start')
print("p.asfreq('M', how='start') = \n", p.asfreq('M', how='start'))

print("2. 기간연산")
rng = pd.date_range('1/1/2019', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)

pts = ts.to_period('M')

print("rng = \n", rng)
print("ts = \n", ts)
print("pts = \n", pts)

print("pts.to_timestamp(how='end') = \n", pts.to_timestamp(how='end'))

print("3. 기간 변환 및 배열을 이용한 Period Index 생성")
data = pd.read_csv('macrodata.csv')
print("data = \n", data)

index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq='Q-DEC')
data.index = index
print("data = \n", data)
