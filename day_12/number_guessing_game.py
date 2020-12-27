from random import randint

from logo import logo

EASY_LIVES = 10
HARD_LIVES = 5

def check_answer(guess, answer, turn):
    """
    Checks players answer to see if it matches random number. 
    Returns the amount of turns remaining.
    """
    if guess > answer:
        print("Too high. Try again")
        return turn - 1
    elif guess < answer:
        print("Too low. Try again")
        return turn - 1
    elif guess == answer:
        print(f"{guess} is correct. Well done!!")

def pick_difficulty():
    """Player chooses and returns the games difficulty level."""
    difficulty = input("Select difficulty: 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        return EASY_LIVES
    elif difficulty == "hard":
        return HARD_LIVES

def play():
    """Main game loop."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    answer = randint(1, 100)

    #* Get returned difficulty level and make equal to turn
    turn = pick_difficulty()
    guess = 0
    # print(answer)
    while guess != answer:
        print(f"{turn} turns left.")
        guess = int(input("Pick a number from between 1 and 100: "))
        #* 
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("You ran out of guesses. Game Over!")
            #* Empty return statement stops the function.
            return
        elif guess != answer:
            print("Guess again.")
play()





















