import matplotlib.pyplot as plt
from classes.BattleshipsGame import BattleshipsGame
from classes.ai.RandomShooter import RandomShooter
from classes.ai.HuntingShooter import HuntingShooter


def plotChart(plotting_data, title_param='Change me..'):
    
    plt.cls
    # prepare the data
    keys = [value[0] for value in plotting_data]
    values = [value[1] for value in plotting_data]

    # make the plot
    plt.plot(keys, values)
    plt.title(title_param)
    plt.show()


# run the game with respective AI and plot the results:
plotChart(BattleshipsGame(RandomShooter()).play_game(rounds=1000), "Random shooter")

#plotChart(BattleshipsGame(HuntingShooter()).play_game(rounds=1000), "Hunting shooter")
