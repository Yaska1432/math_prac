from pylab import *
import random
import numpy as np
from scipy.stats import kstest
import scipy.stats as sps

N = 10
EPS = 1e-8
random.expovariate(lambd = 1.5)

x = [round(random.expovariate(lambd = 1.5), 2)]
for i in range(1, N+1):
	x.append(round(random.expovariate(lambd = 1.5), 2))

xx = sorted(x)

y = [round(xx[0], 2)]
for i in range(1, N):
	y.append(round((N-i+1)*(xx[i+1]-xx[i]), 2))

sample = y

def norm_distr (x):
	return sps.norm(loc=0, scale=1).cdf(x)

x = arange (-2, 2, 1e-3)
plot (x, sps.norm(loc=0, scale=1).cdf(x), label=r'$Normal\ distribution$')
arrowprops = {'arrowstyle': '->', 'color':'green'}
annotate(u'', xy = (sample[0],0), xytext = (-max(abs(sample[0]), abs(sample[-1])) - 0.5, 0), arrowprops = arrowprops)
for i in range(1, N):
    annotate(u'', xy = (sample[i],i/N), xytext = (sample[i-1],i/N), arrowprops = arrowprops)
annotate(u'', xy = (max(abs(sample[0]), abs(sample[-1]))+0.5,1), xytext = (sample[-1], 1), arrowprops = arrowprops)

plot (x, sps.uniform(loc=0, scale=1).cdf(x), label=r'$Uniform\ distribution$')
arrowprops = {'arrowstyle': '->', 'color':'red'}
annotate(u'', xy = (norm_distr(sample[0]),0), xytext = (0,0), arrowprops = arrowprops)
for i in range(1, N):
    annotate(u'', xy = (norm_distr(sample[i]),i/N), xytext = (norm_distr(sample[i-1]),i/N), arrowprops = arrowprops)
annotate(u'', xy = (1,1), xytext = (norm_distr(sample[-1]), 1), arrowprops = arrowprops)


k1 = 0
i = 0
Dn = 0
for k in range (0, N):
	if Dn < abs(norm_distr(sample[k])-(k-1)/N):
		Dn = abs(norm_distr(sample[k])-(k-1)/N)
		k1 = k
		i = -1
	if Dn < abs(norm_distr(sample[k])-k/N):
		Dn = abs(norm_distr(sample[k])-k/N)
		k1 = k
		i = 0

arrowprops = {'arrowstyle': '<->', 'color':'black'}
annotate(u'', xy = (sample[(k1+i)], (k1+i)/N), xytext = (sample[(k1+i)], norm_distr(sample[k1+i])), arrowprops = arrowprops)
plt.text(Dn,Dn, f"$\ \ \ \ \ \ \ \ Dn = {Dn:.6f}$")

sum = 1
k = 1
while abs((-1)**(k+1)*exp(-2*(k+1)**2*N*Dn**2)) > EPS:
	sum += 2*(-1)**k*exp(-2*k**2*N*Dn**2)
	k+=1

plot (0, 0, label=r"$K(\sqrt{n} D_n)\ $" + f"$in\ first\ case\ =\ {sum:.6f}$")

sum = 1
i = -1
k = 1
while 1:
	s = (-1)**k*exp(-2*k**2*N*Dn**2)
	sum += 2*s
	if sum < 0.95:
		if i == 1: break
		else: i = 1
	else:
		if i == -1: break
		else: i = -1
	k+=1
plot (0, 0, label=r"$K(\sqrt{n} D_n)\ $" + f"$second\ case\ =\ {sum:.6f}$")

mu,sigma = 1, 0
kstest(np.random.normal(mu,sigma,10000),'norm')

legend(loc=4)
title('Выборочная функция распределения', color='b', weight='bold', size=14)

show()
