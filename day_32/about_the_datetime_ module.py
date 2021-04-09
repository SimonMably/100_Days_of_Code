import datetime as dt

# Current day and time at local time zone (yyyy-mm-dd hr:min:sec)
now = dt.datetime.now()
print(now)
print(type(now))
# The below code won't work because dt.datetime.now() is a class/method
# if now == 2020 or now == 2021:
#     print(f"It's {now}, wear a face mask.")

# Accessing attribute of dt.datetime.now() (as now (var))
year = now.year
print(year)
print(type(year))
# This works because its datatype is an integer
if year == 2020 or year == 2021:
    print(f"It's {year}, wear a face mask.")

month = now.month
# Prints the numerical value of the month, not the name of the month
print(month)

day_of_week = now.weekday()
# Prints the numerical value of the weekday. Computers start counting at 0, so:
# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday
print(day_of_week)

# The year, month and day positional arguments are required, all other
# positional arguments that can be used here have default values and don't
# need to be used. This will also use the time (as hour:min:sec) but will use
# the default value of '00:00:00' if the hour, minute and second positional
# arguments aren't used.
date_of_birth = dt.datetime(year=1989, month=5, day=25)
print(date_of_birth)


