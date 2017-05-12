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
    
    
    
    
    def computer_move(board)
            
        # gets the coordinates of where the computer shoots
        # >>> at the moment the computer just shoots at random <<<
        while(true):
            # random.randit returns a random number between x and y
            x = random.randit(1,10)-1
            y = random.randit(1,10)-1
            res = general_movement(board,x,y)
            if res == "hit":
                print("Hit at " + str(x+1) + "," + str(y+1)
                check_sink(board,x,y)
                board[x][y] = '$'
                if check_win(board):
                      return "ROMA VICTOR"
            elif res == "miss":
                      board[x][y] = "*"
                      
            return board
                      
                      
                      
                      
                      
    def general_movement(board,x,y):
            
        #checks for miss              
        if board[x][y] == -1:
            return "miss"
        #checks for hit at location where there had already been shot              
        elif board[x][y] == "*" or board[x][y] == "$":
            return "try again"         
        else:
            return "hit"
        
    
    
    
    
