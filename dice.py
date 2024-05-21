# Project 1 - Dice Class
# Defines a dice class to be used by the game class

import random


class Dice:
    # Rolls dice and returns the result
    def roll(self):
        num = random.randint(1, 6)
        if num == 1:
            return "L"
        elif num == 2:
            return "R"
        elif num == 3:
            return "C"
        else:
            return "."
