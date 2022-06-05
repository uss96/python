# 함수(function)에 대한 실습

# 1. 함수는 프로그램 안에서 중복된 코드를 제거한다.
# 2. 복잡한 프로그래밍 작업을 더 간단한 작업으로 분해할 수 있다.
# 3. 함수는 한 번 만들어두면 재사용이 언제든지 가능하다.
# 4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.

# 간단한 함수
# def 키워드 함수이름(매개변수)

from hello import *


# 위와 같이 함수를 정의만 했다면 출력값은 없다. 출력값이 나오게 하려면 호출(call)을 해야한다.
# 함수 호출 (function call)

say_hello_name("신은혁")
say_hello_name("홍길동")

# 함수가 호출되어 10을 출력하긴 하지만, 가독성이 좋지 않다.
# 이유는 함수의 매개변수명이 name이니, 웬만하면 이름을 매개변수 값으로 주는 것이 현명한 코드가 될 것이다.
# say_hello(10)

say_hello_name_msg("신은혁", "반갑습니다.")
say_hello_name_msg("홍길동", "도와주세요.")
# 파이썬에서는 오버로딩의 개념이 없다. 같은 함수의 이름이라면 마지막에 정의되어진 함수만 인식하게 된다. 하여, 함수명은 유니크한 값으로 이름을 짓도록 한다.

# 값을 반환하는 함수 예제


result = get_sum(1, 10)
print(type(result))
print("1~10 누적합 : ", result)

result = get_sum(1, 30)
print(type(result))
print("1~10 누적합 : ", result)

result = get_sum(1, 100)
print(type(result))
print("1~10 누적합 : ", result)
