#Class Player
from move import Move
import random
class Player:
    PLAYER_MARKER = "X"
    COMP_MARKER = "O"
    def __init__(self, is_human=True):
        self._is_human = is_human
        if self._is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMP_MARKER
    @property
    def is_human(self):
        return self._is_human
    
    @property
    def marker(self):
        return self._marker
    
    def get_move(self):
        logfile = open("logfile.txt","a")
        logfile.write("\n\t-----Player Class Initiated-----------")
        logfile.close()
        
        if self._is_human:
            logfile = open("logfile.txt","a")
            logfile.write("\n\t\t\tHuman Player Selected")
            logfile.close()
            return self.get_human_move()
        else:
            logfile = open("logfile.txt","a")
            logfile.write("\n\t\t\tComputer Player Selected")
            logfile.close()
            return self.get_computer_move()
    def get_human_move(self):
        while True:
            user_input = int(input("Choose your Move (1-9)"))
            logfile = open("logfile.txt","a")
            logfile.write(f"\n\tHuman Selected Move {user_input}")
            logfile.close()
            mv = Move(user_input)
            if mv.is_valid() != 'E':
                break
            else:
                logfile = open("logfile.txt","a")
                logfile.write(f"\n\t\t\tInvalid User Input {user_input}")
                logfile.close()
        return mv
    def get_computer_move(self):
        random_choice = random.choice(range(1,10))
        logfile = open("logfile.txt","a")
        logfile.write(f"\n\t\t\tComputer Move Selected {random_choice}")
        logfile.close()
        move = Move(random_choice)
        print("Computer Chose Position ",move.value)
        return move