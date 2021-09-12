import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("QueryResults.csv")
df = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POST"], header=0)

# Prints top 5 rows
print(df.head())

# Prints bottom 5 rows
print(df.tail())

# Amount of rows, amount of columns
print(df.shape)

# Counts the number of entries in each column of the dataframe
print(df.count("index"))

# The total number of post per language
print(df.groupby("TAG").sum())

# How many months of data exist per language?
print(df.groupby("TAG").count())


# Data Cleaning

# Non-Formatted Date
# Second entry in the column
print(df["DATE"][1])
# Same as:
print(df.DATE[1])

# Formatted Date
df["DATE"] = pd.to_datetime(df["DATE"])
print(df.head())


# Data Manipulation

## Example #####################################################################
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
# print(test_df)
################################################################################

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POST")

# Dimensions of reshaped_df
print(reshaped_df.shape)

# Top 5 rows of reshaped_df
reshaped_df.head()


# Data Visualisation with with Matplotlib

# Visualises the popularity of a programming language, Python in this case.
plt.figure(figsize=(16, 10))
plt.xlabel("DATE", fontsize=18)
plt.ylabel("POST",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Popularity of Python", fontsize=22)
plt.plot(reshaped_df["python"])

# Visualises popularity of Python and Java in the same chart.
plt.figure(figsize=(16, 10))
plt.xlabel("Date", fontsize=18)
plt.ylabel("Number of Posts",fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("Popularity of Python & Java", fontsize=20)
# plt.plot(reshaped_df["python"], label="Python")
# plt.plot(reshaped_df["java"], label="Java")
# plt.legend(loc="upper left", fontsize=16)

# For all languages in csv
for column in reshaped_df.columns:
  plt.plot(reshaped_df[column], linewidth=3, label=reshaped_df[column].name)
  plt.legend(loc="upper left", fontsize=16)


# Smoothing out Time Series Data

roll_df = reshaped_df.rolling(6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(
        roll_df.index, roll_df[column],
        linewidth=3, label=roll_df[column].name
        )

plt.legend(fontsize=16)











