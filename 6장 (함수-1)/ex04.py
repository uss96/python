# 화씨 온도를 섭씨 온도로 변환하여 반환하는 함수 FtoC()를 작성하시오.
# 공식 : 화씨 = (9.0/5.0) * 섭씨 + 32

def main() :
    # 함수 호출
    print("화씨 온도", temp_f, "도는 섭씨 온도로", round(FtoC(temp_f), 1), "도 입니다.")

temp_f = float(input("화씨 온도를 입력하세요 : "))

def FtoC(temp_f) :
    result = (temp_f-32) * (5/9)
    return result

main()