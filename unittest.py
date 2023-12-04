import unittest

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
    main()
    unittest.main(exit=False)