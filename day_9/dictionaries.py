# Dictionaries are a type of array that made up of key-value pairs (entries
# that are groups of 2 items. e.g. they are kind of like a words and their
# associated definitions in actual dictionaries.)

# Example of a dictionary
programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.",
	"Function": "A piece of code that you can easily call over and over again.",
}
print("Dictionary with 2 Key-Values pairs")
print(programming_dictionary)
# Retrieving an item from a dictionary

# Retrieving an item from a list == list[1] # using the lists index
# position to gain access to list item.

# Dictionaries have elements which are identified by their key
# e.g.
# Specifying a dictionary Key in a print statement will print that
# Key Value.
print("\nAccessing a Value for a specific Key")
print(programming_dictionary["Bug"],)
# When specifying the Key, the Key has to be absolutely correct (Spelling
# and case-sensitive wise), other wise there will be an error (KeyError).
# Also, it's important to use the correct data type. e.g If a dictionary Key is
# a variable name and we reference that Key in a print statement as a string,
# then we will get an error. For this reason, when referencing a dictionary
# Key or retrieving the data/Value of a dictionary Key, then the Key and any
# references that Key have to be of the same data type.

# Adding pieces of data to a dictionary:
# To add a new piece of data (Key-Value Pair), we have to tap into the
# dictionary along with the new Key and then add the Value for that Key.
# e.g.
print("\nAdding new Key-Value Pair to dictionary")
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)


print("Creating an empty dictionary")
# Often it's very helpful to create empty dictionaries.
empty_dictionary = {}
print(empty_dictionary)
# We can add new information (Key-Value Pairs) with the method above

print("\nWiping/clearing an entire dictionary.")
# If we want get rid of all the information in an existing dictionary, we can
# set that existing dictionary as an empty dictionary.
# eg.
# Non-empty dictionary
greetings = {
	"English": "Hello",
	"French": "Bonjour",
	"Italian": "Ciao",
}
print("Non-empty 'greetings' dictionary -", greetings)
# Wiping non-empty dictionary (must have data inside)
greetings = {}
print("\nWiped 'greetings' dictionary -", greetings, "\n")

# Editing an existing dictionary Value
print("Editing Dictionary Values")
programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.",
	"Function": "A piece of code that you can easily call over and over again.",
	"Loop": "The action of doing something over and over again.",
}
print("Unedited Value:", programming_dictionary["Bug"])

programming_dictionary["Bug"] = "A moth in your computer."
print("Edited Value:", programming_dictionary["Bug"], "\n")
# NOTE: If we're trying to edit the Value of a Key that doesn't exist, then 
# that 'edited' Key and Value will be created and placed into the dictionary.

# Looping through a dictionary
for thing in programming_dictionary:
    	print(thing)
# Using a for loop to iterate through a dictionary like above will only loop 
# through the dictionaries Keys. In the for loop above, the dictionaryies Keys
# only get printed onto the screen, not the Values.

# 1. When using a for loop to iterate through a dictionary, it's best to use
#    the word 'key' as the for loops variable since that is essentialy what 
#    the for loop is iterating over.
# 2. To access the dictionaries values, type in the name of the dictionary 
#    along with the for loops variable name.
# e.g.
for key in programming_dictionary:
	print(key)
	print(programming_dictionary[key], "\n")
	