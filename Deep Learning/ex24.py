import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, 10)

# 60000개의 훈련 데이터 중 784개의 입력 데이터, 10개의 정답 데이터

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(t_batch)

# 10개의 배치 데이터를 임의로 뽑기...?

def cross_entropy_error(y, t) :
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

# 정답 레이블이 원-핫 인코딩인 경우의 교차 엔트로피 오차

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] +1e-7)) / batch_size

# 정답 레이블이 원-핫 인코딩이 아닌, '2'나 '7' 등의 숫자 레이블인 경우의 교차 엔트로피 오차



