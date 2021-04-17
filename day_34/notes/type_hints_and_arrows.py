

# Defining/specifying a variables datatype
# age: int
# # variable must contain defined datatype
# age = 10
# print(age)
# # If variable contains non-defined datatype, the datatype is highlighted with
# # the message "Expected type 'int', got 'str' instead". This is a type hint.
# age = "ten"
# print(age)

# age = int
# name = str
# height = float
# is_human = bool

# We can specify the output of a function with '->' along with the expected
# datatype. If we use a datatype that's not expected, the datatype will also
# be highlighted with warning, eg, Expected type 'bool', got 'str' instead

#               type hint| expected datatype
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(12))

if police_check("twelve"):
    print("You may pass.")
else:
    print("Pay a fine.")
