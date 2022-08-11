import numpy as np
from scipy.linalg import inv
import scipy.stats as sps
import matplotlib.pyplot as plt
from pylab import *
from scipy.linalg import solve
N = 100

X = np.linspace(-5, 5, N)

a_0 = float(input ('write a_0 = '))
a_1 = float(input ('write a_1 = '))
a_2 = float(input ('write a_2 = '))

plt.plot(X, a_0 + X * a_1 + X * X * a_2, c = 'black', label = f'{str(a_2)} * x^2 + {str(a_1)} * x + {str(a_0)}')
A = np.zeros((3, 3))
A[0][0] = N
b = np.zeros((3, 1))

for x in X:
	y = a_0 + x * a_1 + x * x * a_2 + sps.norm(loc = 0, scale = 1).rvs(size = 1)
	plt.plot (x, y, '.', color = 'blue')
	A[0][2] += x * x
	A[1][1] += x * x
	A[2][0] += x * x
	A[2][2] += x * x * x * x
	b[0] += y
	b[1] += x * y
	b[2] += x * x * y

theta = solve (A, b)
plt.plot(X, theta[0] + theta[1] * X + theta[2] * X * X, c = 'gray', label = f'{theta[2][0]:.{3}} * x^2 + {theta[1][0]:.{3}} * x + {theta[0][0]:.{3}}')

plt.legend(loc = 0)
plt.show()