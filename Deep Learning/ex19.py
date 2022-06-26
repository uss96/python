import numpy as np

a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)

print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

# 소프트맥스

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

# 함수로 소프트맥스를 표현

a = np.array([1010, 1000, 900])
# exp_a = np.exp(a)
# sum_exp_a = np.sum(exp_a)
# print(exp_a / sum_exp_a) # overflow

c = np.max(a)
b = a - c
exp_b = np.exp(b)
sum_exp_b = np.sum(exp_b)

print(exp_b / sum_exp_b)

# 소프트맥스의 문제인 오버플로우 현상 개선

def softmax_nof(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 오버플로우를 개선한 소프트맥스 함수

a = np.array([0.3, 2.9, 4.0])
y = softmax_nof(a)

print(y)
print(np.sum(y))

# 소프트맥스 함수의 출력 총합은 1이기 때문에, 함수의 출력을 확률로 해석할 수 있다.
