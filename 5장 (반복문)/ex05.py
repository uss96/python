# for문을 이용하여 팩토리얼을 계산하는 프로그램을 작성해보자.
# 팩토리얼 n!은 1부터 n까지의 정수의 모든 곱

factorial = 1.0
n = int(input("정수값을 입력하시오 : "))

for i in range (1, n+1):
    factorial *= i

print(n, "!은", factorial, "입니다.")