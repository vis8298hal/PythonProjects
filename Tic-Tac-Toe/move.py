import datetime
#Class Move
class Move:
    def __init__(self,value):
        self._value = value
    @property
    def value(self):
        return self._value
    def is_valid(self):
        Error_string = ""
        if isinstance(self._value,int):
            if self._value >= 1 and self._value <= 9:
                Error_string = ""
            else:
                Error_string = f"\n{datetime.datetime.now()} --> Value Provided is Out of Range Error should be between (1-9)"
        else:
            Error_string += f"\n{datetime.datetime.now()} --> Value Provided is Invalid Expecting Integer"
       
        file1 = open("logfile.txt","a")
        file1.write(Error_string)
        file1.close()
        if Error_string == "":
            return 1
        else:
            return 'E'
    def get_row(self):
        if self._value in (1,2,3):
            return 0       #  First Row
        elif self._value in (4,5,6):
            return 1      #  Second Row
        elif self._value in (7,8,9):
            return 2     #  Third Row
        else:
            file1 = open("logfile.txt","a")
            file1.write(f"\n{datetime.datetime.now()} --> No Rows Found")
            file1.close()
            return 'E'
        

    def get_column(self):
        
        if self._value in (1,4,7):
            return 0   #  First Column
        elif self._value in (2,5,8):
            return 1   #  Second Column
        elif self._value in (3,6,9):
            return 2   #  Third Column
        else:
            file1 = open("logfile.txt","a")
            file1.write(f"\n{datetime.datetime.now()} --> No Columns Found")
            file1.close()
            return 'E'