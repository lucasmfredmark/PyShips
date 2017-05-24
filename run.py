#!/usr/bin/env python3

import matplotlib.pyplot as plt
from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter
from classes.ai.HuntTargetShooter import HuntTargetShooter
from classes.ai.ParityShooter import ParityShooter
from classes.ai.ProbabilityShooter import ProbabilityShooter

number_of_rounds = 10000
number_of_shots = 100

def plot_chart(plot_data, data_label):
    # prepare the data
    keys, values = zip(*plot_data)

    # make the plot
    plt.plot(keys, values, label=data_label)
    plt.title('Distribution of shots taken to win (over {} rounds)'.format(number_of_rounds))
    plt.legend(loc='upper left')
    plt.xlim(xmin=0, xmax=number_of_shots)
    plt.ylim(ymin=0)
    plt.xticks(range(0, number_of_shots + 1, 5))
    plt.xlabel('Number of shots')
    plt.ylabel('Number of rounds')

if __name__ == '__main__':
    game1_data = BattleshipsGame(RandomShooter()).play_game(rounds=number_of_rounds)
    game2_data = BattleshipsGame(HuntTargetShooter()).play_game(rounds=number_of_rounds)
    game3_data = BattleshipsGame(ParityShooter()).play_game(rounds=number_of_rounds)
    game4_data = BattleshipsGame(ProbabilityShooter()).play_game(rounds=number_of_rounds)

    plot_chart(game1_data, 'Random shooter')
    plot_chart(game2_data, 'Hunt/Target shooter')
    plot_chart(game3_data, 'Parity shooter')
    plot_chart(game4_data, 'Probability shooter')

    plt.show()
