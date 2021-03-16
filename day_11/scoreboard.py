from card import Card

class Scoreboard:
    """Class that calculates the scores for the player and dealer."""

    def __init__(self):
        self.player_score = 0
        self.dealer_score = 0
        self.cards = Card()

    def calculate_score(self, cards):
        """Takes a list of cards, from both the player or the dealer, returns 
        the score calculated from cards within lists and adds to players and 
        dealers scores."""
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0

        if 11 in self.cards and sum(self.cards) > 21:
            self.cards.remove(11)
            self.cards.append(1)

    def compare(self):
        """Compares players and dealers scores. Checks if scores are over the
        score limit, and for wins, loses and draws by score."""
        if self.player_score > 21:
            return "Youn went over 21. You lose."

        
























