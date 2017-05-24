from .BattleshipsAI import BattleshipsAI
import random

class ProbabilityShooter(BattleshipsAI):
    def __init__(self):
        BattleshipsAI.__init__(self)
        self.shots = [[False for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.probabilities = None

    def get_shot_position(self, ships):
        self.calculate_probabilities()
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                print(self.probabilities[x][y], end=' ')
            print()
        print()
        max_probability = max(map(max, self.probabilities))
        possible_indexes = []
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if self.probabilities[x][y] == max_probability:
                    possible_indexes.append((x, y))
        random_index = random.randint(0, len(possible_indexes) - 1)
        print(possible_indexes)
        print(random_index)
        random_position = possible_indexes[random_index]
        return random_position

    def hit_feedback(self, is_hit, ships):
        pass

    def calculate_probabilities(self):
        self.probabilities = [[0 for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]

        for ship_length in self.SHIPS.values():
            for x in range((self.BOARD_SIZE - ship_length) + 1):
                for y in range(self.BOARD_SIZE):
                    for s in range(x, x + ship_length):
                        self.probabilities[s][y] += 1
                        self.probabilities[y][s] += 1
