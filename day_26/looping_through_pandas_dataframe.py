import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries (regular for loop):
# for (key, value) in student_dict.items():
#     print(value)


# Looping through a Pandas DataFrame

# Prints dictionary as a DataFrame
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Looping through student_dict dataframe
# for (key, value) in student_data_frame.items():
#     # print(key)  # Only prints dictionaries keys
#     print(value)  # Prints data from each column

# Loop through rows of dataframe
for (index, row) in student_data_frame.iterrows():
    # print(index)  # Prints dataframes indices (row numbers)
    # print(row)  # Prints data from each row
    # row is a Pandas Series object. Because of this, we can tap into the row
    # and get the value of a particular column (eg. the "student" column)
    print(row.student)  # Prints values from student column

# Prints score for the student "Angela"
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)





