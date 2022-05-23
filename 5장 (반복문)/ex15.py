# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니깐 무한루프를 이용하고, 아울러 사용자가 "끝"이라고 입력을 하면 루프를 탈출하게끔 조건을 주도록 한다.
from operator import eq

cnt = 0
hap = 0
price = 0

while True :
    price = input(str(cnt + 1) + "번째 상품의 가격을 입력하세요. : ")
    if eq(price, "끝"):
        print(str(cnt) + "개의 상품 가격의 총액은 " + str(hap) + " 원 입니다.")
        break
    else :
        cnt += 1
        hap += int(price)
        print("상품의 총액 : %d, 계산을 끝내려면 '끝'이라고 입력해주세요." % hap)

