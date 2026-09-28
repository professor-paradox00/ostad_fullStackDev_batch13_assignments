class Student:
    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        

    def display_info(self):
        print(f"Name: {self.name}\nID: {self.student_id}\nEmail: {self.__email}\nAge: {self.age}\nDepartment: {self.department}")

    def calculate_result(self, *marks):
        if len(marks) == 0:
            return "No marks provided"

        average = sum(marks) / len(marks)
        return average

    def get_student_type(self):
        return "Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    def display_info(self):
            super().display_info()
            print(f"Semester: {self.semester}")
    
    def get_student_type(self):
        return "Undergraduate Student"


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")

    def get_student_type(self):
        return "Graduate Student"



print("\n\n")

student1 = UndergraduateStudent("Rahim", "UG001", "rahim@gmail.com", 22, "CSE", 5)

student1.display_info()

print("\n")

student2 = GraduateStudent("Karim", "GR001", "karim@gmail.com", 25, "CSE", "Artificial Intelligence")

student2.display_info()

print("\n")

print(student1.get_student_type())
print(student2.get_student_type())

print("\n")

students = [student1, student2]

for student in students:
    print(student.get_student_type())

print("\n")

print(student1.calculate_result(80))
print(student1.calculate_result(80, 90))
print(student1.calculate_result(80, 90, 85))

print("\n")

print(student1.calculate_result())

print("\n")

student3 = Student("Hasan", "ST001", "hasan@gmail.com", 23, "EEE")

student3.display_info()

print(student3.get_student_type())