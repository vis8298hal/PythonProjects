class Suit:
    SYMBOLS = {"club" : "♣", "spade" : "♠", "diamond" : "♦", "heart" : "♥","invalid" : ""}
    def __init__(self, description):
        self._symbol = Suit.SYMBOLS[description.lower()]
        self._description = description
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def description(self):
        return self._description
    
    def __str__(self):
        return f"{self._description} of {self._symbol}"
    
