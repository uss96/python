import numpy as np
import matplotlib.pyplot as plt

# 은닉층의 활성화값 분포

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

x = np.random.randn(1000, 100) # 1000개의 데이터
node_num = 100 # 각 은닉층의 노드(뉴런) 수
hidden_layer_size = 5 #은닉층이 5개
activations = {} # 이곳에 활성화 결과 (활성화값)를 저장

for i in range (hidden_layer_size):
    if i != 0 :
        x = activations[i-1]

    # w = np.random.randn(node_num, node_num) * 1 # 가중치의 표준편차가 1인 경우
    # w = np.random.randn(node_num, node_num) * 0.01 # 가중치의 표준편차가 0.01인 경우
    # w = np.random.randn(node_num, node_num) / np.sqrt(node_num) # 자비에 초깃값 (초깃값의 표준편차가 1/root(n)이 되도록)
    w = np.random.randn(node_num, node_num) / np.sqrt(node_num/2) # He 초깃값 (초깃값의 표준편차가 1/root(n/2)이 되도록)
    a = np.dot(x, w)
    z = sigmoid(a)
    activations[i] = z

for i, a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range = (0, 1))

plt.show()
# 가중치의 표준편차가 1일 때 히스토그램을 통해 출력이 0 또는 1에 가까워질수록 기울기가 0에 가까워지는, 기울기 소실을 확인할 수 있음
# 가중치의 표준편차가 0.01일 때에는 0, 1로 치우치진 않음! -> 기울기 소실 문제는 일어나지 않음, 그러나 활성화값이 0.5 부근에 집중되어 표현력을 제한함 ㅠㅠ
# 각 층의 활성화값은 적당히 고루 분포되는 게 가장 좋다! 층과 층 사이에 적당하게 다양한 데이터가 흘러야 신경망 학습이 효율적으로 이뤄지기 때문

# 자비에 초깃값을 사용할 경우, 앞 층에 노드가 많을수록 대상 노드의 초깃값으로 설정하는 가중치가 좁게 퍼진다!
# 층이 깊어지며 형태가 다소 일그러지지만, 이전보단 넓게 분포되긴 함! 이걸 해결하려면 시그모이드 대신 tanh함수 활용하면 됨 (시그모이드, tanh의 경우 자비에)

# He 초깃값은 ReLU를 사용할 때 사용! 음의 영역이 0이라서 더 넓게 분포시키기 위해 2배의 계수가 필요




