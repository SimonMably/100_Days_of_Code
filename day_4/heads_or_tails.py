import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

coin_flip = random.randint(0, 1)

if coin_flip == 0:
    print("Tails")
else:
    print("Heads")




