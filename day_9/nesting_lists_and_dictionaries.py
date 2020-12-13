# Dictionaries can have multiple key-value pairs, but each key-value pair can
# only have one key and one value. In a nested dictionary, there still can be 
# only one key per key-value pair, but we can have a list or dictionary as a 
# value, which means we can have many values or key-value pairs as a
# dictionaries value.

# Ordinary dictionary
dictionary = {
    "Key_1": "Value_1",
    "Key_2": "Value_2"
}

# Nested dictionary - a list and a dictionary nested as values inside a 
# dictionary
nested_dictionary = {
    "Key_1": ["list_item_1", "list_item_2"],
    "Key_2": {"dictionary_item_1", "dictionary_item_2"},
}

# Examples

# Ordinary unnested dictionary
capitals= {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested dictionary - used to make more complex structures 
# e.g. Making a travel log to show what countries we've been to in each country
travel_log = {
    "France": ["Paris", "Lille", "Dijon", "Dieppe"],
    "Germany": ["Berlin", "Hamberg", "Stuttgart"],
}

# Lists can also be nested (apparently not as useful as a nested dictionary 
# because of the way they are structured).
nested_list_1 = ["A", "B", ["C", "D"]]

# Nesting a dictionary in a dictionary
travel_log_2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon", "Dieppe"], 
                "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamberg", "Stuttgart"],
                "total_visits": 6},
}

print(travel_log_2)


# Nesting a dictionary inside a list
# eg.
nested_list_2 = [{
    "Key_1": ["list_item_1, list_item_2" ],
    "Key_2": {"dictionary_item_1", "dictionary_item_2"},
    },
    {
    "Key_1": "Value_1",
    "Key_2": "Value_2"
}]
# -----------------------------------------------------------------------------
# Accessing data

# Items in a list can be accessed by their index positions. The 1st dictionary
# is a index position 0, while the 2nd dictionary is at index position 1, and 
# so on and so forth.

# With dictionaries, data (Keys and Values) is accessed by their Keys.
# -----------------------------------------------------------------------------

# Example of nesting a Dictionary in a List (travel log)
travel_log_3 = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamberg", "Stuttgart"],
        "total_visits": 5
    },
]
# This list can be iterated over in a for loop. 
# Also, if they contain a lot of key-value pairs, Dictionaries can be written
# this way so they can be more readable. If a Dictionary contains just a few
# key-value pairs, then the entire Dictionary can be cotained on a single line.

# Each Key-Value pair within a dictionary can contain a mix of data type.






