"""
Object Oriented Programming
"""


class Student:
    number_of_students = 0
    school_name = "Online School"

    def __init__(self, st_first_name, st_last_name, st_major):
        self.st_firstname = st_first_name
        self.st_last_name = st_last_name
        self.st_major = st_major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f"{self.st_firstname} {self.st_last_name} is takes {self.st_major} as major!"

    def fullname_with_major_school(self):
        return f'{self.st_firstname} {self.st_last_name} take the major as {self.st_major} going to {self.school_name}'

    @classmethod
    def set_online_school(cls, new_school):  # use a classmethod using a decorator (@)
        cls.school_name = new_school

    @classmethod
    def split_students(cls, student_str):
        st_first_name, st_last_name, st_major = student_str.split('.')
        return cls(st_first_name, st_last_name, st_major)


print(f'Number of Students in the School = {Student.number_of_students}')
student_1 = Student('Gazi', 'Al- Amin', 'Software Engineering')
student_2 = Student('Masudul', 'karim', 'Computer Science & Engineering')
student_3 = Student('Tareq', 'Mahmud', 'English')

new_student = 'Aliza.Mehrish.English'
student_4 = Student.split_students(new_student)
student_4.set_online_school("Dhaka University")

print(student_1.fullname_with_major_school())
print(student_2.fullname_with_major())
print(student_3.fullname_with_major_school())
print(student_4.fullname_with_major_school())
print(f'Number of Students in the School = {Student.number_of_students}')

