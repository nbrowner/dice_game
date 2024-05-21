# Project 1 - Game Class
# Defines a game class to be used by the main program

import random

import dice
import player


class Game:
    # Initializes the Game class
    def __init__(self, players, start_chips, seed):
        self.players = players
        self.dice = dice.Dice()
        self.seed = seed
        random.seed(seed)

    # Plays a turn for the current player
    def play_turn(self, index):
        rolls = min(3, self.players[index].chips)

        if self.players[index].chips == 0:
            self.players[index].turns_left -= 1
        else:
            self.players[index].turns_left = 2

        for x in range(rolls):
            result = self.dice.roll()
            if result == "L":
                self.pass_chip(index, "L")
            elif result == "C":
                self.pass_chip(index, "C")
            elif result == "R":
                self.pass_chip(index, "R")

        if self.players[index].turns_left == 0:
            self.players.pop(index)

    # Passes a chip from the current player to the recipient
    def pass_chip(self, give_index, direction):
        if direction == "L":
            receive = self.get_next_player(give_index, -1)
        elif direction == "C":
            receive = "center"
        elif direction == "R":
            receive = self.get_next_player(give_index, 1)

        if receive == "center":
            self.players[give_index].chips -= 1
        else:
            self.players[give_index].chips -= 1
            self.players[receive].chips += 1

    # Determines the recipient
    def get_next_player(self, give_index, direction):
        if (give_index + direction) == len(self.players):
            return 0
        elif (give_index + direction) < 0:
            return len(self.players) - 1
        else:
            return give_index + direction

    # Checks to see if the game has been won
    def check_win(self):
        return len(self.players) == 1

    # Returns the winner's name
    def get_winner(self):
        winner = self.players[0]
        return winner.get_name()
