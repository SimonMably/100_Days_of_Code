
# Dictionary comprehension is useful because it allows us to create a new
# dictionary from values in an existing list or dictionary.

# Example of a dictionary comprehension with 'keyword' method:
# new_dict = {'new_key':'new_value' for 'item' in 'list'}

# Example of dictionary comprehension (with 'keyword' method) from values of
# an existing dictionary:
# my_dict = {'new_key':'new_value' for '(key, value)' in 'dict.items()'}
#                     [1]                   [2], [3]            [4]
# We can take an existing dictionary, get hold of its items (with .items()
# method [4]), and then split them into a key [2] and a value [3]. This means
# that the dictionary comprehension is looping through the keys [2] and
# values [3] of a dictionary [4] and putting them into another dictionary [1].

# We can also use an if statement at the end of the dictionary comprehension
# to test for conditions. eg:
#new_dict ={'new_key':'new_value' for '(key, value)' in 'dict.items()' if 'test'}


# Example 1 of dictionary comprehension (looping through a list):
# Giving student random scores
import random
names = ['Alex', 'Beth', 'Dave', 'Eleanor', 'Freddie']

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Challenge: Place students with scores of 60 or higher into new dictionary
# Example 2 of dictionary comprehension (looping through  the student_scores
# dictionary):
passed_students = {student: score for (student, score) in student_scores.items()
                   if score >= 60}
print(passed_students)
