import numpy as np

x = np.array([1, 2])
print(x.shape)

w = np.array([[1, 3, 5], [2, 4, 6]])
print(w)
print(w.shape)

y = np.dot(x, w)
print(y)

# 신경망에서의 행렬의 곱

x = np.array([1.0, 0.5])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])

print(w1.shape)
print(x.shape)
print(b1.shape)

a1 = np.dot(x, w1) + b1
print(a1)

# 다중신경망의 1층

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

z1 = sigmoid(a1)

print(z1)

# a1 -> z1으로의 활성화 함수 변환 (시그모이드 활용)

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

print(z1.shape)
print(w2.shape)
print(b2.shape)

a2 = np.dot(z1, w2) + b2
z2 = sigmoid(a2)
print(a2)
print(z2)

# 다중신경망의 2층

def identity_function(x) :
    return x

w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

a3 = np.dot(z2, w3) + b3
y = identity_function(a3)
print(a3)
print(y)
