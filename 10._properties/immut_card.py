

class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit
    
    @property
    def rank(self):
        return self._rank
    

suits = ["Heart", "Clubs", "Spades", "Diamonds"]

cards = [Card(suit, rank) for suit in suits for rank in range(1, 14)]

for card in cards:
    print(f"{card.rank} of {card.suit}")


class Number():
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if value > self._value:
            self._value = value
        else:
            raise ValueError

number = Number(40)
print(number.value)
number.value = 400
print(number.value)
number.value = 40
print(number.value)