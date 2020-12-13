# 180 124 165 173 189 169 146

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# How this can be done with the for loop:
# Replicating the sum() function (the total height of all students)
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

# Replicating len() function (the length of student_heights list)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)



'''
# How this can be done without the for loop:
# each item in student_heights list would need to be converted into an integer
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)
'''

