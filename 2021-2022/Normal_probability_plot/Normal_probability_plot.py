from pylab import *
import numpy
rc ('font', family='verdana')
from scipy.stats import norm
import matplotlib.lines as mlines

colors = ['blue', 'red', 'green']
stform = 'ods'
distrib = ['norm', 'uniform', 'expon']
N = 16 #len of sample

scope = arange (.5/N, 1.0, 1/N)
y_values  = norm.ppf(scope)

figure = figure(1)
axes = figure.add_subplot (111)

plt.gca().axhline(y = 0, color = 'k')
plt.gca().axvline(x = 0, color = 'k')

shift = float(input('Значение сдвига = '))
sigma = float(input('Значение коэффициента масштаба = '))

for l in range (3):
	lib = 'from scipy.stats import {}'.format(distrib[l])
	exec (lib)
	x_values = sort(eval(distrib[l]+'.rvs('+str(shift)+', '+str(sigma)+',size='+str(N)+')'))
	x_mean = mean (x_values)
	y_mean = mean (y_values)

	vx = 0
	sum = 0
	for i in range (N):
		sum += (x_values[i] - x_mean)*(y_values[i] - y_mean)
		vx += (x_values[i] - x_mean)**2
	sum /= vx
	if sum == 0: sum = 1
	s = sqrt(vx/(N-1))

	plot (x_values, y_values, colors[l][0] + stform[l], label = r'{} distribution'.format(distrib[l]))

	#[x1, x2], [y1, y2]

	plot ([x_mean - (6 + y_mean)/sum, x_mean + (6 - y_mean)/sum], [-6, 6], colors[l][0],
		label = r'('+str(numpy.round(x_mean, 2)) + ', ' + str(numpy.round(1/sum, 2)) + ')')
	if l == 0: x_min = x_values[0]
	shift+=1

width = x_values[N-1] - x_min + shift
scope_ = arange (1 - scope[len(scope) - 1], 1.0, 2/N)
y_mark = list(norm.ppf(scope)) + [0.0] + list(norm.ppf(scope_))
scope = list(scope) + [0.5] + list(scope_)

for i in range (len(scope)):
	text (x_min - width*0.075, y_mark[i] - 0.04, str(numpy.round(scope[i], 3)))
locatory = matplotlib.ticker.FixedLocator (y_mark)
axes.yaxis.set_major_locator (locatory)
axes.grid('auto') #drawing grid (net)

legend (loc = 4)
title ('Probability plot. Number of observation = ' + str(N), size = 14)
plt.xlim ([x_min - 0.09*width, x_values[N-1] + 0.05*width])
plt.ylim ([y_values[0] - 0.3, y_values[N-1] + 0.4])
plot ([x_min - 0.035*width, x_values[N-1] + 0.02*width], [0, 0], 'k')
plot ([x_values[N-1] + 0.02*width], [0], 'k>')
text (x_min - width*0.12, y_values[N-1] + 0.2, 'Q   Prob')

plt.show()
