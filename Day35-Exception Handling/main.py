i = 0

while True:
    n = input("Enter the number (1 to 10): ") 
    print("\n")
    print(f"Multiplicaion table of {n}".center(50))
    
    try:
        for i in range(1, 11):
            print(f"{int(n)} X {i} = {int(n) * i}")
    except:
        print(f"No table of {n}")

        print("some lines of code")
        print("end of the program")

# try:
#     num = int(input("Enter the integer: "))
#     a = [20,30]
#     print(a[num])

# except ValueError as ve:
#     print(ve)
# except IndexError:
#     print("Index Error")

# while True:
#     try:
#         fruits = []
#         fruitsadd = input("Enter the fruits to add to the list: ")
#         askingMore = bool(input("Do you want to add more: "))
#         print(askingMore)

#         if askingMore == True:
#             fruits = fruits.append(askingMore)
#             print(fruits)

#         list = fruits.append(fruitsadd)
#         print(fruits)

#     except:
#         print("Invalid input")
