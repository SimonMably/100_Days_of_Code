
age = input("What is your current age?")

age_as_int = int(age)

day = 1

week = 1

month = 1

end_life = 90

# -----------------------------------------------------------------------------

days_year = (end_life - age_as_int) * (day * 365) 

weeks_year = (end_life - age_as_int) * (week * 52)

months_year = (end_life - age_as_int) * (month * 12)

time_left = (f"You have {days_year} left, or {weeks_year} left, or "
            f"{months_year} left.")

print(time_left)



















