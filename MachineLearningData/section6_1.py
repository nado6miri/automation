import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

print("[시계열 데이터 기초]")
print("1. 날짜와 시간처리 - datetime, time, calendar 라이브러리")

now = datetime.now()
print("\n now = ", now)
print("{0}년 {1}월 {2}일".format(now.year, now.month, now.day), "\n")

delta = datetime(2018, 1, 7) - datetime(2015, 6, 24, 8, 15)
print('delta = \n', delta)
print("day:{0} second:{1}".format(delta.days, delta.seconds), "\n")

stamp = datetime(2018, 1, 3)
print(str(stamp), "\n")
print(stamp.strftime('%Y-%m-%m'), "\n")

value = '2017-01-03'
date1 = datetime.strptime(value, '%Y-%m-%d')
print("date1 = ", date1)

datestrs = ['7/6/2018', '8/6/2018']
print([datetime.strptime(x, '%m/%d/%Y') for x in datestrs], "\n")

from dateutil.parser import parse
print("parse('2017-01-03') = ", parse('2017-01-03'))
print("parse('Jan 31, 2001 10:45 PM') = ", parse('Jan 31, 2001 10:45 PM'))


print("2. 시계열 indexing 및 선택 - TimeSeries 인덱싱")
np.random.seed(12345)
dates = [datetime(2017, 1, 2), datetime(2017, 1, 5),datetime(2017, 1, 7),
        datetime(2017, 1, 8),datetime(2017, 1, 10),datetime(2017, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)

print("ts = \n", ts)
print("type(ts) = \n", type(ts))
print("ts[2] = \n", ts[2])
print("ts['1/10/2017'] = \n", ts['1/10/2017'])
print("ts['20170110'] = \n", ts['20170110'])
print("ts['1/6/2017':'1/11/2017'] = \n", ts['1/6/2017':'1/11/2017'])
print("ts.truncate(after='1/9/2017') = \n", ts.truncate(after='1/9/2017'))

print("3. 날짜 범위 생성과 데이터 시프트")
np.random.seed(12345)
index = pd.date_range('4/1/2012', '6/1/2012')
print("index = \n", index)
print("pd.date_range(start='4/1/2012', periods = 20) = \n", pd.date_range(start='4/1/2012', periods = 20))
print("pd.date_range(end='6/1/2012', periods = 20) = \n", pd.date_range(end='6/1/2012', periods = 20))

from pandas.tseries.offsets import Hour, Minute
hour = Hour()
print("hour = \n", hour)
four_hour = Hour(4)
print("four_hour = \n", four_hour)

print("pd.date_range('1/1/2018', '1/2/2018 23:59', freq = '4h') = \n", pd.date_range('1/1/2018', '1/2/2018 23:59', freq = '4h'))
print("pd.date_range('1/1/2018', periods=10, freq='1h30min') = \n", pd.date_range('1/1/2018', periods=10, freq='1h30min'))
rng = pd.date_range('1/1/2019', '9/1/2019', freq = 'WOM-2FRI') # 월별 주 차수 - 각 월 2주차 금요일
print("list(rng) = \n", list(rng))