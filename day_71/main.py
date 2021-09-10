import pandas as pd
from bs4 import BeautifulSoup
import requests

# Reads a csv file/turns into a dataframe
df = pd.read_csv("salaries_by_college_major.csv")

# .head() method displays the first 5 rows of a dataframe
df.head()

# Displays the amount of rows and columns of dataframe
df.shape

# Displays the names of each column in a list
df.columns

# NAN = Not A  Number - blank cells or cells that contain strings instead of
# numbers
# To check for NAN values, use .insa() method (See row 50)
df.isna()

# .tail() method displays the last 5 rows of dataframe
df.tail()

# Creates a new dataframe without the last row
clean_df = df.dropna()
# Displays last 5 rows of new dataframe
clean_df.tail()

# Accessing a particular column. eg. Starting Median Salary - or Finding College
# Major with Highest Starting Salaries
clean_df["Starting Median Salary"]

# To find the row with the highest number (or highest starting salary in this
# case)
clean_df["Starting Median Salary"].max()

# .idxmax() method isplays the row number or index that contains the highest
# number
clean_df["Starting Median Salary"].idxmax()

# To see the value that corresponds to a particular column and row,
# use the .loc (location) property
# The 1st square brackets contain the name of the column, the 2nd square
# brackets
# contain the row number
clean_df["Undergraduate Major"].loc[43]

# This achieves the same thing as above (.loc isn't needed)
clean_df["Undergraduate Major"][43]

# If a column name isn't specified, the .loc property can be used to retrieve
# the whole row
clean_df.loc[43]

# Challenge: College major with the highest mid-career salary
index = clean_df['Mid-Career Median Salary'].idxmax()
highest_mid_salary = clean_df['Mid-Career Median Salary'].max()
undergraduate_major = clean_df['Undergraduate Major'][index]
print(f"{index}: {undergraduate_major} - {highest_mid_salary}")

# Challenge: College major with the lowest starting salary
index = clean_df['Starting Median Salary'].idxmin()
min_starting_salary = clean_df['Starting Median Salary'].min()
undergraduate_major = clean_df['Undergraduate Major'][index]
print(f"{index}: {undergraduate_major} - {min_starting_salary}")

# Challenge: College with the lowest mid-career salary
index = clean_df['Mid-Career Median Salary'].idxmin()
min_mid_salary = clean_df['Mid-Career Median Salary'].min()
undergraduate_major = clean_df['Undergraduate Major'][index]
print(f"{index}: {undergraduate_major} - {min_mid_salary}")

# Nesting code to find what we need, eg. using .loc accessing the row at
# the index of the smallest mid-career salary:
clean_df.loc[clean_df["Mid-Career Median Salary"].idxmin()]

# Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk

# Lowest Risk Majors

# Pandas allows  us to do simple arithmetic with entire columns,
# eg. subtracting numbers
# from 1 column from numbers from another column to find the difference
clean_df['Mid-Career 90th Percentile Salary'] - clean_df[
    'Mid-Career 10th Percentile Salary']

# Alternatively, we could use the .subtract() method
clean_df['Mid-Career 90th Percentile Salary'].subtract(
    clean_df['Mid-Career 10th Percentile Salary']
    )

# Adding another column with the .insert() method
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df[
    'Mid-Career 10th Percentile Salary']

# The first argument is the position of where the column should be inserted,
# eg. 1 = position one (the second column, since things start at 0)
# The second argument is the name of the column.
# The third arguement is the data that is being inserted. In this case,
# what's contained in spread_col

clean_df.insert(
    1, 'Spread', spread_col
    )  # Can't run this again as "Spread" has already been inserted
clean_df.head()

# Sorting the Lowest Spread

# Using the .sort_values() method to see which degrees have the smallest spread
low_risk = clean_df.sort_values("Spread")
# Displays top 5 values from specified columns in ascending order by default
low_risk[["Undergraduate Major", "Spread"]].head()

# Challenge 1: Using .sort_values(), find the top 5 degrees with the highest
#              values in the 90th percentile
# In course, variable name = highest_postential
highest_ninety_percentile = clean_df.sort_values(
    "Mid-Career 90th Percentile Salary", ascending=False
    )
highest_ninety_percentile[
    ["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head()

# Challenge 2: Find the degrees with the greatest spread. Which majors have the
#              largest difference between high & low earners after graduation
# In course, variable name = highest_spread
high_risk = clean_df.sort_values("Spread", ascending=False)
high_risk[["Undergraduate Major", "Spread"]].head()

# Grouping and Pivoting Data with Pandas

# Sometimes we will want to sum rows that belong to a perticular category. For
# example, which degrees have the highest average salary (Business,
# STEM (Science,
# Technology, Engineering, and Mathematics), HASS (Humanities, Arts,
# and Social Science)).
# To do this, we can use the .groupby() method, which allows us to manipulate
# data
# similar to a Microsoft Excel Pivot Table
clean_df.groupby("Group").count()

# Challenge: Use the .mean() method to find the average salary by group:
clean_df.groupby("Group").mean()

# Number Formats in the Output

# The values in the above table are hard to read. We can use Pandas to format it
# to be more readable
pd.options.display.float_format = "{:,.2f}".format
clean_df.groupby("Group").mean()

records = []

for current_page in range(34):
    endpoint = f"https://www.payscale.com/college-salary-report/majors-that" \
               f"-pay-you-back/bachelors/page/{current_page + 1}"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table.data-table tbody tr")
    for row in rows:
        cells = row.select("span.data-table__value")
        record = {
            "Undergraduate Major": cells[1].getText(),
            "Starting Median Salary": float(
                cells[3].getText().strip("$").replace(",", "")
                ),
            "Mid-Career Median Salary": float(
                cells[4].getText().strip("$").replace(",", "")
                ),
        }
        records.append(record)

pd.DataFrame(records).to_csv(
    "salaries_by_college_major_updated.csv", index=False
    )

example_df = pd.read_csv("salaries_by_college_major_updated.csv")
print(example_df)