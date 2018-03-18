import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2,0.01)
plt.plot(x, x, linewidth=3.0, c='r')
plt.plot(x, x**2, linewidth=3.0, c='royalblue')
plt.plot(x, x**3, linewidth=3.0, c='orange')
plt.axhline(y=0.0, linewidth=2, c='k')
plt.axvline(x=0.0, linewidth=2, c='k')
plt.grid()
plt.show()
