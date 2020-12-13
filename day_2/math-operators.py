# Mathematical Operators:
'''
+ - plus/addition (concatonates when used inbetween strings)
- - minus/subtraction
* - multiply
/ - divide (results in float data type)
** - exponents (used to get a numbers power. eg. 2 to the power of 5 (2 ** 5))
'''

# If multiple types of math operators are used in the same line of code, then 
# each operator should take a certain level of priority. eg. division and
# multiplication will be seen as first class, while addition and subtraction 
# be seen as economy.

# PEMDAS (order of priority, from left to right):
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication *
# 4. Division /
# 5. Addition +
# 6. Subtraction -

# Multiplication and division are equally as important as each other, but
# multiplication will take priority over division. The same can be said for 
# addition and subtraction.

# This equation will get executed (from left to right), even though the maths
# operators are in the "wrong" order.
print(3 * 3 + 3 / 3 - 3)  # =  7.0

# Same operators as above, but in proper order:
print(3 * 3 / 3 + 3 - 3)  # = 3.0

# If we have to do this equation in the original order, we can place parentheses
# the parts that should get priority. eg:
print(3 * (3 + 3) / 3 - 3)


print("\nBMI calculator")
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(int((weight / height) * height))
bmi = int(weight / height ** 2)
print(bmi)



















