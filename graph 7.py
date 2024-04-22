import numpy as np
import matplotlib.pyplot as plt
x = np. linspace(-5,5)
y= x**3-2*x**2-10*x +3
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()