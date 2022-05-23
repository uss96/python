# 더블 루프를 사용하여 아래와 같이 출력하는 프로그램 작성하기
# 출력 결과
# *
# **
# ***
# ****
# *****

# 더블 루프 이용

for i in range(5):
    for x in range(i+1):
        print("*", end="")
    print("")

# format 함수 이용
# format 함수는 {} 이용하고 숫자도 같이 이용된다.
# format 함수도 인덱스를 활용하여 해당하는 값들을 출력할 수 있다.
print("정수값 : {}, string : {}, float : {}".format(10, "안녕하세요", 10.10))
print("정수값 : {0}, string : {1}, float : {2}".format(10, "안녕하세요", 10.10))
print("정수값 : {2}, string : {1}, float : {0}".format(10, "안녕하세요", 10.10))

# format()는 공간확보 및 0으로 채우는 기능도 지원
# 콜론(:)을 기준으로 우측에 > 혹은 < 부등호를 사용해서 방향을 지정해줄 수 있다.
print("숫자 '{:>5d}'".format(300)) # 오른쪽으로 밀어서 출력
print("숫자 '{:<5d}'".format(300)) # 왼쪽으로 밀어서 출력

for i in range(5):
    print("{:<5}".format("*" * (i+1)))


for i in range (5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

for i in range (5, 0, -1):
    print("{:<5}".format("*" * (i)))