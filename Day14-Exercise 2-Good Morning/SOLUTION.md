# Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
```python
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
```
![image](https://github.com/marjan-ahmed/100-Days-Of-Python/assets/159646510/042ce734-cc2f-4fe2-853c-c4c1b1e3c7be) ![image](https://github.com/marjan-ahmed/100-Days-Of-Python/assets/159646510/b1cac652-9783-407c-8f0f-5022d85a03d3)


