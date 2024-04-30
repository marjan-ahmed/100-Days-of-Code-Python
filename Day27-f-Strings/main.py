text = "Hey my name is {}, and I am from {}"

name = "Marjan" 
country = "Pakistan"

print(text.format(name, country)) # put the varibles in the sequence
print(text.format(country[1], name[0])) # put the varibles in wrong order, but show the correct index number

# the below code fragment can be found in:

# Example 1:

qoute = "The coder will die, but their loops never die."
author = "Marjan"

print(f"{author} said: {qoute}")

# Example 2:

print(f"The sum of 28 and 45 is {28+45}")

# Example 3:

txt = "I have {price:.2f} dollars!"
print(txt.format(price = 49))

# Example 4:

userName = input("What is your name? ")
password = int(input("Enter your password: "))

print(f"Hello {userName}, your password is {password}")