
# Calculator

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Dictionary containing operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

'''PART 1
num1 = int(input("what's the first number?: "))
for operator in operations:
    print(operator)
operation_symbol = input("Pick an operation from above: ")
num2 = int(input("what's the first number?: "))


# My solution for lecture 101. Calcultor Part 1. Combining Dictionaries and
# Functions.
answer = ""
if operation_symbol == "+":
    answer = add(num1, num2)
elif operation_symbol == "-":
    answer = subtract(num1, num2)
elif operation_symbol == "*":
    answer = multiply(num1, num2)
elif operation_symbol == "/":
    answer = divide(num1, num2)

#COURSE SOLUTION
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")



# print(f"{first_answer} {operation_symbol} {num3}")
'''
# PART 2

'''MY ATTEMPT AT SOLUTION (re-do to understand)
while calculating:

    continueing = input(f"Type 'y' to continue with {first_answer},  "
                        "or type 'n' to exit: ")

    if continueing == "n":
        if num_3 not in first_answer:
            print(f"{num_1} {operation_symbol} {num_2} = {first_answer}")
            break
        #calculating = False

    for operator in operations:
        print(operator)
    operation_symbol = input("Pick an operation from above: ")
    num_3 = int(input("What is the next number?: "))

    second_answer = calculation_function(first_answer, num_3)

    if continueing == "n":
        print(f"{first_answer} {operation_symbol} {num_3} = {second_answer}")
        break
'''



def calculator():
    '''Function utilises recursion.'''

    num_1 = int(input("\nWhat's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num_2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num_1, num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        # 'answer' = answer of previous calculation
        if input(f"Type 'y' to continue with {answer}, "
                "or 'n' to start a new calculation: ") == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()





calculator()


''' MAY NOT NEED
    operation_symbol = input("Pick another operation: ")
    num_3 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(first_answer, num_3)

    print(f"{first_answer} {operation_symbol} {num_3} = {second_answer}")
'''

