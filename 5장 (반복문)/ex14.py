# 임의의 숫자를 발생시켜 사용자로부터 입력을 받아 숫자를 맞추는 게임을 만들어보기
from random import *

cnt = 0
num = randint(1, 100)
print ("발생한 난수의 값 : ", num)

print("1부터 100 사이의 숫자를 맞추어 보세요.")
print("단, 기회는 10번입니다.")

while cnt < 10:
    guess = int(input("숫자를 입력하세요 : "))
    cnt += 1
    if guess < num:
        print("입력한 수가 난수보다 작습니다.")

    elif guess > num :
        print("입력한 수가 난수보다 큽니다.")

    else :
        print("정답입니다. 시도 횟수 :", cnt)
        break

print("기회 10번이 다 소진되었습니다. 게임이 종료되었습니다.")