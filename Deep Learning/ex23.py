import numpy as np

# 손실함수 교차 엔트로피 오차

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# ex 1) '2'일 확률이 가장 높다고 추정 (0.6)

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
error1 = cross_entropy_error(np.array(y1), np.array(t))

print(error1)

# ex 2) '7'일 확률이 가장 높다고 추정 (0.6)

y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
error2 = cross_entropy_error(np.array(y2), np.array(t))

print(error2)