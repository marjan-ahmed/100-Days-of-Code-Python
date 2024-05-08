class Teacher:
    def __init__(self, name, staff):
        self.name = name
        self.staff = staff

    def  showDetails(self):
        print(f"{self.name} is a teacher and she is in {self.staff} staff")

th = Teacher("Ayesha", "science")
print(th)
print(th.showDetails())
