#!/usr/bin/env python3

from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter

if __name__ == '__main__':
    game = BattleshipsGame(RandomShooter())
    game.play_game()
