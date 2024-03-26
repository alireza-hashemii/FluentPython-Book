# how formatting works in python
from datetime import datetime

now = datetime.now()

v2 = format(now , "%H:%M:%S")
v3 = "It's now {:%H:%M %p}".format(now)
