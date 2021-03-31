
fruits = ["Apple", "Pear", "Orange"]


# My attempt:
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


try:
    make_pie(4)
except IndexError:
    # make_pie(2)
    print("Fruit pie")
else:
    make_pie(4)

'''


# Course Solution:
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")
    

make_pie(4)
'''

