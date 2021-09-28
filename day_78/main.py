import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Notebook Formating
pd.options.display.float_format = '{:,.2f}'.format

# Reading the data
df_data = pd.read_csv('nobel_prize_data.csv')

# The exact birth dates for Michael Houghton, Venkatraman Ramakrishnan, and
# Nadia Murad are unknown. Their birth dates have been substituted with a
# mid-year estimate of July 2nd

# Data Exploration & Cleaning

# Preliminary data exploration

# Shape of dataframe
print(f"Shape of the DataFrame: {df_data.shape}")

# Displays the names of each column, the starting year of the Nobel Prize and
# the top 5 rows of DataFrame
print(df_data.head())

# Data Exploration & Cleaning

# Preliminary data exploration

# Shape of dataframe
print(f"Shape of the DataFrame: {df_data.shape}")

# Displays the names of each column, the starting year of the Nobel Prize and
# the top 5 rows of DataFrame
print(df_data.head())

# Checking for duplicates
print(f"Duplicates: {df_data.duplicated().values.any()}")

# Checking for NaN Values
print(f"NaN values: {df_data.isna().values.any()}")

# Getting the count of NaN values per column
print(df_data.isna().sum())

# Thehe columns 'birth_date', 'organization_name', 'organization_city', and
# 'organization_country' having many missing values.
# If we filter on the NaN values in the 'birth_date' column, we'll see that
# names of organisations have been placed in the 'full_name' column.
col_subset = ['year', 'category', 'laureate_type',
              'birth_date', 'full_name', 'organization_name']
print(df_data.loc[df_data.birth_date.isna()][col_subset])

# Also, many prizes went to peple who were not associated with a university or
# research institute. This includes many of the Litrature and Peace prize winners
# (the 'organisation_name' column have NaN values for these winners).

col_subset = ['year','category', 'laureate_type','full_name', 'organization_name']
print(df_data.loc[df_data.organization_name.isna()][col_subset])

# Type Conversion

# Convert Year and Birth Date to a Datetime object
df_data["birth_date"] = pd.to_datetime(df_data.birth_date)

# Adding a Column with the Prize Share as a Percentage
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denominator

# The birth_date column (row 7) contains values that are of a Datetime type
print(df_data.info())

# Plotly Donut Chart: Percentage of Male vs. Female Laureates

biology = df_data.sex.value_counts()
fig = px.pie(
    labels=biology.index,
    values=biology.values,
    title="Percentage of Male vs. Female Winners",
    names=biology.index,
    hole=0.4, )

fig.update_traces(textposition="inside", textfont_size=15, textinfo="percent")

fig.show()


# The First 3 Women to Win the Nobel Prize
print(df_data[df_data.sex == "Female"].sort_values("year", ascending=True)[:3])

# Finding Repeat Winners

# Finding duplicate winners by name
is_winner = df_data.duplicated(subset=["full_name"], keep=False)
multiple_winners = df_data[is_winner]

# The amount of winners that have won more than once
print(f"There are {multiple_winners.full_name.nunique()}"
      " winners who were awarded the prize more than once.")

# Repeat winners. Who won and when and for what category. 4 were individuals,
# 2 were organisations
col_subset = ["year", "category", "laureate_type", "full_name"]
print(multiple_winners[col_subset])


# Number of Prizes per Category

# Finding the number of unique categories in a column
print(df_data.category.nunique())

# Generating a vertical plotly chart
prizes_per_category = df_data.category.value_counts()
vertical_bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale="Aggrnyl",
    title="Number of Prizes Awarded per Category"
)

vertical_bar.update_layout(
    xaxis_title="Nobel Prize Category",
    coloraxis_showscale=False,
    yaxis_title="Number of Prizes"
)

vertical_bar.show()

# The Economics Prize

# Displays the first 3 winners of the economics prize.
print(df_data[df_data.category == "Economics"].sort_values("year")[:3])

# The first prize in the the Economics field was awarded in 1969 to Jan Tinbergen
# from the Netherlands and Ragnar Frisch of Norway as joint winners

# Male & Female Winners by Category

cat_men_women = df_data.groupby(["category", "sex"],
                                as_index=False).agg({"prize": pd.Series.count})
cat_men_women.sort_values("prize", ascending=False, inplace=True)

print(cat_men_women)

vert_bar_split = px.bar(
    x=cat_men_women.category,
    y=cat_men_women.prize,
    color=cat_men_women.sex,
    title="Number of Prizes Awarded per Category split by Men and Women"
    )

vert_bar_split.update_layout(
    xaxis_title="Nobel Prize Category",
    yaxis_title="Number of Prizes"
    )
vert_bar_split.show()

# Number of Prizes Awarded Over Time

# Counting the number of Nobel prizes that are awarded each year
prize_per_year = df_data.groupby(by="year").count().prize

# Calculating the 5-year moving average
moving_average = prize_per_year.rolling(window=5).mean()

# Putting the above into a scatter plot
plt.figure(figsize=(16, 8), dpi=200)
plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)
plt.yticks(fontsize=14)

# 5 year ticks, displays every 5th year along the x-axis,
plt.xticks(
    ticks=np.arange(1900, 2021, step=5),
    fontsize=14,
    rotation=45
    )

ax = plt.gca()  # get current axis
ax.set_xlim(1900, 2020)

# Entries per year
ax.scatter(
    x=prize_per_year.index,
    y=prize_per_year.values,
    c="dodgerblue",  # dot colour
    alpha=0.7,
    s=100, )

# The rolling average
ax.plot(
    prize_per_year.index,
    moving_average.values,
    c="crimson",  # line colour
    linewidth=3, )

plt.show()


# Investigating if more prizes are shared than before

# Calculating the rolling/moving average of the percentage share of the prize
yearly_avg_share = df_data.groupby(by="year").agg({"share_pct": pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

# Scatter plot to display the increase in shared Nobel prizes as years go on
plt.figure(figsize=(16, 8), dpi=200)
plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(
    ticks=np.arange(1900, 2021, step=5),
    fontsize=14,
    rotation=45
    )

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)

# Inverting the prize sharing average axis, to be displayed alongside red
# moving average plot
ax2.invert_yaxis()

ax1.scatter(
    x=prize_per_year.index,
    y=prize_per_year.values,
    c="dodgerblue",  # colour of the dots for prize per year
    alpha=0.7,
    s=100, )

ax1.plot(
    prize_per_year.index,
    moving_average.values,
    c="crimson",  # colour for line for moving average plot
    linewidth=3, )

ax2.plot(
    prize_per_year.index,
    share_moving_average.values,
    c="grey",  # colour of the prize share average plot
    linewidth=3, )

plt.show()

# The Countries with the Most Nobel Prizes

# Prize ranking by country

# Top 20 countries with Nobel prize winners
top_countries = df_data.groupby(
    ["birth_country_current"],
    as_index=False
    ).agg({"prize": pd.Series.count})

top_countries.sort_values(by="prize", inplace=True)
top20_countries = top_countries[-20:]

# Horizontal bar chart displaying the ranking of the top 20 countries for
# Nobel prizes
h_bar = px.bar(
    x=top20_countries.prize,
    y=top20_countries.birth_country_current,
    orientation="h",
    color=top20_countries.prize,
    color_continuous_scale="Viridis",
    title="Top 20 Countries by Number of Prizes"
    )

h_bar.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="Country",
    coloraxis_showscale=False
    )
h_bar.show()


# Using a Choropleth Map to Show the Number of Prizes Won by Country

# New county dataframe, grouping by birth country and ISO (country code) columns
# from original df_data dataframe
df_countries = df_data.groupby(["birth_country_current", "ISO"],
                               as_index=False).agg({"prize": pd.Series.count})

# Ranks country by the amount of Nobel prizes won
df_countries.sort_values("prize", ascending=False)

# Creating a choropleth map chart
world_map = px.choropleth(
    df_countries,
    locations="ISO",
    color="prize",
    hover_name="birth_country_current",
    color_continuous_scale=px.colors.sequential.matter
    )

world_map.update_layout(coloraxis_showscale=True, )

world_map.show()


# The category breakdown by country

# Counting the prizes by category in each country
cat_country = df_data.groupby(["birth_country_current", "category"],
                               as_index=False).agg({"prize": pd.Series.count})

# , inplace=True  # taken out to make work. Overwise will give value of 'None'
cat_country.sort_values(by="prize", ascending=False)

# Merging the cat_country dataframe with the top20_countries dataframe
merged_df = pd.merge(cat_country, top20_countries, on="birth_country_current")
# change column names
merged_df.columns = ["birth_country_current", "category", "cat_prize", "total_prize"]

# , inplace=True  # taken out to make work. Overwise will give value of 'None'
merged_df.sort_values(by="total_prize")

# Creating the horizontal bar chart
# x-axis = category prize, y-axis = the prize winners country of origin and each
# colour represents a category
cat_cntry_bar = px.bar(
    x=merged_df.cat_prize,
    y=merged_df.birth_country_current,
    color=merged_df.category,
    orientation="h",
    title="Top 20 Countries by Number of Prizes and Category"
    )

cat_cntry_bar.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="Country"
    )
cat_cntry_bar.show()

# Number of Prizes Won by Each Country Over Time

# Making a new dataframe. Grouping data by birth country and year, then sorting by year
prize_by_year = df_data.groupby(by=["birth_country_current", "year"], as_index=False).count()
prize_by_year = prize_by_year.sort_values("year")[["year", "birth_country_current", "prize"]]
print(prize_by_year)

# Creating a series the has the cumulative sum for the number of prizes won
cumulative_prizes = prize_by_year.groupby(by=["birth_country_current",
                                              "year"]).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True)

# Using the cumulative_prizes series to create a chart, using the current birth
# country as the colour
line_chart = px.line(
    cumulative_prizes,
    x="year",
    y="prize",
    color="birth_country_current",
    hover_name="birth_country_current"
    )

line_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Prizes"
    )

line_chart.show()

# The Top Research Institutions

# A dataframe representing the top 20 organisations and sorting the values in
# acending order
top20_orgs = df_data.organization_name.value_counts()[:20]
top20_orgs.sort_values(ascending=True, inplace=True)

# Using the top20_org dataframe to create a vertical bar chart
org_bar = px.bar(
    x=top20_orgs.values,
    y=top20_orgs.index,
    orientation='h',
    color=top20_orgs.values,
    color_continuous_scale=px.colors.sequential.haline,
    title="Top 20 Research Institutions by Number of Prizes"
    )

org_bar.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="Institution",
    coloraxis_showscale=False
    )
org_bar.show()

# Cities that make the most discoveries

# A dataframe for the top 20 cities that do the most research
top20_org_cities = df_data.organization_city.value_counts()[:20]
top20_org_cities.sort_values(ascending=True, inplace=True)

# Using the top20_org_cities dataframe to create a vertical bar chart
city_bar2 = px.bar(
    x=top20_org_cities.values,
    y=top20_org_cities.index,
    orientation="h",
    color=top20_org_cities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Which Cities Do the Most Research?"
    )

city_bar2.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="City",
    coloraxis_showscale=False
    )
city_bar2.show()


# Charting the Laureate Birth Cities - Where the Nobel winners were born

# Dataframe to sort the top 20 cities where Nobel winners were born
top20_cities = df_data.birth_city.value_counts()[:20]
top20_cities.sort_values(ascending=True, inplace=True)

# Creating a horizontol bar chart with plotly
city_bar = px.bar(
    x=top20_cities.values,
    y=top20_cities.index,
    orientation="h",
    color=top20_cities.values,
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Where were the Nobel Laureates Born?"
    )

city_bar.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="City of Birth",
    coloraxis_showscale=False
    )
city_bar.show()

# Plotly Sunburst Chart: Combine Country, City, and Organisation

# Grouping data by organisations name, city and country
country_city_org = df_data.groupby(
    by=["organization_country",
        "organization_city",
        "organization_name"], as_index=False
    ).agg({"prize": pd.Series.count})

# Sorting data
country_city_org = country_city_org.sort_values('prize', ascending=False)
print(country_city_org)

# Using the data to create a sunburst chart
burst = px.sunburst(
    country_city_org,
    path=["organization_country", "organization_city", "organization_name"],
    values="prize",
    title="Where do Discoveries Take Place?",
    )

burst.update_layout(
    xaxis_title="Number of Prizes",
    yaxis_title="City",
    coloraxis_showscale=False
    )

burst.show()


# Patterns in the Laureate Age at the Time of the Award

# Extracting the birth year from the birth_date column
birth_years = df_data.birth_date.dt.year

# Calculating the age ate the time of the award
df_data["winning_age"] = df_data.year - birth_years

print(df_data)


# The oldest and youngest winners

# Displaying the youngest and oldest Nobel winners
print(df_data.nlargest(n=1, columns="winning_age"))
print(df_data.nsmallest(n=1, columns="winning_age"))

# Descriptive Statistics for the Laureate Age at Time of Award

# Creating a histogram
plt.figure(figsize=(8, 4), dpi=200)
sns.histplot(data=df_data,
             x=df_data["winning_age"],
             bins=30)
plt.xlabel("Age")
plt.title("Distribution of Age on Receipt of Prize")
plt.show()

# Winning Age Over Time in All Categories

# Chart shows that not only is the ages of laureates is increasing, but also in
# the last decade, the age range of laureates is widening
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(
        data=df_data,
        x="year",
        y="winning_age",
        lowess=True,
        scatter_kws={"alpha": 0.4},
        line_kws={"color": "black"}
        )

plt.show()

# Winning Age Across the Nobel Prize Categories

# Box plot by category
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.boxplot(
        data=df_data,
        x="category",
        y="winning_age"
        )

plt.show()

# Laureate Age Over Time by Category

# Using Seaborns .lmplot() to compare the ages of lauretes from multiple
# categories
with sns.axes_style("whitegrid"):
    sns.lmplot(
        data=df_data,
        x="year",
        y="winning_age",
        row="category",
        lowess=True,
        aspect=2,
        scatter_kws={"alpha": 0.6},
        line_kws={"color": "black"}, )

plt.show()

# Combine the above charts into the same chart using the 'hue' parameter
with sns.axes_style("whitegrid"):
    sns.lmplot(
        data=df_data,
        x="year",
        y="winning_age",
        hue="category",
        lowess=True,
        aspect=2,
        scatter_kws={"alpha": 0.5},
        line_kws={"linewidth": 5}
        )

plt.show()
