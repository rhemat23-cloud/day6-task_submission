class User:
    def __init__(self, username, email):
        # Encapsulated attributes (private)
        self.__username = username
        self.__email = email

    # Getter for username
    def get_username(self):
        return self.__username

    # Setter for username
    def set_username(self, username):
        self.__username = username

    # Getter for email
    def get_email(self):
        return self.__email

    # Setter for email
    def set_email(self, email):
        self.__email = email

    # Display user information
    def display_info(self):
        return f"Username: {self.__username}, Email: {self.__email}"


# Student class inherits from User
class Student(User):
    def __init__(self, username, email, student_id, course):
        super().__init__(username, email)
        self.__student_id = student_id
        self.__course = course

    # Getter and Setter for student_id
    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    # Getter and Setter for course
    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Student ID: {self.__student_id}, Course: {self.__course}"


# Faculty class inherits from User
class Faculty(User):
    def __init__(self, username, email, faculty_id, department):
        super().__init__(username, email)
        self.__faculty_id = faculty_id
        self.__department = department

    # Getter and Setter for faculty_id
    def get_faculty_id(self):
        return self.__faculty_id

    def set_faculty_id(self, faculty_id):
        self.__faculty_id = faculty_id

    # Getter and Setter for department
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Faculty ID: {self.__faculty_id}, Department: {self.__department}"


# Usage example
def main():
    student = Student("reo", "reo@example.com", "s342", "Computer Science")
    faculty = Faculty("heman", "hm@example.com", "F987", "Physics")

    print(student.display_info())
    print(faculty.display_info())

    # Updating encapsulated fields
    student.set_course("Data Science")
    faculty.set_department("Mathematics")

    print("After updates:")
    print(student.display_info())
    print(faculty.display_info())


if __name__ == "__main__":
    main()
