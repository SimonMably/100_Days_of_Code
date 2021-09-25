import pandas as pd
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LinearRegression

# Notebook Presentation
pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()

# Reading the data
data = pd.read_csv('cost_revenue_dirty.csv')

# Explore and Clean the Data

# The amount of rows and columns in the dataset
print(f"Rows and columns: {data.shape}\n")

# Checks for NaN values
print(f"Any NaN values: {data.isna().values.any()}\n")

# Checks for duplicates
duplicated_rows = data[data.duplicated()]
print(f"The amount of duplicated rows: {len(duplicated_rows)}\n")

# Information on the dataset. Will tell us if there are any null values and shows
# if we need to do some type conversion.
print(data.info())

# Data Type Conversions

# In specified columns, replacing specified characters with an empty string and
# then converting the values in these columns into numeric datatypes.
characters_to_remove = [",", "$"]
column_to_clean = ["USD_Production_Budget",
                   "USD_Worldwide_Gross",
                   "USD_Domestic_Gross"]

for column in column_to_clean:
    for character in characters_to_remove:
        # Replace each character with an empty string
        data[column] = data[column].astype(str).str.replace(character, "")
    # Convert column to a numeric data type
    data[column] = pd.to_numeric(data[column])

# Converting the Release_Date column to a DateTime object
data["Release_Date"] = pd.to_datetime(data["Release_Date"])
print(data.head(), "\n")

print(data.info())

# Descriptive Statistics

# Shows the average production budget, the average worldwide gross revenue, the
# minimums for the worldwide and domestic revenue, and the highest worldwide gross
# revenue. All data is from this data set. (Domestic, in this case, refers to
# inside the US)
print(data.describe(), "\n")

# The film with the lowest budget in the dataset - My Date With Drew
print(data[data["USD_Production_Budget"] <= 1200.00], "\n")

# The film with the highest budget in the dataset - Avatar
print(data[data["USD_Production_Budget"] >= 425000000], "\n")

# Investigating the Zero Revenue Films

# No domestic revenue
zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False), "\n")

# No worldwide revenue
zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
print(zero_worldwide.sort_values('USD_Production_Budget', ascending=False))

# Filtering on Multiple Conditions

# Filtering condition using the bitwise and operator. Because the bitwise
# operator takes presedence, we need to include parantheses around the comparisons
# we want to prioritise.
international_releases = data.loc[(data.USD_Domestic_Gross == 0) & (data.USD_Worldwide_Gross != 0)]
print(f'Number of international releases: {len(international_releases)}')
print(international_releases.head())

bool_list1 = [True, True, False, False]
bool_list2 = [False, True, True, False]

# Bitwise operators allow us to do comparisons on an element by element basis
# in NumPy and Pandas. For example:
print(pd.array(bool_list1) & pd.array(bool_list2))

# Using the .query() function to do the above
inter_releases = data.query("USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0")
print(f'Number of international releases: {len(inter_releases)}')
print(inter_releases.tail())

# Unreleased Films

# Date of Data Collection
scrape_date = pd.Timestamp("2018-5-1")

# Films released after 1st of May 2018
future_releases = data[data["Release_Date"] >= scrape_date]
print(f"Number of unreleased movies: {len(future_releases)}")
print(future_releases)


# Films taht lost money

# New dataset that excludes the above unreleased films
data_clean = data.drop(future_releases.index)

# Films that Lost Money
money_losing = data_clean.loc[data_clean.USD_Production_Budget > data_clean.USD_Worldwide_Gross]
# This equates to 37%
len(money_losing)/len(data_clean)

# Using .query() instead of .loc[] gives the same result
# money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
# money_losing.shape[0]/data_clean.shape[0]


# Seaborn for Data Viz: Bubble Charts

# Creating a .scatterplot()

# Increasing the size of the figure/plot (instead of using the default size),
# from Matplotlib
plt.figure(figsize=(8, 4), dpi=200)

# providing the DataFrame along with the columns as the axes (the x and y).
ax = sns.scatterplot(data=data_clean,
                     x="USD_Production_Budget",
                     y="USD_Worldwide_Gross")

# To add style to the chart we can simply configure the Axes object that is
# returned from sns.scatterplot()
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel="Revenue in $ billions",
       xlabel="Budget in $100 millions")

# also from Matplotlib
plt.show()

# creating a bubblechart

plt.figure(figsize=(8, 4), dpi=200)

# Seaborn has 5 of built-in themes to style charts. These themes include:
# darkgrid (as used below), dark, whitegrid, white and ticks.
# Set styling on a single chart using the with keyword
with sns.axes_style("darkgrid"):
    ax_2 = sns.scatterplot(
        data=data_clean,
        x='USD_Production_Budget',
        y='USD_Worldwide_Gross',
        hue='USD_Worldwide_Gross',  # colour
        size='USD_Worldwide_Gross', )  # dot size

    ax_2.set(
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions', )

plt.show()
print("\n")

# Movie Budgets over Time
plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(
        data=data_clean,
        x='Release_Date',
        y='USD_Production_Budget',
        hue='USD_Worldwide_Gross',
        size='USD_Worldwide_Gross', )

    ax.set(
        ylim=(0, 450000000),
        xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
        xlabel='Year',
        ylabel='Budget in $100 millions'
        )

# Converting Years to Decades Trick

# Creating a DateTimeIndex
dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

# Converting the years to decades by using floor division (or integer division)
# floor dividing years by 10, then multiplying by ten
decades = years // 10 * 10

# Creating a new column in data_clean and placing the values for decades into column
data_clean["Decade"] = decades

print(data_clean)


# Seperating the films made before and after 1970

old_films = data_clean[data_clean["Decade"] <= 1960]
new_films = data_clean[data_clean["Decade"] > 1960]

print("Old Films:")
print(old_films.describe())
print(old_films.sort_values("USD_Production_Budget", ascending=False).head(), "\n")

print("New Films:")
print(new_films.describe())
print(new_films.sort_values("USD_Production_Budget", ascending=False).head())


# Seaborn Regression Plots

# Visualising the relationship between the movie budget and the worldwide revenue
# using linear regression. Creates a scatter plot and draws a linear regression
# line together with the confidence interval at the same time.

# Chart for old films
# Styling this chart
plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x="USD_Production_Budget",
                y="USD_Worldwide_Gross",
                # Customising the scatter plot by changing the transparency
                # of the dots
                scatter_kws = {"alpha": 0.4},
                # Customising the regression line by changing the colour to black
                line_kws = {"color": "black"}
                ).set(title="Old Movies - Before the 1970's")

# Linear Regression Plot for New Films
plt.figure(figsize=(8, 4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.regplot(
        data=new_films,
        x="USD_Production_Budget",
        y="USD_Worldwide_Gross",
        color="#2f4b7c",
        scatter_kws={"alpha": 0.3},
        line_kws={"color": "#ff7c43"}
        )

    ax.set(
        title="New Movies - 1970's and After",
        ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions'
        )

# Regression with scikit-learn

# We are using a univariate regression. This is a regression with a single
# explanatory variable (in this case, the movie BUDGET). Explanatory variables
# are also referred to as features in machine learning terminology.

# Using our data on budgets, the linear regression estimates the best possible
# line to fit our movie revenues. The regression line has the following
# structure:

# REVÊNUE = θ0 + θ1 BUDGET

# REVÊNUE: estimated revenue
# θ0 (theta zero): y-axis intercept
# θ1 (theta one): slope

# To find the best possible line, our regression will estimate the y-intercept
# ("theta zero") and the slope ("theta one"). The line's intercept on the y-axis
# tells us how much revenue a movie would make if the budget was 0. The slope
# tells us how much extra revenue we get for a $1 increase in the movie budget.

# From Scikit-Learn, a LinearRegression object
regression = LinearRegression()

# Specifying features and targets (i.e. a response variable). We often see
# features named as a capital 'X' and the target named as a lower case 'y':

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])

# Find the best-fit line (running the calculations)
regression.fit(X, y)

# Theta zero
print(f"Theta zero: {regression.intercept_}")

# Theta one
print(f"Theta one: {regression.coef_}")

# One measure of figuring out how well our model fits our data is by looking at
# a metric called r-squared. This is a good number to look at in addition to
# eyeballing our charts.

# R-squared
print(f"R-squared: {regression.score(X, y)}")

# Running a linear Regression on old_films

# Feature and Target
X = pd.DataFrame(old_films, columns=["USD_Production_Budget"])
y = pd.DataFrame(old_films, columns=["USD_Worldwide_Gross"])

# Find the best-fit line (running the calculations)
regression.fit(X, y)

print(f"The slope coefficient: {regression.coef_}")
print(f"The intercept: {regression.intercept_}")
print(f"The r-squared: {regression.score(X, y)} (just below 3%)")

# Prediction
budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')
# (The colon : and dot . in a print statement is quite handy for controlling
# the number of digits you'd like to show up in the output)
