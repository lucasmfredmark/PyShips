from .. import BattleshipsGameSettings

class BattleshipsAI:
    def __init__(self):
        self.BOARD_SIZE = BattleshipsGameSettings.BOARD_SIZE
        self.ships = BattleshipsGameSettings.SHIPS

    def get_shot_position(self, ships):
        raise NotImplementedError

    def hit_feedback(self, is_hit, ships):
        raise NotImplementedError
