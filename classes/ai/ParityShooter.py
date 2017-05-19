from .BattleshipsAI import BattleshipsAI
import random

class ParityShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.hunting = True
        self.shotArray = []
        self.lastX = 0
        self.lastY = 0
        
        self.directions = [0, 1, 2, 3]
        self.originalX = 0
        self.originalY = 0

        self.potential_targets = []

    def get_shot_position(self, ships):
        
        # If there are potential targets, shoot at them first
        if len(self.potential_targets)!=0:
            while True:
                # when we still have targets left
                if len(self.potential_targets)!=0:
                    target = self.potential_targets.pop(0)
                    if not self.shots[target[0]][target[1]]:
                        self.lastX = target[0]
                        self.lastY = target[1]
                        self.shots[target[0]][target[1]] = True
                        return target
                # in case we run out of targets, go back to hunting
                else:
                    break

            #print("Target removed: " + str(target))
            
        # If there are no potential targets, hunt for ships
        while True:
            position_x = random.randint(0,9)
            position_y = random.randint(0,9)
            if not self.shots[position_x][position_y]:
                 break

        self.shots[position_x][position_y] = True
        self.lastX = position_x
        self.lastY = position_y
        return position_x, position_y

    
    def hit_feedback(self, is_hit, ships):

        if is_hit:
            if validate_position(self, self.lastX - 1, self.lastY) and (self.lastX - 1, self.lastY) not in self.potential_targets:
                self.potential_targets.append((self.lastX - 1, self.lastY))
                print("Target added: " + str(self.lastX - 1),  str(self.lastY), "around " + str(self.lastX), str(self.lastY))
            
            if validate_position(self, self.lastX + 1, self.lastY) and (self.lastX + 1, self.lastY) not in self.potential_targets:
                self.potential_targets.append((self.lastX + 1, self.lastY))
                print("Target added: " + str(self.lastX + 1), str(self.lastY), "around " + str(self.lastX), str(self.lastY))
            
            if validate_position(self, self.lastX, self.lastY - 1) and (self.lastX, self.lastY - 1) not in self.potential_targets:
                self.potential_targets.append((self.lastX, self.lastY - 1))
                print("Target added: " + str(self.lastX), str(self.lastY - 1), "around " + str(self.lastX), str(self.lastY))

            if validate_position(self, self.lastX, self.lastY + 1) and (self.lastX, self.lastY + 1) not in self.potential_targets:
                self.potential_targets.append((self.lastX, self.lastY + 1))
                print("Target added: " + str(self.lastX), str(self.lastY + 1), "around " + str(self.lastX), str(self.lastY))
            
            print()

def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE
