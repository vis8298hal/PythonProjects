from datetime import datetime
from linkedlist import LinkedList

ll1 = LinkedList()
start_time = datetime.now()
for i in range(100):
    ll1.insert(90+i)
print(len(ll1))
print(ll1)
end_time = datetime.now()
print(f"Program completed in {end_time - start_time}")
