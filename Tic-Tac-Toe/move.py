import datetime
#Class Move
class Move:
    def __init__(self,value):
        file1 = open("logfile.txt","a")
        file1.write("\n----Move Class Intialized---")
        file1.close()
        self._value = value
    @property
    def value(self):
        return self._value
    def is_valid(self):
        file1 = open("logfile.txt","a")
        file1.write("\n\t----Move Class Checking Validation---")
        file1.close()
        Error_string = ""
        if isinstance(self._value,int):
            if self._value >= 1 and self._value <= 9:
                Error_string = "\n\t\tSuccess"
            else:
                Error_string = f"\n\t\tError : {datetime.datetime.now()} --> Value Provided is Out of Range Error should be between (1-9)"
        else:
            Error_string += f"\n\t\tError : {datetime.datetime.now()} --> Value Provided is Invalid Expecting Integer"
       
        file1 = open("logfile.txt","a")
        file1.write(Error_string)
        file1.close()
        if Error_string == "\n\t\tSuccess":
            return 1
        else:
            return 'E'
    def get_row(self):
        file1 = open("logfile.txt","a")
        msg = ""
        ret = None
        file1.write("\n\t----Move Class Checking ROW---")
        if self._value in (1,2,3):
            ret = 0       #  First Row
            msg = "\n\t\tSuccess 1st Row"
        elif self._value in (4,5,6):
            ret = 1      #  Second Row\
            msg = "\n\t\tSuccess 2nd Row"
        elif self._value in (7,8,9):
            ret =  2     #  Third Row
            msg = "\n\t\tSuccess 3rd Row"
        else:
            msg = f"\n\t\tError : {datetime.datetime.now()} --> No Rows Found"
            ret =  'E'
        file1.write(msg)
        file1.close()
        return ret
        

    def get_column(self):
        file1 = open("logfile.txt","a")
        msg = ""
        ret = None
        file1.write("\n\t----Move Class Checking Column---")
        if self._value in (1,4,7):
            ret = 0
            msg = "\n\t\tSuccess 1st Column"   #  First Column
        elif self._value in (2,5,8):
            ret = 1
            msg = "\n\t\tSuccess 2nd Column"   #  Second Column
        elif self._value in (3,6,9):
            ret = 2
            msg = "\n\t\tSuccess 3rd Column"   #  Third Column
        else:
            ret = 'E'
            msg = f"\n\t\tError : {datetime.datetime.now()} --> No Columns Found"
        file1.write(msg)
        file1.close()
        return ret
            