import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *

N = 100
p = 0.3
eps = 0.5

xx = np.linspace (2, 100, 1000)
plt.plot(xx, sqrt(2 * xx * np.log(np.log(xx))), c = 'lightblue', label = f'приближающая парабола')
plt.plot(xx, -sqrt(2 * xx * np.log(np.log(xx))), c = 'lightblue')

plt.plot(xx, (1 + eps) * sqrt(2 * xx * np.log(np.log(xx))), c = 'blue', label = f'эпсилон-окрестность (eps = {eps})')
plt.plot(xx, -(1 + eps) * sqrt(2 * xx * np.log(np.log(xx))), c = 'blue')

for k in range (30):
	x = np.random.binomial (size = N, n = 1, p = p)

	S = []
	S = [0 for i in range(N)] 

	S_ = []
	S_ = [0 for i in range(N)] 

	arrowprops = {'arrowstyle': '-', 'color': 'red'}

	for i in range (N):
		if i == 0: S[i] = x[i]
		else: S[i] = S[i-1] + x[i]
		S_[i] = (S[i] - i * p) / math.sqrt(p * (1 - p))
		plt.scatter(i, S_[i], c = 'red', s = 2)

	for i in range (N - 1):
		annotate(u'', xy = (i, S_[i]), xytext = (i + 1, S_[i + 1]), arrowprops = arrowprops)


title('Закон повторного логарифма', color='black', weight='bold', size=14)

plt.legend(loc = 0)
plt.show()