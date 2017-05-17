from classes.BattleshipsGame import BattleshipsGame
from classes.RandomShooter import RandomShooter

def main():
    game = BattleshipsGame(RandomShooter())
    game.game_loop()

if __name__ == '__main__':
    main()
