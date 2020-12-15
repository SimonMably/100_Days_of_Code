
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    #! FROM COURSE SOLUTION : EXAMPLE (unneessary for completing challenge)
    # Checks for invalid user responses
    # DOES NOT WORK
    # if month > 12 and month < 1:
    #     return "Invalid month"
    #     print("Invalid month")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # If entered year is a leap year, make february 29 days long and print
    # year is leap year.    
    if is_leap(year):

        month_days[1] = 29
        print(f"\nIs {year} a leap year: {is_leap(year)}")
    return month_days[month - 1]
    
    '''FROM COURSE SOLUTION : ALTERNATIVE
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

    '''
    
    # for month_names in months:
    #     for amount_of_days in month_days:
            
    #         month_names == amount_of_days
    #     print(month_names)
    # for amount_of_days in month_days:
    #     month + 1 = month_days


  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







