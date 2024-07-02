### TIMESTAMPS
import datetime
import time

def send_emails():
    for i in range(10000):
        pass

start = time.time()
send_emails()
end = time.time()
duration = end - start

print(duration)


### DATE TIMES

from datetime import datetime

dt = datetime(2024, 6, 29)
print(dt)
dt = datetime.now()
print(dt)
datetime.strptime("2024/08/08", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

### TIME DELTAS

from datetime import datetime, timedelta

dt1 = datetime(2024, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days:", duration.days)
print("seconds:", duration.seconds)
print("total seconds:", duration.total_seconds())

dt1 = datetime(2024, 1, 1) + timedelta(days=1, seconds=100)
print(dt1)