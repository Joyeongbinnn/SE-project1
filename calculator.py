def multiply(x, y):
    if not (isinstance(x, int)) or not (isinstance(y, int)):
        raise ValueError("Error: Please use Integer")
    result = x * y
    return result

<<<<<<< HEAD
# 메인 함수
def main():  
    
    num1 = input("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")
    if num1 = ' ':#이스터에그
    
    operator = input
    num2 = input
            
    num1, num2 = get_numbers()
    
    if operator == '+':
        print("결과: ", add(num1, num2))
    elif operator == '-':
        print("결과: ", subtract(num1, num2))
    elif operator == '*':
        print("결과: ", multiply(num1, num2))
    
=======
# 메인 함수.
def main():

    print("간단한 계산기 입니다. 더하기, 빼기, 곱하기만 가능합니다.")

    num1 = int(input())
    # 이스터에그
    while True:
        operator = input()
        if operator == '=':
            print(num1)
            break
        num2 = int(input())

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)

>>>>>>> 7c20283d19341caacd1f1b21078d45869864bbc6

if __name__ == "__main__":
    main()
