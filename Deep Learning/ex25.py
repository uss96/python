# 미분 함수 구현
import numpy as np
import matplotlib.pylab as plt

# 나쁜 구현 예
def numerical_diff (f, x):
    h = 1e-50 # 너무 작은 값을 활용하면, 반올림 오차 현상이 일어남! 이를 통해 작은 값이 생략되어 최종 계산 결과에 오차가 발생
    return (f(x+h) - f(x)) / h # 차분 방정식이기 때문에, 엄밀하게 말하자면 미분은 아님! 개선 필요

print(np.float32(1e-50)) # 반올림 오차 현상! 보통 10-4정도 활용한다.

def numerical_diff_fixed (f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

# 수치 미분


def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0, 20.0, 0.1) # 0에서 20까지 0.1 간격의 배열 x를 만듦! 20은 미포함
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
#plt.show()

print(numerical_diff(function_1, 5)) # 왜 0으로 나오지??
print(numerical_diff(function_1, 10)) # 왜 0으로 나오지??
