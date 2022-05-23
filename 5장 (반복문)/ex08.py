# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

n = int(input("구구단 몇 단을 출력할 건가? : "))

for i in range (1, 10, 1):
    if (n < 2) or (n > 9):
        print("정신머리가 있은 놈이니?")
        break
    else:
     print (n, "곱하기", i, "는", n*i)