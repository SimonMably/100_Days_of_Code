
number = int(input("Which number do you want to check? "))

# if statement returns a SyntaxError because condition has been asigned the 
# value of 0.
#! if number % 2 = 0:
# Solve by adding a 2nd = sign to make condition equal to 0.
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
