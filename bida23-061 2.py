#enter number of students
while True:
        NumberOfStudents = int(input("Enter the number of students: "))
        if NumberOfStudents > 0:
            break

#initialize total grades
GradesSum = 0

#loop to collect each student's name and grade
for i in range(1, NumberOfStudents + 1):
    StudentFullnames = input(f"\nEnter Name of Student {i}: ")

    while True:
            StudentGrade = float(input(f"Enter Student's Grade {i}: "))
            if 0 <= StudentGrade <= 100:
                break
            else:
                print("Enter Valid Grade between 0 and 100")

#accumulates total grades
    GradesSum += StudentGrade

#calculates average grade
GradesAverage = GradesSum / NumberOfStudents

#displays whole class average
print(f"\nClass Grade Total: {GradesSum}")
print(f"\nClass Average: {GradesAverage:.2f}")

#written wholey by $herman