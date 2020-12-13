import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = [rock, paper, scissors]
gestures = ["rock", "paper", "scissors"]

combined = [art, gestures]

player = input("Make Your Choice; Rock, Paper, Scissors: ").lower()

opponent = random.choice(combined[0])

if player == combined[1][0]:
    print(f"\nPlayer\n{combined[0][0]}")
elif player == combined[1][1]:
    print(f"\nPlayer\n{combined[0][1]}")
elif player == combined[1][2]:
    print(f"\nPlayer\n{combined[0][2]}")

print(f"\nOpponent\n{opponent}")

if player == combined[1][0] and opponent == combined[0][0]:
    # Player Rock  # Opponent Rock
    print("It's a draw.")
elif player == combined[1][0] and opponent == combined[0][1]:
    # Player Rock  # Opponent Paper
    print("Opponent Wins!")
elif player == combined[1][0] and opponent == combined[0][2]:
    # Player Rock  # Opponent Scissors
    print("Player Wins!")
elif player == combined[1][1] and opponent == combined[0][0]:
    # Player Paper  # Opponent Rock
    print("Player Wins!")
elif player == combined[1][1] and opponent == combined[0][1]:
    # Player Paper  # Opponent Paper
    print("It's a draw.")
elif player == combined[1][1] and opponent == combined[0][2]:
    # Player Paper  # Opponent Scissors
    print("Opponent Wins!")
elif player == combined[1][2] and opponent == combined[0][0]:
    # Player Scissors  # Opponent Rock
    print("Opponent Wins!")
elif player == combined[1][2] and opponent == combined[0][1]:
    # Player Scissors  # Opponent Paper
    print("Player Wins!")
elif player == combined[1][2] and opponent == combined[0][2]:
    # Player Scissors  # Opponent
    print("It's a draw.")
else:
    print("Player forfeits the game!!")

"""
# Angela's Sulution:

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or "
                    "2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw")




"""








