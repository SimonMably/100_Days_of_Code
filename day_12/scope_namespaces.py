
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
















