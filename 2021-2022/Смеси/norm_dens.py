from pylab import *
from math import factorial as fact
rc ('font', family='verdana')

def norm_p (x, a, s):
    return exp((-(x-a)**2)/(2*s))/math.sqrt(2*math.pi)

def bin (n, k):
	return fact(n)/(fact(k)*fact(n-k));

figure(1)
N = 10
for n in range (1, N+1):
    boarder = N
    x = arange(-3, 3, 1e-4)
    def dens_f (x, a1, a2, g1, g2):
        y = 0
        for k in range (n+1):
            Ak = a1*k+a2*(n-k)
            Gk = bin(n,k)*(g1**k)*(g2**(n-k))
            y += Gk*norm_p(n+sqrt(3*n)*x, Ak, n)/sqrt(n)
        return y*sqrt(3*n)
    plot (x, dens_f(x,-1,2,1/3,2/3), label=r'$f$'+str(n))
legend(loc=0)
title('Нормированные плотности сверток', color='b', weight='bold', size=14)
show()

figure(2)
i = complex(0,1)

def phi (t, a, n):
    return exp(i*t*a-(n*t**2)/2)
N = 4
subplot(2,1,1)
for n in range (1, N+1):
    t = arange(-7, 7, 1e-3)
    def char_f (t, a1, a2, g1, g2):
        y = 0
        for k in range (n+1):
            Ak = a1*k+a2*(n-k)
            Gk = bin(n,k)*(g1**k)*(g2**(n-k))
            y += Gk*phi(t/math.sqrt(3*n), Ak-n, n)
        return y.real
    plot (t, char_f(t,-1,2,1/3,2/3), label=r'$\phi$'+str(n))
plot([0],[1.1],'w.')
legend(title='Real part', loc=0)
title('Характеристические функции', color='b', weight='bold', size=14)
subplot(2,1,2)
for n in range (1, N+1):
    t = arange(-7, 7, 1e-3)
    def char_f (t, a1, a2, g1, g2):
        y = 0
        for k in range (n+1):
            Ak = a1*k+a2*(n-k)
            Gk = bin(n,k)*(g1**k)*(g2**(n-k))
            y += Gk*phi(t/math.sqrt(3*n), Ak-n, n)
        return y.imag
    plot (t, char_f(t,-1,2,1/3,2/3), label=r'$\phi$'+str(n))
plot([0],[0.41],'w.')
legend(title='Imag. part', loc=1)
show()
