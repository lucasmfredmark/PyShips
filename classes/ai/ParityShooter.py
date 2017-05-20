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
        self.position_x = 0
        self.position_y = 0
        
        self.directions = [0, 1, 2, 3]
        self.originalX = 0
        self.originalY = 0

        self.potential_targets = []

    def get_shot_position(self, ships):
        position_x = 0
        position_y = 0
        # If there are potential targets, shoot at them first
        if len(self.potential_targets)!=0:
            while True:
                # while we still have targets left
                if len(self.potential_targets)!=0:
                    target_position = self.potential_targets.pop(0)
                    position_x = target_position[0]
                    position_y = target_position[1]

                    # check that we have not shot there before
                    if not self.shots[position_x][position_y]:
                        self.lastX = position_x
                        self.lastY = position_y
                        self.shots[position_x][position_y] = True
                        return position_x, position_y
                # ran out of targets, go back hunting
                else:
                    break
            
        # If there are no potential targets, hunt for ships
        if len(self.potential_targets)==0:
            while True:
                position_x = random.randint(0,9)
                position_y = random.randint(0,9)
                if not self.shots[position_x][position_y]:
                    break

        # Mark the position as shoot at, and save last shot's position
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
