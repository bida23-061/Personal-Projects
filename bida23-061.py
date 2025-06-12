#defining Subjects
SubjectsOfStudy = ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]

#enter the number of students
while True:
        NumberOfStudents = int(input("Enter Number of Students: "))
        if NumberOfStudents > 0:
            break
        else:
            print("Please Enter A Valid INTEGER.")

#stores students' information
StudentsData = []

#initialize total grades
GradesSum = 0
#enter each student's name and grades
for i in range(1, NumberOfStudents + 1):
    StudentFullname = input(f"\nEnter Student Full Namws {i}: ")
    StudentGrades = []

    for subject in SubjectsOfStudy:
        while True:
                StudentGrade = float(input(f"Enter {StudentFullname}'s Grade in {subject}: "))
                if 0 <= StudentGrade <= 100:
                    StudentGrades.append(StudentGrade)
                    break
                else:
                    print("ENTER A VALID GRADE")

#store the student's name and grades as a tuple
    StudentsData.append((StudentFullname, StudentGrades))

#accumulates total grades
    GradesSum += StudentGrade

#calculates average grade
GradesAverage = GradesSum / NumberOfStudents

#displays whole class average
print(f"\nClass Grade Total: {GradesSum}")
print(f"\nClass Average: {GradesAverage:.2f}")

#calculates the total and average grade for each student
print("\nStudent Grades Summary:")
for Student in StudentsData:
    StudentFullname, StudentGrades = Student
    GradesAverage = sum(StudentGrades) / len(StudentGrades)
    print(f"{StudentFullname} Grades: {StudentGrades}, Average Mark: {GradesAverage:.2f}")

#calculate the highest and lowest grade for each subject
for idx, subject in enumerate(SubjectsOfStudy):
    SubjectGrades = [Student[1][idx] for Student in StudentsData]
    HighestGrade = max(SubjectGrades)
    LowestGrade = min(SubjectGrades)
    print(f"\n{subject}= Highest Grade: {HighestGrade}, Lowest Grade: {LowestGrade}")

#written wholey by $herman