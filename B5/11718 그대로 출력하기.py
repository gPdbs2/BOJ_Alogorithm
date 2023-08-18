# 11718 그대로 출력하기

# 반복문을 통해 입력받는 값들은 모두 출력
while True:
    try:
        print(input())
    # EOFError : End Of File -> 입력 값의 끝 글자
    # 문자의 끝 글자를 확인 후 break를 걸어 반복문 종료
    except EOFError:
        break