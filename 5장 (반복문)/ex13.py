# 사용자로부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후 출력하는 프로그램을 작성해보시오.
# 단, 센티널은 음수의 값을 사용하시오.

cnt = 0
hap = 0
score = 0

# 센티널(보초값)을 사용자에게 제시하는 코드
print("종료하시려면 음수를 입력하세요. (예 : -1)")

while score >= 0:
    score = int(input(str(cnt+1) + "번째 학생의 성적을 입력해주세요 : "))
    if score >= 0:
        hap += score
        cnt += 1
hap = hap/cnt
print("성적의 평균은 %.1f입니다." %hap)