import unittest
from calculator import Calculator

class testCalculator(unittest.TestCase):
    def test_add(self):
        #test add method
        self.assertEqual(Calculator.add(1, 1), 2)

if __name__ == "__main__":
    unittest.main()