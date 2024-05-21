# Project 1 - Main Program
# Main program for the dice game project

import random

import game
import player


def main():
    print("Welcome to the dice game!\n")

    # Prompts user for a seed
    gameSeed = input("Please enter a seed: ")

    # Checks if input is a valid seed
    try:
        gameSeed == int(gameSeed)
    except:
        print("Invalid seed: input is not an integer\n")
        while type(gameSeed) != int:
            try:
                gameSeed = int(input("Please enter a seed: "))
            except:
                print("Invalid seed: input is not an integer\n")

    # Prompts user for starting chip amount
    numChips = input("Please enter the starting amount of chips: ")

    # Checks if input is a valid integer
    try:
        numChips == int(numChips)
    except:
        print("Invalid input: input is not an integer\n")
        while type(numChips) != int:
            try:
                numChips = int(input("Please enter the starting amount of chips: "))
            except:
                print("Invalid input: input is not an integer\n")

    # Prompt user for number of players
    numPlayers = input("Please enter the number of players (3+): ")

    # Checks if input is a valid integer
    try:
        numPlayers == int(numPlayers)
    except:
        print("Invalid input: input is not an integer\n")
        while type(numPlayers) != int:
            try:
                numPlayers = int(input("Please enter the number of players (3+): "))
            except:
                print("Invalid input: input is not an integer\n")

    # Check if less than three players have been declared
    if int(numPlayers) < 3:
        print("Invalid player count: must be three or more players\n")
        tooSmall = True
    else:
        tooSmall = False

    while tooSmall == True:
        numPlayers = input("Please enter the number of players (3+): ")
        if int(numPlayers) < 3:
            print("Invalid player count: must be three or more players\n")
            tooSmall = True
        else:
            tooSmall = False

    # Fix input variables for compatability
    gameSeed = int(gameSeed)
    numChips = int(numChips)
    numPlayers = int(numPlayers)

    # Variables for player name input counter
    counter = 1
    players = []

    # Ask for each player's name
    while counter <= numPlayers:
        print(f"Enter Player {counter}'s name:")
        p = input()
        players.append(player.Player(numChips, p))
        counter += 1

    # Start of new game
    new_game = game.Game(players, numChips, gameSeed)

    # Variables for turn counter and player index
    turns = 0
    ind = 0

    # Game loops until winner is found
    while new_game.check_win() != True:
        print(ind)
        new_game.play_turn(ind)

        if ind == (len(new_game.players) - 1):
            ind = 0
        elif ind == len(new_game.players):
            ind = 0
        else:
            ind += 1

        turns += 1

    # Pulls winner from game
    winner = new_game.get_winner()

    # Prints winners name
    print(f"The winner is {winner} after {turns} turns!")


# Runs everything
main()
