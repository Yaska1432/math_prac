import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *

N = 100
A = log(19)
number_of_graphs = 9000
eps = 0.52

f, (ax1, ax2) = plt.subplots(1, 2, sharey = True)
f.suptitle('Проверка гипотез', color = 'black', weight = 'bold', size = 14)
colors = plt.cm.jet (np.linspace (0, 1, number_of_graphs))

l = 0
for k in range (number_of_graphs):
	
	x = np.random.normal (loc = 1/2, scale = 1, size = N)
	S = [0 for i in range(N + 1)]
	for i in range (N):
		if i == 0 : S[i + 1] = x[i]
		else: S[i + 1] = S[i] + x[i]
		if k % 100 == 0 : ax1.scatter(i, S[i], c = 'red', s = 2)
		if S[i] > A - eps:
			K = i
			break
		if S[i] < -A + eps :
			K = i
			l += 1
			break
	if l / number_of_graphs > 0.05 : print(f'1ОШИБКА = {l / number_of_graphs}')
	for i in range (K):
		if k % 100 == 0 : ax1.annotate(u'', xy = (i, S[i]), xytext = (i + 1, S[i + 1]), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
ax1.set_title(r'Гипотеза: $\mathcal{N}(\frac{1}{2}, 1)$')
ax1.axhline(y = A - eps, xmin = 0, xmax = 30, color = 'gray', label = f'{log(19) - eps}')
ax1.axhline(y = -A + eps, xmin = 0, xmax = 30, color = 'gray', label = f'{-log(19) + eps}')
ax1.legend(loc = 0)

l = 0
for k in range (number_of_graphs):
	y = np.random.normal (loc = -1/2, scale = 1, size = N)
	T = [0 for i in range(N + 1)]
	for i in range (N):
		if i == 0 : T[i + 1] = y[i]
		else : T[i + 1] = T[i] + y[i]
		if k % 100 == 0 : ax2.scatter(i, T[i], c = 'blue', s = 2)
		if T[i] > A - eps :
			K = i
			l += 1
			break
		if T[i] < -A + eps :
			K = i
			break
	if l / number_of_graphs > 0.05 : print(f'2ОШИБКА = {l / number_of_graphs}')
	for i in range (K):
		if k % 100 == 0 : ax2.annotate(u'', xy = (i, T[i]), xytext = (i + 1, T[i + 1]), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
ax2.set_title(r'Гипотеза: $\mathcal{N}(-\frac{1}{2}, 1)$')

ax2.axhline(y = A - eps, xmin = 0, xmax = 30, color = 'gray', label = f'{log(19) - eps}')
ax2.axhline(y = -A + eps, xmin = 0, xmax = 30, color = 'gray', label = f'{-log(19) + eps}')
ax2.legend(loc = 0)

show()