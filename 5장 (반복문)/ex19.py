# 더블루프를 이용해 아래를 출력하는 프로그램 작성하기
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    print("*" * (2*i-1), end="")
    for j in range(5-i):
        print(" ", end="")
    print("")

for i in range (1, 11, 2):
    print("{:^9}".format("*" * i))


for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    print("*" * (2*i-1), end="")
    for j in range(5-i):
        print(" ", end="")
    print("")
for i in range(5):
    for j in range(i):
        print(" ", end="")
    print("*" * (9-2*i), end="")
    for j in range(i):
        print(" ", end="")
    print("")