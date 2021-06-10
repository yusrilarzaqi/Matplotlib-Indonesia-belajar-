# Multiple Scatter plot
import matplotlib.pyplot as plt
import numpy as np

x1 = [2, 4, 6, 8, 10, 11.5, 11.7]
y1 = np.arange(1, 5, .5)

x2 = np.arange(8, 11.5, .5)
# [8, 8.5, 9, 9.5, 10, 10.5, 11]
y2 =[3, 3.5, 3.7, 4, 4.5, 5, 5.2]

plt.scatter(x1, y1, label='Data 1', color="r")
plt.scatter(x2, y2, label='Data 2', color="g")
plt.title('Contoh Multiple Plot')
plt.show()
