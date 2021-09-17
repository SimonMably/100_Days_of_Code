import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')


# Data Exploration

# Tesla Dataframe
print("Tesla\n")

# Shape of the Tesla dataframe
print(df_tesla.shape, "\n")

# Names of each column and the amount of rows in each column
print(df_tesla.count(), "\n")

# Number of rows and columns in Tesloa dataframe
print(f"Number of rows: {len(df_tesla.index)}")
print(f"Number of columns: {len(df_tesla.columns)}")

# Largest & smallest values in "Web Search" column

large_web_search = df_tesla["TSLA_WEB_SEARCH"].max()
small_web_search = df_tesla["TSLA_WEB_SEARCH"].min()

print(f"Largest value for Tesla in Web Search: {large_web_search}")
print(f"Smallest value for Tesla in Web Search: {small_web_search}")

# Displays information on Tesla web search Tesla $US close in their own columns
print(df_tesla.describe(), "\n")

# Shows that the periodicity is monthly
print(df_tesla["MONTH"].head(), "\n")
print(df_tesla["MONTH"].tail(), "\n")

# Unemployment Dataframe
print("Unemployment\n")

# The shape of the unemployment datafram
print(df_unemployment.shape, "\n")

# Names of each column and the amount of rows in each column
print(df_unemployment.count(), "\n")

# Number of rows and columns in Tesla dataframe
print(f"Number of rows: {len(df_unemployment.index)}")
print(f"Number of columns: {len(df_unemployment.columns)}")

# Largest value in the "Web Search" column
largest_unemployed_web = df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()
print("Largest value for 'Unemployment Benefits' "
      f"in Web Search: {largest_unemployed_web}", "\n")

# Bitcoin Dataframe

print("Bitcoin\n")

# df_btc_search
# df_btc_price

# Shape of the Bitcoin price dataframe
print(df_btc_price.shape, "\n")

# Names of each column and the amount of rows in each column
print(df_btc_price.count(), "\n")

# Number of rows and columns in Tesla dataframe
print(f"Number of rows: {len(df_btc_price.index)}")
print(f"Number of columns: {len(df_btc_price.columns)}")

# Displays information on Tesla web search Tesla $US close in their own coloumns
print(df_btc_price.describe(), "\n")

# Shows that the periodicity is daily
print(df_btc_price["DATE"].head(), "\n")
print(df_btc_price["DATE"].tail(), "\n")

# Largest Bitcoin news search
large_btc_news_search = df_btc_search["BTC_NEWS_SEARCH"].max()

print(f'largest BTC News Search: {large_btc_news_search}')


# Data Cleaning

# Check for Missing Values
print(f"Missing values for Tesla?: {df_tesla.isna().values.any()}")
print(f"Missing values for U/E?: {df_unemployment.isna().values.any()}")
print(f"Missing values for BTC Search?: {df_btc_search.isna().values.any()}")

print(f"Missing values for BTC Price?: {df_btc_price.isna().values.any()}")

print(f"Missing values for BTC Price?: {df_btc_price.isna().values.any()}")

# Using .dropna() to remove missing values
# df_btc_price = df_btc_price.dropna(inplace=True)  # <-This causes the dataframe to become 'None
df_btc_price.dropna(inplace=True)
print(df_btc_price)

# Convert Strings to DateTime Objects

df_tesla["MONTH"] = pd.to_datetime(df_tesla["MONTH"])
print(df_tesla["MONTH"], "\n")

df_unemployment["MONTH"] = pd.to_datetime(df_unemployment["MONTH"])
print(df_unemployment["MONTH"], "\n")

df_btc_price["DATE"] = pd.to_datetime(df_btc_price["DATE"])
print(df_btc_price["DATE"], "\n")

df_btc_search["MONTH"] = pd.to_datetime(df_btc_search["MONTH"])
print(df_btc_search["MONTH"], "\n")


# Converting from Daily to Monthly Data

# The average price of the month
df_btc_monthly_average = df_btc_price.resample('M', on='DATE').mean()

# The last available price of the month
df_btc_monthly = df_btc_price.resample('M', on='DATE').last()
print(df_btc_monthly.shape)
print(df_btc_monthly.head(), "\n")


# Data Visualisation with Matplotlib

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

# Tesla Stock Price v.s. Search Volume

# version 1
ax1 = plt.gca()
ax2 = ax1.twinx()

# Colouring both axis labels and the lines on the chart using keyword
# arguments (kwargs)
ax1.set_ylabel('TSLA Stock Price', color='#E6232E')  # can use a HEX code
ax2.set_ylabel('Search Trend', color='skyblue')  # or a named colour

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E')
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue')

# Version 2: making chart bigger and easier to read with fontsize and
# linewidth kwargs
# increases size and resolution
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

# Also, increase fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

# Displays chart explicitly
plt.show()

# Version 3: Adding formatting on the x-axis
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)

# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# Set the minimum and maximum values on the axes
ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])

# format the ticks
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

print(plt.show())


# Bitcoin (BTC) Price v.s. Search Volume

# Chart for the Bitcoin Prices vs. Search volumes

plt.figure(figsize=(14, 8), dpi=120)

plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color='#F08F2E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=0, top=15000)
ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])

# Experiment with the linestyle and markers
ax1.plot(
    df_btc_monthly.index, df_btc_monthly.CLOSE,
    color='#F08F2E', linewidth=3, linestyle='--'
    )
ax2.plot(
    df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH,
    color='skyblue', linewidth=3, marker='o'
    )

plt.show()


# Unemployment Benefits Search vs. Actual Unemployment in the U.S.

# Unemployement Benefits Search vs. Actual Unemployment in the U.S.

plt.figure(figsize=(14, 8), dpi=120)
plt.title(
    'Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate',
    fontsize=18
    )
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])

# Show the grid lines as dark grey lines
ax1.grid(color='grey', linestyle='--')

# Change the dataset used
ax1.plot(
    df_unemployment.MONTH, df_unemployment.UNRATE,
    color='purple', linewidth=3, linestyle='--'
    )
ax2.plot(
    df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH,
    color='skyblue', linewidth=3
    )

print(plt.show())

# 6 month rolling average for web searches

plt.figure(figsize=(14, 8), dpi=120)
plt.title(
    'Rolling Monthly US "Unemployment Benefits" Web Searches vs UNRATE',
    fontsize=18
    )
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([df_unemployment.MONTH[0], df_unemployment.MONTH.max()])

# Calculate the rolling average over a 6 month window
roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(
    window=6
    ).mean()

ax1.plot(
    df_unemployment.MONTH, roll_df.UNRATE, 'purple', linewidth=3, linestyle='-.'
    )
ax2.plot(
    df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, 'skyblue',
    linewidth=3
    )

print(plt.show())


# Including 200 in Unemployment Charts

df_ue_rate_20 = pd.read_csv("UE Benefits Search vs UE Rate 2004-20.csv")
df_ue_rate_20["MONTH"] = pd.to_datetime(df_ue_rate_20["MONTH"])

plt.figure(figsize=(14, 8), dpi=120)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
plt.title(
    'Monthly US "Unemployment Benefits" Web Search vs UNRATE incl 2020',
    fontsize=18
    )

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color='purple', fontsize=16)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=16)

ax1.set_xlim([df_ue_rate_20["MONTH"].min(), df_ue_rate_20["MONTH"].max()])

ax1.plot(df_ue_rate_20["MONTH"], df_ue_rate_20["UNRATE"], 'purple', linewidth=3)
ax2.plot(
    df_ue_rate_20["MONTH"], df_ue_rate_20["UE_BENEFITS_WEB_SEARCH"], 'skyblue',
    linewidth=3
    )

print(plt.show())
