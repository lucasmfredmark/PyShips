import matplotlib.pyplot as plt
from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter
from classes.ai.HuntingShooter import HuntingShooter
from classes.ai.ParityShooter import ParityShooter


def plotChart(plotting_data, title_param='Change me..'):
    
    # prepare the data
    keys = [value[0] for value in plotting_data]
    values = [value[1] for value in plotting_data]

    # make the plot
    plt.plot(keys, values)
    plt.title(title_param)
    plt.xlim(xmin=0, xmax=100)


# run the game with respective AI and plot the results:
plotChart(BattleshipsGame(RandomShooter()).play_game(rounds=1000), "Random shooter")
plotChart(BattleshipsGame(ParityShooter()).play_game(rounds=1000), "Parity shooter (only hunting)")

plt.show()