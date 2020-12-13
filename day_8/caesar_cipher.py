from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    # start_text, shift_amount, cipher_direction
    end_text = ""

    # if statement can't go in for loop because it will cause a bug.
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        # If we wanted to, instead of doing this if statement to ignore extra
        # characters, we could include all characters (not just letters) in the 
        # list at top of file. That way, all characters that get entered in
        # this cipher can be encoded/encoded.
        if character in alphabet:
            position = alphabet.index(character)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
            # Equations for shift_amount and new_position together is basially 
            # the same as subtraction.
            # eg. 
            # 5(shift_amount) * -1 = -5
            # 12(new_postion) + -5 = 7
        else:
            end_text += character
    print(f"The {cipher_direction}d text is {end_text}")

# Prints ASCII art from 'caesar_cipher_art.py' module
print(logo)

#------------------------------------------------------------------------------
# At end of encoding/decoding of message, program asks user if they want to restart
def retry_cipher():
    retry = input(str("\nWould you like to use the Caesar Cipher again? yes/no\n"))
    retry.lower()

    if retry == "yes":
        direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
        retry_cipher()

    elif retry == "no":
        print("The Caesar Cipher will close now.")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
""" COURSE ANSWER
should_continue = True
while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = input(str("\nWould you like to use the Caesar Cipher again? yes/no\n"))
    if result == "no":
        should_continue = False
        print("Goodbye")
"""

# -----------------------------------------------------------------------------

# shift == shift_amount
# If user gives a shift_amount > length of alphabet list, the program will
# give an IndexError. 
# The code below takes the user provided shift amount, divides it by the total
# number of letters in the alphabet as many times as needed, and then returns 
# the ramainding amount (eg. 45(shift) % 26(amount of letters) = 19(remainder)).

# The remainer of the equation will then be set as the value of shift. This 
# value (of the remainder) will be used to get each letter in the for loop in
# the 'caesar()' function instead of the original shift amount given by the 
# user.
# This is the equivalent of getting a shift amount of 45, iterating 
# though the alphabet list to get the letter at the 45th position, getting to 
# the letter at the 26th position and then returning to the beginning of the 
# the alphabet list to continue iterating throught the next 19 letters.

# The code below effectively bypasses the original given shift amount and sets 
# the shift amount as the remainder instead, since the remainder would be used
# on the second-go-round anyway.
shift = shift % 26  # 26 == the number of letters in alphabet


caesar(start_text=text, cipher_direction=direction, shift_amount=shift)
retry_cipher()




















