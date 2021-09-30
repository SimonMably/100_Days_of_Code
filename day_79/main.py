import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter("%Y")

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Reading the data
df_yearly = pd.read_csv("annual_deaths_by_clinic.csv")
# parse_dates avoids DateTime conversion later
df_monthly = pd.read_csv("monthly_deaths.csv",
                      parse_dates=["date"])

# Preliminary Data Exploration

# Monthly Data
print(f"Shape of Monthly DataFrame: {df_monthly.shape}\n")
print(df_monthly.head())
print(df_monthly.tail(), "\n")

print(df_monthly.info())

# Yearly Data
print(f"Shape of yearly DataFrame: {df_yearly.shape}\n")
print(df_monthly.head())
print(df_monthly.tail(),"\n")
print(df_yearly.info())

# Check for Nan Values and Duplicates
print(f"Monthly duplicates: {df_monthly.duplicated().values.any()}")
print(f"Yearly duplicates: {df_yearly.duplicated().values.any()}")

print(df_monthly.describe(), "\n")
print(df_yearly.describe())

# Percentage of Women Dying in Childbirth

death_prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f"Chances of dying in the 1840s in Vienna: {death_prob:.3}%")

# Visualise the Total Number of Births and Deaths over Time

# Ploting the Monthly Data on Twin Axes
plt.figure(figsize=(14, 8), dpi=200)
plt.title("Total Number of Monthly Births and Deaths", fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel("Births", color="skyblue", fontsize=18)
ax2.set_ylabel("Deaths", color="crimson", fontsize=18)

# Use Locators
ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

ax1.grid(color="grey", linestyle="--")

# The amount of births per year, birth amounts on left axis
ax1.plot(
    df_monthly.date,
    df_monthly.births,
    color="skyblue",
    linewidth=3
    )

# The amount of deaths per year, deatth amounts on right axis
ax2.plot(
    df_monthly.date,
    df_monthly.deaths,
    color="crimson",
    linewidth=2,
    linestyle="--"
    )

plt.show()

# Analysing the Yearly Data Split by Clinic

# Line chart displaying the amount of births in each clinic
births_line = px.line(df_yearly,
                      x="year",
                      y="births",
                      color="clinic",
                      title="Total Yearly Births by Clinic")

births_line.show()

# The amount of deaths in each clinic
deaths_line = px.line(
    df_yearly,
    x="year",
    y="deaths",
    color="clinic",
    title="Total Yearly Deaths by Clinic"
    )

deaths_line.show()

# Calculating the Proportion of maternal Deaths at Each Clinic

# Adding a column that contains the percentage of deaths
df_yearly["pct_deaths"] = df_yearly.deaths / df_yearly.births

# The average death rate for the entire time period fo clinic 1
clinic_1 = df_yearly[df_yearly.clinic == "clinic 1"]
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
print(f"Average death rate in clinic 1 is {avg_c1:.3}%.")

# The average death rate for the entire time period fo clinic 2
clinic_2 = df_yearly[df_yearly.clinic == "clinic 2"]
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f"Average death rate in clinic 2 is {avg_c2:.3}%.")

# Plotting the Proportion of Yearly Deaths by Clinic
avg_deaths_line = px.line(
    df_yearly,
    x="year",
    y="pct_deaths",
    color="clinic",
    title="Proportion of Yearly Deaths by Clinic"
    )

avg_deaths_line.show()

# The Effect of Handwashing

# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime("1847-06-01")

# Adding a column call 'pct_deaths' to the df_monthly dataframe - divides births from deaths
df_monthly["pct_deaths"] = df_monthly.deaths / df_monthly.births

# Creating 2 subsets based on the handwashing_start date
before_washing = df_monthly[df_monthly.date < handwashing_start]
after_washing = df_monthly[df_monthly.date >= handwashing_start]

# Determining the average death rate before and after the start of handwashing
# bw_rate = before washing rate
# aw_rate = after washing rate
bw_rate = before_washing.deaths.sum() / before_washing.births.sum() * 100
aw_rate = after_washing.deaths.sum() / after_washing.births.sum() * 100
print(f"Average death rate before 1847 was {bw_rate:.4}%")
print(f"Average death rate AFTER 1847 was {aw_rate:.3}%")

# The :.4 & the :.3 inside the {} in the f-strings determine the number of digits
# that get printed out in the print statement to form a number (eg. :.4 can give
# number of 10.53)

# Creating a DataFrame that has a 6 6 month rolling average death rat prior to
# mandatory handwashing
roll_df = before_washing.set_index("date")
roll_df = roll_df.rolling(window=6).mean()

# Using the previous line chart and adding the hand washing information to it
plt.figure(figsize=(14, 8), dpi=200)
plt.title("Percentage of Monthly Deaths over Time", fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)

plt.ylabel("Percentage of Deaths", color="crimson", fontsize=18)

ax = plt.gca()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim([df_monthly.date.min(), df_monthly.date.max()])

plt.grid(color="grey", linestyle="--")

# The 6 month moving average line
ma_line, = plt.plot(
    roll_df.index,
    roll_df.pct_deaths,
    color="crimson",
    linewidth=3,
    linestyle="--",
    label="6m Moving Average"
    )

# The before washing line
bw_line, = plt.plot(
    before_washing.date,
    before_washing.pct_deaths,
    color="black",
    linewidth=1,
    linestyle="--",
    label="Before Handwashing"
    )

# The after washing line
aw_line, = plt.plot(
    after_washing.date,
    after_washing.pct_deaths,
    color="skyblue",
    linewidth=3,
    marker="o",
    label="After Handwashing"
    )

plt.legend(
    handles=[ma_line, bw_line, aw_line],
    fontsize=18
    )

plt.show()

# Visualising Distributions and Testing for Statistical Significance

# Calculating the Difference in the Average Monthly Death Rate
avg_prob_before = before_washing.pct_deaths.mean() * 100
print(
    f"Chance of death during childbirth before handwashing: "
    f"{avg_prob_before:.3}%."
    )

avg_prob_after = after_washing.pct_deaths.mean() * 100
print(
    f"Chance of death during childbirth AFTER handwashing: "
    f"{avg_prob_after:.3}%."
    )

mean_diff = avg_prob_before - avg_prob_after
print(
    f"Handwashing reduced the monthly proportion of deaths by {mean_diff:.3}%!"
    )

times = avg_prob_before / avg_prob_after
print(f"This is a {times:.2}x improvement!")

# Using Box Plots to Show How the Death Rate Changed Before and After Handwashing
df_monthly["washing_hands"] = np.where(df_monthly.date < handwashing_start, "No", "Yes")

box = px.box(
    df_monthly,
    x="washing_hands",
    y="pct_deaths",
    color="washing_hands",
    title="How Have the Stats Changed with Handwashing?"
    )

box.update_layout(
    xaxis_title="Washing Hands?",
    yaxis_title="Percentage of Monthly Deaths", )

box.show()

# Using Histograms to Visualise the Monthly Distribution of Outcomes

hist = px.histogram(
    df_monthly,
    x="pct_deaths",
    color="washing_hands",
    nbins=30,
    opacity=0.6,
    barmode="overlay",
    histnorm="percent",
    marginal="box", )

hist.update_layout(
    xaxis_title="Proportion of Monthly Deaths",
    yaxis_title="Count", )

hist.show()

# Using a Kernel Density Estimate (KDE) to visualise a smooth distribution

plt.figure(dpi=200)
# By default the distribution estimate includes a negative death rate!
sns.kdeplot(before_washing.pct_deaths,
            shade=True,
            clip=(0,1))
sns.kdeplot(after_washing.pct_deaths,
            shade=True,
            clip=(0,1))
plt.title("Est. Distribution of Monthly Death Rate Before and After Handwashing")
plt.xlim(0, 0.40)
plt.show()

# Using a T-Test to Show Statistical Significance

t_stat, p_value = stats.ttest_ind(a=before_washing.pct_deaths,
                                  b=after_washing.pct_deaths)
print(f"p-palue is {p_value:.10f}")
print(f"t-statistic is {t_stat:.4}")
