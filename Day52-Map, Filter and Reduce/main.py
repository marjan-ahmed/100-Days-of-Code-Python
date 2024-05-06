# MAP
def cube(x):
    return x*x*x

print(cube(3))

l = [1,2,3,4,5,4,]

# newl = []

# for numbers in l:
#     newl.append(cube(numbers))
    
newl = list(map(cube, l))
print(newl)

# FILTER
def filter_func(n):
    return n>3

newl2 = list(filter(filter_func, l))
print(newl2)

# REDUCE

from functools import reduce

numbers = [1,2,3,4,5] #Calculate the sum of numbers using the reduce function

sum = reduce(lambda x,y: x+y, numbers)
print(sum)
