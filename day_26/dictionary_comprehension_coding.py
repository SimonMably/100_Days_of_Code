
# Coding Challenge 1:
# Use dictionary comprehension to count all character in each word of a
# string and store the character count in a dictionary

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result)


# Coding Challenge 2:
# Use dictionary comprehension to convert a dictionaries values of
# temperatures from Celsius to Fahrenheit .

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
