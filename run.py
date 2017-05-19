#!/usr/bin/env python3

from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter

if __name__ == '__main__':
    game1 = BattleshipsGame(RandomShooter())
    game1_shots = game1.play_game(rounds=1, debug=True)
    #print(game1_shots)
