# 두 개의 정수를 입력받아서 두 수 중 더 큰 수를 찾아서 큰 수를 리턴하는 함수를 만들어보자.
# return 문은 최소화하는 것이 좋은 코드이다.
def compare_func (a, b):
    if a > b :
        temp = a
    elif a < b :
        temp = b
    else :
        temp = "두 수가 같습니다."
    return temp


# 정수를 사용자로부터 입력받아서 제곱한 값을 반환하는 함수를 만들어 보시오.
# 사용자가 5를 입력하면 출력값은 25가 되어야 한다.

def square_func (input_value) :
    square_value = input_value * input_value
    return square_value

# 거듭제곱 구하는 함수

def power(x, y) :
    result = 1
    for i in range (y):
        result *= x
    return result