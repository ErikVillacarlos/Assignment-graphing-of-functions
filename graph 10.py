import numpy as np
import matplotlib.pyplot as plt
x= np. linspace(-5,5)
y = (x+2)*(x+3)*(x-4)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()