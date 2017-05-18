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
                    if board[position_x + i][position_y] != '#':
                        return False
            else:
                for i in range(ship_length):
                    if board[position_x][position_y + i] != '#':
                        return False

        return True

    def validate_position(self, position_x, position_y):
        return 0 <= position_x < self.BOARD_SIZE and 0 <= position_y < self.BOARD_SIZE

    def place_ships(self, board, ships):
        for ship in ships.keys():
            valid_placement = False

            while not valid_placement:
                is_vertical = bool(random.getrandbits(1))
                position_x = random.randint(0, self.BOARD_SIZE - 1)
                position_y = random.randint(0, self.BOARD_SIZE - 1)
                valid_placement = self.validate_ship_placement(board, ships[ship], is_vertical, position_x, position_y)

            board = self.place_ship(board, ships[ship], ship[0], is_vertical, position_x, position_y)

        return board

    def make_move(self, board, position_x, position_y):
        if board[position_x][position_y] == '#' or board[position_x][position_y] == '!':
            return False
        else:
            return True

    def check_sink(self, board, position_x, position_y):
        for ship in self.ships.keys():
            if board[position_x][position_y] == ship[0]:
                ship_name = ship
                break

        self.ships[ship_name] -= 1

        if self.ships[ship_name] == 0:
            print(ship_name + ' sunk')
            return True
        else:
            return False

    def check_win(self):
        for ship in self.ships:
            if ship != 0:
                return False

        return True

    def print_board(self, board):
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                # position was shot at
                if board[x][y] == '@':
                    print('\x1b[6;30;42m' + " " + '\x1b[0m' + " ", end='')
                
                # shot was a miss
                if board[x][y] == '!':
                    print('\x1b[0;30;41m' + " " + '\x1b[0m' + " ", end='')
                
                # default
                if board[x][y] == '#':
                    print('\x1b[0;30;40m' + " " + '\x1b[0m' + " ", end='')
                
                # ship
                if board[x][y] in ['A', 'B', 'C', 'D', 'S']:
                    print('\x1b[0;34;47m' + board[x][y] + '\x1b[0m' + " ", end='')
            print()

    def play_game(self):
        self.place_ships(self.board, self.ships)
        self.print_board(self.board)

        hasWon = False

        for i in range(self.BOARD_SIZE * self.BOARD_SIZE):
            position_x, position_y = self.player.get_shot_position()

            if self.make_move(self.board, position_x, position_y):
                if self.board[position_x][position_y] != '@':
                    if self.check_sink(self.board, position_x, position_y):
                        self.board[position_x][position_y] = '@'

                        if self.check_win():
                            hasWon = True
                            break
                    else:
                        self.board[position_x][position_y] = '@'
            else:
                self.board[position_x][position_y] = '!'

        self.print_board(self.board)
        print('hasWon: {}'.format(hasWon))
