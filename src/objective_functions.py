import numpy as np

def rastrigin(x, y):   #here you can chnage the objective function intead of rastrigin function
    """
    Rastrigin function
    Global minimum at (0, 0) with a value of 0
    Has many local minima arranged in a regular lattice
    """
    A = 10
    return A * 2 + (x**2 - A * np.cos(2 * np.pi * x)) + (y**2 - A * np.cos(2 * np.pi * y))

# Add more objective functions here as needed