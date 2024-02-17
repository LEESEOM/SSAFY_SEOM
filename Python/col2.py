from datetime import datetime
from collections import namedtuple

Month = namedtuple('Month', ['days', 'name'])

months = {
    1: Month(31, 'January'),
    2: Month(28, 'February'),
    3: Month(31, 'March'),
    4: Month(30, 'April'),
    5: Month(31, 'May'),
    6: Month(30, 'June'),
    7: Month(31, 'July'),
    8: Month(31, 'August'),
    9: Month(30, 'September'),
    10: Month(31, 'October'),
    11: Month(30, 'November'),
    12: Month(31, 'December')
}

date = datetime.now()
year = date.year
month = date.month

current_month = months.get(month)

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        current_month = current_month._replace(days=29)

print(f"{current_month.days} days for {year}-{current_month.name}")
