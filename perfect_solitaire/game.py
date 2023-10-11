class Card:
    def __init__(self, rank, suit, face_up=False):
        self.rank = rank
        self.suit = suit
        self.face_up = False
        self.location = "stock"

     

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
    
    def get_face_up_cards_info(self):
        cards_info = []
        for card in self.stock.cards + self.waste.cards + \
                     self.foundation_hearts.cards + self.foundation_diamonds.cards + \
                     self.foundation_spades.cards + self.foundation_clubs.cards + \
                     [card for tableau in self.tableaus for card in tableau.cards]:
            if card.face_up:
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
    
    def get_foundation_from_suit(self, suit):
        if suit == "clubs":
            return self.foundation_clubs
        elif suit == "diamonds":
            return self.foundation_diamonds
        elif suit == "spades":
            return self.foundation_spades
        else:
            return self.foundation_hearts
        
    def compare_card_ranks(self, rank_1, rank_2):
        rank_1 = self.convert_to_digit(rank_1)
        rank_2 = self.convert_to_digit(rank_2)
        return rank_1 - rank_2

    def convert_to_digit(self, rank):
        if rank == 'J':
            return 11
        if rank == 'Q':
            return 12
        if rank == 'K':
            return 13
        if rank == 'A':
            return 1
        return rank    

    def move_from_waste_to_foundation(self, foundation, make_move):
        if not self.waste.cards:
            print("Waste empty")
            return False
        card_to_move = self.waste.cards[-1]
        try:
            top_foundation_card = foundation.cards[-1].rank
        except:
            top_foundation_card = None
        if card_to_move.suit == foundation.suit and ((not foundation.cards and card_to_move.rank == 'A') or (top_foundation_card and self.compare_card_ranks(foundation.cards[-1].rank, self.waste.cards[-1]) == -1)):
            foundation.cards.append(card_to_move)
            #Assign self.foundation to foundation
            self.waste.cards.remove(card_to_move)
            return True
        return False
    
    def move_from_stock_to_waste(self):
        if not self.stock.cards:
            return False
        
        card = self.stock.cards.pop()
        if not card.face_up:
            card.face_up = True

        self.waste.cards.append(card)
        return True
    
    
    def move_from_waste_to_tableau(self, tableau_pile):
        if not self.waste.cards:
            print("Waste empty")
            return False
        card_to_move = self.waste.cards[-1]
        try:
            top_tableau_card = self.tableaus[tableau_pile].cards[-1]
        except:
            top_tableau_card = None
            self.waste.cards.remove(card_to_move)
            self.tableaus[tableau_pile].cards.append(card_to_move)
            return True
        if ((self.is_red(top_tableau_card.suit) == self.is_red(card_to_move.suit)) and self.compare_card_ranks(top_tableau_card.rank, card_to_move.rank) == 1):
            self.waste.cards.remove(card_to_move)
            self.tableaus[tableau_pile].append(card_to_move)
            return True
        return False

    def is_red(self, suit):
        if suit == "clubs" or suit == "spades":
            return True
        return False


    def print_cards_in_list(self, cards):
        for card in cards:
            print(self.get_card_variables(card))
    
    

def main():
    print("Let's play Solitaire!")
    
    solitaire = Solitaire()
    #print(solitaire.get_cards_info())
    solitaire.move_from_stock_to_waste()
    solitaire.move_from_waste_to_foundation(solitaire.foundation_spades, True)
    solitaire.move_from_stock_to_waste()
    solitaire.move_from_waste_to_tableau(3)

    print("All cards in Tableaus:", solitaire.get_tableau_cards())
    print("All cards in Foundations:", solitaire.get_foundation_cards())
    print("All cards in Stock:", solitaire.get_stock_cards())
    print("All cards in Waste:", solitaire.get_waste_cards())
    print("All face up cards:", solitaire.get_faceup_cards())

    print("\n Face-up:" + str(solitaire.get_face_up_cards_info()))


if __name__ == "__main__":
    main()
