def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year_check = 2025
if is_leap_year(year_check):
    print(year_check,"is a leap year")
else:
    print(year_check,"is not a leap year") 