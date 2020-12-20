import  random
from os import system, name
from time import sleep

from blackjack_ascii_logo import logo

print(logo)

###############################################################################
# Cards/card values, player/computer cards and score

# Card values;
    # 11 = Ace card
    # 10, 10, 10, 10 = 10, Jack, Queen, King cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# User = The player
user_cards = []
#user_score = 0

# Computer = The Dealer (opponent)
computer_cards = []
#computer_score = 0
###############################################################################
# FIX LIST: ###################################################################
# 1. Turn 11 in user/computer cards list into a 1 if user/computer score > 21
# 2. Fix logic for user and computer getting a draw.
# FIX LIST ^ ##################################################################
###############################################################################
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
    # Calculates the users score and the computers score
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    # Checks users/computers cards for a blackjack
    if user_cards == [11, 10] or user_cards == [10, 11]:
        # Makes users score equal 0 o represent a Blackjack
        user_score = 0
        print("User has a Blackjack. User wins!!")
        game_over = True
    elif computer_cards == [11, 10] or computer_cards == [10, 11]:
        # Makes computers score equal 0 to represent a Blackjack
        computer_score = 0
        print("Computer has a Blackjack. The computer wins!!")
        game_over = True
    # FIX: Doen't come out as a draw.
    elif (computer_cards == [11, 10] or computer_cards == [10, 11]) and (user_cards == [11, 10] or user_cards == [10, 11]):
        computer_score = 0
        user_score = 0
        print("The User and the Computer have an Ace. It's a draw!!")
    
    # User/computer loses game if user/computer score > 21
    if user_score > 21:
        print(f"User busts with a score of {user_score}.")
        game_over = True
    elif computer_score > 21:
        print(f"Computer busts with a score of {computer_score}.")

    print(user_score)
    print(computer_score)

    return user_score, computer_score

def compare_score(user_score, computer_score):
    '''Compares the scores of the user and the computer.'''
    pass

def clear_screen():
    '''Clears terminal screen.'''
    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def game_over():
    '''Ends the game.'''
    #! Gives TypeError: 'bool' object is not callable
    game_over = True

def blackjack():
    '''Main game loop for blackjack.'''
    game_over = False
    user_score = 0
    computer_score = 0

    while not game_over:
        # If user and computer have no cards, give each 2 cards
        if len(user_cards) == 0 and len(computer_cards) == 0:
            user_cards.append(deal_card())
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            computer_cards.append(deal_card())

        # If user/computer has an Ace AND has a score > 21, remove Ace and 
        # replace with 1
        # FIX: Both for loops are not working at all.
        for card in user_cards:
            if user_score > 21 and card == 11:
                user_cards.remove(11)
                user_cards.append(1)
        for card in computer_cards :
            if computer_score > 21 and card == 11:
                computer_cards.remove(11)
                computer_cards.append(1)
        
        # TODO: Hint 9
        # TODO: Hint 10
        # TODO: Hint 11
        # TODO: Hint 12
        # TODO: Hint 13
        # TODO: Hint 14


        # End game if user/computer either has a blackjack or a score > 21
        calculate_score(user_cards, computer_cards)
        #if 


        #* Next 3 lines of code: To make sure everything is working.
        print(f"User: {user_cards}")
        print(f"Computer: {computer_cards}")
        calculate_score(user_cards, computer_cards)

        game_over = True

blackjack()