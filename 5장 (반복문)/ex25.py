# 입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오.

statements = input("문자열을 입력하세요 : ")

s_reverse = ""

for ch in statements:
    s_reverse = ch + s_reverse

print("입력한 문자열 : " + statements)
print("역순으로 출력한 문자열 : " + s_reverse)

# list() 함수는 문자열을 리스트 타입으로 바꾸는 함수이다.
s_list = list(statements)
print(type(s_list))
print("s_list : ", s_list)
s_list.reverse()
#join() 함수는 역순으로 된 문자열을 연결해서 출력을 하고 있는 코드
print("".join(s_list))

print("------------------------------")
print(statements[::-1])
print(statements[3::-1])