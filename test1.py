import datetime
import time

ms = datetime.datetime.now(datetime.timezone.utc)

x = ms.timestamp()

t1 = datetime.datetime.fromtimestamp(x)
print(ms)
print(x)
print(int(x * 1000000))
print(t1.strftime('%Y-%m-%d %H:%M:%S'))

t2 = datetime.datetime.fromtimestamp(1721189439.6231236)
print(t2.strftime('%Y-%m-%d %H:%M:%S'))
