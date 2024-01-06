from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)  # adding one day
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)  # this is just the seconds
# this is the days and hours and minutes and seconds transformed into seconds
print(duration.total_seconds())

# months an years are not existinf in time delta
