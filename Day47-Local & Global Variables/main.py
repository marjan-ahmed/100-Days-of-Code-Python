x = 10 # Global variable
y = "Hello world" # Global variable

def func():
    # global x
    x = 5 # local Variable
    y = "No Hello world" # local Variable
    print("The value is print by local variable:",x) 
    print("The value is print by local variable:",y)
    print("\n")

func()
print("This is print with global varible",x)
