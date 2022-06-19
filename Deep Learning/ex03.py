import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
print(a*b)

x = np.array([[51, 55], [14, 19], [0, 4]])
print(x)
print(x[0])
print(x[0][1])

for row in x:
    print(row)

x = x.flatten()
print(x)
print(x[np.array([0, 2, 4])])

print(x > 15)
print(x[x>15])