from datetime import datetime
class Log:
    def __init__(self,filename="logfile.txt"):
        self._filename = filename
    
    @property
    def filename(self):
        return "filename is not allowed to be extracted"
    
    def initiate_log(self):
        file1 = open(self._filename,"w")
        curr_dt = datetime.today().strftime("%d-%b-%Y %H:%M")
        file1.write(f"{curr_dt}\nProgram Id : {id(curr_dt)}")
        file1.close()

        
    def write_msg(self, message, pos=0):
        file1 = open(self._filename,"a")
        tab_spc = ""
        for i in range(pos):
            tab_spc += "\t"
        file1.write(f"\n{tab_spc}-->{message}")
        file1.close()

    def __str__(self):
        str1 = f"Logfile {self._filename} successfully generated please check the attched logfile for clarifications"
        return str1
