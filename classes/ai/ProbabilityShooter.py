from .BattleshipsAI import BattleshipsAI
import random

class ProbabilityShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.hits = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.probabilities = None

    def get_shot_position(self, ships):
        self.calculate_probabilities()

        # print probabilities
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                print(self.probabilities[x][y], end=' ')
            print()
        print()

        # find highest probability
        max_probability = max(map(max, self.probabilities))
        possible_indexes = []

        # get indexes with probability equal to the highest
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if self.probabilities[x][y] == max_probability:
                    possible_indexes.append((x, y))

        # pick a random of the possible positions
        random_index = random.randint(0, len(possible_indexes) - 1)
        position_x, position_y = possible_indexes[random_index]
        self.shots[position_x][position_y] = True

        return position_x, position_y

    def hit_feedback(self, is_hit, ships):
        # filter out ships that has been sunk
        self.SHIPS = {ship: ship_length for ship, ship_length in ships.items() if not ship_length == 0}

    def calculate_probabilities(self):
        # reset probabilities
        self.probabilities = [[0 for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]

        # calculate probabilities based on the current alive ships
        for ship_length in self.SHIPS.values():
            for x in range((self.BOARD_SIZE - ship_length) + 1):
                for y in range(self.BOARD_SIZE):
                    ship_x = True
                    ship_y = True

                    # check if there is a miss horizontally
                    for s in range(x, x + ship_length):
                        if self.shots[s][y] and not self.hits[s][y]:
                            ship_x = False
                            break

                    # check if there is a miss vertically
                    for s in range(x, x + ship_length):
                        if self.shots[y][s] and not self.hits[y][s]:
                            ship_y = False
                            break

                    # if ship can be placed horizontally
                    if ship_x:
                        for s in range(x, x + ship_length):
                            self.probabilities[s][y] += 1

                    # if ship can be placed vertically
                    if ship_y:
                        for s in range(x, x + ship_length):
                            self.probabilities[y][s] += 1
