class Student:
    def __init__(self, name):
        """Initialize a student with a name and an empty grades dictionary."""
        self.name = name
        self.grades = {subject: [] for subject in ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject, ensuring it's valid."""
        if subject in self.grades and 0 <= grade <= 100:
            self.grades[subject].append(grade)
        else:
            raise ValueError("Invalid subject or grade")

    def calculate_average(self):
        """Calculate the average grade across all subjects."""
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_subjects = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_subjects if total_subjects > 0 else 0

    def print_details(self):
        """Print the student's name, grades, and average grade."""
        average = self.calculate_average()
        print(f"Student: {self.name}, Grades: {self.grades}, Average: {average:.2f}")


class Gradebook:
    def __init__(self):
        """Initialize an empty gradebook."""
        self.students = {}

    def add_student(self, name):
        """Add a new student to the gradebook."""
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print("Student already exists.")

    def remove_student(self, name):
        """Remove a student from the gradebook."""
        if name in self.students:
            del self.students[name]
            print(f"{name} has been removed.")
        else:
            print("Student not found.")

    def search_student(self, name):
        """Search for a student by name and print their details."""
        if name in self.students:
            self.students[name].print_details()
        else:
            print("Student not found.")

    def add_grade(self, name, subject, grade):
        """Add a grade for a specific student and subject."""
        if name in self.students:
            try:
                self.students[name].add_grade(subject, grade)
            except ValueError as e:
                print(e)
        else:
            print("Student not found.")

    def display_summary(self):
        """Display a summary of all students' grades and averages."""
        for student in self.students.values():
            student.print_details()

    def sort_by_average(self):
        """Sort students by their average grade in descending order."""
        sorted_students = sorted(self.students.values(), key=lambda s: s.calculate_average(), reverse=True)
        for student in sorted_students:
            student.print_details()

    def sort_by_subject(self, subject):
        """Sort students by their average grade in a specific subject."""
        sorted_students = sorted(self.students.values(), key=lambda s: sum(s.grades[subject]) / len(s.grades[subject]) if s.grades[subject] else 0, reverse=True)
        for student in sorted_students:
            student.print_details()

# Main program
def main():
    """Main function to run the gradebook application."""
    gradebook = Gradebook()

    while True:
        #Displays menu options
        print("\nOptions: 1. Add Student 2. Remove Student 3. Search Student 4. Add Grade 5. Display Summary 6. Sort by Average 7. Sort by Subject 8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            #Adds a new student
            name = input("Enter student name: ")
            gradebook.add_student(name)
        elif choice == '2':
            #Removes an existing student
            name = input("Enter student name to remove: ")
            gradebook.remove_student(name)
        elif choice == '3':
            #Searchs for a student
            name = input("Enter student name to search: ")
            gradebook.search_student(name)
        elif choice == '4':
            #Add a grade for a student
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                gradebook.add_grade(name, subject, grade)
            except ValueError:
                print("Please enter a valid number for the grade.")
        elif choice == '5':
            #Displays a summary of all students
            gradebook.display_summary()
        elif choice == '6':
            #Sorts students by average grade
            gradebook.sort_by_average()
        elif choice == '7':
            #Sorts students by a specific subject
            subject = input("Enter subject to sort by: ")
            gradebook.sort_by_subject(subject)
        elif choice == '8':
            #Exits the program
            break
        else:
            print("Invalid entry. Try again.")

if __name__ == "__main__":
    main()