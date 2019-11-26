#!/usr/bin/env python3
# --*-- encoding --*--

import re
import unittest

from papamath.calc import addition


class AdditionTest(unittest.TestCase):
    """
    Test addition module
    """

    def test_add_ints(self):
        """
        Test questions generator function
        """
        limit, num = 100, 3
        questioner = addition.add_ints(limit=limit, num=num)
        for _ in range(5):
            question, solution = next(questioner)
            addends = re.split(r'[+=]', question)[:num]
            self.assertEqual(sum(map(int, addends)), solution)


if __name__ == '__main__':
    unittest.main()
