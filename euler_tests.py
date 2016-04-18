
import unittest
from euler1 import sum_3_5_multipliers_below
from euler2 import sum_even_fibonacci_below
from euler4 import is_palindrome, biggest_palindrome_for_2_numbers
from euler5 import get_factors, list_difference

class Tests(unittest.TestCase):
    def test_euler1(self):
        self.assertEqual(sum_3_5_multipliers_below(1000), 233168)
        self.assertEqual(sum_3_5_multipliers_below(2), 0)
        self.assertEqual(sum_3_5_multipliers_below(4), 3)
        self.assertEqual(sum_3_5_multipliers_below(11), 33)


    def test_euler2(self):
        self.assertEqual(sum_even_fibonacci_below(2), 0)
        self.assertEqual(sum_even_fibonacci_below(4000000), 4613732)


    def test_euler4(self):
        self.assertEqual(is_palindrome(90), False)
        self.assertEqual(is_palindrome(901), False)
        self.assertEqual(is_palindrome(909109), False)
        self.assertEqual(is_palindrome(909909), True)
        self.assertEqual(is_palindrome(99), True)
        self.assertEqual(biggest_palindrome_for_2_numbers(2), 9009)
        self.assertEqual(biggest_palindrome_for_2_numbers(3), 906609)


    def test_euler5(self):
        self.assertEqual(get_factors(4),[2,2])
        self.assertEqual(get_factors(6),[2,3])
        self.assertEqual(get_factors(17),[17])
        self.assertEqual(list_difference([1], [1,1,2,3]), [1,2,3])
        self.assertEqual(list_difference([1,2,3], [1,1,2,3]), [1])


if __name__ == '__main__':
    unittest.main()
