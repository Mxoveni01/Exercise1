import unittest
from data_structures import *
from io import StringIO
import sys

class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, 2, -3, 4, -5, 6, -9, 10]), 10)
        self.assertEqual(find_max([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), 19)

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-1, 2, -3, 4, -5, 6, -9, 10]), -9)
        self.assertEqual(find_min([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -20)

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(find_average([-1, 2, -3, 4, -5, 6, -9, 10]), 0.5)
        self.assertEqual(find_average([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -0.5)

    def test_find_even_pairs(self):
        self.assertEqual(find_even_pairs([1, 2, 3, 4, 5]), [])
        self.assertEqual(find_even_pairs([1, 2, 3, 4, 5, 6]), [])
        self.assertEqual(find_even_pairs([6, 2, 3, 5, 9, 4, 1, 11]), [(0, 1), (2, 3), (3, 4), (6, 7)])

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_5_square(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        draw_square(10)
        self.assertEqual(
            """**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
""",
            text_capture.getvalue(),
        )


if __name__ == "__main__":
    unittest.main()