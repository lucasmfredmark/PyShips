from .BattleshipsAI import BattleshipsAI
import random

class HuntTargetShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.lastX = 0
        self.lastY = 0
        self.position_x = 0
        self.position_y = 0
        self.potential_targets = []

    def get_shot_position(self, ships):
        position_x = 0
        position_y = 0
        # If there are potential targets, shoot at them first
        if len(self.potential_targets) != 0:
            while True:
                # while we still have targets left
                if len(self.potential_targets) != 0:
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
        if len(self.potential_targets) == 0:
            while True:
                position_x = random.randint(0, self.BOARD_SIZE - 1)
                position_y = random.randint(0, self.BOARD_SIZE - 1)
                if not self.shots[position_x][position_y]:
                    break

        # Mark the position as shoot at, and save last shot's position
        self.shots[position_x][position_y] = True
        self.lastX = position_x
        self.lastY = position_y
        return position_x, position_y

    def hit_feedback(self, is_hit, ships):
        last_x = self.lastX
        last_y = self.lastY
        if is_hit:
            # target to the left
            target_left = (last_x - 1, last_y)
            if self.validate_position(target_left[0], target_left[1]) and target_left not in self.potential_targets:
                self.potential_targets.append(target_left)
            
            # target to the right
            target_right = (last_x + 1, last_y)
            if self.validate_position(target_right[0], target_right[1]) and target_right not in self.potential_targets:
                self.potential_targets.append(target_right)
            
            # target above
            target_above = (last_x, last_y - 1)
            if self.validate_position(target_above[0], target_above[1]) and target_above not in self.potential_targets:
                self.potential_targets.append(target_above)

            # target below
            target_below = (last_x, last_y + 1)
            if self.validate_position(target_below[0], target_below[1]) and target_below not in self.potential_targets:
                self.potential_targets.append(target_below)

    def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE
