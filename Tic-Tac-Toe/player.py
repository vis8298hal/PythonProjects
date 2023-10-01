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
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
    def get_human_move(self):
        while True:
            user_input = int(input("Choose your Move (1-9)"))
            mv = Move(user_input)
            if mv.is_valid() != 'E':
                break
        return mv
    def get_computer_move(self):
        random_choice = random.choice(range(1,10))
        move = Move(random_choice)
        print("Computer Chose Position ",move.value)
        return move