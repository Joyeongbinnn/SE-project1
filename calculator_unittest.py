import unittest

# 더하기 함수
def add(x, y):
    return x + y

# 빼기 함수
def subtract(x, y):
    return x - y

# 곱하기 함수
def multiply(x, y):
    return x * y

# 팩토리얼 함수
def factorial(n):
    if n < 0:
        raise ValueError("[ERROR] Out Of Range")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 이스터에그 함수
def easterEgg(number):
  if number == 404:
    print('[EVENT]"not found"')
  elif number == 1004:
    print('[EVENT]"thanks for your kindness!"')
  elif number == 7942:
    print('[EVENT]"Amigo!"')
  elif number == 505:
    print('[EVENT]"SOS"')
  elif number == 777:
    print('[EVENT]"lucky!"')
  elif number == 82100:
    print('[EVENT]"빨리 돌아와"')
  elif number == 1015:
    print('[EVENT]전북대 개교기념일입니다.')

# 메인 함수
def main():
    flag = True
    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기, 팩토리얼만 가능합니다.")
    try:
        num1 = int(input())
    except:
        flag = False
        num1 = 1
    easterEgg(num1)
    last_operator = None  # 이전 연산자를 저장할 변수 추가

    while True:
        operator = input()
        if operator == '=':
            if flag == False:
                print("ERROR!")
                break
            print(num1)
            break
        elif operator == '!':
            try:
                # 두 번째 숫자 입력을 받음
                num2 = int(input())
                # 두 개 이상의 숫자가 입력된 경우 에러 메시지 출력
                print("[ERROR] Input Error")
                break
            except ValueError:
                flag = False
                num2 = 1
            except:
                flag = False
                num2 = 1

            try:
                result = factorial(num1)
                print(result)
            except ValueError as e:
                print(str(e))
                break
            except:
                print("[ERROR] Input Error")
                break
        else:
            if last_operator and operator != last_operator:  # 두 가지 이상의 연산자 사용 시 에러 메시지 출력
                print("ERROR! 한 종류의 연산자만 사용 가능")
                break

            try:
                num2 = int(input())
            except:
                flag = False
                num2 = 1
            easterEgg(num2)

            if operator == '+':
                num1 = add(num1, num2)
            elif operator == '-':
                num1 = subtract(num1, num2)
            elif operator == '*':
                num1 = multiply(num1, num2)
            else:
                flag = False

            last_operator = operator  # 현재 연산자를 이전 연산자로 저장

# 유닛 테스트
class TestCalculatorFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 7), 0)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)

        with self.assertRaises(ValueError):
            factorial(-1)  # 음수에 대한 팩토리얼은 예외 발생 확인

if __name__ == '__main__':
    unittest.main(exit=False)
    main()