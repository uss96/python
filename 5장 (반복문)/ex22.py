# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수, 스페이스의 개수를 출력하는 프로그램을 작성하시오.

original = input("문자열을 입력하세요 : ")
# 입력 받은 문자열을 전부 소문자로 변경한다.
word = original.lower() #대문자로 바꾸고 싶다면 upper() 사용
alpha = 0
num = 0
blank = 0

# 문자열의 길이가 0을 초과하고, 알파벳이라면 참을 반환
if len(original) > 0 :
    for ch in word:

        if ch in "abcdefghijklmnopqrstuvwxyz":
            alpha += 1
        elif ch in "1234567890":
            num += 1
        elif ch in " ":
            blank += 1

print("문자의 개수 : ", alpha)
print("숫자의 개수 : ", num)
print("공백의 개수 : ", blank)