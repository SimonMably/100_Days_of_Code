import random
from card import Card


class Dealer:

    def __init__(self):
        self.card = Card()
        self.cards = []

    def deal_card(self):
        """Deals cards to player and dealer."""
        random_card = random.choice(self.card.cards)
        random_suit = random.choice(self.card.suits)
        return f"{random_card} of {random_suit}"














