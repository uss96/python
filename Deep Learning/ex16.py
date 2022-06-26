import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a.shape)

b = np.array([[5, 6], [7, 8]])
print(b.shape)

print(np.dot(a, b))

# 2차원 행렬의 곱

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

b = np.array([[1, 2], [3, 4], [5, 6]])
print(b.shape)

print(np.dot(a, b))

# 2x3 행렬과 3x2 행렬의 곱

c = np.array ([[1, 2], [3, 4]])
print(c.shape)
print(a.shape)

# np.dot(a, c)

# 행렬 곱셈 차원이 맞지 않는 경우

a = np.array([[1,2], [3,4], [5,6]])
print(a.shape)

b = np.array([7,8])
print(b.shape)

print(np.dot(a,b))

# 곱셈 차원이 맞는 경우