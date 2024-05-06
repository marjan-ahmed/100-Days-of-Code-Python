# def double(x):
#     return x * 2

# print(double(5))

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x + y + z)/2  # We can use multiple values for Lamda

print(double(5))
print(cube(5))
print(avg(5, 3, 10))
print(appl(lambda x: x*x*x, 2))