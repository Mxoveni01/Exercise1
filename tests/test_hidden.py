import unittest
from data_structures import *

class TestHidden(unittest.TestCase):

    def test_fizz_buzz(self):
        # fizz cases
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")
        self.assertEqual(fizz_buzz(9), "Fizz")

        # buzz cases
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(20), "Buzz")

        # fizzbuzz cases
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
        self.assertEqual(fizz_buzz(45), "FizzBuzz")

        # not divisible by 3 or 5
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(7), 7)

        # invalid input
        cases = [
            (0, "Expected a value error when 0 is entered"),
            ("3", "Expected a value error when a string is entered as an argument")
            ([3,5],"Expected a value error when a list is entered as an argument")
            ({"fizz":3,"buzz":5}, "Expected a value error when a dictionary is entered as an argument")
        ]

        for case in cases:
            with self.assertRaises(ValueError, msg=case[1]):
                fizz_buzz(case[0])

    def test_is_palindrome(self):
        # True cases
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")

        # False cases
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")
        self.assertTrue(is_palindrome("civic"), "Expected true when civic is entered")

    def test_factorial(self):
        self.assertEquals(factorial(5), 120)
        self.assertEquals(factorial(0), 1)
        with self.assertRaises(ValueError, msg="negative values are not allowed"):
            factorial(-1)

    def test_anagrams(self):
        self.assertTrue(are_anagrams("listen","silent"))
        self.assertTrue(are_anagrams("a gentleman","elegant man"))
        self.assertFalse(are_anagrams("rub","bake"))

    def test_n_0(self):
            # Test for n = 0 (base case)
            self.assertEqual(pascal_triangle(0), [1])

    def test_n_3(self):
        # Test for n = 3
        self.assertEqual(pascal_triangle(3), [1, 3, 3, 1])

    def test_n_5(self):
        # Test for n = 5
        self.assertEqual(pascal_triangle(5), [1, 5, 10, 10, 5, 1])

    def test_n_negative(self):
        # Test for a negative value of n
        with self.assertRaises(ValueError):
            pascal_triangle(-1)

    def test_n_large(self):
        # Test for a large value of n
        self.assertEqual(pascal_triangle(20), [1, 20, 190, 1140, 4845, 15504, 38760, 77520, 125970, 167960, 184756, 167960, 125970, 77520, 38760, 15504, 4845, 1140, 190, 20, 1])


if __name__ == '__main__':
    unittest.main()


if __name__ == "__main__":
    unittest.main()
