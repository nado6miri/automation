import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt


print("[그래프를 위한 라이브러리 활용]")
print("1. seaborn - countplot - matplotlib기반 다양한 테마와 통계용 차트 추가한 package")
import seaborn as sns

titanic = sns.load_dataset('titanic')
print("titanic = ", titanic)
sns.countplot(x='class', data=titanic)
plt.title("Titanic")
plt.show()

print("2. seaborn - jointplot - matplotlib기반 다양한 테마와 통계용 차트 추가한 package")
iris = sns.load_dataset('iris')
print("iris = ", iris)
sns.jointplot(x='sepal_length', y='sepal_width', data = iris)
plt.show()

print("3. seaborn - stripplot - matplotlib기반 다양한 테마와 통계용 차트 추가한 package")
tips = sns.load_dataset('tips')
print("tips = ", tips)
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)
plt.show()