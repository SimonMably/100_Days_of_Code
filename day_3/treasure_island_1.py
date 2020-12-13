print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Triple single-quotes allow python to accept multi-line strings without 
# needing a lot of code or a print() function on each line. Great for ASCII art

# -----------------------------------------------------------------------------

find_treasure = '''Congratulations!!!! You found treasure. You're staying 
                   alive! But more importantly, the rum is on you!!'''

other_answer = '''You chose to do something else. For that, the locals of 
                  Treasure Island have sacrificed you to their treasure gods. 
                  You are dead!!!'''


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print('''
When promted to make a choice, pick a word (displayed in single quotes) and 
enter in the prompt to proceed. Pick wisely.
''')

# First Choice
answer_1 = input("You are on the beach, Would you like to head 'East' or "
                 "'West'? ")
choice_1 = answer_1.lower()
if choice_1 == "west":
    print("You fell into quick-sand. You're dead!!")

elif choice_1 == "east":
    # Second Choice
    answer_2 = input("You have come to a lake. Would you like to 'Swim' or "
                     "'Wait'? ")
    choice_2 = answer_2.lower()

    if choice_2 == "swim":
        print('''
          The lake contained deadly piranhas. They thought you were 
          delicious. You are dead!!)
    
    elif choice_2 == "wait":
        answer_3 = input('''
        A local of Treasure Island appear in a row boat and takes you to a 
        little island containing a building with three different coloured 
        doors. Do you pick the 'Green', 'Red' or 'Yellow' door?''')
        choice_3 = answer_3.lower()
        
        if choice_3 == "green" or choice_3 == "red":
            print("A fellow treasure hunter is hiding behind the door. He "
                  "kills you and is kind enough to bury you. You're dead!!")
        
        elif choice_3 == "yellow":
            print(find_treasure)
        
        else:
            print(other_answer)

"""
(

if choice_1 == "east":
    # 
    if choice_1 == "west":
      print("You fell into quick-sand. You're dead!!")
    elif choice_2 == "wait":    # 
        if choice_3 == "yellow":
            print("Congratulations!!!! You found treasure. You're staying "
                  "")
        elif choice_3 == "green" or choice_3 == "red":
            print("A fellow treasure hunter is hiding behind the door. He "
                  "kills you and is kind enough to bury you. You're dead!!")
        else:
            print('''
            You chose to do something else. For that, the locals of Treasure 
            Island have sacrificed you to their treasure gods. You are dead.
            ''')
    elif choice_2 == "swim":
        print("The lake contained deadly piranhas. They thought you were "
            "delicious. You are dead!!")
    else:
        print('''
        You chose to do something else. For that, the locals of Treasure Island 
        have sacrificed you to their treasure gods. You're dead!!
        ''')
elif 
else:
    print('''
You chose to do something else. For that, the locals of Treasure Island have
sacrificed you to their treasure gods. You are dead.
    ''')

)


"""




















