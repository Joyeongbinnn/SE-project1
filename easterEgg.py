
#�̽��Ϳ��� 

def easterEgg(number):
    if number == 7:
        print("LUCKY!")

# ���� �Լ�
def main():
    print("������ ���� �Դϴ�. ���ϱ�, ����, ���ϱ⸸ �����մϴ�.")

    num1 = get_integer_input()
    # �̽��Ϳ���
    easterEgg(num1)

    while True:
        operator = input("�����ڸ� �Է��ϼ���(+, -, *, =): ")
        if operator == '=':
            print(num1)
            break

        num2 = get_integer_input()  # ����� �κ�
        # �̽��Ϳ���
        easterEgg(num2)

        if operator == '+':
            num1 = add(num1, num2)
        elif operator == '-':
            num1 = subtract(num1, num2)
        elif operator == '*':
            num1 = multiply(num1, num2)
        else:
            print("�߸��� �������Դϴ�. ���ϱ�(+), ����(-), ���ϱ�(*)�� �����մϴ�.")

if __name__ == "__main__":
    main()