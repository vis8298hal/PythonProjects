from board import Board
from player import Player
class TicTacToe:

    def start(self):
        print("******************************************")
        print("****** Welcome to Tic-Tac-Toe Game *******")
        print("******************************************")

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
                self.start_new_round(board)

    def start_new_round(self,board):
        print("******************************************")
        print("****** Starting a New Round *******")
        print("******************************************")
        print(board.reset_board())


game = TicTacToe()
game.start()

