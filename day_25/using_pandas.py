import pandas

# pandas Documentation: https://pandas.pydata.org/docs/index.html

data = pandas.read_csv("weather_data.csv")
'''
# In pandas, tables are otherwise known as DataFrames
# Prints '<class 'pandas.core.frame.DataFrame'>'
print(type(data))

# A tables column is known as a series
# Prints '<class 'pandas.core.series.Series'>'
print(type(data["temp"]))

# In Pandas, the whole table is a DataFrame, while each column in a table is
# a Series.

# Converting  data into a dictionary
data_dict = data.to_dict()
print(data_dict)

# Converting data's "temp" column/Series into a list
temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

# Print average (or mean) temperature of data without Pandas
temp_average = sum(temp_list) / len(temp_list)
print(f"Average Temperature without Pandas: {temp_average}")

# Print average (or mean) temperature of data with Pandas
print(f"Average Temperature with Pandas: {data['temp'].mean()}")

# todo: Use a Series method from Pandas to get the maximum value of the "temp"
print(data["temp"].max())

# To get data from a column using Pandas, we have to specify the name of the
# column we want from a DataFrame (table) inside squared brackets and
# quotation marks. For example, data["temp"]. data is the name of the
# DataFrame (table) and temp is the name of the Series (column) that is being
# specified.
# A column gets its name the first line of the tabular data. In tabular data,
# commas are used to split up pieces of data on each row. In the above
# example of weather_data, "temp" is the second piece of data on the first
# row signifying that it's the middle column. In this case, Pandas knows
# that, in the same file, all pieces of data underneath "temp" (or the second
# piece of data on each row/line) is apart of the "temp" column. When accessing
# a column/Series, the name needs to be exact.
# Another way of accessing a DataFrames Series is using the dot notation. For
# example:
# Instead of using data["temp"]
print(data.temp)

# Instead of using data["condition"]
print(data.condition)


# Getting data from a row

# 'data[day["day"]' to access the column, and followed by '== "Monday' to
# retrieve the row (the row for monday in this case)
print(data[data["day"] == "Monday"])

# Retrieve row of data with highest temperature
print(data[data.temp == data.temp.max()])
# or
print(data[data["temp"] == data["temp"].max()])


monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge: convert temperatures in "temp" column/Series to fahrenheit
for temp in data.temp:
    temp = temp * 1.8 + 32
    print(temp)
print()
# course solution to challenge
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)
'''
# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_dictionary = pandas.DataFrame(data_dict)
print(data_dictionary)
# Saving the above dictionary to disk as CSV file
data_dictionary.to_csv("new_data.csv")





