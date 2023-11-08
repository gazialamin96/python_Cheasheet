"""
Inheritance
"""


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f" Hi! I am {self.first_name} {self.last_name}"


class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major

    def greeting(self):
        return f"Hi! I am {self.first_name} {self.last_name} and I am studying in {self.major}"


student_1 = Student("Gazi", "Al- Amin")
student_2 = CollegeStudent("Aliza", "Mehrish", "Medicine")

print(student_1.greeting())
print(student_2.greeting())
