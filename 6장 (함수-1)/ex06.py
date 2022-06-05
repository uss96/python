# 간단한 사칙연산 계산기 만들기

# 더하기 함수
def add(x, y):
    return x+y

# 빼기 함수

def substract(x, y):
    temp = 0
    if x > y :
        temp = x-y
    elif x < y :
        temp = y-x
    else :
        temp = 0
    return temp

# 곱하기 함수

def multiply (x, y):
    return x * y

# 나누기 함수

def divide (x, y):
    return round((x / y), 2)

temp = "y"

while True:
    if temp == "n":
        print("계산기를 종료합니다.")
        break
    elif temp == "y":
        n1 = float(input("첫 번째 수 입력 : "))
        n2 = float(input("두 번째 수 입력 : "))

        op = input("원하는 연산을 입력(+, -, *, /) : ")

        if op == "+":
            print("두 수의 합은 : ", add(n1, n2))
        elif op == "-":
            print("두 수의 차는 : ", substract(n1, n2))
        elif op == "*":
            print("두 수의 곱은 : ", multiply (n1, n2))
        elif op == "/":
            print("두 수의 나누기는 : ", divide(n1, n2))
        else :
            print("잘못된 연산자입니다.")
    else :
        print("제대로 된 종료문자를 입력하세요.")
    temp = input("계속 계산하시겠습니까? (y or n) : ")
