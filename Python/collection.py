from datetime import datetime

date = datetime.now()
year = date.year
month = date.month

print(date)
print(year)
print(month)

days = None

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28

print(f"{days} days for {year}-{month}")