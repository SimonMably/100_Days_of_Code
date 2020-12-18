import random

from blackjack_ascii_logo import logo

#print(logo)

#############################################################################
# Cards/card values, player/computer cards and score.

# Card values;
    # 11 = Ace card
    # 10, 10, 10, 10 = 10, Jack, Queen, King cards
cards = [11, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 10, 10, 10]

# User == the Player
user_cards = []
user_score = 0

# Computer == the Dealer
computer_cards = []
computer_score = 0

##############################################################################
# Functions

def deal_card():
    '''Deals cards to the computer and to the user.'''
    random_card = random.choice(cards)

    return random_card
    

def calculate_score(user_cards, computer_cards):
    '''
    Calculates the combined values of the players cards and the combined values
    of the computer.
    '''
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    # TODO 1: Hint 7
    # TODO 2: Hint 8
    # TODO 3: Hint 9

    return user_score, computer_score

def compare_score():
    '''Compares the scores of the user and the computer.'''
    # TODO 1: Hint 13
    pass

##############################################################################
# TEST FUNCTION LAB == Making sure that functions work as intended
 
# deal_card() #! THIS DOESN'T WORK
# print(deal_card(), deal_card())  #? THIS DOES WORK (prints 2 cards)

#------------------------------------------------------------------------------
'''
print(user_cards)
# user_cards.append(deal_card())
# user_cards.append(deal_card())
deal_card()
print(user_cards)
total = sum(user_cards)  # WORKS, adds all integers in list together
print(total)             # prints the result of the above sum(user_cards)
'''
#------------------------------------------------------------------------------

#* Appends 2 cards to each list if both lists are empty.
if len(user_cards) == 0 and len(computer_cards) == 0:
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

print(f"User: {user_cards}")
print(f"Computer: {computer_cards}")


print(len(user_cards))

##############################################################################
# Game Loop















