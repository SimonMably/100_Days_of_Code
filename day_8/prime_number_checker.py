
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    # divider = the number that's dividing the variable 'number'
    # To get the dividing number (divider), use a for loop to get the dividing
    # number from a range from 2 - 'number'.
    for divider in range(2, number):
        # Calculates whether the 'number' is or isn't a prime number.
        if number % divider == 0:     
            is_prime = False

    # If 'is_prime' == True      
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# There are other ways to accomplish all of this.
