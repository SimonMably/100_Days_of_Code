'''Debug the following bugs.'''

############DEBUGGING#####################

#* Describe Problem
# The problem was with the condition in the if statement and the second 
# parameter in the range() function. The thing about the range() function is 
# that it will take 2 numbers and will go from the first number up to and not 
# including the second number, in this case the first number being 1 and the 
# second number being 20. The range() function will cycle through these numbers
# until it gets to 20 and stops before it uses the number. And because of the 
# condition in the if statement, its print() statement wouldn't have done 
# anything. 
# To solve this problem, either change the second parameter in the range()
# function to 21.
# Works
def my_function():
  for i in range(1, 21):
      if i == 20:
          print("You got it")
my_function()

print("\n")
#* Reproduce the Bug
# The issue was with the parameters in the randint() function. In this example,
# the parameters in the randint() function are being used to get the value from
# a random index from the 'dice_imgs' list. Originally, the parameters for the 
# randint() function were set to 1, 6 which in this case were to act as index 
# positions. This is where the problem lies as 1) in programming, list indeces 
# start at 0 and 2) the 'dice_imgs' list (even thought there are 6 items in this
# list) its last item occurs on its 5th index position. If this example was 
# not fixed, it would return an IndexEerror.
# Works
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

print("\n")
#* Play Computer
# This looks like one of those 'really easy to spot' bugs. The logic/conditions
# totally miss out on the year 1994, which I don't think was intentional. To fix
# this, edit the logic to include the = sign (eg. if year > 1980 and year <= 1994)
# Works
year = int(input("What's your year of birth? "))
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

print("\n")
#* Fix the Errors
# Problem 1) The code directly after the if statement is not properly indented, 
# so it willreturn an IndentationError. To fix, indent the print() statement so 
# it will fall imto the if statements scope.
# Problem 2) Since inputs from an input() function are classes as strings, its 
# datatype doesn't match the datatype of the integer within the if statement. 
# To fix this, the input() function below has to be wrapped within an int() 
# function to turn the string from the input() function into an integer.
# Problem 3) The print() statement has what is supposed to be an f-string, but 
# the f-strings 'f' is missing. To fix, enter an f just before the opening 
# quotation mark.
# Works
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

print("\n")
#* Print is Your Friend
# Problem 1) The 'pages' and 'words_per_page' variables appear twice. The first
# instance of both variables have values of 0, while the second instance of 
# both variables contain input() functions. For this reason, I judge the first 
# instance of both variables to be useless and can be removed.
#   Problem 2) The second instance of the 'word_per_page' variable contains a 
# double equal sign (==), which makes it absolutely equal to its value. This can
# be fixed by removing one of the equal signs to leave just one.
#   Problem 3) The print() statement prints a number. There is no indication as 
# to what this number means when printed (we know what it means when we look at
# the code). To fix this, we could include an f-sting in the print statement
# along with 'total_words' to describe what the number means.
# Fixed
# pages = 0
# word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"Total words: {total_words}")

print("\n")
#* Use a Debugger
# Works
# The problem in this example is that 'b_list.append(new_item)' was not
# indented properly. To fix this, indent the line containing 
# 'b_list.append(new_item)', so it falls within the for loops scope.
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

##############################################################################*

#* Other Debugging Tips
# 1. Take a break
# 2. Ask a friend/developer
# 3. Run code often (to see if code working properly)
# 4. Ask StackOverflow
