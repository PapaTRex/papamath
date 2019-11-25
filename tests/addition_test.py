#!/usr/bin/env python3
# --*-- encoding --*--

import re
import unittest

from calc import addition


class AdditionTest(unittest.TestCase):
    """
    Test addition module
    """

    def test_questions(self):
        """
        Test questions generator function
        """
        limit = 100
        questioner = addition.questions(limit)
        for _ in range(5):
            question, solution = next(questioner)
            left, right, *_ = re.split(r'[+=]', question)
            self.assertEqual(int(left.strip()) + int(right.strip()), solution)


if __name__ == '__main__':
    unittest.main()
