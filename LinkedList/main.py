from datetime import datetime
from linkedlist import LinkedList
from log import Log

filename = "logfile_001.txt"
logfile1 = Log(filename)
logfile1.initiate_log()
ll1 = LinkedList()
ll1._LinkedList__logfile =  filename
start_time = datetime.now()
for i in range(100):
    ll1.insert(90+i)
print(len(ll1))
print(ll1)
end_time = datetime.now()
print(f"Program completed in {end_time - start_time}")
print(ll1.find_node(91))

