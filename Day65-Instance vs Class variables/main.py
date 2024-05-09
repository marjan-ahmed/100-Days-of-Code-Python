class Employee:
    company = "Apple Inc."
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 110.5
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.company} is: {self.raise_amount}")

# For Employee 1
emp1 = Employee("Marjan")
emp1.raise_amount = 209.8
emp1.company = "Microsoft Corporation"
emp1.noOfEmployees = 100
emp1.showDetails()

# For Employee 2
spm2 = Employee("Sufyan")
spm2.showDetails()