# Attendance Tracker

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    attendance = input("Enter P for Present or A for Absent: ")

    students[name] = attendance

print("\nAttendance Report")

present = 0
absent = 0

for name, status in students.items():
    print(name, ":", status)

    if status.upper() == "P":
        present += 1
    else:
        absent += 1

print("Total Present:", present)
print("Total Absent:", absent)
