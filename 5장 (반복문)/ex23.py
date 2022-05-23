# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력받도록 하고 출력을 할 때는 "-" 삭제를 한 문자열을 출력하는 프로그램을 작성하시오.

phone_num = input("전화번호를 입력하세요 : ")
result = ""

if len(phone_num) == 12 or len(phone_num) == 13:
    for letter in phone_num:
        if letter not in "-" :
            result += letter
    else:
        print("번호 입력이 잘못되었습니다.")

print("번호 숫자 : ", result)
