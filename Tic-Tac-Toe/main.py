import datetime
from move import Move

#  | 1 | 2 | 3 |
#  | 4 | 5 | 6 |
#  | 7 | 8 | 9 |   
logfile = open("logfile.txt","w")
tday = datetime.datetime.today()
logfile.write(f"Logfile Initiated for {tday.strftime('%d-%B-%Y')}")
logfile.write(f"\nProgram Id : {id(tday)}")
logfile.close() 
mv1 = Move("12")

valid = mv1.is_valid()
column = mv1.get_column()
row = mv1.get_row()

if valid != 'E':
    print(f"Value is Valid {mv1.value}")
else:
    print("Error : Check the Log File")
    
if column != 'E':
    print(f"{column} is a Valid Column for {mv1.value}")
else:
    print("Error : Check the Log File")
if  row != 'E':
    print(f"{row} is the Valid Row for {mv1.value}")
else:
    print("Error : Check the Log File")
    
