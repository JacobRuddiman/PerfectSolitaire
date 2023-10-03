class Card:
    def __init__(self, rank, suit, face_up=False):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up 

class Pile:
    def __init__(self):
        self.cards = []

class Foundation:
    def __init__(self, suit):
        self.suit = suit
        self.cards = []

class Stock:
    def __init__(self, cards):
        self.cards = cards

class Waste:
    def __init__(self):
        self.cards = []

class Solitaire:
    def __init__(self):
        self.stock = Stock(self.create_deck())
        self.foundation_hearts = Foundation("hearts")
        self.foundation_diamonds = Foundation("diamonds")
        self.foundation_spades = Foundation("spades")
        self.foundation_clubs = Foundation("clubs")
        self.piles = [Pile() for _ in range(7)]
        self.waste = Waste()

    def create_deck(self):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'hearts diamonds clubs spades'.split()
        return [Card(rank, suit) for suit in suits for rank in ranks]
    

def main():
    print("Let's play Solitaire!")
    
    solitaire = Solitaire()
    deck = solitaire.create_deck()


if __name__ == "__main__":
    main()
