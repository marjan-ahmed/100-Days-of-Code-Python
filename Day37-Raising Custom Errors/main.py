a = int(input("Enter the number between 2 to 5: "))

if int(a) < 2 or int(a) > 5:
    raise ValueError("Enter a number between 2 and 5")