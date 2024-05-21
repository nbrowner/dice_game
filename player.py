# Project1 - Player Class
# Defines a player class to be inherited by the game class

import unittest


class Player:
    # Initializes the player class
    def __init__(self, start_chips, name):
        self.chips = start_chips
        self.name = name
        self.turns_left = 2

    # Checks if player has chips remaining
    def has_chips(self):
        return self.chips > 0

    # Returns the players name
    def get_name(self):
        return self.name
