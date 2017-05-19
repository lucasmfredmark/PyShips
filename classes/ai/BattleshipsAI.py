from .. import BattleshipsGameSettings
import copy

class BattleshipsAI:
    def __init__(self):
        self.BOARD_SIZE = copy.deepcopy(BattleshipsGameSettings.BOARD_SIZE)
        self.SHIPS = copy.deepcopy(BattleshipsGameSettings.SHIPS)

    def get_shot_position(self, ships):
        raise NotImplementedError

    def hit_feedback(self, is_hit, ships):
        raise NotImplementedError
