
import unittest
from euler1 import sum_3_5_multipliers_below
from euler2 import sum_even_fibonacci_below

class Tests(unittest.TestCase):
    def test_euler1(self):
        self.assertEqual(sum_3_5_multipliers_below(1000), 233168)
        self.assertEqual(sum_3_5_multipliers_below(2), 0)
        self.assertEqual(sum_3_5_multipliers_below(4), 3)
        self.assertEqual(sum_3_5_multipliers_below(11), 33)


    def test_euler2(self):
        self.assertEqual(sum_even_fibonacci_below(2), 0)
        self.assertEqual(sum_even_fibonacci_below(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()
