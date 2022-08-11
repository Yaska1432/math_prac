import numpy as np
import matplotlib.pyplot as plt

num_sample = 200
num = 1000

def n_times_pos(n_t):
    t = np.cumsum(np.random.choice([-1,1], size = n_t))
    return sum(t > 0)

x = np.array([n_times_pos(num_sample) for i in range(num)])

bins = np.linspace(0, num_sample, 50)
hist, bin_edges = np.histogram(x, bins = bins, normed = True)
bin_centres = (bin_edges[:-1] + bin_edges[1:]) / 2
plt.bar(bin_centres, hist, align = 'center', facecolor='blue', alpha = 0.7)

x = np.linspace(0, 1, 200)
plt.plot(x * num_sample, 1 / np.pi / np.sqrt(x*(1-x))/num_sample, color = 'g')
plt.grid("auto")
plt.show()