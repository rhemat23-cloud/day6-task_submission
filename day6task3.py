# Parent class
class User:
    def greet(self):
        print("Welcome User")

# Child class - Student
class Student(User):
    def greet(self):
        print("Welcome Student")

# Child class - Faculty
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

# Testing
student = Student()
faculty = Faculty()

student.greet()   # Output: Welcome Student
faculty.greet()   # Output: Welcome Faculty

