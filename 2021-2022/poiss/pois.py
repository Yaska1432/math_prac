import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *

N = 50
number_of_graphs = 200
fig = plt.figure()
fig.suptitle ('Пуассоновский процесс', color = 'black', weight = 'bold', size = 14)
ax = fig.add_subplot(1, 1, 1)
colors = plt.cm.jet (np.linspace (0, 1, number_of_graphs))
boarder = 30
S = [0 for i in range(N)]
num = [0 for i in range(N)]


for k in range (number_of_graphs):
	sample = np.random.exponential (scale = 1, size = N)
	for i in range (1, N):
		if i != 1 : S[i] = sample[i] + S[i - 1]
		else : S[i] = sample[i]
		if S[i] >= boarder :
			num[i] += 1
			ax.annotate(u'', xy = (S[i - 1], i), xytext = (boarder, i), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
			break
		if i == 1 :
			ax.annotate(u'', xy = (0, 0), xytext = (S[1], 0), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
			ax.annotate(u'', xy = (S[1], 0), xytext = (S[1], 1), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
		else :
			ax.annotate(u'', xy = (S[i - 1], i - 1), xytext = (S[i], i - 1), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})
			ax.annotate(u'', xy = (S[i], i - 1), xytext = (S[i], i), arrowprops = {'arrowstyle' : '-', 'color' : colors[k]})

for i in range (N):
	ax.annotate(u'', xy = (boarder, i), xytext = (boarder + num[i], i), arrowprops = {'arrowstyle' : '-', 'color' : 'black', 'linewidth' : 1})


ax.set_title (f'Экран на расстоянии {boarder}')
ax.annotate(u'', xy = (boarder, 0), xytext = (boarder, 50), arrowprops = {'arrowstyle' : '-', 'color' : 'gray', 'linewidth' : 1.5})
ax.set_xlim([0, boarder + 25])
ax.set_ylim([0, 50])
ax.grid('auto')
ax.legend(loc = 0)
show()