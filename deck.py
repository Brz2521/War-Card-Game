from card import Card,suits,ranks,values,random

class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)


new_deck = Deck()

bottom_card = new_deck.all_cards[-1]
