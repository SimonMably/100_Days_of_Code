
# CSV = Comma Separated Values

# CSV files are a common way of representing tabular data, which can be used
# in tables and spreadsheets.
# Each line has a single set of data, which is separated by commas.

# with open("weather_data.csv") as weather_data:
#     csv_data = weather_data.readlines()
#     data = []
#     for line in csv_data:
#         data.append(line.strip())
# 
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         ''' ALSO WORKS:
#         if "temp" in row:
#             pass
#         else:
#             temperatures.append(int(row[1]))
#         '''
#     print(temperatures)

# The pandas module is great for reading tabular data (whether in csv files or
# other file formats)
import pandas

data = pandas.read_csv("weather_data.csv")
# Prints contents of csv file in a formatted table
# print(data)

# Identifies "temp" column and prints temperatures
print(data["temp"])


