import random
import unittest

import dice


class testDice(unittest.TestCase):
    def test_roll(self):
        random.seed(4)
        d = dice.Dice()
        self.assertEqual(d.roll(), "R")


unittest.main()
