from . import BattleshipsGameSettings
import random

class BattleshipsGame:
    def __init__(self, player):
        self.BOARD_SIZE = BattleshipsGameSettings.BOARD_SIZE
        self.ships = BattleshipsGameSettings.SHIPS
        self.board = [['#' for y in range(self.BOARD_SIZE)] for x in range(self.BOARD_SIZE)]
        self.player = player

    def reset_game(self):
        self.__init__(self.player)

    def place_ship(self, ship_length, ship_char, is_vertical, position_x, position_y):
        if is_vertical:
            for i in range(ship_length):
                self.board[position_x + i][position_y] = ship_char
        else:
            for i in range(ship_length):
                self.board[position_x][position_y + i] = ship_char

    def validate_ship_placement(self, ship_length, is_vertical, position_x, position_y):
        if not self.validate_position(position_x, position_y):
            return False
        elif is_vertical and ship_length + position_x >= self.BOARD_SIZE:
            return False
        elif not is_vertical and ship_length + position_y >= self.BOARD_SIZE:
            return False
        else:
            if is_vertical:
                for i in range(ship_length):
                    if self.board[position_x + i][position_y] != '#':
                        return False
            else:
                for i in range(ship_length):
                    if self.board[position_x][position_y + i] != '#':
                        return False

        return True

    def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE

    def place_ships(self):
        for ship in self.ships.keys():
            valid_placement = False

            while not valid_placement:
                is_vertical = bool(random.getrandbits(1))
                position_x = random.randint(0, self.BOARD_SIZE - 1)
                position_y = random.randint(0, self.BOARD_SIZE - 1)
                valid_placement = self.validate_ship_placement(self.ships[ship], is_vertical, position_x, position_y)

            self.place_ship(self.ships[ship], ship[0], is_vertical, position_x, position_y)

    def make_move(self, position_x, position_y):
        if not self.validate_position(position_x, position_y):
            return False

        state = self.board[position_x][position_y]

        if state == '#':
            self.board[position_x][position_y] = '!'
            return False
        elif state == '@' or state == '!':
            return False
        else:
            self.hit_ship(position_x, position_y)
            self.board[position_x][position_y] = '@'
            return True

    def hit_ship(self, position_x, position_y):
        for ship in self.ships.keys():
            if self.board[position_x][position_y] == ship[0]:
                ship_name = ship
                break

        self.ships[ship_name] -= 1

    def check_win(self):
        for ship_length in self.ships:
            if ship_length != 0:
                return False

        return True
    
    def print_board(self):
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                # shot was a hit
                if self.board[x][y] == '@':
                    print('\x1b[6;30;42m' + " " + '\x1b[0m', end='')
                # shot was a miss
                elif self.board[x][y] == '!':
                    print('\x1b[0;30;41m' + " " + '\x1b[0m', end='')
                # default
                elif self.board[x][y] == '#':
                    print('\x1b[0;30;40m' + " " + '\x1b[0m', end='')
                # ship
                else:
                    print('\x1b[0;34;47m' + self.board[x][y] + '\x1b[0m', end='')
            print()

    def play_game(self):
        self.place_ships()
        self.print_board()
        has_won = False

        for i in range(self.BOARD_SIZE * self.BOARD_SIZE):
            position_x, position_y = self.player.get_shot_position(self.ships)
            hit = self.make_move(position_x, position_y)
            self.player.hit_feedback(hit, self.ships)

            if self.check_win():
                has_won = True
                break

        self.print_board()
        print('has_won: {}'.format(has_won))
