import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

length_of_names = len(names)

# bill_payee = random.randrange(-1, length_of_names)
#print(f"{names[bill_payee]} has to pay the bill.")

bill_choice = random.randint(0, length_of_names - 1)

bill_payee = names[bill_choice]
print(f"{bill_payee} is going to buy the meal today!")


# random.choice() would be better for all of this.
















