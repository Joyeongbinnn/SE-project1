
# 이스터에그 함수
def easterEgg(number):
    if number == 404:
        print('[EVENT]"not found"')
    elif number == 1004:
        print('[EVENT]"thanks for your kindness!""')
    elif number == 7942:
        print('[EVENT]"Amigo!""')
    elif number == 505:
        print('[EVENT]"SOS"')
    elif number == 777:
        print('[EVENT]"lucky!""')
    elif number == 82100:
        print('[EVENT]"빨리 돌아와"')
    elif number==1015:
        print('[EVENT]전북대 개교기념일입니다.')
    

# 메인 함수
def main():
    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

    num1 = get_integer_input()
    # 이스터에그
    easterEgg(num1)

    while True:
        operator = input("연산자를 입력하세요(+, -, *, =): ")
        if operator == '=':
            print(num1)
            break

        num2 = get_integer_input()  # 변경된 부분
        # 이스터에그
        easterEgg(num2)

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)
        else:
            print("잘못된 연산자입니다. 더하기(+), 빼기(-), 곱하기(*)만 가능합니다.")

if __name__ == "__main__":
    main()
