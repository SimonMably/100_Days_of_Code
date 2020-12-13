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

find_treasure = ("\nCongratulations!!!! You found treasure. You're staying "
                "alive! But more \nimportantly, the rum is on you!!")

other_answer = ("\nYou choose to do something else. For that, the locals of "
                "Treasure Island have \nsacrificed you to their treasure gods. "
                "You are dead!!!")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print('''
When promted to make a choice, pick a word (displayed in single quotes) and 
enter in the prompt to proceed. Pick wisely.
''')


# First Choice
answer_1 = input("You are on the beach, Would you like to head 'East' or "
                 "'West'? \n")
choice_1 = answer_1.lower()
if choice_1 == "west":
    print("\nYou fell in quick-sand. You're dead!!")

elif choice_1 == "east":
    answer_2 = input("\nYou have come to a lake. Would you like to 'Swim' or "
                     "'Wait'? \n")
    choice_2 = answer_2.lower()
    if choice_2 == "swim":
        print("\nThe lake contained deadly piranhas. They thought you were "
            "delicious. You are \ndead!!")

    elif choice_2 == "wait":
        answer_3 = input("\nA local of Treasure Island appear in a row boat and "
                        "takes you to a little \nisland containing a building "
                        "with three different coloured doors. Do you pick \n" 
                        "the 'Green', 'Red' or 'Yellow' door? \n")
        choice_3 = answer_3.lower()
        if choice_3 == "red" or choice_3 == "green":
            print("\nA fellow treasure hunter is hiding behind the door. He "
                "kills you and is nice \nenough to bury you. You're dead!!")

        elif choice_3 == "yellow":
            print(find_treasure)

        else:
            print(other_answer)

    else:
        print(other_answer)

else:
    print(other_answer)



















