import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
sigma = np.random.rand(len(x))
y = 1/np.sqrt(2*np.pi) * np.exp(-(x+3)**2/2) + sigma*0.01

plt.scatter(x, y)
#plt.show()

np.savetxt('test1.csv', np.vstack([x, y]).T, delimiter=',')