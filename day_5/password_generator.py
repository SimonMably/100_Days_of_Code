import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    password += random_letter
    # or can use:
    # password = random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    password += random_symbol
    # or can use:
    # password = random.choice(symbols)

for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    password += random_number
    # or can use:
    # password = random.choice(numbers)

print(f"Easy Password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

shuffled_password = random.sample(password, k=len(password))

password = "".join(shuffled_password)

print(f"Hard Password: {password}")
'''
# Or:

password_list = []

for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

# Turn 'password_list' into a string
# Method #1: for loop
password = ""
for character in password_list:
    password += character

print(f"Hard Password: {password}")

'''