# Student Grading System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)

print("\nStudent Details")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", student["grade"])
    print("----------------")
