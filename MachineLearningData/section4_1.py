import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt


print("[Matplotlib 기초 및 활용]")
print("1. 그래프 그리기 기초")
plt.title("rs--style plot")
plt.plot([10, 20, 30, 40], [1, 2, 9, 16], 'rs--') # color, marker, line style
plt.show()

plt.title("plot")
plt.plot([10, 20, 30, 40], [1, 4, 9, 17])
plt.show()

plt.title("x axis, y axis range setting")
plt.plot([10, 20, 30, 40], [1, 2, 9, 16], c="b", lw = 5, ls = '--', marker = "o", ms = 10, mec = "g", mew = 5, mfc = "r" ) # color, marker, line style
plt.xlim(0, 50)
plt.ylim(-10, 30)
plt.show()

print("2. Thick 설정")
X = np.linspace(-np.pi, np.pi, 256)
C = np.cos(X)
plt.title("X, Y axis tick label setting")
plt.plot(X, C)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])
plt.show()


print("3. Multi Data 표현")
t = np.arange(0, 5, 0.2)
plt.plot(t, t, 'r--', t, 0.5*t**2, 'bs:', t, 0.2*t**3, 'g^-')
plt.show()

print("4. 범례")
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, ls="--", label = "cosine")
plt.plot(X, S, ls=":", label = "sine")
plt.legend(loc = 1)
plt.show()

print("5. figure")
#Figure객체 : matplotlib.figure,Figure class에 포함. Figure객체를 사용하면 세부 세팅이 가능하다.
np.random.seed(0)
f1 = plt.figure(figsize = (10, 2))
plt.title("figure size : (10, 2)")
plt.plot(np.random.randn(100))
plt.show()

print("6. axex객체와 subplot")
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2*np.pi*x1) * np.exp(-x1)
y2 = np.cos(2*np.pi*x2)

ax1 = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title("plots of 2 subplots")
plt.ylabel('flow data')

ax2 = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('result')
plt.tight_layout()
plt.show()







