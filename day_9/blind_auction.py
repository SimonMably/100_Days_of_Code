from os import system, name
from time import sleep
# from replit import clear  # Only works on repl.it

from blind_auction_art import logo

# -----------------------------------------------------------------------------
# My attempt at solution
"""
bids = {}

bidding_finished = False

def clear():
    '''Clear command-line screen.'''

    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_bid():

    while not bidding_finished:
        # TODO 2: Ask bidder for name (user input)
        bidder_name = input("What is your name? ")
# TODO 2: Ask bidder for name (user input)
# TODO 3: Ask bidder for bid (user input)
        bid_amount = int(input("How much would you like to bid? £"))

        
        bids[bidder_name] = bid_amount

        find_bidders()

def find_bidders():
# TODO 4: Put name of bidder and their bid in a dictionary as Key and Value
# TODO 5: Ask if there are any other bidders (user input - yes/no)
        # ! 'yes' - Clear Screen, get bidder name and bid, place in dictionary.
        # ! 'no' - Find the highest bidder and announce that they won the bid
    more_bidders = str(input("Is there any more bidders? yes/no: ")).lower()
    if more_bidders == "yes":
        clear()
        get_bid()
    elif more_bidders == "no":
        
        highest_bid = 0
        for bid in bids[bidder_name]:
            if bid > highest_bid:
                highest_bid = bids[bidder_name]
                print(bid)
        print(bids)
        bidding_finished = True
    # else:
    #     print("You can only type 'yes' or 'no'.")

# ! IDEA: Place TODO's 2, 3 and 4 in a function and TODO 5 in its own function
# -----------------------------------------------------------------------------
# Log and other stuff

# TODO 1: Import ASCII art logo from art.py (provided by course) and print
# Program logo
print(logo)

# Each bidder & their bid will be entered into 'bids' dictionary

get_bid()
"""
###############################################################################
# With the help of the course solution

def clear_command_line():
    '''Clear command-line screen. For use outside of repl.it'''

    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding-record represents all of the bids (the names and values) in
    # the 'bids' dictionary.
    for bidder in bidding_record:  # Looping through the keys (bidder = dictionary key)
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of £{highest_bid}.")

print(logo)

finished_bidding = False
while not finished_bidding:
    bidder_name = input("What is your name? ")
    # bid_amount needs to be an integer to be compared with highest_bid in 
    # find_highest_bid() function.
    bid_amount = int(input("how much would you like to bid? £"))
    bids = {}
    bids[bidder_name] = bid_amount
    more_bidders = input("are there more bidders? 'yes'/'no': \n")
    if more_bidders == "no":
        finished_bidding = True
        find_highest_bidder(bids)
    elif more_bidders == "yes":
        clear_command_line()
