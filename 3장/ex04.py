# 문자열에 대한 실습

# 큰따옴표(double quotation)로 묶으면 문자열이 된다. (권장)
welcome = "Happy New Year 2022"
print(welcome)

# 작은 따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2022'
print(welcome)

# 문자열을 만들때 시작을 "로 했는데 '로 끝내면, EOL(End of Line) 에러가 발생한다.
# 그 이유는 "로 시작을 했는데 "의 끝내용을 찾을 수 없기 때문

# welcome = "Happy New Year 2022'
# welcome = "Happy New Year 2022

# 아래와 같이 "" 안에 또 다른 ""이 들어있다면 컴파일러가 혼돈을 일으켜 틀린 문법이다라고 에러가 발생
# message = "인호형이 "안녕하세요"라고 인사했습니다."
# print(message)

message = "인호형이 '안녕하세요'라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하고자 할 때, \를 이용한다.
# \가 따옴표 앞에 있으면 '는 특수한 의미를 잃어버리고 하나의 문자로 편승이 되어 문자열을 이룬다.
message = 'doesn\'t'
print(message)

message = "\"Yes,\" I can do it"
print(message)