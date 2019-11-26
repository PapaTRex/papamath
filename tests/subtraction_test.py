#!/usr/bin/env python3
# --*-- encoding --*--

import re
import unittest

from papamath.calc import subtraction as sub


class SubtractionTest(unittest.TestCase):
    """
    Test subtraction module
    """

    def test_sub_ints(self):
        """
        Test questions generator function
        """
        limit = 100
        questioner = sub.sub_ints(limit=limit)
        for _ in range(5):
            question, solution = next(questioner)
            subtracted, subtraction, *_ = re.split(r'[-=]', question)
            self.assertEqual(int(subtracted) - int(subtraction), solution)


if __name__ == '__main__':
    unittest.main()
