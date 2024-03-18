import unittest
from src.calculations import Calculations


class testCalculations(unittest.TestCase):

    def test_sum(self):
        self.assertEquals(Calculations.sum(1, 1), 2)
        self.assertEquals(Calculations.sum(8, 12), 20)
        self.assertEquals(Calculations.sum(9, -1021), -1012)

    def test_multiplication(self):
        self.assertEquals(Calculations.multiplication(1, 1), 1)
        self.assertEquals(Calculations.multiplication(0, 3), 0)
        self.assertEquals(Calculations.multiplication(-5, 3), -15)
        self.assertEquals(Calculations.multiplication(5, 8), 40)

    def test_division(self):
        self.assertEquals(Calculations.division(3, 1), 3.0)
        self.assertEquals(Calculations.division(16, 2), 8.0)
        self.assertEquals(Calculations.division(1, 5), 0.2)
        self.assertEquals(Calculations.division(6, -2), -3.0)

        with self.assertRaises(ZeroDivisionError):
            Calculations.division(4, 0)


if __name__ == "__main__":
    unittest.main()
