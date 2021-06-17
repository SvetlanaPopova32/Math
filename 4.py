
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
ax.plot(x, np.sin(2*x))
plt.show()