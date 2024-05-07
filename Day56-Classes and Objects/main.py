class Student:
    name = "Marjan"
    rollNum = 26
    subject = "English"

    def info(self):
       print(f"{self.name}, roll number is {self.rollNum}")

a = Student()
b = Student()

a.name = "Vernrie"
a.rollNum = 12
# print(f"{a.name}, roll number is {a.rollNum}")

b.name = "Raheel"
a.rollNum = 49

a.info()
b.info()