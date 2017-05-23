#!/usr/bin/env python3

from classes.BattleshipsGame import BattleshipsGame
from classes.ai.ProbabilityShooter import ProbabilityShooter

if __name__ == '__main__':
    BattleshipsGame(ProbabilityShooter()).play_game(rounds=1, debug=True)
