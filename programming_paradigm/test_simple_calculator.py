# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """
        Create a new SimpleCalculator instance before each test method runs.
        """
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        # You can add more edge cases as you like (floats, large numbers, etc.)

    def test_subtract(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_multiply(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_divide(self):
        """Test the divide method with normal inputs and special cases."""
        # Normal divisions
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        # Floating-point result
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Division by zero returns None
        self.assertIsNone(self.calc.divide(5, 0))
        # Negative over negative
        self.assertEqual(self.calc.divide(-6, -3), 2)

if __name__ == '__main__':
    unittest.main()
