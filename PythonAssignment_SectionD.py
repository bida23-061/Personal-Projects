#Defines the subjects!
SubjectsOfStudy = ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]

#Initializes data structure to store students' information!
students = {}

#Function to Add a new student and their grades!
def add_student():
    StudentFullname = input("\nEnter Student Full Name: ")
    StudentGrades = {subject: [] for subject in SubjectsOfStudy}

    for subject in SubjectsOfStudy:
        grade = get_valid_grade(StudentFullname, subject)
        StudentGrades[subject].append(grade)

    students[StudentFullname] = StudentGrades

#Function to Prompt for a valid grade for a given student and subject!
def get_valid_grade(student_name, subject):
    while True:
        try:
            grade = float(input(f"Enter {student_name}'s Grade in {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Enter a valid grade between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for the grade.")

#Function to Update grades for an existing student!
def update_student():
    StudentFullname = input("\nEnter name of the student to update: ")
    if StudentFullname in students:
        for subject in SubjectsOfStudy:
            grade = get_valid_grade(StudentFullname, subject)
            students[StudentFullname][subject].append(grade)
    else:
        print("Student not found.")

#Function to Remove a student from the records!
def remove_student():
    StudentFullname = input("\nEnter the name of the student to remove: ")
    if StudentFullname in students:
        del students[StudentFullname]
        print(f"{StudentFullname} has been removed.")
    else:
        print("Student not found.")

#Functiont to View grades for a specific subject across all students!
def view_subject_grades():
    subject = input("\nEnter the subject to view grades for: ")
    if subject in SubjectsOfStudy:
        print(f"\nGrades for {subject}:")
        for StudentFullname, StudentGrades in students.items():
            if subject in StudentGrades:
                print(f"{StudentFullname}: {StudentGrades[subject]}")
    else:
        print("Subject not found.")

#Function to Search for a student by name and display their grades and average!
def search_student():
    StudentFullname = input("\nEnter the name of the student to search for: ")
    if StudentFullname in students:
        display_student_summary(StudentFullname)
    else:
        print("Student not found.")

#Display grades and average for a specific student!
def display_student_summary(student_name):
    StudentGrades = students[student_name]
    total_grades = sum([sum(grades) for grades in StudentGrades.values()])
    total_subjects = sum([len(grades) for grades in StudentGrades.values()])
    GradesAverage = total_grades / total_subjects if total_subjects > 0 else 0
    print(f"\n{student_name} Grades: {StudentGrades}, Average Mark: {GradesAverage:.2f}")

#Display a summary of all students' grades and class averages!
def display_summary():
    GradesSum = 0
    print("\nStudent Grades Summary:")
    for StudentFullname in students:
        display_student_summary(StudentFullname)
        StudentGrades = students[StudentFullname]
        GradesSum += sum([sum(grades) for grades in StudentGrades.values()])

    if students:
        ClassAverage = GradesSum / (len(students) * len(SubjectsOfStudy))
        print(f"\nClass Grade Total: {GradesSum}")
        print(f"\nClass Average: {ClassAverage:.2f}")

    for subject in SubjectsOfStudy:
        SubjectGrades = [grades for student in students.values() for grades in student[subject]]
        if SubjectGrades:
            HighestGrade = max(SubjectGrades)
            LowestGrade = min(SubjectGrades)
            print(f"\n{subject} - Highest Grade: {HighestGrade}, Lowest Grade: {LowestGrade}")

#Main Program!
def main():
    while True:
        print("\nOptions: 1. Add Student 2. Update Student 3. Remove Student 4. Display Summary 5. View Subject Grades 6. Search Student 7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            display_summary()
        elif choice == '5':
            view_subject_grades()
        elif choice == '6':
            search_student()
        elif choice == '7':
            break
        else:
            print("Invalid entry. Try again.")

if __name__ == "__main__":
    main()