import numpy as np
import matplotlib.pyplot as plt
x = np. linspace(5,-5)
y = x**3 + 1*x -100
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()