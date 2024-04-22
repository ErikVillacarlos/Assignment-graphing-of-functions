import numpy as np
import matplotlib.pyplot as plt
x = np. linspace(-10,10)
y = x**4 +x**3 +x**2 +x +1
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()