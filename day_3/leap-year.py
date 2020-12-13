
# Every year is evenly divisible by 4 
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# e.g. the year 200
'''
2000 / 4 = 500 (Leap year)

2000 / 100 = 20 (Not leap year)

2000 / 400 = 5
'''


year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!!")
        else:
            print(f"{year} is not leap a year.")
    else:
        print(f"{year} is a leap year!!!")
else:
    print(f"{year} is a not a leap year.")















