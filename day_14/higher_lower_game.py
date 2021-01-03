import random
from os import system, name
from time import sleep

from art import logo, vs
from game_data import data
# from replit import clear  #* Only works on repl.it

def clear():
    """Clears the terminal window."""
    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#!! Solution from Udemy course
# Format the account data into printable format.
def format_account_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description} from {account_country}"

## Use if statement to check if user is correct
def check_answer(player_guess, a_followers, b_followers):
    """
    Takes player guess and follower counts and returns if they got it right.
    """
    # Need an if statement to check if players guess is correct
    #? See 'player_guess_if_statement.png' as reference for logic
    # 1) shorter and more simpler way than 2
    if a_followers > b_followers:
        return player_guess == "a"
        #* When evaluated, 'player_guess == "a"' will return 'True', but if
        #* 'player_guess == "a"' isn't "a", it will return 'False'.
    else:
        return player_guess == "b"
        #* The same thing that's going on in the if statement, except for "b"
        #* instead of "a".
    '''#> 2 other ways for the if statement
    # 2) Shorter version
    if a_followers > b_followers:
        if player_guess == "a":
            return True
        else:
            return False
    # 3) The really long way - cons = a lot of code, easy to get lost in logic
    if a_followers > b_followers and player_guess == "a":
        print("something")
    elif a_followers > b_followers and player_guess == "b":
        print("something")
    elif b_followers > a_followers and player_guess == "a":
        print("something")
    elif b_followers > a_followers and player_guess == "b":
        print("something")
    '''
# Display art.
print(logo)
player_score = 0
game_should_continue = True
account_b = random.choice(data)

# Make game repeatable
while game_should_continue:

    # Generate a random account from the game data.
    # Making account at position b become the next account ast position a
    account_a = account_b
    account_b = random.choice(data)

    # To stop account_a and account_b from retreving the same data.
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_account_data(account_b)}")

    # Ask user for a guess
    player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count for each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(player_guess, a_follower_count, b_follower_count)

    # Clear screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        player_score += 1
        print(f"You're right!! Current score: {player_score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {player_score}.")


'''#!! My attempt at solution
profile_a = {}
profile_b = {}

def clear():
    """Clears the terminal window."""
    # For windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
def get_profile_data():
    """Retrieves profile data."""
    
    profile_a = random.choice(data)
    profile_b = random.choice(data)

    print(f"a) {profile_a['name']}, a {profile_a['description']} from {profile_a['country']}")
    print(vs)
    print(f"b) {profile_b['name']}, a {profile_b['description']} from {profile_b['country']}")

    return random.choice(data)
    

def compare_profiles():
    """Compares the profiles of two people/organisations."""
    pass

def game():
    """Main function for the game."""
    print(logo)

    player_score = 0
    game_end = False

    while not game_end:
        get_profile_data()

        player_guess = input("\nGuess who has more followers. Type 'a' or 'b': ")

        if player_guess == "a":
            compare_profiles()
            player_score += 1        
        elif player_guess == "b":
            compare_profiles()
            player_score += 1  
   
game()
'''
