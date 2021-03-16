import random
from os import system, name
from time import sleep

from deck import Deck
from card import Card
from player import Player
from dealer import Dealer
from scoreboard import Scoreboard


deck = Deck()
card = Card()
player = Player()
dealer = Dealer()
score = Scoreboard()

def clear_screen():
    """Clears the terminal screen."""
    # For Windows Operating Systems
    if name == 'nt':
        _ = system('clear')

    #For Mac and Linux Operating Systems (here, os.name is 'postix')
    else:
        _ = system('clear')


def blackjack():
    is_game_over = False

    while not is_game_over:
        # Deal (append) 2 cards to both player and dealer
        pass






