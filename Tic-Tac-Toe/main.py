import datetime
from move import Move
from player import Player

#  | 1 | 2 | 3 |
#  | 4 | 5 | 6 |
#  | 7 | 8 | 9 |   
logfile = open("logfile.txt","w")
tday = datetime.datetime.today()
logfile.write(f"Logfile Initiated for {tday.strftime('%d-%B-%Y')}")
logfile.write(f"\nProgram Id : {id(tday)}")
logfile.close() 
    
p1 = Player(is_human=False)
p1_move = p1.get_move()
print(p1_move.value)
