from .BattleshipsAI import BattleshipsAI
import random

class HuntingShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        hunting = False
        self.shotArray = []
        self.lastX = 0
        self.lastY = 0
        self.hunting = False
        self.directions = [0, 1, 2, 3]
        self.originalX = 0
        self.originalY = 0

    def get_shot_position(self, ships):
        if self.hunting:
            lastX = self.lastX
            lastY = self.lastY

            if self.directions[0] == 0:
                lastX = lastX-1
            elif self.directions[0] == 1:
                lastX = lastX+1
            elif self.directions[0] == 2:
                lastY = lastY-1
            elif self.directions[0] == 3:
                lastY = lastY+1

            self.lastX = lastX
            self.lastY = lastY

            if not self.validate_position(lastX, lastY):
                self.directions.pop(0)
                self.lastX = self.originalX
                self.lastY = self.originalY

            position_x = lastX
            position_y = lastY
        else:
            while True:
                position_x = random.randint(0, self.BOARD_SIZE - 1)
                position_y = random.randint(0, self.BOARD_SIZE - 1)

                if not self.shots[position_x][position_y]:
                    self.shots[position_x][position_y] = True
                    break

            self.lastX = position_x
            self.lastY = position_y

        return position_x, position_y


    def hit_feedback(self, is_hit, ships):
        if is_hit:
            if not self.hunting:
                self.hunting = True
                self.directions = [0, 1, 2, 3]
                self.originalX = self.lastX
                self.originalY = self.lastY
        else:
            if self.hunting:
                self.directions.pop(0)
                self.lastX = self.originalX
                self.lastY = self.originalY

                if len(self.directions) == 0:
                    self.hunting = False

    def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE
