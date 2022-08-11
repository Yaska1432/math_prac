import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *

N = 100
A = log(19)
number_of_graphs = 9000
eps = 0.52

fig = plt.figure()
fig.suptitle ('Проверка гипотез', color = 'b', weight = 'bold', size = 14)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
colors = plt.cm.jet (np.linspace (0, 1, number_of_graphs))

def function (tetta, board, side, graph, sample, k, time):
	l = 0
	K = 0
	for i in range (N):
		if i == 0 : S[i + 1] = sample[i]
		else: S[i + 1] = S[i] + sample[i]
		if graph == 1 :
			if k % 100 == 0 :
				if side == 'down' : ax1.scatter(i, S[i], c = 'red', s = 2)
				if side == 'up' : ax2.scatter(i, S[i], c = 'red', s = 2)
		#выход вверх
		if side == 'down' :
			if S[i] > board:
				K = i
				break
			if S[i] < -board:
				K = i
				l += 1
				break
		#выход вниз
		if side == 'up' :
			if S[i] > board :
				K = i
				l += 1
				break
			if S[i] < -board :
				K = i
				break
	if time == 1 : return K
	if graph == 1 :
		for i in range (K):
			if k % 100 == 0 :
				if side == 'down' : ax1.annotate(u'', xy = (i, S[i]), xytext = (i + 1, S[i + 1]), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
				if side == 'up' : ax2.annotate(u'', xy = (i, S[i]), xytext = (i + 1, S[i + 1]), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
	return l

l = 0
m = 0
for k in range (number_of_graphs):

	x = np.random.normal (loc = 1/2, scale = 1, size = N)
	S = [0 for i in range(N + 1)]
	l += function (0, A - eps, 'down', 1, x, k, 0)
	if l / number_of_graphs > 0.05 : print(f'1ОШИБКА = {l / number_of_graphs}')

	y = np.random.normal (loc = -1/2, scale = 1, size = N)
	T = [0 for i in range(N + 1)]
	m += function (0, A - eps, 'up', 1, y, k, 0)
	if m / number_of_graphs > 0.05 : print(f'2ОШИБКА = {m / number_of_graphs}')

ax1.set_title(r'Гипотеза: $\mathcal{N}(\frac{1}{2}, 1)$')
ax1.axhline(y = A - eps, xmin = 0, xmax = 30, color = 'gray', label = f'{log(19) - eps}')
ax1.axhline(y = -A + eps, xmin = 0, xmax = 30, color = 'gray', label = f'{-log(19) + eps}')
ax1.legend(loc = 0)
ax1.grid('auto')
ax2.set_title(r'Гипотеза: $\mathcal{N}(-\frac{1}{2}, 1)$')
ax2.axhline(y = A - eps, xmin = 0, xmax = 30, color = 'gray', label = f'{log(19) - eps}')
ax2.axhline(y = -A + eps, xmin = 0, xmax = 30, color = 'gray', label = f'{-log(19) + eps}')
ax2.legend(loc = 0)
ax2.grid('auto')

def h(tetta):
	return -2 * tetta
def f(tetta, alpha):
	return (1 - 1 / alpha ** (h(tetta))) / (alpha ** (h(tetta)) - 1 / alpha ** (h(tetta)))

def g(tetta, alpha):
	return (f(tetta, alpha) * log (alpha) + (1 - f(tetta, alpha)) * log (1 / alpha)) / tetta


t = np.linspace (-1 / 2, 1 / 2, 100)
ax3.plot (t, f(t, 19), color = 'red', label = 'Теоретическая функция оценки вероятности выхода вверх')
ax4.plot (t, g(t, 19), color = 'red', label = 'Теоретическая функция времени выхода')


for tetta in t:
	l1, l2 = 0, 0
	time1, time2 = 0, 0
	for k in range (number_of_graphs):
		x = np.random.normal (loc = tetta, scale = 1, size = N)
		S = [0 for i in range(N + 1)]
		l1 += function(tetta, log(19), 'up', 0, x, k, 0)
		l2 += function(tetta, log(11), 'up', 0, x, k, 0)
		time1 += function(tetta, log(19), 'up', 0, x, k, 1)
		time2 += function(tetta, log(11), 'up', 0, x, k, 1)
	ax3.scatter(tetta, l1 / number_of_graphs, c = 'blue', s = 2)
	ax3.scatter(tetta, l2 / number_of_graphs, c = 'purple', s = 2)
	ax4.scatter(tetta, time1 / number_of_graphs, c = 'blue', s = 2)
	ax4.scatter(tetta, time2 / number_of_graphs, c = 'purple', s = 2)

ax3.scatter(tetta, l1 / number_of_graphs, c = 'blue', s = 2, label = f'граница = {log(19)}')
ax3.scatter(tetta, l2 / number_of_graphs, c = 'purple', s = 2, label = f'граница = {log(11)}')
ax4.scatter(tetta, time1 / number_of_graphs, c = 'blue', s = 2, label = f'граница = {log(19)}')
ax4.scatter(tetta, time2 / number_of_graphs, c = 'purple', s = 2, label = f'граница = {log(11)}')
ax3.legend(loc = 0)
ax4.legend(loc = 0)
ax3.set_ylim([-0.5, 2])
ax3.set_title('Логистическая кривая')
ax3.grid('auto')
ax4.set_title('Время выхода')
ax4.grid('auto')


show()