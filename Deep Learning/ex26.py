import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

# 2변수 함수
def function_2(x):
    return x[0]**2 + x[1]**2


# x0 = 3, x1 = 4일 때, x0에 대한 편미분을 구하여라.
def function_tmp1 (x0):
    return x0*x0 + 4.0**2.0

def numerical_diff (f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

print(numerical_diff(function_tmp1, 3.0))

# x0 =3, x1 = 4일 때, x1에 대한 편미분을 구하여라

def function_tmp2 (x1):
    return 3.0**2.0 + x1*x1

print(numerical_diff(function_tmp2, 4.0))

# x0과 x1의 편미분을 동시에 계산하는 함수

def numerical_gradient(f, x):
    h = 1e-4 #0.0001
    grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 값 복원

    return grad

print(numerical_gradient(function_2, np.array([3.0, 4.0])))
print(numerical_gradient(function_2, np.array([0.0, 2.0])))
print(numerical_gradient(function_2, np.array([3.0, 0.0])))


