import numpy as np

def step_function(x):
    y = x > 0
    y = y.astype(np.int)
    return y

x = np.array([-1.0, 1.0, 2.0])

print(step_function(x))