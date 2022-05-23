# 1. 증속, 2. 감속, 3. 중지를 출력하고 사용자의 입력을 1, 2, 3으로 받아서
# 증속을 하면 속도를 10씩 증가하고 출력해준다.
# 감속을 하면 속도를 10씩 감소하고 출력해준다.
# 중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나간다.

from operator import eq

velo = 0


while True:
    inpu = input("속도 조정값을 입력해주세요 (1 : 증속, 2 : 감속, 3 : 중지) : ")
    if eq(inpu, "3"):
        print("중지합니다.")
        break
    elif eq(inpu, "1"):
        velo += 10
        print("현재 속도는 %d입니다." %velo)
    elif eq(inpu, "2"):
        velo -= 10
        print("현재 속도는 %d입니다." %velo)

