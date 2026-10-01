class Student:
    def __init__(self, name, age, email, phone, address, gender, course, Department, year):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        self.gender = gender
        self.course = course
        self.Department = Department
        self.year = year

    def display_info(self):
        print("Name: " + self.name + "\nAge: " + str(self.age) + "\nEmail: " + self.email + "\nPhone: " + self.phone + "\nAddress: " + self.address + "\nGender: " + self.gender + "\nCourse: " + self.course + "\nDepartment: " + self.Department + "\nYear: " + str(self.year) + "\n------------------------")
student1 = Student("Ali", 20, "ali@example.com", "1234567890", "ABC", "Male", "Computer Science", "CS", 2)
student2 = Student("Ahmed", 22, "ahmed@example.com", "0987654321", "DEF", "Male", "Mathematics", "MATH", 3)
student1.display_info()
student2.display_info()