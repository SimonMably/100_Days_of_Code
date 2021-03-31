
# The 'raise' keyword allows us to bring up (or raise) our own Exceptions.
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary)
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # Will cause an Exception no matter what. The string within the parentheses
#     # is the message that will show in the run terminal along with the
#     # Exception.
#     raise TypeError("This is an error that I made up.")

# An example of when we might want to raise an Exception:
height = float(input("Height: "))
weight = float(input("Weight: "))

# Raising an Exception in case someone inputs an unrealistic height
if height > 3:
    raise ValueError("Human height should not be over 3 metres.")

bmi = weight / height ** 2
print(bmi)


