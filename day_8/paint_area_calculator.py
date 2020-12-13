import math

#Write your code below this line 👇

def paint_calc(height, width, cover):
    total_cans_of_paint =  round((height * width) / cover + 1)
    #total_cans_of_paint = math.ceil((height * width) / cover)

    print(f"You'll need {total_cans_of_paint} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

'''
# Course solution

import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


'''









