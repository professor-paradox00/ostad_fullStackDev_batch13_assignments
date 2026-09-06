print("\n===Welcome to Student Grade Calculator===\n")
student_name = input("Enter you name: ")
first_sub = float(input("Enter first subject number: "))
second_sub = float(input("Enter second subject number: "))
third_sub = float(input("Enter third subject number: "))

total_marks = first_sub + second_sub + third_sub
avg = total_marks/3
grade = ""

if 100>=avg>=80:
    grade = "A+"
elif 79>=avg>=70:
    grade = "A"
elif 69>=avg>=60:
    grade = "B"
elif 59>=avg>=50:
    grade = "C"
elif avg<50:
    grade = "F"
else:
    grade = "Not Found suitable grade"

print(f"\nStudent Name: {student_name}\nTotal Marks: {total_marks:.2f}\nAverage: {avg:.2f}\nGrade: {grade}\n")
