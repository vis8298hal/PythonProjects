class Board:
    
    EMPTY_CELL = 0
    
    
    def __init__(self):
        self._game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
    @property
    def game_board(self):
        str1 = "\nPositions : "
        str1 += self.print_board_with_positions()
        str1 += "\nBoard : "
        str2 = "\n"
        for row in self._game_board:
            str2 += "|"
            for column in row:
                if column == Board.EMPTY_CELL:
                    str2 += "   |"
                else:
                    str2 += f" {column} |"
            str2 += "\n"
        return str1+str2
        
    
    def print_board_with_positions(self):
        return "\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n"
    
    def submit_move(self,player,move):
        row = move.get_row()
        col = move.get_column()
        value = self._game_board[row][col]
        
        if value == Board.EMPTY_CELL:
            self._game_board[row][col] = player.marker
        else:
            print("This Position is already taken select any other position")
            
    def check_row(self,player,last_move):
        row_index = last_move.get_row()
        board_row = self._game_board[row_index]
        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
        marker_counter = 0
        column_index  = last_move.get_column()
        for i in range(3):
            if self._game_board[i][column_index] == player.marker:
                marker_counter += 1
        return marker_counter == 3 
    
    def check_diagonal(self,player):
        counter = 0
        for i in range(3):
            if self._game_board[i][i] == player.marker:
                counter += 1
        return counter == 3
    
    def check_anti_diagonal(self,player):
        counter = 0
        for i in range(3):
            if self._game_board[i][2-i] == player.marker:
                counter += 1
        return counter == 3
    
    def check_is_game_over(self,player, last_move):
        return ((self.check_row(player, last_move)) or (self.check_column(player, last_move)) or (self.check_diagonal(player) or (self.check_anti_diagonal(player))))
    
    def check_tie(self):
        empty_counter = 0
        for row in self._game_board:
            empty_counter =+ row.count(Board.EMPTY_CELL)
        return empty_counter == 0
    
    def reset_board(self):
        self._game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
        print("Resetting the Game Board")
        return self.game_board