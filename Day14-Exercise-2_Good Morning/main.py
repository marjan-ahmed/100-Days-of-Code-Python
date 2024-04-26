import time # built-in module

timestamp = time.strftime('%Hh:%Mm:%Ss %p')
print(timestamp.center(50))

timestamp = time.strftime('Hours: %H')
print(timestamp)
timestamp = time.strftime('Minutes: %M')
print(timestamp)
timestamp = time.strftime('Seconds: %S')
print(timestamp)
timestamp = time.strftime('PM / AM: %p')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime