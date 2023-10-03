class Board:
    
    EMPTY_CELL = 0
    
    
    def __init__(self):
        logfile = open("logfile.txt","a")
        logfile.write("\n\t---------------Initialized Board Class------------------")
        self._game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
        logfile.write(f"Initial Board : \n\t\t| {self._game_board[0][0]} | {self._game_board[0][1]} | {self._game_board[0][2]} |")
        logfile.write(f"\n\t\t| {self._game_board[1][0]} | {self._game_board[1][1]} | {self._game_board[1][2]} |")
        logfile.write(f"\n\t\t| {self._game_board[2][0]} | {self._game_board[2][1]} | {self._game_board[2][2]} |\n")
        logfile.close()
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
            logfile = open("logfile.txt","a")
            logfile.write(f"\n--------------------Position {move.value} is already taken so lost turn")
            logfile.close()
            
    def check_row(self,player,last_move):
        row_index = last_move.get_row()
        board_row = self._game_board[row_index]
        logfile = open("logfile.txt","a")
        logfile.write(f"\nChecking Row Level Game Over")
        if board_row.count(player.marker) == 3:
            logfile.write("\n\t\t Game Over by Row")
        else:
            logfile.write("\n\t\t Not Over yet")
        logfile.close()
        return board_row.count(player.marker) == 3
    
    def check_column(self, player, last_move):
        marker_counter = 0
        column_index  = last_move.get_column()
        for i in range(3):
            if self._game_board[i][column_index] == player.marker:
                marker_counter += 1
        logfile = open("logfile.txt","a")
        logfile.write(f"\nChecking Column Level Game Over")
        if marker_counter == 3:
            logfile.write("\n\t\t Game Over by Column")
        else:
            logfile.write("\n\t\t Not Over yet")
        logfile.close()
        return marker_counter == 3 
    
    def check_diagonal(self,player):
        counter = 0
        for i in range(3):
            if self._game_board[i][i] == player.marker:
                counter += 1
        logfile = open("logfile.txt","a")
        logfile.write(f"\nChecking Diagonal Level Game Over")
        if counter == 3:
            logfile.write("\n\t\t Game Over by Diagonal")
        else:
            logfile.write("\n\t\t Not Over yet")
        logfile.close()
        return counter == 3
    
    def check_anti_diagonal(self,player):
        counter = 0
        for i in range(3):
            if self._game_board[i][2-i] == player.marker:
                counter += 1
        logfile = open("logfile.txt","a")
        logfile.write(f"\nChecking Cross Diagonal Level Game Over")
        if counter == 3:
            logfile.write("\n\t\t Game Over by Cross Diagonal")
        else:
            logfile.write("\n\t\t Not Over yet")
        logfile.close()
        return counter == 3
    
    def check_is_game_over(self,player, last_move):
        return ((self.check_row(player, last_move)) or (self.check_column(player, last_move)) or (self.check_diagonal(player) or (self.check_anti_diagonal(player))))
    
    def check_tie(self):
        empty_counter = 0
        for row in self._game_board:
            empty_counter =+ row.count(Board.EMPTY_CELL)
        logfile = open("logfile.txt","a")
        if empty_counter > 0:
            logfile.write("\n\t\t Not a Tie still Running")
        else:
            logfile.write("\n\t\t Game in Tie state")
        logfile.close()
        return empty_counter == 0
    
    def reset_board(self):
        self._game_board = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
        print("Resetting the Game Board")
        return self.game_board