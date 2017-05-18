from .BattleshipsAI import BattleshipsAI
import random

class RandomShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]

    def get_shot_position(self, ships):
        while True:
            position_x = random.randint(0, self.BOARD_SIZE - 1)
            position_y = random.randint(0, self.BOARD_SIZE - 1)

            if not self.shots[position_x][position_y]:
                self.shots[position_x][position_y] = True
                break

        return position_x, position_y

    def hit_feedback(self, is_hit, ships):
        pass
