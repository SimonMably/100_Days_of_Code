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
user_score = 0

# Computer = The Dealer (opponent)
computer_cards = []
computer_score = 0

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


    for card in user_cards:
        user_score += card
    
    for card in computer_cards:
        computer_score += card

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
  
    # User/computer loses game if user/computer score > 21
    if user_score > 21:
        print(f"User busts with a score of {user_score}.")
        game_over = True
    elif computer_score > 21:
        print(f"Computer busts with a score of {computer_score}.")
    
    # If user/computer has an Ace AND has a score > 21, remove Ace and 
    # replace with 1
    if 11 in user_cards and user_score > 21:
        user_cards.remove(11)
        user_cards.append(1)
    if 11 in computer_cards and computer_score > 21:
        computer_cards.remove(11)
        computer_cards.append(1)

    return user_score, computer_score

def compare_score(user_score, computer_score):
    '''Compares the scores of the user and the computer.'''
    # TODO: Hint 13
    
    pass

def clear_screen():
    '''Clears terminal screen.'''
    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def blackjack():
    '''Main game loop for blackjack.'''
    game_over = False
    


    while not game_over:
        # If user and computer have no cards, give each 2 cards
        if len(user_cards) == 0 and len(computer_cards) == 0:
            user_cards.append(deal_card())
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
            computer_cards.append(deal_card())

        # FIX
        # End game if user/computer either has a blackjack or a score > 21
        calculate_score(user_cards, computer_cards)
        if user_score == 0:
            game_over = True
        elif user_score > 21:
            game_over = True
        if computer_score == 0 or computer_score > 21:
            game_over = True
        elif computer_score > 21:
            game_over = True       
        
        # TODO: Hint 11
        # TODO: Hint 12
        # TODO: Hint 13
        # TODO: Hint 14

        #* Next 3 lines of code: To make sure everything is working.
        print(f"User: {user_cards}")
        print(f"Computer: {computer_cards}")
        calculate_score(user_cards, computer_cards)

        # FIX: Hint 10
        # TODO: Hint 10
        # if user_score < 21:
        if not game_over:
            another_card = input("Would you like another card? y/n: ")
            if another_card == "y":
                user_cards.append(deal_card())
                print(sum(user_cards))
                calculate_score(user_cards, computer_cards)
                print(user_score)
            elif another_card == "n":
                game_over = True
        
        print(user_cards)
        print(user_score)

        #game_over = True
        
blackjack()

##############################################################################!
#* FIX LIST
# FIX: user_score reverts to 0 when user presses 'y' for a new card.
# FIX: If user_score < 21, game does not ask user if they want another card.

