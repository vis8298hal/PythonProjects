from card import Card
from random import shuffle
from copy import deepcopy



class Deck:

    def __init__(self, cards):
        self._cards = cards
        if len(self._cards) == 0:
            self._isempty = True
        else:
            self._isempty = False

    @property
    def size(self):
        return len(self._cards)

    @property
    def cards(self):
        return self._cards

    @property
    def isempty(self):
        return self._isempty

    def build(self):
        in_val = {"y" : "YES", "YES" : "YES", "yes" : "YES", "Yes" : "YES", "Y" : "Yes", "N" : "NO", "no" : "NO", "n" : "NO", "No" : "NO", "NO" : "NO"}
        suits = ["club", "spade", "heart", "diamond"]
        if self._isempty:
            for suit in suits:
                for card in range(2,15):
                    card1 = Card(card,suit)
                    self._cards.append(card1)
        else:
            read_val = in_val[input("Your progress will be lost do you want to rebuild again?(y/n)")]
            if read_val == "YES":
                self._cards = []
                for suit in suits:
                    for card in range(2,15):
                        card2 = Card(card,suit)
                        self._cards.append(card2)

    def show(self):
        for card in self._cards:
            print(card)
            
    def shuffle(self):
        shuffle(self._cards)
    
    def draw(self):
        last_card = deepcopy(self._cards[-1])
        self._cards.remove(self._cards[-1])
        return last_card
    
    def add(self, card):
        self._cards.insert(0,card)
