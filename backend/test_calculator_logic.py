import unittest
import calculator_logic

class TestCalculatorLogic(unittest.TestCase):

    def test_ad(self):
        self.assertEqual(calculator_logic.add(2, 3), 5)
        self.assertEqual(calculator_logic.add(2, -1), 1)
        self.assertEqual(calculator_logic.add(-2, 1), -1)
        self.assertEqual(calculator_logic.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator_logic.subtract(5, 2), 3)
        self.assertEqual(calculator_logic.subtract(-4, 2), -6)
        self.assertEqual(calculator_logic.subtract(0, 8), -8)

    def test_multiply(self):
        self.assertEqual(calculator_logic.multiply(2, 3), 6)
        self.assertEqual(calculator_logic.multiply(0, 5), 0)
        self.assertEqual(calculator_logic.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator_logic.divide(5, 2), 2.5)
        self.assertEqual(calculator_logic.divide(0, 5), 0)
        self.assertEqual(calculator_logic.divide(7, 7), 1)
        self.assertEqual(calculator_logic.divide(-5, 2), -2.5)
        self.assertEqual(calculator_logic.divide(6, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()