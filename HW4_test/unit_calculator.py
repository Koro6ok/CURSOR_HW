import unittest
from function_to_test import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_substract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3, 2), 6)

    def test_devide(self):
        self.assertRaises(ValueError, Calculator.divide, 6, 0)

if __name__ == '__main__':
    unittest.main()
