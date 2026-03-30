# Parent Class
class User:
    def register(self):
        print("User registered successfully.")

    def login(self):
        print("User logged in successfully.")


# Child Class 1
class Student(User):
    def student_greet(self):
        print("Hello Student")


# Child Class 2
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel Inheritance: TempFaculty inherits from Faculty
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# ------------------- DEMONSTRATION -------------------

# 1. Student object can access parent methods
student_obj = Student()
student_obj.register()       # From User
student_obj.login()          # From User
student_obj.student_greet()  # From Student

print("-" * 40)

# 2. Faculty object can access parent methods
faculty_obj = Faculty()
faculty_obj.register()       # From User
faculty_obj.login()          # From User
faculty_obj.faculty_greet()  # From Faculty

print("-" * 40)

# 3. TempFaculty object can access methods from Faculty and User
temp_faculty_obj = TempFaculty()
temp_faculty_obj.register()          # From User
temp_faculty_obj.login()             # From User
temp_faculty_obj.faculty_greet()     # From Faculty
temp_faculty_obj.tempFaculty_greet() # From TempFaculty

print("-" * 40)

# 4. Parent object cannot access child methods
parent_obj = User()
parent_obj.register()
parent_obj.login()
# The following will cause AttributeError if uncommented:
# parent_obj.student_greet()
# parent_obj.faculty_greet()
# parent_obj.tempFaculty_greet()



