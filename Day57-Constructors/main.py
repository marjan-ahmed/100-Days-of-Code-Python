class Person:
    
    def __init__(self, name, age):
        print("Hey I am a person")
        self.name = name
        self.age = age

        def info(self):
            print(f"{self.name} is {self.age} years old")


a = Person("Marjan", 15)
b = Person("Yousuf", 14)
c = Person("Usaid", 13)

print("\n")

obj = print(f"{a.name} is {a.age} years old")
obj = print(f"{b.name} is {b.age} years old")
obj = print(f"{c.name} is {c.age} years old")

# a.info()
# b.info()
# c.info()
