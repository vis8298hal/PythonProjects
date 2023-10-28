from suit import Suit
    
class Card:

    CARD_VALUE = {11 : "Jack", 12 : "Queen", 13 : "King" ,14 : "Ace"}
    def __init__(self,value,suit):
        self.__value = value
        if value >= 11:
            self._value = Card.CARD_VALUE[value]
            self._suit = Suit(suit)
        elif value <= 1:
            self._value = "Invalid"
            self._suit = Suit("invalid")
        else:
            self._value = value
            self._suit = Suit(suit)
    @property
    def value(self):
        return self._value
    
    @property
    def suit(self):
        return self._suit

    def show(self):
        return self.value,self.suit,self.suit.symbol

    @property
    def is_special(self):
        if self.__value >= 11:
            return True
        else:
            return False

    def __str__(self):
        return f"The {self._value} of {self._suit.symbol}"