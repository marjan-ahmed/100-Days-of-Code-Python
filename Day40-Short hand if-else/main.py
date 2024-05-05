#Ex 1:

# n = int(input("Enter the number between 1 to 5: "))

# print("5 is also my favorite") if n == 5 else print("2,3,4 is common bro") if n > 1 and n < 4 else print("Be the first in your work") if n == 1 else print("Nice choise")

# Ex 2:
age = int(input("Enter your age: "))

print("Yeah! You can vote") if age >= 18 else print("Sorry! You can not vote") if age < 18 else print("Wrong answer")

note = 18 if age < 18 else 0
print("You are currently", age,"You have to be atleast",note)