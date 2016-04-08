
import unittest
from euler1 import sum_3_5_multipliers_below
from euler2 import sum_even_fibonacci_below
from euler3 import is_prime, largest_prime_factor

class Tests(unittest.TestCase):
    def test_euler1(self):
        self.assertEqual(sum_3_5_multipliers_below(1000), 233168)
        self.assertEqual(sum_3_5_multipliers_below(2), 0)
        self.assertEqual(sum_3_5_multipliers_below(4), 3)
        self.assertEqual(sum_3_5_multipliers_below(11), 33)


    def test_euler2(self):
        self.assertEqual(sum_even_fibonacci_below(2), 0)
        self.assertEqual(sum_even_fibonacci_below(4000000), 4613732)


    def test_euler3(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(15), False)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(9), 3)
if __name__ == '__main__':
    unittest.main()
