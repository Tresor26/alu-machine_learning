import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

plt.plot(x, y, color='red', linestyle='-')
plt.xlim(0, 10)

plt.show()