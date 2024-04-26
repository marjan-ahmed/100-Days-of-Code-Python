name = "Marjan"
print("Hello, " + name)

# If I want to print all the words and single/double quotes, So what I will do

# Method 1: Put single qoutes to the str

print('The word computer is derived from the Latin word "computare",which means "to calculate"')

# Method 2: Put triple qoutes and then statements and all kind of sentences will be string or any special characters ("",'', etc)

print(
'''
Hey You!
My surname is 'Ahmed',
You are here right now,
Just code -> like an "AI" (Artificial Intelligence)
'''
)

# Object: You can print the indivisual characters in the words in two Methods

# Method 1: Time taking by calling each character by their index number (the code depends upon your characters)

language = "Python"
aboutPy = "Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5],"\n")

# Method 2: Use for-loop to print each character in the str of aboutPy (2 lines of code)

for character in aboutPy:
    print(character)