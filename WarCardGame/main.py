from card import Card
from deck import Deck
from  ... import LinkedList

LinkedList.main
d1 = Deck([123])
lg1 = Log()
lg1.write_msg("Hello",4)
print(d1.isempty)
d1.build()
print(d1.isempty)
print("---------------------------------------------------------------------------------------------------------------")
d1.show()
d1.shuffle()
print("---------------------------------------------------------------------------------------------------------------")
d1.show()
print(d1.size)
print(d1.draw())
print(d1.draw())
print(d1.draw())
print(d1.draw())
cc1 = Card(3, "spade")
d1.add(cc1)
print(d1.size)
print("--------------------------------------------------------------------------------------------------------------")
d1.show()