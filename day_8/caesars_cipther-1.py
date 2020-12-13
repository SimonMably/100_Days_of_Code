
# Letters of the alphabet are duplicated (in order) to compensate for shift
# amount (without duplicate letters in list, the for loop in the 'encrypt()' 
# function will encounter an 'IndexError: list index out of range' error).
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function 
#TODO-1: called caesar(). 

# Best not to give the parameters and arguments the same name as to not get 
# confused as to which is which.
def encrypt(plain_text, shift_amount):

    cipher_text = ""

    for letter in plain_text:
    
        # Get the index of each letter in alphabet list, place in variable
        position = alphabet.index(letter)
        # Add position/index to given shift amount, place in new variable
        new_position = position + shift_amount
        # Place letter of new position in it's own variable.
        new_letter = alphabet[new_position]
        # Add new letter to 'cipher_text' variable
        cipher_text += new_letter
    print(cipher_text)

# works
def decrypt(plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        # This is the only difference between the decrypt() and encrypt()
        # functions
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

'''FROM COURSE SOLUTION FOR DYCRYPT FUNCTIONALITY
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
'''

# 'plain_text' & 'shift_amount' are the arguments
# 'text' & 'shift' are the parameters
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
    
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 
#TODO-2: 'direction' values.



