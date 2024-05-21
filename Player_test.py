import unittest

import player


class testPlayer(unittest.TestCase):
    def test_chips(self):
        d = player.Player(10, "Joe")
        d.turn()
        self.assertEqual(d.has_chips(), True)

    def test_name(self):
        d = player.Player(10, "Joe")
        self.assertEqual(d.get_name(), "Joe")


unittest.main()
