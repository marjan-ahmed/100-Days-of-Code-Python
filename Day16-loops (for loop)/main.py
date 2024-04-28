myName = "Marjan"

for i in myName:
    print(i.upper())

cars = 'fortuner mercides audi ferrori porche'
listConverter = cars.split(' ')

print(listConverter)

for i in listConverter:
    print("\n",i)
    for x in cars:
        print(x)

for i in range(len(cars)): # The characters of the string in the cars
    print("\n",i)

# Even numbers
print("\n Even numbers till 10")
for i in range(0, 12, 2): # The last number in the range is how many numbers will you want to clear from each
    print(i)

# Odd Number
print("\n Odd Numbers till 11")
for i in range(1, 12, 2): # The last number in the range is how many numbers will you want to clear from each
    print(i)
