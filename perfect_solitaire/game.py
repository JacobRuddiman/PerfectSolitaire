class Card:
    def __init__(self, rank, suit, face_up=False):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up 

class tableau:
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
        self.tableaus = [tableau() for _ in range(7)]
        self.waste = Waste()

    def create_deck(self):
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')
        suits = 'hearts diamonds clubs spades'.split()
        return [Card(rank, suit) for suit in suits for rank in ranks]
    
    def get_cards_info(self):
        cards_info = []
        for card in self.stock.cards + self.waste.cards + \
                     self.foundation_hearts.cards + self.foundation_diamonds.cards + \
                     self.foundation_spades.cards + self.foundation_clubs.cards + \
                     [card for tableau in self.tableaus for card in tableau.cards]:
            cards_info.append({
                "rank": card.rank,
                "suit": card.suit,
                "face_up": card.face_up
            })
        return cards_info
    
    def get_card_variables(self, card_list):
        card_variables = []
        for card in card_list:
            card_variables.append({"rank": card.rank, "suit": card.suit, "face_up": card.face_up})
        return card_variables
    
    def get_tableau_cards(self):
        tableau_cards = []
        for tableau in self.tableaus:
            tableau_cards.extend(tableau.cards)
        return self.get_card_variables(tableau_cards)

    # Function to get all cards in Foundations
    def get_foundation_cards(self):
        foundation_cards = self.foundation_hearts.cards + self.foundation_diamonds.cards + self.foundation_spades.cards + self.foundation_clubs.cards
        return self.get_card_variables(foundation_cards)

    # Function to get all cards in Stock
    def get_stock_cards(self):
        return self.get_card_variables(self.stock.cards)

    # Function to get all cards in Waste
    def get_waste_cards(self):
        return self.get_card_variables(self.waste.cards)
    
    def get_faceup_cards(self):
        faceup_cards = []
        for card in self.stock.cards:
            if card.face_up:
                faceup_cards.append(card)

        for card in self.waste.cards:
            if card.face_up:
                faceup_cards.append(card)

        for tableau in self.tableaus:
            for card in tableau.cards:
                if card.face_up:
                    faceup_cards.append(card)

        for foundation in [self.foundation_hearts, self.foundation_diamonds, self.foundation_spades, self.foundation_clubs]:
            for card in foundation.cards:
                if card.face_up:
                    faceup_cards.append(card)
        return faceup_cards

    
    
    

def main():
    print("Let's play Solitaire!")
    
    solitaire = Solitaire()
    #print(solitaire.get_cards_info())

    print("All cards in tableaus:", solitaire.get_tableau_cards())
    print("All cards in Foundations:", solitaire.get_foundation_cards())
    print("All cards in Stock:", solitaire.get_stock_cards())
    print("All cards in Waste:", solitaire.get_waste_cards())
    print("All face up cards:", solitaire.get_faceup_cards())


if __name__ == "__main__":
    main()
