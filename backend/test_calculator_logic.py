import unittest
import backend.logic as logic

class TestCalculatorLogic(unittest.TestCase):

    def test_ad(self):
        self.assertEqual(logic.add(2, 3), 5)
        self.assertEqual(logic.add(2, -1), 1)
        self.assertEqual(logic.add(-2, 1), -1)
        self.assertEqual(logic.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(logic.subtract(5, 2), 3)
        self.assertEqual(logic.subtract(-4, 2), -6)
        self.assertEqual(logic.subtract(0, 8), -8)

    def test_multiply(self):
        self.assertEqual(logic.multiply(2, 3), 6)
        self.assertEqual(logic.multiply(0, 5), 0)
        self.assertEqual(logic.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(logic.divide(5, 2), 2.5)
        self.assertEqual(logic.divide(0, 5), 0)
        self.assertEqual(logic.divide(7, 7), 1)
        self.assertEqual(logic.divide(-5, 2), -2.5)
        self.assertEqual(logic.divide(6, 0), "Error: Division by zero")

if __name__ == "__main__":
    unittest.main()