
#! Namespaces: Local vs Global Scope

# Local scope = Variables (or anything that we name) that are declared inside
#  a function and can only be accessed inside that particular function. 

# Global scope = Variables (or anything that we name) that are declared outside
# of functions and can be accessed anywhere in the program (in any function, 
# class or loop).

player_health = 10  #- Variable has global scope

def drink_potion():
    potion_strength = 2  #* Variable has local scope
    print(potion_strength)  #* 1) Accessing variable with local scope
    print(player_health)  #- 1) Accessing variable with global scope
drink_potion()
#* print(potion_strength)  #* 2) Accessing variable with local scope
print(player_health)  #- 2) Accessing variable with global scope
#* If 'potion_strength' variable is accessed outside of the 'drink_potion()' 
#* function, then the program will retrn a traceback error:
    #* 'NameError: name 'potion_strength' is not defined'

#- Global variables can be accessed in any function AND outide functions.

# Anything that is given a name has a 'Namespace'. That Namespace is valid 
# in certain scopes. This concept of scope applies to anything that we name.
# So, when we name something, we need to be aware of WHERE we created it.

##############################################################################?
##############################################################################?
#! Does Python have Block Scope
# Unlike some other languages (eg. c++ and java), Python doesn't have Block
# Scope. This means that variables that are created inside for loops, while 
# loops and if-elif-else statements can be used outside these for loops, while 
# loops and if-elif-else statements. Variables created with for loops, while 
# loops and if-elif-else statements are still subject to LOCAL and GLOBAL scope
# though, meaning that loop/if statement variables created inside functions can
# only be used inside functions (local scope) and variables created outside of
# functions can be used anywhere.

#* TO CLARIFY: for loops, while loops and if-elif-else statements DO NOT create
#*             their own LOCAL scope.

##############################################################################?
##############################################################################?
#! How to Modify Variables with Global Scope

# A variable with a global scope and variable with a local scope can have the 
# same name within the same file, but they will be considered 2 different
# variables. For example:
'''
enemies = 1

def increase_enemies():
    enemies = 2
    # This will print the 'enemies' variable from inside the function
    print(f"Enemies inside function: {enemies}")
increase_enemies()

# This will print the 'enemies' variable from outside the function
print(f"Enemies outside function: {enemies}")
'''
#! Giving the same name to 2 or more variables in the same program/file is 
#! typically a bad idea, regardless of scope. It is confusing and is prone to
#! creating bugs and errors.
#! Two reasons why this is a bad idea anderror prone: 
    #! 1. The variable that has global scope could have been entered anywhere 
    #!    in the program/file,
    #! 2. The global scope variable and local scope variable could have been
    #!    written independently of each other, easily hours or days apart.

#! These can make everything more fallible and easy to fail. This is why people 
#! say to avoid modifying global scope variables. We can read and use global
#! variables, but not modify them.

# For a variable with a local scope to modify a variable with a global scope, 
# we have to explicitly tell the function that we want to tap into a global
# variable from inside the local scope. We can do this with the 'global' 
# keyword. For example:
'''
enemies = 1

def increase_enemies():
    global enemies
    enemies += 1  #! Doing this is not a good idea.
    print(f"Enemies inside function: {enemies}")
increase_enemies()

print(f"Enemies outside function: {enemies}")
'''

#! Without the global keyword, we cannot access a variable with a global scope
#! from a variable with a local scope.

#? How to change values in a global variable in a good way
enemies = 1

def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

##############################################################################?
##############################################################################?
#! Python Constants and Global Scope

# Python constants are variables that have global scope and have values we know
# should not change. Also, when naming these constants, all leeters in the name
# should be in uppercase (numbers and underscore can be included as normal).




