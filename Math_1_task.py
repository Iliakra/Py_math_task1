%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,121)
k = 1
plt.plot(x, np.cos(k*x))
k = 5
plt.plot(x, np.cos(k*x))