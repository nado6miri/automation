import numpy as np
from numpy.linalg import inv, qr

import pandas as pd 

import re
import matplotlib.pyplot as plt


print("[Matplotlib 기초 및 활용]")
print("1. 선 막대 히스토그램")

customers = ['ABC', 'DEF', 'GMI', 'JKL', 'MNO']
customers_index = range(len(customers))
sale_amount = [117, 90, 201, 111, 232]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amount, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom') 
ax1.yaxis.set_ticks_position('left') 
plt.xticks(customers_index, customers, rotation=0, fontsize='small')

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')
plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
plt.show()


mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

print(x1)
print(x2)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.hist(x1, bins=50, color='darkgreen')
ax1.hist(x2, bins=50, color='orange', alpha = 0.5)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.xlabel('Bins')
plt.ylabel('Data Size of Values in Bin')
fig.suptitle('Histograms', fontsize=14, fontweight='bold')
ax1.set_title("Two Frequency Data")
plt.show()


print("2. 산점도 그래프")
x = np.arange(start=1., stop=15., step=1.)
y_linear = x + 5. * np.random.randn(14)
y_quadratic = x**2 + 10. * np.random.randn(14)

fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
fn_quardratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', x, fn_linear(x), 'b-', x, fn_quardratic(x), 'g-', linewidth=2.)
ax1.scatter(x=x, y=y_linear, c='b', marker='s')
ax1.scatter(x=x, y=y_quadratic, c='g', marker='o')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title("Scatter Plots with Best Fit Lines")
plt.show()


print("3. Box 그래프")
N = 500
normal = np.random.normal(loc=0.0, scale=1.0, size=N)
print("normal = ", normal)
lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
print("lognormal = ", lognormal)
index_value = np.random.random_integers(low=0, high=N-1, size=N)
print("index_value = ", index_value)
normal_sample = normal[index_value]
print("normal_sample = ", normal_sample)
lognormal_sample = lognormal[index_value]
print("lognormal_sample = ", lognormal_sample)
box_plot_data = [normal, normal_sample, lognormal, lognormal_sample]
print("box_plot_data = ", box_plot_data)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

box_labels = ['normal', 'mormal_sample', 'lognormal', 'lognormal_sample']
ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title("Box Plots : Resampling of Two Distributions")
ax1.set_xlabel("Distribution")
ax1.set_ylabel("Value")
plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

box_labels = ['normal', 'mormal_sample', 'lognormal', 'lognormal_sample']
ax1.boxplot(box_plot_data, notch=True, sym='*', vert=False, whis=3.5, showmeans=True, labels=box_labels)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
ax1.set_title("Box Plots : Resampling of Two Distributions")
ax1.set_xlabel("Distribution")
ax1.set_ylabel("Value")
plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
plt.show()

