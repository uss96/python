import numpy as np

# 손실함수 오차제곱합

def sum_squares_error (y, t) :
    return 0.5 * np.sum((y-t)**2)

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# ex 1) '2'일 확률이 가장 높다고 추정 (0.6)

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
error1 = sum_squares_error(np.array(y1), np.array(t))

print(error1)

# ex 2) '7'일 확률이 가장 높다고 추정 (0.6)

y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
error2 = sum_squares_error(np.array(y2), np.array(t))

print(error2)