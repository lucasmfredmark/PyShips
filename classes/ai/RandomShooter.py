from .BattleshipsAI import BattleshipsAI
import random

class RandomShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)

    def get_shot_position(self, ships):
        position_x = random.randint(0, self.BOARD_SIZE - 1)
        position_y = random.randint(0, self.BOARD_SIZE - 1)

        return position_x, position_y

    def hit_feedback(self, is_hit, ships):
        pass
