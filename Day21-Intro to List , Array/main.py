marks = [     2,     32,     4,    "Maths",   True] # Can we store different data types in the list? "YES"
#            [0]     [1]     [2]     [3]       [4]

print(marks)
print(type(marks))

print(marks[0]) # the index is the sequence number of the list which start with the number 0
print(marks[1])
print(marks[2]) 
print(marks[3])
print(marks[4])

print(marks[-1]) # negitiv index
print(marks[len(marks)-1]) #positive index

print(marks[:])
print(marks[:3])

## Linear Search (sequential search) in the list

if "a" in "Marjan":
    print("Yes")

if marks[1] in marks:
    print("Yes")

if "Maths" in marks:
    print("Yes")

# list indexing

animals = ["cat", "dog", "bat", "dolphin", "cheetah", "horse", "puma", "goat", "cow"]
print(animals[1:8:3])