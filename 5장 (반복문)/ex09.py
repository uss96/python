#사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터 두 번째 입력받은 값까지의 범위에서 3의 배수이고 4의 배수를 제외하고 출력하는 프로그램을 작성하시오.

n1 = int(input("첫 번째 정수를 입력하시오 : "))
n2 = int(input("두 번째 정수를 입력하시오 : "))

if n1 > n2:
    for i in range (n2, n1+1):
        if (i % 3 != 0) and (i % 4 != 0) :
            print(i)
elif n1 == n2:
    print(n1,"과",n2,"가 같은 숫자입니다.")

else:
    for i in range (n1, n2+1):
        if (i % 3 != 0) and (i % 4 != 0) :
            print(i)