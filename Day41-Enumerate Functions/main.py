marks = [12, 43, 45, 56, 89, 100, 32, 98]

# for mark in marks:
#     print(mark)
#     if mark == marks[5]:
#         print("You are great")

# Using Enumerate function
# for index, mark in enumerate(marks):
#     print(mark)
#     if(index == 5):
#         print("You are great")

fruits = ['apple', 'orange', 'banana']

for index, fruit in enumerate(fruits):
    print(f"{index+1}: {fruit}")
