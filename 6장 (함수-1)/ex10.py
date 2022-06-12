# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자.
# 그리고, 반지름을 사용자로부터 입력받고 구의 부피를 구하는 함수를 호출해서 테스트 하라.

import math

def sphereVolume(r):
    volume = 4/3 * pow(r, 3) * math.pi
    return volume

continue_value = "y"

while True :
    if continue_value == "n":
        print("구 부피 계산기를 종료합니다.")
        break

    elif continue_value == "y":
        radius = float(input("구의 반지름을 입력하세요 : "))
        volume = sphereVolume(radius)
        print("반지름이 ", radius, "인 구의 부피는", round(volume, 2), "입니다." )
        input("계속 하시겠습니까? (y or n) : ")


