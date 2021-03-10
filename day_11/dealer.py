import random
from deck import Deck


class Dealer:

    def __init__(self):
        self.dealer_cards = []
        self.deck = Deck()

    def deal_card(self):
        """"""
        random_card = random.choice(self.deck.cards)














