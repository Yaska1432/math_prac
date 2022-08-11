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
	return a*x + b

def tang (x, a, b, alpha, x_0, y_0):
	return (a*a*b*b-x*(b*b*x_0*cos(alpha) + a*a*y_0*sin(alpha)))/(a*a*y_0*cos(alpha) - b*b*x_0*sin(alpha))

N = 100
x_ = np.linspace(-2, 2, 100)
figure(1)

subplot(131)
scale = 1, 1
A = np.array([-1, -1, 2**(1/2), 2, 1, 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1])
Q = linalg.inv(A.dot(A.T))

norm_veсt = np.random.randn(N, 2) #2 N-мерных вектора
QQ = norm_veсt.dot(Q)
scaled = QQ * scale
x = scaled[:, 0]
y = scaled[:, 1]
w, v = np.linalg.eig(Q)
vector_1 = complex(v[0][0], v[0][1])
angle = np.angle(vector_1, deg=True)

a, b = get_params(x, y)
print(a,b)
plt.plot(x_, lin_reg(x_, a, b), linewidth = 1, linestyle = 'dashed', color = 'red', label = 'linear regression')
plt.plot(x_, tang(x_, a, b, angle + 90, 0.7, 0.5), linewidth = 1, linestyle = 'dashed', color = 'blue', label = 'tangent')

plt.scatter (x, y, s = 2, c = 'blue')
ell = mp.Ellipse((0, 0), 4 * w[0], 4 * w[1], angle + 90, color = 'green', fill = False)
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.gca().add_patch(ell)
plt.legend(title='Положительная корреляция', loc=1)


subplot(132)
scale = 1, 1
A = np.array([1, 1, sqrt (2), 2, 1, 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1])
Q = linalg.inv(A.dot(A.T))
norm_veсt = np.random.randn(N, 2) #2 N-мерных вектора
QQ = norm_veсt.dot(Q)
scaled = QQ * scale
x = scaled[:, 0]
y = scaled[:, 1]

a, b = get_params(x, y)
print(a,b)
plt.plot(x_, lin_reg(x_, a, b), linewidth = 1, linestyle = 'dashed', color = 'red', label = 'linear regression')

w, v = np.linalg.eig(Q)
vector_1 = complex(v[0][0], v[0][1])
angle = np.angle(vector_1, deg=True)
plt.scatter (x, y, s = 2, c = 'blue')
ell = mp.Ellipse((0, 0), 4 * w[0], 4 * w[1], angle + 90, color = 'green', fill = False)
plt.xlim([-4, 4])
plt.ylim([-2, 2])
plt.gca().add_patch(ell)
legend(title='Отрицательная корреляция', loc=1)


subplot(133)
scale = 1, 1
A = np.array([cos (1), sin (1), 0, -sin (1), cos (1), 0]).reshape(2, 3)
for i in range (N):
	sample_ = np.array(sps.norm(loc = 0, scale = 1).rvs(size = 3)).reshape(3, 1)
	sample = A.dot(sample_)
	plt.plot(sample[0], sample[1])
Q = linalg.inv(A.dot(A.T))
norm_veсt = np.random.randn(N, 2) #2 N-мерных вектора
QQ = norm_veсt.dot(Q)
scaled = QQ * scale
x = scaled[:, 0]
y = scaled[:, 1]

a, b = get_params(x, y)
print(a,b)
plt.plot(x_, lin_reg(x_, a, b), linewidth = 1, linestyle = 'dashed', color = 'red', label = 'linear regression')

w, v = np.linalg.eig(Q)
vector_1 = complex(v[0][0], v[0][1])
angle = np.angle(vector_1, deg=True)
plt.scatter (x, y, s = 2, c = 'blue')
ell = mp.Ellipse((0, 0), 4 * w[0], 4 * w[1], angle + 90, color = 'green', fill = False)
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.axis('equal')
plt.gca().add_patch(ell)
legend(title='Корреляция = 0', loc=1)


plt.show()