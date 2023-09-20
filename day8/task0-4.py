import math
import numpy as np
import matplotlib.pyplot as plt

def plot_fct(func, x_min, x_max):
    x = np.linspace(x_min, x_max)
    y = func(x)
    
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of the Function')
    plt.grid(True)
    plt.show()

# Example usage:
def f(x):
    return x ** 2 + x * 3 + 2

plot_fct(np.sin, 0, 50)
plot_fct(f, -100, 200)
plot_fct(lambda x: x ** 2, -10, 10)
plot_fct(lambda x: 1 / x, -100, 100)
