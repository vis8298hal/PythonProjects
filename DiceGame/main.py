import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value

class Player:
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
    
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1
    
    def decrement_counter(self):
        self._counter -= 1

    def roll_dice(self):
        return self._die.roll()
    
class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def welcome_round(self):
        print("--------------New Round Starts------------------------")
        input("Press any key to roll the dice")
    
    def show_dice(self,player_value,computer_value):
        print(f"Player1 : {player_value}")
        print(f"Player2(Computer) : {computer_value}")

    def update_counter(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counter(self):
         print(f"Player1 Counter : {self._player.counter}\nPlayer2(Computer) Counter : {self._computer.counter}")
    
    def play_round(self):
        self.welcome_round()
        player_value = self._player.roll_dice()
        computer_value = self._computer.roll_dice()
        #Show the Values
        self.show_dice(player_value, computer_value)
        #Determine the Winner or Looser
        if player_value > computer_value:
            print("Player1 Wins the Round")
            self.update_counter(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("Player2(Computer Wins the round)")
            self.update_counter(winner=self._computer, loser=self._player)
        else:
            print("It's a tie")
        
        self.show_counter()

    def show_game_over(self, winner):
        output_str = """=====================\nGAME OVER\n====================
                        """
        if winner.is_computer:
            output_str = output_str + "\nSorry The Player2(Computer) Wins the Game\nRetry Again"
        else:
            output_str = output_str + "\nCongratulations For your Win !\nYou Won this Game Player1"
        output_str = output_str + "\n======================================="
        print(output_str)

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def play(self):
        output_string = """=======================================================
                                Welcome to Roll the Dice Game
                            ====================================================="""
        print(output_string)
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
    
    

player_die = Die()
computer_die = Die()
player1 = Player(player_die, is_computer=False)
player2 = Player(computer_die, is_computer=True)
game = DiceGame(player1, player2)

#Start The Game
game.play()