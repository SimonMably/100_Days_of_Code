import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/colors.csv")

# How many different colours does the LEGO company produce? 135
print(df["name"].nunique())

print(df.head())

transparent = 0
opaque = 0

for value in df["is_trans"]:
    if value == "t":
        transparent += 1
    elif value == "f":
        opaque += 1

print(f"Transparent: {transparent}, Opaque: {opaque}")

df.groupby("is_trans").count()

# f = opaque
# t = transparent
df["is_trans"].value_counts()

sets_df = pd.read_csv("data/sets.csv")
print(sets_df.head())
print(sets_df.tail())

# In which year were the first LEGO sets released and what were these sets called?
print(sets_df.sort_values("year").head())

# How many different sets did LEGO sell in their first year?
# How many types of LEGO products were on offer in the year the company started?
print(sets_df[sets_df["year"] == 1949])

# Find the top 5 LEGO sets with the most number of parts.
print(sets_df.sort_values("num_parts", ascending=False).head())

sets_by_year = sets_df.groupby("year").count()
print(sets_by_year["set_num"].head())
print(sets_by_year["set_num"].tail())

# Show the number of LEGO releases on a line chart using Matplotlib (uses slicing
# to exclude data from early 2021)
print(plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2]))


# Aggregate Data with the Python .agg() Function
themes_by_year = sets_df.groupby("year").agg({"theme_id": pd.Series.nunique})

themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
print(themes_by_year.head())

print(plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2]))


# Line Chart with Two Seperate Axis

# This looks terrible
# plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
# plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

# We need configure and plot data o two seperate axis on the same chart. This involves
# getting hold of an axis object from Matplotlib.
ax1 = plt.gca()  # get current axes
ax2 = ax1.twinx()  # create another axis that shares the same x-axis

# The .twinx() method allows "ax1" and "ax2" to share the same x-axis.

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# Add styling
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Sets", color="red")
ax2.set_ylabel("Number of Themes", color="blue")
# Line in graph not adhering to colours, but x and y labels are


# The average number of parts per LEGO set released in 1954 and 2017
parts_per_set = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
print(parts_per_set.head())
print(parts_per_set.tail())


# Visualising with a Scatter plot

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])

set_theme_count = sets_df["theme_id"].value_counts()
print(set_theme_count[:5])


themes_df = pd.read_csv("data/themes.csv")
print(themes_df.head())

print(themes_df[themes_df.name == "Star Wars"])

print(sets_df[sets_df.theme_id == 18])

print(sets_df[sets_df.theme_id == 209])


# Merging DataFrames and Creating Bar Charts

set_theme_count = pd.DataFrame({"id": set_theme_count.index,
                                "set_count": set_theme_count.values})
print(set_theme_count.head())

# The Pandas .merge() Function

merged_df = pd.merge(set_theme_count, themes_df, on="id")
print(merged_df[:3])

# Creating a Bar Chart

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

print(plt.bar(merged_df.name[:10], merged_df.set_count[:10]))
