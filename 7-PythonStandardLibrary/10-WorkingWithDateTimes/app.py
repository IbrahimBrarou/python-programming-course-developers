from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()
datetime.strptime("2018/01/01", "%Y/%m/%d")  # string to date


dt = datetime.fromtimestamp(time.time())
print(f"{dt.year} / {dt.month}")


string_format = dt.strftime("%Y/%m")  # date to string
print(string_format)

print(dt1 > dt2)
