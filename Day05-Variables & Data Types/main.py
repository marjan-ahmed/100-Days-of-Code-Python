# Text data: str

print("\n")
name = "Marjan"
print("The type of name is:",type(name))
print("\n")
# Numeric data: int, float, complex

grade = 9
age = 15.5
randomMath = complex(2,4)

print("The type of grade/class is:",type(grade))
print("The type of age is:",type(age))
print("The type of randomMath (Algerba) is:",type(randomMath))
print("\n")

# Boolean data:

canVote = False
isCoder = True

print("The type of canVote is:",type(canVote))
print("The type of isCoder is:",type(isCoder))
print("\n")

# Sequenced data: list, tuple, dict ("dict stands for dictionary and it is also called an object")

customList = [["apple","banana","strawberry","watermelon","mango"],[2,4,6,8,10]]
animalsTuple = (("Lion","Tiger","Puma"), ("Fish", "Seahorse", "Octopus"))
employerDict = {
               "name": "marjan",
               "email": "marjanahmed.dev@gmail.com",
               "password": 1234,
               "isPresent": True
               }

print("The type of customList isL:",type(customList))
print("The type of animals is",type(animalsTuple))
print("tThe type of employer is:",type(employerDict))