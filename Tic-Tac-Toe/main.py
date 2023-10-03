from board import Board
from player import Player
import datetime
class TicTacToe:

    def start(self):
        print("******************************************")
        print("****** Welcome to Tic-Tac-Toe Game *******")
        print("******************************************")
        curr_dt = datetime.datetime.today().strftime("%d-%b-%Y %H:%M")
        logfile = open("logfile.txt", "w")
        logfile.write("**********Game Started ***************\n")
        logfile.write(f"Date and Time : {curr_dt}\n")
        logfile.write(f"Program Id  : {id(curr_dt)}")
        logfile.close()
        board = Board()
        player = Player()
        computer = Player(False)

        print(board.game_board)
        while True:
            while True:
                player_move = player.get_move()
                board.submit_move(player,player_move)
                print(board.game_board)
                if board.check_tie():
                    print("It's a Tie Please try next time :: ")
                    break
                elif board.check_is_game_over(player, player_move):
                    print("Awesome You Won the Game")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer,computer_move)
                    print(board.game_board)

                    if board.check_is_game_over(computer,computer_move):
                        print("Computer Won this Game Please try Again Later")
                        break
            play_again = input("Do you want to play again ?.(Y/N)").upper()
            if play_again == "N":
                print("Thank you for Playing the Game")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("I think you want to play again but the input was Invalid")
                logfile = open("logfile.txt","a")
                logfile.write("\n\t\t----Invalid input provided by Users")
                logfile.close()
                self.start_new_round(board)

    def start_new_round(self,board):
        print("******************************************")
        print("****** Starting a New Round *******")
        print("******************************************")
        logfile = open("logfile.txt","a")
        logfile.write("\n********************Started a New Round**********************************")
        logfile.close()
        print(board.reset_board())

start_time = datetime.datetime.now()
game = TicTacToe()
game.start()
end_time = datetime.datetime.now()
logfile = open("logfile.txt","a")
time_diff = end_time - start_time
logfile.write(f"\n\n\nProgram Completed in {time_diff} ")
logfile.close()

