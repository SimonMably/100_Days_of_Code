# Can't Use:
# max() function
# min() function

# -----------------------------------------------------------------------------
# High Score Checker
# -----------------------------------------------------------------------------

# List of scores 
# [78, 65, 89, 86, 55, 91, 64, 89]
# 78 65 89 86 55 91 64 89
student_scores = input("Input a list student scores: ").split()

# For Loop That Replicates The max() Function
high_score = 0
for score in student_scores:
    if int(score) > high_score:
        high_score = int(score)

# For Loop That Replicates The min() Function
low_score = high_score
for score in student_scores:
    if int(score) < low_score:
        low_score = int(score)

# Output
print(f"\nThe highest score in the class is: {high_score}")

print(f"\nThe lowest score in the class is: {low_score}")

