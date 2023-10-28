from datetime import datetime
from linkedlist import LinkedList
from log import Log

class App:

    def __init__(self):
        self._filename  = "logfile_001.txt"
        self._logfile1 = Log(self._filename)
        self._logfile1.initiate_log()
        self._ll1 = LinkedList()
        self._ll1._LinkedList__logfile =  self._filename
        self._start_time = datetime.now()
    
    def take_input(self):
        inp = int(input("Enter your choice here : "))
        self.perform_action(inp)
    def show_menu(self):
        print("================================================================================================")
        print("Please Choose from below Options")
        str1 = "Insert"
        int1 = 1
        print("{:<5}{:<20}{:<5}{:<20}".format(1,"Insert",2,"Update"))
        print("{:<5}{:<20}{:<5}{:<20}".format(3,"Delete",4,"Truncate"))
        print("{:<5}{:<20}{:<5}{:<20}".format(5,"Find Value",6,"Show the List"))
        print("{:<5}{:<20}".format(9,"Exit the Program"))
        self.take_input()
    
    def perform_action(self,action):
        if action == 1:
            self.insert_into(self._ll1)
            self.show_menu()
        elif action == 9:
            print("================================================================================================")
            print("{:>20}{:>20}".format("","Thank you for using us Please come back again."))
            print("================================================================================================")
            exit(0)
        elif action == 2:
            self.update_list()
        elif action == 3:
            self.delete_list()
        elif action == 4:
            self.truncate_list()
        elif action == 5:
            self.find_val()
        elif action == 6:
            self.show_list()
        else:
            self.invalid_entry()

    def insert_to_list(self,list1, value):
        if value == "q":
            return False
        else:
            list1.insert(int(value))
            return True

    def insert_into(self,list1):
        inp_val = input("Press 'q' for Exit \n Enter Value to insert into List : ")
        res = self.insert_to_list(list1,inp_val)
        if res:
            return self.insert_into(list1)
    
    def update_list(self):
        print("This feature is not available right now we are working on it")
    def delete_list(self):
        user_inp = int(input("Enter Value to be deleted : "))
        if self._ll1.delete_node(user_inp):
            print("=========================================================")
            print("{:<20}{:<2}{:<20}".format("",user_inp,"Deleted Successfully"))
            print("=========================================================")
            self.show_menu()
    def truncate_list(self):
        self._ll1.head = None
        self.show_list()
    def find_val(self):
        pass
    def show_list(self):
        print("{:<2}{}{:>2}".format("================","The List is ","=============="))
        print(self._ll1)
        self.show_menu()
    def invalid_entry(self):
        pass
ap1 = App()
ap1.show_menu()
