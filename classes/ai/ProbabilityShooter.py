from .BattleshipsAI import BattleshipsAI
import random

class ProbabilityShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]

    def get_shot_position(self, ships):
        return 0, 0

    def hit_feedback(self, is_hit, ships):
        pass
