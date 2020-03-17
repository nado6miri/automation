import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt
import seaborn as sns


print("[그래프를 위한 라이브러리 활용]")
print("1. Pandas 데이터 처리 그래프")

fig, axes = plt.subplots(nrows=1, ncols=2)
ax1, ax2 = axes.ravel()
data_frame = pd.DataFrame(np.random.rand(5, 3), 
                index=['Customer1', 'Customer2', 'Customer3', 'Customer4', 'Customer5'],
                columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metrics'))

data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')
plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
ax1.set_xlabel('Customer')
ax1.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

colors = dict(boxes='Darkblue', whiskers='Gray', medians='Red', caps='Black')
data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')
plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
plt.setp(ax2.get_yticklabels(), rotation=45, fontsize=10)
ax1.set_xlabel('Metric')
ax1.set_ylabel('Value')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.show()

print("2. 시계열 그래프")
close_px_all = pd.read_csv('stock_px.csv', parse_dates=True, index_col = 0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px_resample('B').ffill()
print("\n close_px.info() = ", close_px.info())
print(close_px.head(10), '\n')

close_px['AAPL'].plot()
plt.show()

close_px['AAPL'].loc['01-2001':'03-2011'].plot()
plt.show()




