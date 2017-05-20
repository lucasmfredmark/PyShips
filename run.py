#!/usr/bin/env python3

from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter
from classes.ai.ParityShooter import ParityShooter

if __name__ == '__main__':
    game1 = BattleshipsGame(ParityShooter())
    game1_shots = game1.play_game(rounds=100, debug=False)
    print(game1_shots)
