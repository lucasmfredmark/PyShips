import random

class BattleshipsGame:
    def __init__(self, player):
        self.BOARD_SIZE = 10
        self.ships = {
            'Aircraft Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2
        }
        self.board = [[0 for i in range(self.BOARD_SIZE)] for j in range(self.BOARD_SIZE)]
        self.player = player

    def reset_game(self):
        self.__init__()

    def place_ship(self, board, ship_length, ship_char, is_vertical, position_x, position_y):
        if is_vertical:
            for i in range(ship_length):
                board[position_x + i][position_y] = ship_char
        else:
            for i in range(ship_length):
                board[position_x][position_y + i] = ship_char

        return board

    def validate_ship_placement(self, board, ship_length, is_vertical, position_x, position_y):
        if not self.validate_position(position_x, position_y):
            return False
        elif is_vertical and ship_length + position_x >= self.BOARD_SIZE:
            return False
        elif not is_vertical and ship_length + position_y >= self.BOARD_SIZE:
            return False
        else:
            if is_vertical:
                for i in range(ship_length):
                    if board[position_x + i][position_y] != -1:
                        return False
            else:
                for i in range(ship_length):
                    if board[position_x][position_y + i] != -1:
                        return False

        return True

    def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE

    def place_ships(self, board, ships):
        for ship in ships.keys():
            valid_placement = False

            while not valid_placement:
                is_vertical = bool(random.getrandbits(1))
                position_x = random.randint(0, self.BOARD_SIZE) - 1
                position_y = random.randint(0, self.BOARD_SIZE) - 1
                valid_placement = self.validate_ship_placement(board, ships[ship], is_vertical, position_x, position_y)

            board = self.place_ship(board, ships[ship], ship[0], is_vertical, position_x, position_y)

        return board

    def make_move(self, board, position_x, position_y):
        if board[position_x][position_y] == -1:
            return 'miss'
        else:
            return 'hit'

    def game_loop(self):
        self.place_ships(self.board, self.ships)

        for i in range(self.BOARD_SIZE * self.BOARD_SIZE):
            fire_position = self.player.get_fire_position()
            print(fire_position)
