from . import BattleshipsAI
import random

class RandomShooter(BattleshipsAI):
    def __init__(self):
        super().__init__()

    def get_fire_position(self):
        position_x = random.randint(1, 10) - 1
        position_y = random.randint(1, 10) - 1

        return position_x, position_y

    def hit_feedback(self, hit):
        return True
