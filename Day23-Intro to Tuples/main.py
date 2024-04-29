marks = (20,28,34,40,True,"computer")

print(type(marks))
print(marks)

print(marks[0])
print(marks[-2])
print(marks[3])
print(marks[:2])

if 40 in marks:
    print("Yes, 40 is in the tuple")

if 20 in marks and "computer" in marks:
    print("Yes, 20 and 'computer' are in the tuple")