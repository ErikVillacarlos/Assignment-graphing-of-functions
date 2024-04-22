import numpy as np
import matplotlib.pyplot as plt
x= np. linspace(-5,5)
y= np.cos(x)/5*x
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()