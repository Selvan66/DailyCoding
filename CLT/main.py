import numpy as np
import matplotlib.pyplot as plt
import time
 
ex = np.pi;
ex2 = np.pi/6 * (8 * pow(np.pi, 2) - 3)
var = ex2 - pow(ex, 2)

def fun(x):
    return pow(np.sin(x), 2);

def CLT(num_of_sample): 
    t = int( time.time() * 1000.0 )
    np.random.seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24))
    dist = []
    while len(dist) < num_of_sample:
        x = np.random.random() * (2*np.pi)
        y = np.random.random() 
        if y <= fun(x):
            dist.append(x)
    return np.average(dist)

n = 10000;
N = [1, 10, 100]

fig, ax = plt.subplots(2, 2)
t = np.arange(0.0, 2 * np.pi, 0.001)
s = [fun(x) for x in t]
ax[0,0].plot(t, s)
ax[0,0].set_title(label='sin^2(x)')
means = [(CLT(N[0]) - np.pi) / (np.sqrt(var/N[0])) for _ in range(n)]
ax[0,1].hist(means, 25)
ax[0,1].set_title(label='CLT for N=%d, n=%d' % (N[0], n))
means = [(CLT(N[1]) - np.pi) / (np.sqrt(var/N[1])) for _ in range(n)]
ax[1,0].hist(means, 25)
ax[1,0].set_title(label='CLT for N=%d, n=%d' % (N[1], n))
means = [(CLT(N[2]) - np.pi) / (np.sqrt(var/N[2])) for _ in range(n)]
ax[1,1].hist(means, 25)
ax[1,1].set_title(label='CLT for N=%d, n=%d' % (N[2], n))
plt.show()