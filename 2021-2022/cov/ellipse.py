from pylab import *
import numpy as np
from math import sqrt
from math import cos
from math import sin
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from statistics import mean
import scipy.stats as sps

def calculate_slope(x, y):
    mx = x - x.mean()
    my = y - y.mean()
    return sum(mx * my) / sum(mx**2)

def get_params(x, y):
    a = calculate_slope(x, y)
    b = y.mean() - a * x.mean()
    return a, b

def lin_reg (x, a, b):
	return a * x + b

def tang (x, a1, a2, a3, x0, y0):
	return (4 - x * (a1 * x0 + a2 * y0)) / (a2 * x0 + a3 * y0)

def intersection (a, b, a1, a2, a3):
	return 	((-b * a2 - a3 * a * b + sqrt (b * b * a2 * a2 - a1 * a3 * b * b + 4 * a1 + 8 * a * a2 + 4 * a * a * a3)) / (a1 + 2 * a * a2 + a * a * a3),
			(-b * a2 - a3 * a * b - sqrt (b * b * a2 * a2 - a1 * a3 * b * b + 4 * a1 + 8 * a * a2 + 4 * a * a * a3)) / (a1 + 2 * a * a2 + a * a * a3))

N = 100
figure(1)

subplot(131)
x = np.arange(N)
y = np.arange(N)
A = np.array([-1, -1, 2**(1/2), 2, 1, 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1], '.', color = 'blue')
	x[i], y[i] = sample[0], sample[1]
Q = linalg.inv(A.dot(A.T))
a1, a2, a3 = Q[0][0], Q[0][1], Q[1][1]
y1 = lambda x: (-a2 * x + np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
y2 = lambda x: (-a2 * x - np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
x_ = np.linspace (-sqrt (4 * a3 / (a1 * a3 - a2 * a2)), 2 * sqrt (a3 / (a1 * a3 - a2 * a2)), 200)
plt.plot(x_, y1(x_), color = 'green')
plt.plot(x_, y2(x_), color = 'green')
a, b = get_params(np.array(x), np.array(y))
plt.plot(x_, lin_reg(x_, a, b), linewidth = 1, linestyle = 'dashed', color = 'red', label = 'linear regression')
x1 = 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
x2 = - 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
y1 = y1(x1)
y2 = y2(x2)
x_ = np.linspace (-6, 6, 100)
plt.plot (x_, tang(x_, a1, a2, a3, x1, y1), linestyle = 'dashed', color = 'pink', label = 'first tangent')
plt.plot (x_, tang(x_, a1, a2, a3, x2, y2), linestyle = 'dashed', color = 'pink', label = 'second tangent')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.gca().set_aspect('equal', adjustable='box')
legend(title = 'Отрицательная корреляция', loc = 0)


subplot(132)
x = np.arange(N)
y = np.arange(N)
A = np.array([1, 1, sqrt (2), 2, 1, 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1], '.', color = 'blue')
	x[i], y[i] = sample[0], sample[1]
Q = linalg.inv(A.dot(A.T))
a1, a2, a3 = Q[0][0], Q[0][1], Q[1][1]
y1 = lambda x: (-a2 * x + np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
y2 = lambda x: (-a2 * x - np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
x_ = np.linspace (-sqrt (4 * a3 / (a1 * a3 - a2 * a2)), 2 * sqrt (a3 / (a1 * a3 - a2 * a2)), 200)
plt.plot(x_, y1(x_), color = 'green')
plt.plot(x_, y2(x_), color = 'green')
a, b = get_params(np.array(x), np.array(y))
plt.plot(x_, lin_reg(x_, a, b), linewidth = 1, linestyle = 'dashed', color = 'red', label = 'linear regression')
x1 = 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
x2 = - 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
y1 = y1(x1)
y2 = y2(x2)
x_ = np.linspace (-6, 6, 100)
plt.plot (x_, tang(x_, a1, a2, a3, x1, y1), linestyle = 'dashed', color = 'pink', label = 'first tangent')
plt.plot (x_, tang(x_, a1, a2, a3, x2, y2), linestyle = 'dashed', color = 'pink', label = 'second tangent')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(title = 'Положительная корреляция', loc = 0)


subplot(133)
x = np.arange(N)
y = np.arange(N)
A = np.array([cos (1), sin (1), 0, -sin (1), cos (1), 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1], '.', color = 'blue')
	x[i], y[i] = sample[0], sample[1]
Q = linalg.inv(A.dot(A.T))
a1, a2, a3 = Q[0][0], Q[0][1], Q[1][1]
y1 = lambda x: (-a2 * x + np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
y2 = lambda x: (-a2 * x - np.sqrt (a2 * a2 * x * x - a1 * x * x * a3 + 4 * a3)) / a3
x_ = np.linspace (-sqrt (4 * a3 / (a1 * a3 - a2 * a2)), 2 * sqrt (a3 / (a1 * a3 - a2 * a2)), 200)
plt.plot(x_, y1(x_), color = 'green')
plt.plot(x_, y2(x_), color = 'green')
a, b = get_params(np.array(x), np.array(y))
plt.hlines(0, -2, 2, linestyle = 'dashed', color = 'red', label = 'linear regression')
x1 = 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
x2 = - 2 * sqrt (a3 / (a1 * a3 - a2 * a2))
plt.vlines(x1, -6, 6, linestyle = 'dashed', color = 'pink', label = 'first tangent')
plt.vlines(x2, -6, 6, linestyle = 'dashed', color = 'pink', label = 'first tangent')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.gca().set_aspect('equal', adjustable='box')
legend(title='Корреляция = 0', loc=1)


plt.show()