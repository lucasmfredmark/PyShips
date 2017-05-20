import matplotlib.pyplot as plt
from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter
from classes.ai.HuntingShooter2 import HuntingShooter
from classes.ai.ParityShooter import ParityShooter


def plotChart(plotting_data, label):
    
    # prepare the data
    keys = [value[0] for value in plotting_data]
    values = [value[1] for value in plotting_data]

    # make the plot
    plt.plot(keys, values, label=label)
    plt.title("Results of the AIs")
    plt.legend(loc='upper left')
    plt.xlim(xmin=0, xmax=100)
    plt.ylim(ymin=0)


# run the game with respective AI and plot the results:
plotChart(BattleshipsGame(RandomShooter()).play_game(rounds=10000), "Random shooter")
plotChart(BattleshipsGame(HuntingShooter()).play_game(rounds=10000), "Hunting shooter")
plotChart(BattleshipsGame(ParityShooter()).play_game(rounds=10000), "Parity shooter")

plt.show()