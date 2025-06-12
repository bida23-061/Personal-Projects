SubjectsOfStudy = ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]

# Initialize data structure to store students' information
students = {}

# Function to add a new student
def add_student():
    StudentFullname = input("\nEnter Student FullName: ")
    StudentGrades = {}

    for subject in SubjectsOfStudy:
        while True:
                grade = float(input(f"Enter {StudentFullname}'s Grade in {subject}: "))
                if 0 <= grade <= 100:
                    StudentGrades[subject] = grade
                    break
                else:
                    print("PLEASE ENTER A VALID GRADE")


# Define the subjects
SubjectsOfStudy = ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]

# Initialize data structure to store students' information
students = {}

def add_student():
    StudentFullname = input("\nEnter Student Full Name: ")
    StudentGrades = {}

    for subject in SubjectsOfStudy:
        while True:
                grade = float(input(f"Enter {StudentFullname}'s Grade in {subject}: "))
                if 0 <= grade <= 100:
                    StudentGrades[subject] = grade
                    break
                else:
                    print("Enter a valid grade between 0 and 100.")

    students[StudentFullname] = StudentGrades

def update_student():
    StudentFullname = input("\nEnter the name of the student to update: ")
    if StudentFullname in students:
        for subject in SubjectsOfStudy:
            while True:
                    grade = float(input(f"Enter new grade for {StudentFullname} in {subject} (or press Enter to skip): ") or students[StudentFullname][subject])
                    if 0 <= grade <= 100:
                        students[StudentFullname][subject] = grade
                        break
                    else:
                        print("ENTER A VALID GRADE!")
    else:
        print("STUDENT NOT FOUND!")

def remove_student():
    StudentFullname = input("\nEnter the name of the student to remove: ")
    if StudentFullname in students:
        del students[StudentFullname]
        print(f"{StudentFullname} has been removed.")
    else:
        print("Student not found.")

# Main program loop
while True:
    print("\nOptions: 1. Add Student 2. Update Student 3. Remove Student 4. Display Summary 5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        remove_student()
    elif choice == '4':
        # Calculate and display the average grade for each student
        GradesSum = 0
        print("\nStudent Grades Summary:")
        for StudentFullname, StudentGrades in students.items():
            GradesAverage = sum(StudentGrades.values()) / len(StudentGrades)
            GradesSum += sum(StudentGrades.values())
            print(f"{StudentFullname} Grades: {StudentGrades}, Average Mark: {GradesAverage:.2f}")

        # Display whole class average
        if students:
            ClassAverage = GradesSum / (len(students) * len(SubjectsOfStudy))
            print(f"\nClass Grade Total: {GradesSum}")
            print(f"\nClass Average: {ClassAverage:.2f}")

        # Calculate the highest and lowest grade for each subject
        for subject in SubjectsOfStudy:
            SubjectGrades = [grades[subject] for grades in students.values()]
            HighestGrade = max(SubjectGrades)
            LowestGrade = min(SubjectGrades)
            print(f"\n{subject} - Highest Grade: {HighestGrade}, Lowest Grade: {LowestGrade}")
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")
#written wholey by $herman