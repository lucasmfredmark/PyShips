import copy

class BattleshipsGame:
    def __init__(self):
        self.BOARD_SIZE = 10
        self.SHIPS = {
            'Aircraft Carrier': 5,
            'Battleship': 4,
            'Cruiser': 3,
            'Submarine': 3,
            'Destroyer': 2
        }
        self.player_board = {
            'board': [0] * self.BOARD_SIZE,
            'ships': self.SHIPS
        }
        self.computer_board = copy.deepcopy(self.player_board)

    def reset_game(self):
        self.__init__()

    def place_ship(self, board, ship_length, is_vertical, position_x, position_y):
        if is_vertical:
            for i in range(ship_length):
                board[position_x + i][position_y] = ship_length
        else:
            for i in range(ship_length):
                board[position_x][position_y + i] = ship_length

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
