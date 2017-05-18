from .. import BattleshipsGameSettings

class BattleshipsAI:
    def __init__(self):
        self.BOARD_SIZE = BattleshipsGameSettings.BOARD_SIZE
        self.ships = BattleshipsGameSettings.SHIPS

    def get_shot_position(self):
        raise NotImplementedError
