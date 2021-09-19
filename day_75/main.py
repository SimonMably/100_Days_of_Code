import pandas as pd
import plotly.express as px

# Notebook Presentation

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

# Reading the dataset
df_apps = pd.read_csv('apps.csv')


# Data Cleaning

print(df_apps.shape)
df_apps.head()  # not in print() to show NaN values

# The .sample() function returns a specified amount of random samples
print(df_apps.sample(5))

# Removing unused columns
df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)

# Removing NaN values in the Rating column
df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)


# Finding and removing duplicates

# Finding duplicates
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]

# Number of rows & columns in duplicated_rows & the 1st 5 rows
print(duplicated_rows.shape)
duplicated_rows.head()

# Duplicated data for Instagram, specified via the "App" column
print(df_apps_clean[df_apps_clean.App == "Instagram"])

# Using the .drop_duplicates() function to get rid of duplicated data, specifying
# the subset(s), eg. in this case, the the columns named "App", "Type" & "Price"
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
print(df_apps_clean[df_apps_clean.App == "Instagram"])

print(df_apps_clean.shape)


# The highest rated apps

# The highest rated app
print(df_apps_clean["App"].loc[df_apps_clean["Rating"].idxmax()])

# The 5 highest rated apps.
# These apps have very few reviews, a low amount of installs and 5 star ratings,
# presumably by friends and family.
df_apps_clean.sort_values("Rating", ascending=False).head()

# The 5 largest apps in terms of file size (MBs)
df_apps_clean.sort_values("Size_MBs", ascending=False).head()

# The most popular apps tend to have the most reviews and installs.
df_apps_clean.sort_values("Reviews", ascending=False).head()


# Data Visualisation with Plotly

# Visualising Categorical Data: Content Ratings

ratings = df_apps_clean["Content_Rating"].value_counts()
print(ratings)

# Pie Chart
pie_fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             )
pie_fig.update_traces(textposition="outside", textinfo="percent+label")

# .show() can also be stacked onto the above and will have the same effect as the below
pie_fig.show()

# Doughnut Chart
doughnut_fig = px.pie(labels=ratings.index,
                      values=ratings.values,
                      title="Content Rating",
                      names=ratings.index,
                      hole=0.6
                      )
doughnut_fig.update_traces(textposition="outside", textinfo="percent+label")

doughnut_fig.show()


# Numeric Type Conversion: Examining the Number of Installs

# Checking the datatype of the Installs column
df_apps_clean["Installs"].describe()

# This will give the datatypes of all columns,
df_apps_clean.info()

# Displaying two columns names Installs and App. Grouped by amount of installs,
# how many apps come under each install group.
# As the Installs column contain non-numeric data types (this is down to commas
# separating numbers containing  more than 3 0s), this is causing a problem with
# ordering. eg, 5,000,000 - this should be 5000000 instead.
df_apps_clean[["App", "Installs"]].groupby("Installs").count()

# Replacing commas (",") with an empty string
df_apps_clean["Installs"] = df_apps_clean["Installs"].astype(str).str.replace(",", "")

# Converting the above data into a number
df_apps_clean["Installs"] = pd.to_numeric(df_apps_clean["Installs"])

# Displaying both columns in the correct ordering
df_apps_clean[['App', 'Installs']].groupby('Installs').count()


# Finding the Most Expensive Apps, Filter out the Junk, and Calculate a (ballpark) Sales Revenue Estimate

# Replacing "$" sign in values for the Price column with an empty string
df_apps_clean["Price"] = df_apps_clean["Price"].astype(str).str.replace("$", "")
df_apps_clean["Price"] = pd.to_numeric(df_apps_clean["Price"])

# Displays top 20 rows in dataframe.
df_apps_clean.sort_values("Price", ascending=False).head(20)

# The above contain 15 variations of "I am Rich" apps priced at $299.99 or more.
# Leaving this bad data in the dataset will misinterpret the analysis of the
# most expensive "real" apps.
# Removing the above rows:
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]

# Displays new top 5 rows, sorted by price, making them the most expensive
df_apps_clean.sort_values('Price', ascending=False).head(5)

# Highest Grossing Paid Apps (ballpark estimate)
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)

# The apps that have have a category of "FAMILY" should be classed in the "GAME" category
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])


# Plotly Bar Charts & Scatter Plots: Analysing App Categories

# Finding the number of different/unique app categories
df_apps_clean["Category"].nunique()

# Calculating the number of apps per category using .value_counts()
top_ten_category = df_apps_clean["Category"].value_counts()[:10]
print(top_ten_category)

# Calculates the total number of install for each category
category_installs = df_apps_clean.groupby('Category').agg(
    {'Installs': pd.Series.sum}
    )
category_installs.sort_values('Installs', ascending=True, inplace=True)

# Creating a horizontal bar chart
h_bar = px.bar(
    x=category_installs.Installs,
    y=category_installs.index,
    orientation='h',
    title='Category Popularity'
    )

h_bar.update_layout(xaxis_title='Number of Downloads', )
h_bar.show()

# Vertical Bar Chart - Highest Competition (Number of Apps)

bar = px.bar(x = top_ten_category.index,  # index = category
             y = top_ten_category.values)
bar.show()


# Horizontal Bar Chart - Most Popular Categories (Highest Downloads)

# Calculates the total number of install for each category
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

# Creating a horizontal bar chart
h_bar = px.bar(
    x=category_installs.Installs,
    y=category_installs.index,
    orientation='h',
    title='Category Popularity'
    )

h_bar.update_layout(xaxis_title='Number of Downloads', )
h_bar.show()

# Category Concentration - Downloads vs. Competition

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

# Merging 2 dataframes
cat_merged_df = pd.merge(
    cat_number, category_installs, on='Category', how="inner"
    )
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(
    cat_merged_df,  # data
    x='App',  # column name
    y='Installs',
    title='Category Concentration',
    size='App',
    hover_name=cat_merged_df.index,
    color='Installs'
    )

scatter.update_layout(
    xaxis_title="Number of Apps (Lower=More Concentrated)",
    yaxis_title="Installs",
    yaxis=dict(type='log')
    )

scatter.show()


# Extracting Nested Data from a Column using .stack()

# Number of genres
print(len(df_apps_clean["Genres"].unique()), "\n")

# Problem: Multiple categories seperated by ; - eg. Strategy;Creativity
print(df_apps_clean["Genres"].value_counts().sort_values(ascending=True)[:5])

# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

# Colour Scales in Plotly Charts - Competition in Genres

top_genres_chart = px.bar(
    x=num_genres.index[:15],  # index = category name
    y=num_genres.values[:15],  # count
    title='Top Genres',
    hover_name=num_genres.index[:15],
    color=num_genres.values[:15],
    color_continuous_scale='Agsunset'
    )

top_genres_chart.update_layout(
    xaxis_title='Genre',
    yaxis_title='Number of Apps',
    coloraxis_showscale=False
    )

top_genres_chart.show()


# Grouped Bar Charts: Free vs. Paid Apps per Category

# Displays the amount of free and paid apps
print(df_apps_clean["Type"].value_counts(), "\n")

# Paid app vs. free app
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.head()
# Each category tends to have more free apps than paid apps


# Paid vs. free apps - bar chart

free_or_paid_bar = px.bar(
    df_free_vs_paid,
    x='Category',
    y='App',
    title='Free vs Paid Apps by Category',
    color='Type',
    barmode='group'
    )

free_or_paid_bar.update_layout(
    xaxis_title='Category',
    yaxis_title='Number of Apps',
    xaxis={'categoryorder': 'total descending'},
    yaxis=dict(type='log')
    )

free_or_paid_bar.show()

# Plotly Box Plots: Lost Downloads for Paid Apps

box = px.box(
    df_apps_clean,
    y='Installs',
    x='Type',
    color='Type',
    notched=True,
    points='all',
    title='How Many Downloads are Paid Apps Giving Up?'
    )

box.update_layout(yaxis=dict(type='log'))

box.show()

# Plotly Box Plots: Revenue by App Category

df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']

box = px.box(
    df_paid_apps,
    x='Category',
    y='Revenue_Estimate',
    title='How Much Can Paid Apps Earn?'
    )

box.update_layout(
    xaxis_title='Category',
    yaxis_title='Paid App Ballpark Revenue',
    xaxis={'categoryorder': 'min ascending'},
    yaxis=dict(type='log')
    )

box.show()


# How Much Can You Charge? Examine Paid App Pricing Strategies by Category

# The median price for paid apps, in $US, per category
df_paid_apps["Price"].median()

box = px.box(
    df_paid_apps,
    x='Category',
    y="Price",
    title='Price per Category'
    )

box.update_layout(
    xaxis_title='Category',
    yaxis_title='Paid App Price',
    xaxis={'categoryorder': 'max descending'},
    yaxis=dict(type='log')
    )

box.show()
