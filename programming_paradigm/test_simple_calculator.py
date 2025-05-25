import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a fresh SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Check various scenarios for the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Check various scenarios for the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiplication(self):
        """Check various scenarios for the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_division(self):
        """Check various scenarios for the divide method, including edge cases."""
        # Normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))
        # Negative over negative
        self.assertEqual(self.calc.divide(-6, -3), 2)

if __name__ == '__main__':
    unittest.main()
