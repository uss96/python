# 소수를 2부터 계속 더할 때, 2000보다 작은 최대합은 얼마이고
# 마지막으로 더해지는 소수는 얼마인지 출력하는 프로그램
# 더블루프, 조건식 사용

start_num = 0
num = 0
hap = 0
lastData = 0

for num in range (2, 2001):
    for start_num in range(2, num+1):
        if num % start_num == 0:
            break
    if num == start_num:
        print("소수 : ", start_num)
        hap += start_num
        print("합계 : ", hap)
        lastData = start_num
        print("마지막 소수의 값 : ", lastData)
        print("=============================")