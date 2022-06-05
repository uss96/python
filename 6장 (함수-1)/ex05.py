# 사용자로부터 정수를 입력바당 소수를 판별하는 함수 is_prime()을 작성해보자.
# 소수면 True, 아닐 경우 False 출력
# 1과 자기 자신과 나누어지는 수를 소수라 한다.
def is_prime(num) :
    for i in range(2, num):
        temp = True
        if (num%i) == 0:
            temp = False
        else :
            temp = True
        return temp

prime = int(input("정수를 입력하세요 : "))

# 함수 호출

print(is_prime(prime))


