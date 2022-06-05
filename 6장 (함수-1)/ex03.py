# 큰 수 출력하는 함수 활용

from calc import *

a = int(input("첫 번째 정수를 입력해주세요. : "))
b = int(input("두 번째 정수를 입력해주세요. : "))

result = compare_func(a, b)
print("결과 : ", result)

# 거듭제곱 코드

num1 = int(input("거듭 제곱 대상 숫자 : "))
num2 = int(input("거듭 제곱 횟수 숫자 : "))

value = power(num1, num2)
print(num1, "과", num2, "의 거듭제곱 값은 : ", value)