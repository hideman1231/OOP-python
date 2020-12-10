from datetime import date, timedelta

now = date.today()
month_start = date(now.year, now.month, 1)

weekend = [5,6]

diff = (now - month_start).days + 1

print(now, month_start, diff)

day_count = 0

for day in range(diff):
    print((month_start + timedelta(day)).weekday())
    if (month_start + timedelta(day)).weekday() not in weekend:
        day_count += 1

print(day_count)