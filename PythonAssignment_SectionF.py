class StudentNotFoundError(Exception):
    #Exception raised when a student is not found!
    pass

class InvalidGradeError(Exception):
    #Exception raised for invalid grade inputs!
    pass

class Student:
    def __init__(self, name):
        """Initialize a student with a name and an empty grades dictionary."""
        self.name = name
        self.grades = {subject: [] for subject in ["Mathematics", "Biology", "Chemistry", "Physics", "English", "Optional 1", "Optional 2"]}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject, ensuring it's valid."""
        if subject not in self.grades:
            raise InvalidGradeError(f"Invalid subject: {subject}")
        if not (0 <= grade <= 100):
            raise InvalidGradeError("Grade must be between 0 and 100")
        self.grades[subject].append(grade)

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
            raise StudentNotFoundError(f"Student '{name}' not found.")

    def search_student(self, name):
        """Search for a student by name and print their details."""
        if name in self.students:
            self.students[name].print_details()
        else:
            raise StudentNotFoundError(f"Student '{name}' not found.")

    def add_grade(self, name, subject, grade):
        """Add a grade for a specific student and subject."""
        if name in self.students:
            try:
                self.students[name].add_grade(subject, grade)
            except InvalidGradeError as e:
                print(e)
        else:
            raise StudentNotFoundError(f"Student '{name}' not found.")

    def display_summary(self):
        """Display a summary of all students' grades and averages."""
        for student in self.students.values():
            student.print_details()

    def sort_by_average(self):
        """Sort students by their average grade in descending order."""
        sorted_students = self.insertion_sort(self.students.values(), key=lambda s: s.calculate_average(), reverse=True)
        for student in sorted_students:
            student.print_details()

    def sort_by_name(self):
        """Sort students by their name in ascending order."""
        sorted_students = self.insertion_sort(self.students.values(), key=lambda s: s.name)
        for student in sorted_students:
            student.print_details()

    def sort_by_subject(self, subject):
        """Sort students by their average grade in a specific subject."""
        sorted_students = self.insertion_sort(self.students.values(), key=lambda s: sum(s.grades[subject]) / len(s.grades[subject]) if s.grades[subject] else 0, reverse=True)
        for student in sorted_students:
            student.print_details()

    def insertion_sort(self, students, key=lambda x: x, reverse=False):
        """Sort a list of students using the insertion sort algorithm."""
        students = list(students)
        for i in range(1, len(students)):
            key_student = students[i]
            j = i - 1
            while j >= 0 and ((key(students[j]) < key(key_student)) if reverse else (key(students[j]) > key(key_student))):
                students[j + 1] = students[j]
                j -= 1
            students[j + 1] = key_student
        return students

# Main program
def main():
    """Main function to run the gradebook application."""
    gradebook = Gradebook()

    while True:
        print("\nOptions: 1. Add Student 2. Remove Student 3. Search Student 4. Add Grade 5. Display Summary 6. Sort by Average 7. Sort by Name 8. Sort by Subject 9. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == '1':
                name = input("Enter student name: ")
                gradebook.add_student(name)
            elif choice == '2':
                name = input("Enter student name to remove: ")
                gradebook.remove_student(name)
            elif choice == '3':
                name = input("Enter student name to search: ")
                gradebook.search_student(name)
            elif choice == '4':
                name = input("Enter student name: ")
                subject = input("Enter subject: ")
                try:
                    grade = float(input("Enter grade: "))
                    gradebook.add_grade(name, subject, grade)
                except ValueError:
                    print("Please enter a valid number for the grade.")
            elif choice == '5':
                gradebook.display_summary()
            elif choice == '6':
                gradebook.sort_by_average()
            elif choice == '7':
                gradebook.sort_by_name()
            elif choice == '8':
                subject = input("Enter subject to sort by: ")
                gradebook.sort_by_subject(subject)
            elif choice == '9':
                break
            else:
                print("Invalid entry. Try again.")
        except (StudentNotFoundError, InvalidGradeError) as e:
            print(e)

if __name__ == "__main__":
    main()