import random

import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)

lives = 6

# Hangman ASCII art logo
print(f"{hangman_art.logo}\n\n")

# Testing Code
print(f"The solution is: {chosen_word}")

# Takes the length of 'chosen_word' and populates 'display' with as many 
# underscores.
display = []
word_length = len(chosen_word)
# Method 1
for letter in range(word_length):
    display += "_"
'''
# or Method 2
for letter in chosen_word:
    display += "_"
print(display)
'''
end_of_game = False

while not end_of_game:
# 'while "_" in display:' also would have worked 

    guess = input("\nGuess a letter: ").lower()

    # Prints message to the screen if user guesses an already guessed letter
    if guess in display:
        print(f"You have already guessed {guess}")

    # Taking 'guess' and displaying guessed letter in the relavent position in 
    # the 'display' list.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"\nThe letter {guess} is not in the word. You have {lives} "
               "left. Try again.\n")
        if lives == 0:
            end_of_game = True
            print("\nYou lose.\n")

    # Guessed letters will have replace underscores.
    # Items/elements in the 'display' list will join to make a string.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        # If using 'while "_" in display:' for while loop, if statement should
        # not be used and print statement below should go outside of while loop.
        print("\nCongratulations! You win!\n")

    # Taking lives into account, prints the stage of the hanging man after 
    # each turn.
    print(hangman_art.stages[lives])
    
    '''
    # Also works:
    if lives == 6:
        print(hangman_art.stages[6])
    elif lives == 5:
        print(hangman_art.stages[5])
    elif lives == 4:
        print(hangman_art.stages[4])
    elif lives == 3:
        print(hangman_art.stages[3])
    elif lives == 2:
        print(hangman_art.stages[2])
    elif lives == 1:
        print(hangman_art.stages[1])
    elif lives == 0:
        print(hangman_art.stages[0])
    '''